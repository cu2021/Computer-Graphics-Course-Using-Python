from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def drawFlurry(num: int, numColors: int, width: int, height: int):
    """
    Draws a flurry of random rectangles with grayscale shades.

    Parameters:
    - num: number of rectangles to draw.
    - numColors: the number of grayscale levels (e.g., 10 gives 0.0 to 0.9).
    - width: width of the drawable area.
    - height: height of the drawable area.
    """
    for _ in range(num):
        x1 = GLint(random.randint(0, width))
        y1 = GLint(random.randint(0, height))

        x2 = GLint(random.randint(0, width))
        y2 = GLint(random.randint(0, height))

        # Grayscale color
        lev = random.randint(0, numColors) / float(numColors)
        lev = GLfloat(lev)
        glColor3f(lev, lev, lev)

        glRecti(x1, y1, x2, y2)

    glFlush()


def myInit():
    """
    Initialize OpenGL settings: background color, line width,
    and 2D orthographic projection.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Background: white
    glColor3f(0.0, 0.0, 0.0)          # Default drawing color
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)


def myDisplay():
    """
    GLUT display callback: clears the screen and draws a flurry effect.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    drawFlurry(num=100, numColors=10, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    glFlush()


def main():
    """
    Main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Flurry of Rectangles")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
