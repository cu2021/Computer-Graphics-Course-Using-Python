from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random, time

# Seed the random number generator using the current system time
random.seed(time.time())

corner = []
numCorners = 0

SCREEN_HIEGHT = 480
SCREEN_WIDTH = 640


def randomI(m):
    """
    Return a random integer in the range [0, m-1].

    Args:
        m (int): Upper bound (exclusive) for the random selection.

    Returns:
        int: A randomly chosen integer.
    """
    return random.choice(range(0, m))


class GLintPoint:
    """
    Represents a 2D point with integer coordinates.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    """

    def __init__(self, x: GLint, y: GLint):
        """
        Initialize a GLintPoint with given x and y coordinates.

        Args:
            x (GLint): The x-coordinate.
            y (GLint): The y-coordinate.
        """
        self.x = x
        self.y = y


def drawDot(x: GLint, y: GLint):
    """
    Draw a single point at the specified (x, y) coordinates.

    Args:
        x (GLint): The x-coordinate of the point.
        y (GLint): The y-coordinate of the point.
    """
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def myInit():
    """
    Initialize the OpenGL rendering context.

    Sets up the background color, drawing color, projection matrix,
    and defines the 2D orthographic viewing region.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)  # Make the point size visible
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HIEGHT)


def Sierpinski(corners):
    """
    Generate and draw a Sierpinski triangle using the chaos game algorithm.

    Args:
        corners (list of GLintPoint): List of three corner points of the triangle.
    """
    T = corners
    index = randomI(3)
    point = GLintPoint(T[index].x, T[index].y)

    for _ in range(100000):
        index = randomI(3)
        point.x = (point.x + T[index].x) // 2
        point.y = (point.y + T[index].y) // 2
        drawDot(point.x, point.y)

    glFlush()


def myMouse(button, state, x, y):
    """
    GLUT mouse callback function to handle user input.

    Left-click to define triangle vertices interactively. Once three
    vertices are chosen, the Sierpinski triangle is drawn.

    Args:
        button (int): The mouse button pressed.
        state (int): The state of the button (pressed or released).
        x (int): The x-coordinate of the mouse click.
        y (int): The y-coordinate of the mouse click.
    """
    global corner, numCorners

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        corner.append(GLintPoint(x, SCREEN_HIEGHT - y))
        numCorners += 1

        if numCorners == 3:
            Sierpinski(corner)
            corner.clear()
            numCorners = 0


def myDisplay():
    """
    GLUT display callback function.

    Clears the screen to prepare for drawing.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()


def main():
    """
    Main function to set up the GLUT window and register callbacks.

    Initializes GLUT, sets display mode and window size, and enters the
    main event loop for rendering and interaction.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HIEGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Sierpinski Triangle by mouse")
    glutDisplayFunc(myDisplay)
    glutMouseFunc(myMouse)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
