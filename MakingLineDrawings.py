# Import OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Scaling factors for the symbol's coordinates
# A is the scale factor along the X-axis
# C is the scale factor along the Y-axis
A = C = 5

# Define the conceptual original center of the hashtag symbol in its local coordinate system.
# The drawing coordinates (in myDisplay) are relative to this local system.
symbol_center_x = A * 25  # Scaled center X
symbol_center_y = C * 25  # Scaled center Y

# Compute translation values to center the symbol in the window
# B = X-axis shift, D = Y-axis shift
B = WINDOW_WIDTH // 2 - symbol_center_x
D = WINDOW_HEIGHT // 2 - symbol_center_y

def transform(x, y):
    """
    Apply affine transformation (scaling then translation) to input coordinates.
    This transforms coordinates from the symbol's local space to window space.
    The transformation formula is:
    transformed_x = A * x_local + B
    transformed_y = C * y_local + D
    """
    transformed_x = A * x + B
    transformed_y = C * y + D
    return transformed_x, transformed_y

def drawLineInt(x1: GLint, y1: GLint, x2: GLint, y2: GLint):
    """
    Draw a line between two integer points after applying the transform.
    """
    glBegin(GL_LINES)

    # Transform the start point from local symbol coordinates to window coordinates
    sx1, sy1 = transform(x1, y1)
    glVertex2i(GLint(sx1), GLint(sy1))

    # Transform the end point from local symbol coordinates to window coordinates
    sx2, sy2 = transform(x2, y2)
    glVertex2i(GLint(sx2), GLint(sy2))
    glEnd()

def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D projection setup.
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
    GLUT display callback: clears the screen and draws the centered hashtag symbol.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw horizontal lines of the '#' symbol
    drawLineInt(10, 20, 40, 20)
    drawLineInt(10, 30, 40, 30)

    # Draw vertical lines of the '#' symbol
    drawLineInt(20, 10, 20, 40)
    drawLineInt(30, 10, 30, 40)

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
    glutCreateWindow(b"Drawing # Symbol Using drawLineInt Function")
    # Register myDisplay callback function
    glutDisplayFunc(myDisplay)
    # Initialize OpenGL settings
    myInit()
    # Enter the main event loop
    glutMainLoop()

if __name__ == "__main__":
    main()
