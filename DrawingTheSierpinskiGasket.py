from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random, time

# Seed the random number generator using the current system time
random.seed(time.time())

#define the random function
def randomI(m):
    return random.choice(range(0, m))




# Define a simple class to represent 2D points with integer coordinates
class GLintPoint:
    def __init__(self, x: GLint, y: GLint):
        self.x = x
        self.y = y


# Draw a single point at the specified (x, y) coordinates
def drawDot(x: GLint, y: GLint):
    glBegin(GL_POINTS)  # Begin specifying points
    glVertex2i(x, y)  # Specify a vertex at (x, y)
    glEnd()  # End the specification


# Initialize OpenGL rendering context
def myInit():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor3f(0.0, 0.0, 0.0)  # Set drawing color to black
    # glPointSize(4.0)       # set point size to 4 pixel
    glMatrixMode(GL_PROJECTION)  # Set current matrix mode to projection
    glLoadIdentity()  # Reset projection matrix
    gluOrtho2D(0, 640.0, 0, 480.0)  # Set up orthographic 2D view (origin at bottom-left)


# Generate and draw the Sierpinski triangle using a chaos game approach
def Sierpinski():
    # Define 3 vertices of a triangle
    T = [GLintPoint(10, 10), GLintPoint(300, 30), GLintPoint(200, 300)]

    # Randomly choose one of the triangle's vertices to start from
    index = randomI(3)
    point = GLintPoint(T[index].x, T[index].y)

    # Generate and plot 100,000 points inside the triangle
    for _ in range(100000):
        index = randomI(3)  # Randomly choose a triangle vertex
        point.x = (point.x + T[index].x) // 2  # Move halfway towards that vertex (x)
        point.y = (point.y + T[index].y) // 2  # Move halfway towards that vertex (y)
        drawDot(point.x, point.y)  # Draw the new point

    glFlush()  # Ensure all drawing commands are completed


# GLUT display callback function — clears the screen and draws the fractal
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    Sierpinski()  # Generate and draw the Sierpinski triangle
    glFlush()  # Execute OpenGL commands


def main():
    glutInit(sys.argv)  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffering and RGB color mode
    glutInitWindowSize(640, 480)  # Set the window size
    glutInitWindowPosition(100, 150)  # Set window position on the screen
    glutCreateWindow(b"Sierpinski Triangle")  # Create window with title
    glutDisplayFunc(myDisplay)  # Set the display callback function
    myInit()  # Perform OpenGL initializations
    glutMainLoop()  # Enter the main GLUT event loop


if __name__ == "__main__":
    main()
