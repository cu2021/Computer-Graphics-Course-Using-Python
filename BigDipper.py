# Import OpenGL and system modules
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Define a simple class to represent a 2D point
class GLPoint:
    def __init__(self, x: GLint, y: GLint):
        self.x = x
        self.y = y

# List of points representing the Big Dipper star pattern
points = [
    GLPoint(289, 190),
    GLPoint(320, 128),
    GLPoint(239, 67),
    GLPoint(194, 101),
    GLPoint(129, 83),
    GLPoint(75, 73),
    GLPoint(74, 74),
    GLPoint(20, 10)
]

# Function to draw a single dot at given coordinates
def drawDot(x: GLint, y: GLint):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

# OpenGL initialization function
def myInit():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor3f(0.0, 0.0, 0.0)         # Set drawing color to black
    glPointSize(5.0)                 # Set the size of each point
    glMatrixMode(GL_PROJECTION)     # Set matrix mode to projection
    glLoadIdentity()                # Reset the projection matrix
    gluOrtho2D(0, 640.0, 0, 480.0)   # Set 2D orthographic projection (origin at bottom-left)

# Display callback function for GLUT
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)    # Clear the screen
    for p in points:                # Draw each point from the list
        drawDot(p.x, p.y)
    glFlush()                       # Ensure all OpenGL commands are executed


def main():
    glutInit(sys.argv)                             # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)    # Set display mode to single buffer and RGB color
    glutInitWindowSize(640, 480)                   # Set window size
    glutInitWindowPosition(100, 150)               # Set window position on screen
    glutCreateWindow(b"BigDipper")                 # Create window with title
    glutDisplayFunc(myDisplay)                     # Register display callback
    myInit()                                       # Call initialization function
    glutMainLoop()                                 # Enter the GLUT event processing loop

if __name__ == "__main__":
    main()
