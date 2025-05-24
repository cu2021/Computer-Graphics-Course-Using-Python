from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

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

    # First rectangle: light gray
    glColor3f(0.6, 0.6, 0.6)
    # Bottom-left to top-right
    glRecti(20, 20, 100, 70)

    # Second rectangle: dark gray
    glColor3f(0.2, 0.2, 0.2)
    # Bottom-left to top-right
    glRecti(70, 50, 150, 130)

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
