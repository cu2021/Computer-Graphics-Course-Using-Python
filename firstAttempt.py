from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

"""This Python code uses PyOpenGL to render a simple window with three points plotted using GL_POINTS"""
def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0, 0, 0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glVertex2i(100, 130)
    glVertex2i(150, 130)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"My First Attempt")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()

