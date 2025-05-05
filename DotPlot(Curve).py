from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import numpy as np

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


# Function to calculate e^-x * cos(2πx)
def f(x):
    return math.exp(-x) * math.cos(2 * math.pi * x)

# OpenGL initialization function
def myInit():
    # Set background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Set drawing color to black
    glColor3f(0.0, 0.0, 0.0)
    # Set the size of each point
    glPointSize(2.0)
    # Set matrix mode to projection
    glMatrixMode(GL_PROJECTION)
    # Reset the projection matrix
    glLoadIdentity()
    # Set 2D orthographic projection (origin at bottom-left)
    gluOrtho2D(0, GLdouble(SCREEN_WIDTH), 0, GLdouble(SCREEN_HEIGHT))

# Plot the function from x = 0.0 to x = 4.0 and take 0.005 step at a time
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    
    for x in np.arange(0.0, 4.0, 0.005):
        # Calculate y
        y = f(x)
        # Transform the coordinates to fit the screen
        glVertex2d(GLdouble(SCREEN_WIDTH * x / 4.0), GLdouble(SCREEN_HEIGHT / 2.0 + SCREEN_HEIGHT * y / 2.0))
        
    glEnd()
    glFlush()


def main():
    # Initialize GLUT
    glutInit(sys.argv)
    # Use single buffering and RGB color mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # Set the window size
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Set window position on the screen
    glutInitWindowPosition(100, 150)
    # Create window with a title
    glutCreateWindow(b"Dot Plot of a Function")
    # Set the display callback function
    glutDisplayFunc(myDisplay)
    # Perform OpenGL initializations
    myInit()
    # Enter the main GLUT event loop
    glutMainLoop()


if __name__ == "__main__":
    main()
