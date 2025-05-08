from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def hardwiredHouse():
    """
    Draws a hardcoded 2D wireframe house using OpenGL primitives.
    The house includes the shell, chimney, door, and window.
    """

    # Draw the outer shell of the house (including the roof)
    glBegin(GL_LINE_LOOP)
    glVertex2i(40, 40)   # Bottom-left
    glVertex2i(40, 90)   # Top-left wall
    glVertex2i(70, 120)  # Roof peak
    glVertex2i(100, 90)  # Top-right wall
    glVertex2i(100, 40)  # Bottom-right
    glEnd()

    # Draw the chimney on the roof
    glBegin(GL_LINE_STRIP)
    # Bottom-left of chimney
    glVertex2i(50, 100)
    # Top-left
    glVertex2i(50, 120)
    # Top-right
    glVertex2i(60, 120)
    # Bottom-right
    glVertex2i(60, 110)
    glEnd()

    # Draw the door on the front of the house
    glBegin(GL_LINE_LOOP)
    # Bottom-left
    glVertex2i(60, 40)
    # Top-left
    glVertex2i(60, 70)
    # Top-right
    glVertex2i(80, 70)
    # Bottom-right
    glVertex2i(80, 40)
    glEnd()

    # Optional: Draw the doorknob as a single point
    # glBegin
    # Doorknob position
    # glVertex2i(75, 55)
    # glEnd()

    # Draw the window on the house
    glBegin(GL_LINE_LOOP)
    # Bottom-left
    glVertex2i(50, 75)
    # Top-left
    glVertex2i(50, 85)
    # Top-right
    glVertex2i(60, 85)
    # Bottom-right
    glVertex2i(60, 75)
    glEnd()

    # Optional: Draw the window cross
    # glBegin(GL_LINES)
    # Horizontal middle
    # glVertex2i(50, 80)
    # glVertex2i(60, 80)
    # Vertical middle
    # glVertex2i(55, 75)
    # glVertex2i(55, 85)
    # glEnd()



def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    Line width, and 2D projection setup.
    """
    # Set background to white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Set drawing color to black
    glColor3f(0.0, 0.0, 0.0)

    # Set Line Width
    glLineWidth(2.0)
    # Set matrix mode to projection
    glMatrixMode(GL_PROJECTION)
    # Reset projection matrix
    glLoadIdentity()

    # Define 2D orthographic projection
    gluOrtho2D(0, GLdouble(WINDOW_WIDTH), 0, GLdouble(WINDOW_HEIGHT))

def myDisplay():
    """
    GLUT display callback: clears the screen and draws the centered hashtag symbol.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the house
    hardwiredHouse()

    # Ensure all drawing commands are completed
    glFlush()


def main():
    """The main function to set up GLUT and run the application.

    Initializes GLUT, creates a window, sets up display and keyboard callbacks,
    calls initialization functions, and enters the GLUT event processing loop.
    """
    # Initialize GLUT
    glutInit(sys.argv)
    # Single buffer and RGB color
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set window size
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    # Set window position
    glutInitWindowPosition(100, 150)

    # Create the window with a title
    glutCreateWindow(b"Hardwired House")
    # Register myDisplay callback function
    glutDisplayFunc(myDisplay)
    # Initialize OpenGL settings
    myInit()
    # Enter the main event loop
    glutMainLoop()

if __name__ == "__main__":
    main()
