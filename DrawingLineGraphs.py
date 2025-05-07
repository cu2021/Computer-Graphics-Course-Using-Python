from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window dimensions (pixels)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def f(x):
    """
    Function to be plotted.
    f(x) = 300 - 100 cos(2π x / 100) + 30 cos(4π x / 100) + 6 cos(6π x / 100)

    This is a mathematical function that generates a combination of cosines.
    It is used to create the data points that will be plotted in the OpenGL window.

    Args:
        x: A value in the domain of the function.

    Returns:
        y: The computed value of the function f(x) for the given x.
    """
    return (300
            - ((100 * math.cos((2 * math.pi * x) / 100)))
            + (30 * math.cos((4 * math.pi * x) / 100))
            + (6 * math.cos((6 * math.pi * x) / 100)))

def transform(x, y, y_min, y_max):
    """
    Transforms the (x, y) coordinates using the linear scaling and shifting equations:
    sx = A * x + B
    sy = C * y + D

    This function scales and shifts the coordinates to fit them within the window.

    Args:
        x: Raw x-coordinate.
        y: Raw y-coordinate.
        y_min: Minimum y value for the function (to calculate the scaling factor for y).
        y_max: Maximum y value for the function (to calculate the scaling factor for y).

    Returns:
        tuple: Transformed (sx, sy) coordinates, scaled and shifted to fit the window.
    """
    # Calculate scaling coefficients for x and y
    A = SCREEN_WIDTH / 300.0  # Scaling factor for x, assuming x values range from 0 to 300
    B = 0  # No shifting on x-axis
    C = SCREEN_HEIGHT / (y_max - y_min)  # Scaling factor for y
    D = -C * y_min  # Shift y values to fit the screen (ensures that minimum y aligns with screen bottom)

    # Apply the transformations
    x_transformed = A * x + B
    y_transformed = C * y + D
    return x_transformed, y_transformed


def myInit():
    """
    OpenGL initialization function to set up the background color, line width,
    and the orthographic projection for the 2D plot.

    This function sets the OpenGL environment, such as background color, drawing color,
    and matrix mode. It prepares the 2D orthographic projection where the plot will be drawn.
    """
    # Set background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    # Set drawing color to black
    glColor3f(0.0, 0.0, 0.0)
    # Set point size for drawing (for visualizing individual points)
    glPointSize(2.0)
    # Set matrix mode to projection (set up the view of the 2D space)
    glMatrixMode(GL_PROJECTION)
    # Reset the matrix to identity (clear any previous transformations)
    glLoadIdentity()
    # Set 2D orthographic projection with origin at bottom-left corner
    gluOrtho2D(0, GLdouble(SCREEN_WIDTH), 0, GLdouble(SCREEN_HEIGHT))


def myDisplay():
    """
    OpenGL display callback function to clear the screen and draw the transformed function.

    This function is called whenever the window needs to be redrawn. It clears the screen,
    calculates the data points, transforms them for screen coordinates, and plots the function.
    """
    # Clear the screen for the next frame
    glClear(GL_COLOR_BUFFER_BIT)

    # Generate x values from 0 to 300, in steps of 3
    x_values = list(range(0, 301, 3))
    # Calculate corresponding y values using the function f(x)
    y_values = [f(x) for x in x_values]

    # Find the minimum and maximum y values to compute the scaling factor for y
    y_min = min(y_values)
    y_max = max(y_values)

    glBegin(GL_LINE_STRIP)  # Begin drawing a line strip (a connected series of lines)

    # Transform each (x, y) and plot it
    for x in x_values:
        # Get y value
        y = f(x)

        # Transform x and y coordinates
        sx, sy = transform(x, y, y_min, y_max)

        # Draw the transformed coordinates
        glVertex2d(GLdouble(sx), GLdouble(sy))

    # End drawing
    glEnd()

    # Execute drawing commands
    glFlush()


def main():
    """
    The main function to initialize GLUT, set window properties, and start the GLUT event loop.

    This function sets up the GLUT window, defines display properties, and starts the main loop
    to handle drawing, events, and updates.
    """
    # Initialize GLUT
    glutInit(sys.argv)
    # Use single buffering and RGB color mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set the window size
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    # Set window position on the screen
    glutInitWindowPosition(100, 150)
    # Create the window with a title
    glutCreateWindow(b"Drawing Line Graph")

    # Set the display callback function
    glutDisplayFunc(myDisplay)

    # Perform OpenGL initializations
    myInit()
    # Enter the main GLUT event loop
    glutMainLoop()


if __name__ == "__main__":
    main()  # Start the program
