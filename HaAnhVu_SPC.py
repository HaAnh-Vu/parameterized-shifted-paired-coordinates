import math
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from itertools import permutations

class DatasetVisualizer:
    def __init__(self, file_path):
        # Initialize the DatasetVisualizer with a CSV file path
        self.dataset_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract dataset name from file path
        self.df = pd.read_csv(file_path)  # Load the CSV file into a DataFrame
        self._prepare_data()  # Prepare the data for visualization
        self._run_lda()  # Run Linear Discriminant Analysis (LDA) to calculate coefficients
        self.current_perm_index = 0
        self.perms = self._generate_permutations()  # Generate permutations of feature indices

    def _prepare_data(self):
        # Duplicate the last column if the number of features is odd to make it even
        if (self.df.shape[1] - 1) % 2 != 0:
            last_col = self.df.columns[-2]
            self.df[last_col + '_dup'] = self.df[last_col]

        # Normalize features using Min-Max scaling
        scaler = MinMaxScaler()
        features = self.df.drop(columns=['class']).values
        self.features_normalized = scaler.fit_transform(features)  # Normalize features
        self.labels = self.df['class'].values  # Extract class labels
        self.unique_labels = np.unique(self.labels)  # Get unique class labels
        self.colors = plt.cm.jet(np.linspace(0, 1, len(self.unique_labels)))  # Generate colors for plotting

    def _run_lda(self):
        # Run Linear Discriminant Analysis (LDA) to calculate feature coefficients
        lda = LinearDiscriminantAnalysis()
        lda.fit(self.features_normalized, self.labels)
        self.lda_coefficients = np.abs(lda.coef_).mean(axis=0)

    def _generate_permutations(self):
        # Generate permutations of feature indices
        num_features = self.features_normalized.shape[1]
        perms = list(permutations(range(num_features), num_features))
        sorted_features = np.argsort(self.lda_coefficients)[::-1]
        most_important_perm = tuple(sorted_features)
        if most_important_perm in perms:
            perms.remove(most_important_perm)
        perms.insert(0, most_important_perm)
        return perms

    def update_plot(self, event): #it's not working yet
        # Update the plot when scrolling (up or down) is detected
        num_features = self.features_normalized.shape[1]
        if event.button == 'up':
            self.current_perm_index = (self.current_perm_index + 1) % len(self.perms)
        else:
            self.current_perm_index = (self.current_perm_index - 1) % len(self.perms)

        plt.clf()  # Clear the current plot
        self.draw_plot()  # Redraw the plot

        fig = plt.gcf()
        fig.canvas.mpl_connect('scroll_event', self.update_plot)
        fig.canvas.mpl_connect('key_press_event', self.exit_program)

        current_permutation = self.perms[self.current_perm_index]
        num_subplots = len(current_permutation) // 2 + (len(current_permutation) % 2)
        axes = [fig.add_subplot(1, num_subplots, i+1) for i in range(num_subplots)]


        plt.suptitle(f'{self.dataset_name} in Shifted Paired Coordinates with Permutation')
        plt.draw()

    def draw_plot(self):
        # Draw the main plot with subplots and connections between points
        fig = plt.gcf()
        fig.canvas.mpl_connect('scroll_event', self.update_plot)
        fig.canvas.mpl_connect('key_press_event', self.exit_program)

        current_permutation = self.perms[self.current_perm_index]
        num_subplots = len(current_permutation) // 2 + (len(current_permutation) % 2)
        axes = [fig.add_subplot(1, num_subplots, i + 1) for i in range(num_subplots)]

        # Create legend axis
        legend_axis = fig.add_axes([0.05, 0.85, 0.2, 0.1])
        legend_axis.axis('off')

        # Create legend handles
        legend_handles = [Line2D([0], [0], marker='x', color='w', markeredgecolor=self.colors[i], label=self.unique_labels[i], markersize=10) for i in range(len(self.unique_labels))]

        # Add legend to the axis
        legend_axis.legend(handles=legend_handles, loc='upper left')

        # Plot points in each subplot
        for ax, i, j in zip(axes, current_permutation[::2], current_permutation[1::2]):
            for l in range(len(self.features_normalized)):
                x, y = self.features_normalized[l, i], self.features_normalized[l, j]
                label = self.labels[l]
                color = self.colors[np.where(self.unique_labels == label)[0][0]]

                ax.scatter(x, y, color=color, s=50, marker='x')

            ax.set_title(f"(X{i + 1}, X{j + 1})")

        # Connect points across subplots
        for l in range(len(self.features_normalized)):
            color = self.colors[np.where(self.unique_labels == self.labels[l])[0][0]]
            xy_points = [(self.features_normalized[l, current_permutation[i]], self.features_normalized[l, current_permutation[i + 1]]) for i in range(0, len(current_permutation) - 1, 2)]

            for ax1, ax2, point1, point2 in zip(axes[:-1], axes[1:], xy_points[:-1], xy_points[1:]):
                coord1 = ax1.transData.transform(point1)
                coord2 = ax2.transData.transform(point2)

                fig_coord1 = fig.transFigure.inverted().transform(coord1)
                fig_coord2 = fig.transFigure.inverted().transform(coord2)

                line = Line2D([fig_coord1[0], fig_coord2[0]], [fig_coord1[1], fig_coord2[1]], transform=fig.transFigure, color=color, alpha=0.33)
                fig.lines.append(line)

        plt.suptitle(f'{self.dataset_name} in Shifted Paired Coordinates')
        plt.draw()

    def visualize(self):
        # Create and display the visualization
        fig = plt.figure(figsize=(15, 8))
        self.draw_plot()
        plt.show()

    def exit_program(self, event):
        # Exit the program when the 'escape' key or 'ctrl+q' is pressed
        if event.key == 'escape' or event.key == 'ctrl+q':
            plt.close()

if __name__ == "__main__":
    test_csv_file_path = "test.csv"
    visualizer = DatasetVisualizer(test_csv_file_path)
    visualizer.visualize()
