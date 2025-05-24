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
    def __init__(self, x: GLint = 0, y: GLint = 0):
        self.x = x
        self.y = y


def drawRectangleCornerSize(topLeft: GLintPoint, width: int, aspectRatio: int):
    """
    Draws a rectangle given a top-left corner, width, and aspect ratio.

    Parameters:
    - topLeft: top-left corner as a GLintPoint.
    - width: width of the rectangle.
    - aspectRatio: width divided by height (e.g., 2 means height = width/2).
    """
    height = width // aspectRatio
    bottomRightX = GLint(topLeft.x + width)
    bottomRightY = GLint(topLeft.y - height)

    glRecti(topLeft.x, topLeft.y, bottomRightX, bottomRightY)


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
    GLUT display callback: clears the screen and draws the rectangle.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    topLeftCorner = GLintPoint(300, 300)
    drawRectangleCornerSize(topLeftCorner, width=80, aspectRatio=1)
    glFlush()


def main():
    """
    Main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Rectangle from Corner with Aspect Ratio")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
