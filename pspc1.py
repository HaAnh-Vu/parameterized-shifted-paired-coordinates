from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# window size and position
width, height = 800, 800
window_x, window_y = 300, 300

def draw_vectors_and_points():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Adjusting the viewing area to include our points
    glOrtho(-1, 10, -1, 10, -1, 1)

    # Drawing X1 and X2 in red and blue respectively
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0) # red color for X1
    glVertex2f(0.0, 0.0)
    glVertex2f(2.0, 0.0)
    glColor3f(0.0, 0.0, 1.0) # blue color for X2
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 4.0)
    glEnd()

    # Drawing X3 and X4 in green and purple respectively
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0) # green color for X3
    glVertex2f(3.0, 0.0)
    glVertex2f(3.0, 4.0)
    glColor3f(1.0, 0.0, 1.0) # purple color for X4
    glVertex2f(3.0, 0.0)
    glVertex2f(5.0, 0.0)
    glEnd()

    # Drawing X5 and X6 in yellow and cyan respectively
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0) # yellow color for X5
    glVertex2f(6.0, 0.0)
    glVertex2f(6.0, 5.0)
    glColor3f(0.0, 1.0, 1.0) # cyan color for X6
    glVertex2f(6.0, 0.0)
    glVertex2f(9.0, 0.0)
    glEnd()

    # Drawing the points (2,4), (1,7), and (3,5) with increased size
    glPointSize(10.0)  # Increase point size
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0) # orange color for point (2,4)
    glVertex2f(2.0, 4.0)
    glColor3f(0.0, 0.5, 1.0) # teal color for point (1,7)
    glVertex2f(4.0, 7.0)
    glColor3f(1.0, 0.0, 0.5) # pink color for point (3,5)
    glVertex2f(6.0, 5.0)
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