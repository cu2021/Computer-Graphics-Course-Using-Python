from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

def drawFlurry(num: int, numColors: int, Width: int, Height: int ):
    for i in range(num):
        x1 = GLint(random.choice(range(0,Width)))
        y1 = GLint(random.choice(range(0,Height)))

        x2 = GLint(random.choice(range(0, Width)))
        y2 = GLint(random.choice(range(0, Height)))

        lev = GLfloat(random.choice(range(0, numColors))/10.0)

        glColor3f(lev, lev, lev)
        glRecti(x1, y1, x2, y2)

        glFlush()

def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D orthographic projection.
    """
    # Background color: white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Default drawing color
    glColor3f(0.0, 0.0, 0.0)
    # Line width
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, GLdouble(WINDOW_WIDTH), 0, GLdouble(WINDOW_HEIGHT))


def myDisplay():
    """
    GLUT display callback: clears the screen and draws two rectangles.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    drawFlurry(num=100, numColors=10, Width=WINDOW_WIDTH, Height=WINDOW_HEIGHT)
    # Ensure all drawing commands are executed
    glFlush()


def main():
    """
    The main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Two Rectangles using glRecti")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
