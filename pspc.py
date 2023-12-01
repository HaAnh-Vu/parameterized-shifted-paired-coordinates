import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def draw_points(points, color, point_size):
    glColor3fv(color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    for point in points:
        glVertex4fv([point[0], point[1], 0, 1])  
    glEnd()

def draw_square(points, color, line_width):
    glColor3fv(color)
    glLineWidth(line_width)
    glBegin(GL_LINE_LOOP)
    for point in points:
        glVertex4fv([point[0], point[1], 0, 1])  
    glEnd()

def draw_axes_with_vectors(labels, center_point, vectors):
    # Draw the axes with vectors
    glColor3f(1, 1, 1)  # White color for axes and vectors
    glBegin(GL_LINES)
    # X Axis
    #glVertex2f(-10, 0)
    #glVertex2f(10, 0)
    # Y Axis
    #glVertex2f(0, -10)
    #glVertex2f(0, 10)
    
    for vector in vectors:
        glVertex2fv(center_point)
        glVertex2fv(vector)
    glEnd()

    # Draw the labels
    for label, pos in labels:
        render_text(label, pos)

def render_text(text, position):
    font = ImageFont.load_default()
    w, h = font.getsize(text)
    img = Image.new("RGBA", (w, h), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)
    img_data = img.tobytes("raw", "RGBA")
    glWindowPos2f(position[0], position[1])
    glDrawPixels(w, h, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

def project_6d_to_2d(points):
    return np.array([[point[0], point[1]] for point in points])

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluOrtho2D(-10, 10, -10, 10)

    base_point = [2, 4, 1, 7, 3, 5]
    distance = 1

    # Calculate the 6D points of the square
    square_6d = [
        [base_point[0] + distance, base_point[1] + distance] + base_point[2:],  # Top right
        [base_point[0] - distance, base_point[1] + distance] + base_point[2:],  # Top left
        [base_point[0] - distance, base_point[1] - distance] + base_point[2:],  # Bottom left
        [base_point[0] + distance, base_point[1] - distance] + base_point[2:],  # Bottom right
    ]
    
    square_2d = project_6d_to_2d(square_6d)
    base_point_2d = [2, 4]  
    center_point_2d = [2, 4]  

    # Vectors emanating from the base point
    vectors = [
        [center_point_2d[0]-2, center_point_2d[1]],     # X1
        [center_point_2d[0], center_point_2d[1]],     # X2
        # 
    ]

    axis_labels = [
        ('X1', [vectors[0][0] + 0.5, vectors[0][1]]),
        ('X2', [vectors[1][0], vectors[1][1] + 0.5]),
        # 
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_axes_with_vectors(axis_labels, center_point_2d, vectors)
        draw_points([base_point_2d], (1, 0, 0), 7)  # Pass base_point_2d as a list
        draw_points(square_2d, (0, 0, 1), 5)
        draw_square(square_2d, (1, 1, 1), 2)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()