import pandas as pd
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


iris_data = pd.read_csv('Iris.csv')

class_colors = {
    'Iris-setosa': (1.0, 0.0, 0.0),  # red
    'Iris-versicolor': (0.0, 1.0, 0.0),  # green
    'Iris-virginica': (0.0, 0.0, 1.0)  # blue
}

def draw_axes():
    
    glColor3f(0.0, 0.0, 0.0)  #black
    glBegin(GL_LINES)
    # X
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    # Y
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glEnd()

def draw_iris_data():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #Screen limit
    glOrtho(-3.0, 10.0, -3.0, 10.0, -3.0, 10.0)

    
    draw_axes()

    # Dataset loading
    for index, row in iris_data.iterrows():
        # Pick class colour 
        glColor3f(*class_colors[row['class']])
        # Connected lines
        glBegin(GL_LINES)
        glVertex2f(row['sepal_length'], row['sepal_width'])
        glVertex2f(row['petal_length'], row['petal_width'])
        glEnd()
        # Points
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glVertex2f(row['sepal_length'], row['sepal_width'])
        glVertex2f(row['petal_length'], row['petal_width'])
        glEnd()

    
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Iris Data Visualization")
    glutDisplayFunc(draw_iris_data)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
