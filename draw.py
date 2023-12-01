from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# window size and position
width, height = 1000, 1000
window_x, window_y = 300, 300

def drawText(x, y, text):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(character))

def draw_vectors_and_points():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Adjusting the viewing area to include our points
    glOrtho(-10, 10, -10, 10, -10, 10)
    glLineWidth(3.0)
    # Drawing vector
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0) # red color for X1
    glVertex2f(0.0, 0.0)
    glVertex2f(2.0, 0.0)
    

    glColor3f(0.0, 0.0, 1.0) # blue color for X2
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 4.0)
    glEnd()

    drawText(2.1, 0.0, "X1") #label
    drawText(0.0, 4.1, "X2") #label

    
    # Drawing X3 and X4 in green and purple respectively
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0) # green color for X3
    glVertex2f(1.0, -3.0)
    glVertex2f(2.0, -3.0)
   
    glColor3f(1.0, 0.0, 1.0) # purple color for X4
    glVertex2f(1.0, -3.0)
    glVertex2f(1.0, 4.0)
    glEnd()

    drawText(2.1, -3.0, "X3") #label
    drawText(1.0, 4.1, "X4") #label

    # Drawing X5 and X6 in yellow and cyan respectively
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0) # yellow color for X5
    glVertex2f(-1.0, -1.0)
    glVertex2f(2.0, -1.0)
    
    glColor3f(0.0, 1.0, 1.0) # cyan color for X6
    glVertex2f(-1.0, -1.0)
    glVertex2f(-1.0, 4.0)
    glEnd()

    drawText(2.1, -1.0, "X5") #label
    drawText(-1.0, 4.1, "X6") #label

    #rectangle connected line
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(1.0, 5.0)
    glVertex2f(3.0, 5.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(3.0, 5.0)
    glVertex2f(3.0, 3.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(3.0, 3.0)
    glVertex2f(1.0, 3.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(1.0, 3.0)
    glVertex2f(1.0, 5.0)
    glEnd()

    # Drawing the Base point = [2,4,1,7,3,5]
    glPointSize(7.0)  # Increase point size
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) # orange 
    glVertex2f(2.0, 4.0)
    glEnd()
    drawText(2.1, 4.1, "(2,4,1,7,3,5)")
    glutSwapBuffers()

    # Drawing the point = [1,5,0,8,2,6]
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) 
    glVertex2f(1.0, 5.0)
    glEnd()
    drawText(1.1, 5.1, "(1,5,0,8,2,6)")
    glutSwapBuffers()

    # Drawing the point = [3,5,2,8,4,6]
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) 
    glVertex2f(3.0, 5.0)
    glEnd()
    drawText(3.1, 5.1, "(3,5,2,8,4,6)")
    glutSwapBuffers()

    # Drawing the point = [1,3,0,6,2,4]
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) 
    glVertex2f(1.0, 3.0)
    glEnd()
    drawText(0.8, 2.8, "(1,3,0,6,2,4")
    glutSwapBuffers()

    # Drawing the point = [3,3,2,6,4,4]
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) 
    glVertex2f(3.0, 3.0)
    glEnd()
    drawText(3.1, 3.1, "(3,3,2,6,4,4)")
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(window_x, window_y)
    glutCreateWindow("Fig 3.8")

    # Set the background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glutDisplayFunc(draw_vectors_and_points)
    glutMainLoop()

if __name__ == "__main__":
    main()
