from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

def set_window(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def set_viewport(left, right, bottom, top):
    glViewport(left, bottom, right - left, top - bottom)

def house():
    """
    Draws a hardcoded 2D wireframe house using OpenGL primitives.
    The house includes the shell, chimney, door, and window.
    """
    glBegin(GL_LINE_LOOP)
    glVertex2i(40, 40)
    glVertex2i(40, 90)
    glVertex2i(70, 120)
    glVertex2i(100, 90)
    glVertex2i(100, 40)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2i(50, 100)
    glVertex2i(50, 120)
    glVertex2i(60, 120)
    glVertex2i(60, 110)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2i(60, 40)
    glVertex2i(60, 70)
    glVertex2i(80, 70)
    glVertex2i(80, 40)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2i(50, 75)
    glVertex2i(50, 85)
    glVertex2i(60, 85)
    glVertex2i(60, 75)
    glEnd()

def initCT():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def scale2D(sx, sy):
    glMatrixMode(GL_MODELVIEW)
    glScaled(sx, sy, 1)

def translate2D(tx, ty):
    glMatrixMode(GL_MODELVIEW)
    glTranslated(tx, ty, 0.0)

def rotate2D(angle):
    glMatrixMode(GL_MODELVIEW)
    glRotated(angle, 0, 0, 1)

def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D projection setup.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(2.0)

def myDisplay():
    """
    GLUT display callback: clears the screen and draws the house and a transformed copy.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    set_window(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    set_viewport(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

    initCT()
    house()
    translate2D(100, 75)
    rotate2D(-30)
    house()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Transformed House")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()
