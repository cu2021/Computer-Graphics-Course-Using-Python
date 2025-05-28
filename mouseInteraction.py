from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions in pixels
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# List to store coordinates of clicked points
dots = []


def draw_dot(x, y):
    """
    Appends a new dot at the specified (x, y) position
    and requests the window to be redrawn.

    Parameters:
        x (int): The x-coordinate of the clicked position.
        y (int): The y-coordinate of the clicked position.
    """
    dots.append((x, y))
    glutPostRedisplay()


def display():
    """
    GLUT display callback function.
    Clears the screen and renders all previously clicked dots.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POINTS)
    for x, y in dots:
        glVertex2i(x, y)
    glEnd()

    glFlush()


def myMouse(button, state, x, y):
    """
    GLUT mouse callback function.
    Adds a dot when the left mouse button is clicked, or exits
    the program when the right mouse button is clicked.

    Parameters:
        button (int): The mouse button (e.g., GLUT_LEFT_BUTTON).
        state (int): The state of the button (GLUT_DOWN or GLUT_UP).
        x (int): The x-coordinate of the mouse click.
        y (int): The y-coordinate of the mouse click (converted to OpenGL coordinates).
    """
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = WINDOW_HEIGHT - y  # Convert to OpenGL coordinate system
        draw_dot(x, y)
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        sys.exit(0)


def myInit():
    """
    Initializes the OpenGL rendering context:
    - Sets the background color to white.
    - Sets the drawing color to black.
    - Defines a 2D orthographic projection based on the window size.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)  # Black drawing color
    glPointSize(5.0)  # Size of drawn points
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, GLdouble(WINDOW_WIDTH), 0, GLdouble(WINDOW_HEIGHT))  # 2D orthographic projection


def main():
    """
    The main function initializes GLUT and OpenGL settings,
    creates the window, and starts the event-processing loop.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Click to Draw Dots, and Right Click to Exit")
    myInit()
    glutDisplayFunc(display)
    glutMouseFunc(myMouse)
    glutMainLoop()


if __name__ == "__main__":
    main()
