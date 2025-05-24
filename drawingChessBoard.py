from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Window dimensions (pixels)
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480


def drawChessBoard(square_size):
    """
    Draws an 8x8 chessboard with alternating white and gray squares.

    Parameters:
    square_size (int): The size (in pixels) of each square.
    """
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                glColor3f(1.0, 1.0, 1.0)  # White square
            else:
                glColor3f(0.5, 0.5, 0.5)  # Gray square

            # Draw square at position (col, row)
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            glRecti(x1, y1, x2, y2)


def myInit():
    """
    Initialize OpenGL settings: background color, drawing color,
    line width, and 2D orthographic projection.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Background: white
    glColor3f(0.0, 0.0, 0.0)  # Default drawing color
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)


def myDisplay():
    """
    GLUT display callback: clears the screen and draws an 8x8 chessboard.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    drawChessBoard(60)
    glFlush()


def main():
    """
    Main function to set up GLUT and run the application.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Draw Chessboard using glRecti")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()


if __name__ == "__main__":
    main()
