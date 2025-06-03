from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def draw_a_cube():
    # Front face
    glBegin(GL_POLYGON)
    glVertex2i(100, 100)
    glVertex2i(200, 100)
    glVertex2i(200, 200)
    glVertex2i(100, 200)
    glEnd()

    # Back face
    glBegin(GL_POLYGON)
    glVertex2i(150, 150)
    glVertex2i(250, 150)
    glVertex2i(250, 250)
    glVertex2i(150, 250)
    glEnd()

    # Side faces
    glBegin(GL_QUAD_STRIP)

    # bottom-left
    glVertex2i(100, 100)
    glVertex2i(150, 150)

    # bottom-right
    glVertex2i(200, 100)
    glVertex2i(250, 150)

    # top-right
    glVertex2i(200, 200)
    glVertex2i(250, 250)

    # top-left
    glVertex2i(100, 200)
    glVertex2i(150, 250)

    #bottom-left (closing)
    glVertex2i(100, 100)
    glVertex2i(150, 150)

    glEnd()


def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D projection setup.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # white background
    glColor3f(0.0, 0.0, 0.0)          # black drawing color
    glLineWidth(2.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)


def myDisplay():
    """
    GLUT display callback: clears the screen and draws the cube.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    draw_a_cube()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"GL_POLYGON and GL_QUAD_STRIP")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
