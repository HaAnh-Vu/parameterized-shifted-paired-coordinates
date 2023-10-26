import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

base_point = (2, 4, 1, 7, 3, 5)
points = [
    (1, 5, 0, 8, 2, 6),
    (3, 5, 2, 8, 4, 6),
    (1, 3, 0, 6, 2, 4),
    (3, 3, 2, 6, 4, 4)
]
point_labels = [
    "A (1, 5, 0, 8, 2, 6)",
    "B (3, 5, 2, 8, 4, 6)",
    "C (1, 3, 0, 6, 2, 4)",
    "D (3, 3, 2, 6, 4, 4)"
]

def draw_arrows_from_point(point, base_point):
    offset = 0.2
    for i in range(len(point)):
        direction = (point[i] - base_point[i])
        if direction > 0:
            glBegin(GL_LINES)
            glVertex2f(point[0] + offset, point[1])
            glVertex2f(point[0] + offset, point[1] + direction)
            glEnd()
            offset += 0.2
        elif direction < 0:
            glBegin(GL_LINES)
            glVertex2f(point[0] - offset, point[1])
            glVertex2f(point[0] - offset, point[1] + direction)
            glEnd()
            offset -= 0.2

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)
    for point in points:
        glBegin(GL_POINTS)
        glVertex2f(point[0], point[1])
        glEnd()
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    for i in range(len(points)):
        next_point = points[(i+1)%len(points)]
        glVertex2f(points[i][0], points[i][1])
        glVertex2f(next_point[0], next_point[1])
    glEnd()
    for point in points:
        draw_arrows_from_point(point, base_point)
    glColor3f(0, 0, 0)
    for i, point in enumerate(points):
        renderText(point[0], point[1], point_labels[i])
    glBegin(GL_POINTS)
    glVertex2f(base_point[0], base_point[1])
    glEnd()
    renderText(base_point[0], base_point[1], "Base (2, 4, 1, 7, 3, 5)", size=10)
    glutSwapBuffers()

def renderText(x, y, text, size=15):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("6-D Data Visualization")
    glClearColor(1, 1, 1, 1)
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10)
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()
