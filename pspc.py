import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def draw_points(points, color):
    glColor3fv(color)
    glBegin(GL_POINTS)
    for point in points:
        glVertex2fv(point)
    glEnd()

def draw_square(points, color):
    glColor3fv(color)
    glBegin(GL_LINES)
    for i in range(len(points)):
        glVertex2fv(points[i])
        glVertex2fv(points[(i + 1) % len(points)])  # Connect to next point, loop back at the end
    glEnd()

def draw_axes():
    axes = [
        [[-10, 0], [10, 0]],  # X axis
        [[0, -10], [0, 10]]   # Y axis
    ]
    glColor3f(1, 1, 1)  # White color for axes
    glBegin(GL_LINES)
    for axis in axes:
        for vertex in axis:
            glVertex2fv(vertex)
    glEnd()

def render_text(text, position):
    font = ImageFont.load_default()
    img = Image.new("RGBA", (10, 10), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    img = img.resize((w, h))

    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (255, 255, 255), font=font)
    img_data = np.array(list(img.getdata()), np.uint8)

    glWindowPos2fv(position)
    glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

def project_6d_to_2d(points):
    # Using first two dimensions for projection
    return np.array([[point[0], point[1]] for point in points])

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluOrtho2D(-10, 10, -10, 10)

    square_6d = [
        [3, 5, 2, 8, 4, 6],  # Top right
        [1, 5, 0, 8, 2, 6],  # Top left
        [1, 3, 0, 6, 2, 4],  # Bottom left
        [3, 3, 2, 6, 4, 4]   # Bottom right
    ]
    square_2d = project_6d_to_2d(square_6d)
    center_point_2d = project_6d_to_2d([[2, 4, 1, 7, 3, 5]])[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_axes()
        for i, label in enumerate(['X1', 'X2']):
            render_text(label, (10, -10 + i * 3))
        draw_points(square_2d, (0, 0, 1))  # Blue color for square points
        draw_square(square_2d, (1, 1, 1))  # White color for square
        draw_points([center_point_2d], (1, 0, 0))  # Red color for center point
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
