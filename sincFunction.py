import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def MyInit():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)

def setWindow(left, right,bottom , top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right-left, top-bottom)


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    setWindow(-5.0,5.0,-0.3,1.0)
    setViewport(0,640,0,480)

    glBegin(GL_LINE_STRIP)
    x = -4.0
    while x <= 4.0:
        glVertex2f(GLfloat(x), GLfloat(math.sin(math.pi*x) / (math.pi*x)))
        x += 0.1
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Sinc Funtion Drawing")
    MyInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()

