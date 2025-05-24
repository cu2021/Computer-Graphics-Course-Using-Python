from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480


class GLintPoint:
    """
    Represents a 2D point with integer coordinates.
    """
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


def drawRectangleFromCenterPoint(center: GLintPoint, width: int, height: int):
    """
    Draws a rectangle using a central point and given width and height.

    Parameters:
    - center: the central GLintPoint.
    - width: width of the rectangle.
    - height: height of the rectangle.
    """

    # top-left x
    x1 = GLint(center.x - (width//2))
    y1 = GLint(center.y + (height//2))

    # buttom-right
    x2 = GLint(center.x + (width//2))
    y2 = GLint(center.y - (height//2))

    glRecti(x1, y1, x2, y2)


def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D orthographic projection.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Background: white
    glColor3f(0.0, 0.0, 0.0)          # Drawing color: black
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)


def myDisplay():
    """
    GLUT display callback: clears the screen and draws a centered rectangle.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    center = GLintPoint(300, 300)
    drawRectangleFromCenterPoint(center, width=80, height=80)
    glFlush()


def main():
    """
    Main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Rectangle from Center Point")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
