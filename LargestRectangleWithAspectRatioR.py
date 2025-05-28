from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Drawing window size
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# User-specified aspect ratio (width / height)
R = float(input("Enter aspect ratio (width / height): "))

def myInit():
    """
    Initialize OpenGL settings: background color and orthographic projection.
    """
    # White background
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Black drawing color
    glColor3f(0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

def drawLagestRectWithAspectRatio():
    if R >= 1:
        # Width spans full window so that the height adjusted to maintain aspect ratio
        width = WINDOW_WIDTH
        height = WINDOW_WIDTH // R
    else:
        # Height spans full window so that the width adjusted to maintain aspect ratio
        height = WINDOW_HEIGHT
        width = int(WINDOW_HEIGHT * R)

    # bottom-left corner
    x1 = int((WINDOW_WIDTH - width) // 2)
    y1 = int((WINDOW_HEIGHT - height) // 2)

    # top-right corner
    x2 = int(x1 + width)
    y2 = int(y1 + height)

    # Draw filled rectangle
    glRecti(GLint(x1), GLint(y1), GLint(x2), GLint(y2))

def myDisplay():
    """
    Display callback that draws the largest possible rectangle with given aspect ratio.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    drawLagestRectWithAspectRatio()
    glFlush()


def main():
    """
    Main function to initialize GLUT and start the drawing loop.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Largest Rectangle with Aspect Ratio R")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
