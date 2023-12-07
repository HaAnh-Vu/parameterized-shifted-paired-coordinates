from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load  dataset
iris_data = pd.read_csv('Iris.csv')
# Normalized dataset to [0,1]
numerical_cols = iris_data.select_dtypes(include=['float64', 'int64']).columns
scaler = MinMaxScaler(feature_range=(0, 1))
iris_data[numerical_cols] = scaler.fit_transform(iris_data[numerical_cols])

# Normalized save file
iris_data.to_csv('normalized_iris.csv', index=False)

#Set class colors
class_colors = {
    'Iris-setosa': (0, 0.5, 0.0),  
    'Iris-versicolor': (0.5 , 1, 0.0),  
    'Iris-virginica': (0.0, 0.0, 0.5)
}
#Set class colors for highlight point in Rectangle
class_highlight = {
    'Iris-setosa': (0, 0, 0.0),  
    'Iris-versicolor': (0,  0, 0.0),  
    'Iris-virginica': (1.0, 0.0, 0.0)
}

#Label
def drawText(x, y, text):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(character))

def find_center(): #Find the center point
    virginica_df = iris_data[iris_data['class'] == 'Iris-virginica']
    mean_values = virginica_df.drop(columns=['class']).mean()

    #If you want to adjust the center point coordinate, edit 4 lines below

    # mean_values['sepal_length']= 0.545
    # mean_values['sepal_width']= 0.363333
    # mean_values['petal_length']= 0.662034
    # mean_values['petal_width']=  0.656667


    return mean_values['sepal_length'], mean_values['sepal_width'], mean_values['petal_length'], mean_values['petal_width']
    
def draw_axes():
    a, b, c, d = find_center()
    #print(f"Sepal Length: {a}, Sepal Width: {b}, Petal Length: {c}, Petal Width: {d}") #Checking value of Center point

    glLineWidth(5.0)
    glColor3f(0.0, 0.0, 0.0)  # black
    glBegin(GL_LINES)

    #choosing anchor point =[a,b]
    # X1
    glVertex2f(0.0, 0.0)
    glVertex2f(1, 0.0)

    # X2
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 1)

    # The coordinate calculation based on the chapter 3 of the book
    # X3
    glVertex2f(a - c, b - d)
    glVertex2f(a - c + 1, b - d)

    # X4
    glVertex2f(a - c , b - d)
    glVertex2f(a - c, b - d + 1)

    # Point connected line
    glVertex2f(a - 0.1, b + 0.1)
    glVertex2f(a - 0.1, b - 0.1)

    glVertex2f(a - 0.1, b - 0.1)
    glVertex2f(a + 0.1, b - 0.1)

    glVertex2f(a + 0.1, b - 0.1)
    glVertex2f(a + 0.1, b + 0.1)

    glVertex2f(a + 0.1, b + 0.1)
    glVertex2f(a - 0.1, b + 0.1)

    glEnd()

    # Center point
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(a, b)

    # 4 corner points of the square
    glVertex2f(a + 0.1, b + 0.1)
    glVertex2f(a - 0.1, b - 0.1)
    glVertex2f(a + 0.1, b - 0.1)
    glVertex2f(a - 0.1, b + 0.1)
    glEnd()
    glutSwapBuffers()

    # Label
    drawText(0.91, 0.0, "X1")
    drawText(0.0, 0.91, "X2")
    drawText(a-c+1+0.01,b-d, "X3")
    drawText(a-c,b-d+1+0.01, "X4")  

selected_points = [] 

def draw_iris_data():
    a, b, c, d = find_center()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glOrtho(-0.5, 1.2, -0.5, 1.2, -0.5, 1.2)

    draw_axes()
    
    # Draw the rest cases without inside the square
    for index, row in iris_data.iterrows():
        if not (a - 0.1 <= row['sepal_length'] <= a + 0.1) or not (a - 0.1 <= row['petal_length']+(a-c) <= a + 0.1) or \
           not (b - 0.1 <= row['sepal_width'] <= b + 0.1) or not (b - 0.1 <= row['petal_width'] +(b-d)<= b + 0.1):
            glPointSize(0.5)
            glLineWidth(2)
            glColor3f(*class_colors[row['class']])

            glBegin(GL_LINES)
            glVertex2f(row['sepal_length'], row['sepal_width'])
            glVertex2f(row['petal_length']+(a-c), row['petal_width']+(b-d))
            glEnd()

            glPointSize(5.0)
            glBegin(GL_POINTS)
            glVertex2f(row['sepal_length'], row['sepal_width'])
            glVertex2f(row['petal_length']+(a-c), row['petal_width']+(b-d))
            glEnd()

    # Draw the highlighted cases on top
    for index, row in iris_data.iterrows():
        if (a - 0.1 <= row['sepal_length'] <= a + 0.1) and (a - 0.1 <= row['petal_length'] +(a-c)<= a + 0.1) and \
           (b - 0.1 <= row['sepal_width'] <= b + 0.1) and (b - 0.1 <= row['petal_width'] +(b-d)<= b + 0.1):
            glPointSize(5.5)
            glLineWidth(5.0)
            glColor3f(*class_highlight[row['class']])  # colors for highlighted cases

            glBegin(GL_LINES)
            glVertex2f(row['sepal_length'], row['sepal_width'])
            glVertex2f(row['petal_length']+(a-c), row['petal_width']+(b-d))
            glEnd()

            glPointSize(5.5)
            glBegin(GL_POINTS)
            glVertex2f(row['sepal_length'], row['sepal_width'])
            glVertex2f(row['petal_length']+(a-c), row['petal_width']+(b-d))
            glEnd()

    glutSwapBuffers()




def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Iris Data Visualization")
    glutDisplayFunc(draw_iris_data)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
