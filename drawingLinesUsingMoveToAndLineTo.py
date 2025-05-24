from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


class GLintPoint:
    """
    Represents a 2D point with integer coordinates.
    """
    def __init__(self, x: GLint = 0, y: GLint = 0):
        self.x = x
        self.y = y

# Current drawing position
CP = GLintPoint()


def moveTo(x: GLint, y: GLint):
    """
    Updates the current point to (x, y) without drawing anything.
    """
    CP.x = x
    CP.y = y


def lineTo(x: GLint, y: GLint):
    """
    Draws a line from the current point (CP) to the given point (x, y),
    then updates the current point to (x, y).
    """
    glBegin(GL_LINES)
    glVertex2i(CP.x, CP.y)
    glVertex2i(x, y)
    glEnd()
    glFlush()
    CP.x = x
    CP.y = y


def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D orthographic projection.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)     # Background color: white
    glColor3f(0.0, 0.0, 0.0)            # Drawing color: black
    glLineWidth(2.0)                    # Line width
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, GLdouble(WINDOW_WIDTH), 0, GLdouble(WINDOW_HEIGHT))


def myDisplay():
    """
    GLUT display callback: clears the screen and draws a simple polyline.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    # Set starting point
    moveTo(50, 50)

    # Draw line from (50, 50) to (100, 100)
    lineTo(100, 100)
    # Draw line from (100, 100) to (150, 80)
    lineTo(150, 80)
    # Draw line from (150, 80) to (200, 120)
    lineTo(200, 120)

    glFlush()


def main():
    """
    The main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Polyline using moveTo and lineTo")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
