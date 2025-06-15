from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

class Point2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def setPoint2XY(self, x, y):
        self.x = x
        self.y = y

    def set(self, p):
        self.x = p.x
        self.y = p.y

currentPosition = Point2()
CP = Point2()

def moveTo(point: Point2):
    CP.set(point)

def lineTo(p: Point2):
    glBegin(GL_LINES)
    glVertex2f(CP.x, CP.y)
    glVertex2f(p.x, p.y)
    glEnd()
    glFlush()
    CP.set(p)

def myInit():
    glClearColor(1.0,0.0,0.0,0.0)
    glColor3f(0.0,0.0,1.0)
    glLineWidth(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,640,0,480)

def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def setViewport(left, right, bottom, top):
    glViewport(left, bottom, (right-left), (top-bottom))

def ngon(N, radius):
    if N < 3:
        return

    points = []
    theta = (2.0*math.pi)/N

    for c in range(N):
        x =  radius*(math.cos(theta*c))
        y =  radius*(math.sin(theta*c))
        points.append(Point2(x,y))

    # Drawing
    moveTo(points[0])

    for i in range(1,N):
        lineTo(points[i])

    lineTo(points[0])

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    setWindow(-1,1,-1,1)
    glViewport(0,0,480,480)
    ngon(6,0.66)
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"N-gon (Regular Polygons)")
    myInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
