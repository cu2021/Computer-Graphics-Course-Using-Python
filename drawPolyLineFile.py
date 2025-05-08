from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def drawPolyLineFile(filePath):
    """
    Reads a polyline file and renders its contents using OpenGL.

    File format:
    - First line: number of polylines.
    - For each polyline:
        - First line: number of points in the polyline.
        - Next N lines: (x, y) coordinates for each point.

    All polylines are drawn as connected line strips.

    Args:
        filePath (str): Path to the polyline data file.
    """
    try:
        with open(filePath, 'r') as f:
            # Clear the screen
            glClear(GL_COLOR_BUFFER_BIT)

            # Read number of polylines
            numpolys = int(f.readline())
            for _ in range(numpolys):
                # Read number of points in this polyline
                numLines = int(f.readline())

                # Start drawing connected lines
                glBegin(GL_LINE_STRIP)
                for _ in range(numLines):
                    # Read coordinates
                    x, y = map(int, f.readline().split())
                    # Plot the point
                    glVertex2i(GLint(x), GLint(y))
                glEnd()

            # Execute drawing commands
            glFlush()

    except FileNotFoundError:
        print(f"Error: Polyline data file '{filePath}' not found.")
    except ValueError:
        print(f"Error: Invalid data format in '{filePath}'. Ensure numbers are integers.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filePath}': {e}")

def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D projection setup.
    """
    # Set background to white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Set drawing color to black
    glColor3f(0.0, 0.0, 0.0)
    # Set line width
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
    drawPolyLineFile(r"data/dino.dat")

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
    glutCreateWindow(b"Dino Drawing from file")
    # Register myDisplay callback function
    glutDisplayFunc(myDisplay)
    # Initialize OpenGL settings
    myInit()
    # Enter the main event loop
    glutMainLoop()

if __name__ == "__main__":
    main()
