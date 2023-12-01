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

    # Drawing vector
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0) # red color for X1
    glVertex2f(0.0, 0.0)
    glVertex2f(2.0, 0.0)
    

    glColor3f(0.0, 0.0, 1.0) # blue color for X2
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 4.0)
    glEnd()

    drawText(2.1, 0.0, "X1")
    
    # Drawing X3 and X4 in green and purple respectively
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0) # green color for X3
    glVertex2f(1.0, -3.0)
    glVertex2f(2.0, -3.0)
   
    glColor3f(1.0, 0.0, 1.0) # purple color for X4
    glVertex2f(1.0, -3.0)
    glVertex2f(1.0, 4.0)
    glEnd()


    # Drawing the points 
    glPointSize(10.0)  # Increase point size
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) # orange color for point (2,4)
    glVertex2f(2.0, 4.0)
    glEnd()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(window_x, window_y)
    glutCreateWindow("OpenGL 2D Multiple Coordinate Systems")

    # Set the background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glutDisplayFunc(draw_vectors_and_points)
    glutMainLoop()

if __name__ == "__main__":
    main()
