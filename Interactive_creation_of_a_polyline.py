from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (in pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Maximum number of points in the polyline
NUM = 20
points = []  # Stores GLintPoint objects
last = -1    # Index of the last added point


class GLintPoint:
    """
    Represents a 2D point with integer coordinates.
    """
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


def myMouse(button, state, x, y):
    """
    GLUT mouse callback function to handle interactive polyline drawing.

    - Left-click (GLUT_LEFT_BUTTON): Adds a new point to the polyline.
      The point is created at the mouse click position and adjusted for
      OpenGL's coordinate system.
    - Right-click (GLUT_RIGHT_BUTTON): Clears all previously drawn points
      and resets the canvas.

    Parameters:
    -----------
    button : int
        The mouse button that triggered the event (GLUT_LEFT_BUTTON or GLUT_RIGHT_BUTTON).
    state : int
        The state of the button (GLUT_DOWN or GLUT_UP).
    x : int
        The x-coordinate of the mouse click in window space.
    y : int
        The y-coordinate of the mouse click in window space (converted to OpenGL space).
    """
    global points, last

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and (last < NUM - 1):
        new_point = GLintPoint(x, WINDOW_HEIGHT - y)
        points.append(new_point)
        last += 1

        # Redraw the line strip with new point
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_LINE_STRIP)
        for p in points:
            glVertex2i(p.x, p.y)
        glEnd()
        glFlush()

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        # Clear the polyline on right click
        last = -1
        points.clear()
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()


def myInit():
    """
    Initializes the OpenGL environment.

    Sets the background color to white and the drawing color to black.
    Configures the line width for rendering the polyline and sets up
    an orthographic 2D projection based on the window dimensions.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glColor3f(0.0, 0.0, 0.0)          # Black drawing color
    glLineWidth(2.0)                 # Line thickness

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)


def myDisplay():
    """
    GLUT display callback function.

    Currently used to flush OpenGL drawing commands to ensure all
    rendering operations are completed.
    """
    glFlush()


def main():
    """
    Entry point of the application.

    Initializes the GLUT framework, configures the display mode,
    sets up the window, registers display and mouse callback functions,
    initializes OpenGL state, and starts the GLUT event loop.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Polyline using Mouse Clicks")

    glutDisplayFunc(myDisplay)
    glutMouseFunc(myMouse)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
