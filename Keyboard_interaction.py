from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import os

from BigDipper import GLPoint

# Window dimensions in pixels
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Global list to store points added by left arrow key
points = []
last = -1


class GLintPoint:
    """
    Represents a 2D point with integer coordinates.
    """
    def __init__(self, x: GLint = 0, y: GLint = 0):
        self.x = x
        self.y = y


def drawDot(x: GLint, y: GLint):
    """
    Draws a single point at coordinates (x, y) with fixed size.
    """
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()
    glFlush()


def myKeyboard(theKey, mouseX, mouseY):
    """
    Handles regular ASCII keyboard input.

    Parameters:
    - theKey: pressed key (bytes)
    - mouseX, mouseY: current mouse position in window coordinates

    Actions:
    - 'p': Draws a dot at the current mouse location.
    - 'E': Exits the program immediately.
    """
    global last, points
    x = mouseX
    y = WINDOW_HEIGHT - mouseY  # Convert to OpenGL coordinate system

    if theKey == b'p':
        drawDot(x, y)
    elif theKey == b'E':
        os._exit(0)


def mySpecialKeyboard(key, x, y):
    """
    Handles special keys such as arrow keys.

    Parameters:
    - key: special key code (e.g., GLUT_KEY_LEFT)
    - x, y: current mouse position in window coordinates

    Action:
    - LEFT arrow key: Adds the current mouse position as a GLPoint to the points list and prints all points.
    """
    global last, points
    y = WINDOW_HEIGHT - y  # Convert to OpenGL coordinate system

    if key == GLUT_KEY_LEFT:
        points.append(GLPoint(x, y))
        last += 1

        for i, p in enumerate(points):
            print(f"{i}: X = {p.x}, Y = {p.y}")


def myDisplay():
    """
    GLUT display callback.

    Clears the window to background color.
    (No drawing is done here since dots are drawn immediately on key press.)
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()


def myInit():
    """
    Initializes OpenGL rendering context.

    - Sets background color to white.
    - Sets drawing color to black.
    - Sets point size and line width.
    - Configures 2D orthographic projection to match window size.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)          # Black drawing color
    glPointSize(5.0)
    glLineWidth(2.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)


def main():
    """
    Main entry point:

    - Initializes GLUT.
    - Sets up window and callbacks.
    - Starts the GLUT event loop.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Keyboard Input and Drawing")

    glutDisplayFunc(myDisplay)
    glutKeyboardFunc(myKeyboard)
    glutSpecialFunc(mySpecialKeyboard)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
