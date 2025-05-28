from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480



def draw_polygon():
    """
    Draw a simple polygon within the defined 2D orthographic projection.
    Coordinates are chosen to ensure the shape is visible within the window.
    """
    glBegin(GL_POLYGON)
    glVertex2f(100, 100)
    glVertex2f(380, 100)
    glVertex2f(380, 380)
    glVertex2f(100, 380)
    glEnd()


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
    GLUT display callback:
        - Clears the screen.
        - Draws the polygon.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    draw_polygon()
    glFlush()


def main():
    """
    Main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Polygon in OpenGL")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
