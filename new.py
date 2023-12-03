import pandas as pd

# Đọc dữ liệu từ file CSV
iris_data = pd.read_csv('Iris.csv')

def find_center():
    virginica_df = iris_data[iris_data['class'] == 'Iris-virginica']
    mean_values = virginica_df.drop(columns=['class']).mean()
    return mean_values['sepal_length'], mean_values['sepal_width'], mean_values['petal_length'], mean_values['petal_width']  

a, b, c, d = find_center()
# In giá trị
print("Mean values for Iris-virginica class:")
print(f"Sepal Length: {a}, Sepal Width: {b}, Petal Length: {c}, Petal Width: {d}")
