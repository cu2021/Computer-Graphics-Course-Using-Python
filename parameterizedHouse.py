from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480



# Define a simple class to represent a 2D point
class GLintPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def parameterizedHouse(peak: GLintPoint, width: GLint, height: GLint):
    """
    Draws a scalable 2D wireframe house using OpenGL primitives.

    The house includes:
    - A main body with a peaked roof
    - A rectangular chimney
    - A centered front door (optional: with a doorknob)
    - A square window (optional: with cross panes)

    Args:
    -----------
    peak : GLintPoint
        The top peak of the house's roof (x, y coordinates).
    width : GLint
        The overall width of the house from left to right.
    height : GLint
        The overall height of the house from roof peak to base.
    """

    # Draw the outer shell of the house (including the roof)
    # Compute base coordinates for the roof and walls
    roofRightX = peak.x + width // 2
    roofLeftX = peak.x - width // 2

    # Height where the roof meets walls
    roofBaseY = peak.y - 3 * height // 8
    # Ground-level Y coordinate
    bottomY = peak.y - height

    glBegin(GL_LINE_LOOP)
    # Roof peak
    glVertex2i(peak.x, peak.y)
    # Right roof slope
    glVertex2i(roofRightX, roofBaseY)
    # Bottom-right corner
    glVertex2i(roofRightX, bottomY)
    # Bottom-left corner
    glVertex2i(roofLeftX, bottomY)
    # Left roof slope
    glVertex2i(roofLeftX, roofBaseY)
    glEnd()

    # draw chimney
    chimneyWidth = width // 10
    chimneyHeight = height // 4
    # Offset from peak
    chimneyX = peak.x - width // 5
    # Start lower than peak
    chimneyBaseY = peak.y - height // 6
    # Chimney height
    chimneyTopY = chimneyBaseY + chimneyHeight
    # Mid point for chimney bend
    chimneyMidY = chimneyBaseY + height // 11

    glBegin(GL_LINE_STRIP)
    # Bottom-left of chimney
    glVertex2i(chimneyX, chimneyBaseY)
    # Top-left of chimney
    glVertex2i(chimneyX, chimneyTopY)
    # Top-right of chimney
    glVertex2i(chimneyX + chimneyWidth, chimneyTopY)
    # Bottom-right of chimney
    glVertex2i(chimneyX + chimneyWidth, chimneyMidY)
    glEnd()

    # draw door
    doorWidth = width // 5
    doorHeight = height // 3
    doorX = peak.x - doorWidth // 2
    doorTopY = bottomY + doorHeight

    glBegin(GL_LINE_LOOP)
    # Bottom-left
    glVertex2i(doorX, bottomY)
    # Top-left
    glVertex2i(doorX, doorTopY)
    # Top-right
    glVertex2i(doorX + doorWidth, doorTopY)
    # Bottom-right
    glVertex2i(doorX + doorWidth, bottomY)
    glEnd()

    # Optional: Doorknob
    # doorknobX = doorX + doorWidth - doorWidth // 6
    # doorknobY = bottomY + doorHeight // 2
    #
    # glBegin(GL_POINTS)
    # glVertex2i(doorknobX, doorknobY)
    # glEnd()

    # draw window
    windowSize = width // 8
    windowX = peak.x - width // 4
    windowY = peak.y - height // 2
    windowRightX = windowX + windowSize
    windowTopY = windowY + windowSize

    glBegin(GL_LINE_LOOP)
    # Bottom-left
    glVertex2i(windowX, windowY)
    # Top-left
    glVertex2i(windowX, windowTopY)
    # Top-right
    glVertex2i(windowRightX, windowTopY)
    # Bottom-right
    glVertex2i(windowRightX, windowY)
    glEnd()

    #Optional: draw window cross
    # windowMidX = windowX + windowSize // 2
    # windowMidY = windowY + windowSize // 2
    #
    # glBegin(GL_LINES)
    # # Horizontal left
    # glVertex2i(windowX, windowMidY)
    # # Horizontal right
    # glVertex2i(windowRightX, windowMidY)
    # # Vertical bottom
    # glVertex2i(windowMidX, windowY)
    # # Vertical top
    # glVertex2i(windowMidX, windowTopY)
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
    parameterizedHouse(GLintPoint(220,300), 200, 100)

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
    glutCreateWindow(b"Parameterized House Drawing")
    # Register myDisplay callback function
    glutDisplayFunc(myDisplay)
    # Initialize OpenGL settings
    myInit()
    # Enter the main event loop
    glutMainLoop()

if __name__ == "__main__":
    main()