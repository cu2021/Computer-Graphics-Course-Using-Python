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


def drawPolyLine(poly, closed: int):
    """
    Renders a 2D polyline or polygon using OpenGL primitives.

    Args:
        - poly : list of GLintPoint
            A list of points that define the vertices of the shape.
        -closed : int
            If 1 (or non-zero), draws a closed shape (GL_LINE_LOOP).
            If 0, draws an open polyline (GL_LINE_STRIP).
    """
    glBegin(GL_LINE_LOOP if closed else GL_LINE_STRIP)
    for i in range(len(poly)):
        glVertex2i(poly[i].x, poly[i].y)
    glEnd()
    glFlush()


def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    Line width, and 2D projection setup.
    """
    # Set background to white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Set drawing color to black
    glColor3f(0.0, 0.0, 0.0)

    # Set Line Width
    glLineWidth(2.0)
    # Set matrix mode to projection
    glMatrixMode(GL_PROJECTION)
    # Reset projection matrix
    glLoadIdentity()

    # Define 2D orthographic projection
    gluOrtho2D(0, GLdouble(WINDOW_WIDTH), 0, GLdouble(WINDOW_HEIGHT))

def myDisplay():
    """
    GLUT display callback: clears the screen and draws a simple polyline.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Create a triangle or any shape;
    # You have to use your math skills to define the vertices.
    poly = [
        GLintPoint(100, 100), # Top vertex
        GLintPoint(50, 50),  # Bottom-left vertex
        GLintPoint(150, 50)  # Bottom-right vertex
    ]

    # closed=1 means GL_LINE_LOOP
    drawPolyLine(poly, closed=1)

    # Ensure all drawing commands are completed
    glFlush()


def main():
    """The main function to set up GLUT and run the application.

    Initializes GLUT, creates a window, sets up display and keyboard callbacks,
    calls initialization functions, and enters the GLUT event processing loop.
    """
    # Initialize GLUT
    glutInit(sys.argv)
    # Single buffer and RGB color
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set window size
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    # Set window position
    glutInitWindowPosition(100, 150)

    # Create the window with a title
    glutCreateWindow(b"Draw Polyline using drawPolyLine Function.")
    # Register myDisplay callback function
    glutDisplayFunc(myDisplay)
    # Initialize OpenGL settings
    myInit()
    # Enter the main event loop
    glutMainLoop()

if __name__ == "__main__":
    main()

