import pandas as pd
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


iris_data = pd.read_csv('Iris.csv')
#iris_1= iris_data[iris_data['class'] == 'Iris-virginica']
class_colors = {
    'Iris-setosa': (1.0, 1.0, 0.0),  #yellow
    'Iris-versicolor': (0.0, 1.0, 0.0),  #green
    'Iris-virginica': (0.0, 1.0, 1.0)  #cyan
}
def drawText(x, y, text):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(character))

def find_center(): #Find Center Point
    virginica_df = iris_data[iris_data['class'] == 'Iris-virginica']
    mean_values = virginica_df.drop(columns=['class']).mean()
    return mean_values['sepal_length'], mean_values['sepal_width'], mean_values['petal_length'], mean_values['petal_width']  

def draw_axes():
    a, b, c, d = find_center()
    #print(f"Sepal Length: {a}, Sepal Width: {b}, Petal Length: {c}, Petal Width: {d}")
    #anchor = [a,b]
    glLineWidth(5.0)
    glColor3f(0.0, 0.0, 0.0)  #black
    glBegin(GL_LINES)
    # X1
    glVertex2f(0.0, 0.0)
    glVertex2f(9.0, 0.0)
    # X2
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 9.0)
    # X3
    glVertex2f(a-c, b-d)
    glVertex2f(a-c+8,b-d)
    #X4
    glVertex2f(a-c, b-d)
    glVertex2f(a-c,b-d+8)

    #point connected line
    glVertex2f(a-1, b+1)
    glVertex2f(a-1, b-1)

    glVertex2f(a-1, b-1)
    glVertex2f(a+1, b-1)

    glVertex2f(a+1, b-1)
    glVertex2f(a+1, b+1)
    
    glVertex2f(a+1, b+1)
    glVertex2f(a-1, b+1)
    glEnd()

    #center point
    glPointSize(10.0)  # Increase point size
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0) 
    glVertex2f(a, b)
    glVertex2f(a+1, b+1)
    glVertex2f(a-1, b-1)
    glVertex2f(a+1, b-1)
    glVertex2f(a-1, b+1)
    glEnd()
    glutSwapBuffers()

    #Label
    drawText(9.1, 0.0, "X1") 
    drawText(0.0, 9.1, "X2")
    drawText(a-c+8+0.1,b-d, "X3")
    drawText(a-c,b-d+8+0.1, "X4")   

def draw_iris_data():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #Screen limit
    glOrtho(-1.0, 10.0, -1.0, 10.0, -1.0, 10.0)

    
    draw_axes()

    # Dataset loading
    for index, row in iris_data.iterrows():
        # Pick class colour 
        glPointSize(0.1)
        glLineWidth(0.1)
        glColor3f(*class_colors[row['class']])
        #glColor3f(*class_colors['Iris-virginica'])
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
