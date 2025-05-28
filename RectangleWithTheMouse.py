from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions in pixels
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class GLintPoint:
    """
    Represents a 2D point with integer coordinates.
    """
    def __init__(self, x: GLint = 0, y: GLint = 0):
        self.x = x
        self.y = y

# Store two corner points for the rectangle
corner = [None, None]
numCorners = 0

def display():
    """
    GLUT display callback function.
    Clears the screen and flushes any rendered output.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def myMouse(button, state, x, y):
    """
    GLUT mouse callback function.
    - Left click stores corner points and draws a rectangle after two clicks.
    - Right click clears the screen.

    Parameters:
        button (int): The mouse button (GLUT_LEFT_BUTTON or GLUT_RIGHT_BUTTON).
        state (int): The state of the mouse button (GLUT_DOWN or GLUT_UP).
        x (int): X-coordinate of the click.
        y (int): Y-coordinate of the click (converted to OpenGL coordinates).
    """
    global numCorners, corner

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        corner[numCorners] = GLintPoint(x, WINDOW_HEIGHT - y)
        numCorners += 1

        if numCorners == 2:
            glRecti(corner[0].x, corner[0].y, corner[1].x, corner[1].y)
            glFlush()
            numCorners = 0  # Reset for the next rectangle

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()
        numCorners = 0  # Reset in case it was in the middle of drawing

def myInit():
    """
    Initializes the OpenGL rendering context:
    - Sets background to white and drawing color to black.
    - Defines a 2D orthographic projection.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)  # Black drawing color
    glPointSize(5.0)
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # 2D orthographic projection

def main():
    """
    The main function initializes GLUT and OpenGL settings,
    creates the window, and starts the event-processing loop.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Click Two Points to Draw Rectangle, Right Click to Clear")
    myInit()
    glutDisplayFunc(display)
    glutMouseFunc(myMouse)
    glutMainLoop()

if __name__ == "__main__":
    main()
