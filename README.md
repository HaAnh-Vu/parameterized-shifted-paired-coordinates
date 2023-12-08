# README for Python Scripts: in_square.py and Iris_PSPC.py

## Overview
This repository includes two Python scripts: `in_square.py` and `Iris_PSPC.py`. Both scripts are designed for processing and visualizing the Iris dataset. They utilize OpenGL for graphical representation and pandas for data handling.

### in_square.py
- **Purpose**: Visualizes the Iris dataset using OpenGL. It graphically represents data points, scaled and color-coded based on specific attributes.
- **Output**:  `in_square.py` for visualize in point inside square and export these coordinates

### Iris_PSPC.py
- **Purpose**: Preprocesses the Iris dataset by normalizing the data and saving it to a new CSV file, suitable for further analysis or visualization.
- **Output**: The PSPC would be generated. `Iris_PSPC.py` for display full process.

## Dependencies
This project working smoothly in Python 3.7.9. The scripts require the following libraries:
- OpenGL (including GL, GLUT, and GLU)
- Pandas
- Scikit-learn (specifically, MinMaxScaler)

Install these libraries in your Python environment using pip:
```bash
pip install PyOpenGL PyOpenGL_accelerate pandas scikit-learn

If running the command above does not work, you can manually install the dependencies using the provided files in this folder. Use the following commands:

pip install PyOpenGL-3.1.6-cp37-cp37m-win_amd64.whl
pip install PyOpenGL_accelerate-3.1.6-cp37-cp37m-win_amd64.whl

If you are using another Python version, you can look for compatible dependencies at this link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl