from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (in pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def myMovedMouse(mouseX, mouseY):
    """
    GLUT mouse motion callback function.

    Draws a filled rectangle (brush stroke) at the current mouse position
    as the mouse moves with a button held down. This simulates freehand drawing
    with a square brush.

    Parameters:
    -----------
    mouseX : int
        The x-coordinate of the mouse in window coordinates.

    mouseY : int
        The y-coordinate of the mouse in window coordinates. This will be converted
        to match OpenGL’s bottom-left origin coordinate system.
    """
    x = mouseX
    y = WINDOW_HEIGHT - mouseY  # Convert to OpenGL coordinates (bottom-left origin)
    brushSize = 20

    # Draw a filled rectangle representing the brush stroke
    glRecti(GLint(x), GLint(y), GLint(x + brushSize), GLint(y + brushSize))
    glFlush()


def myInit():
    """
    Initializes the OpenGL rendering context.

    - Sets the background color to white.
    - Sets the drawing color to black.
    - Defines line width for rendering.
    - Configures a 2D orthographic projection based on the window size.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background to white
    glColor3f(0.0, 0.0, 0.0)          # Set drawing color to black
    glLineWidth(2.0)                 # Set line thickness

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Set up orthographic projection


def myDisplay():
    """
    GLUT display callback function.

    Ensures all previously issued OpenGL commands are executed.
    No actual drawing is done here by default.
    """
    glFlush()


def main():
    """
    Entry point of the program.

    Sets up the GLUT framework:
    - Initializes display mode.
    - Creates the application window.
    - Registers callback functions.
    - Initializes OpenGL settings.
    - Starts the GLUT main loop to handle rendering and input.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Freehand Drawing with Mouse Movement")

    glutDisplayFunc(myDisplay)
    glutMotionFunc(myMovedMouse)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
