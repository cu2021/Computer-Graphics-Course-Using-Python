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

    def set(self, point):
        self.x = point.x
        self.y = point.y

CP = Point2()

def moveTo(point: Point2):
    CP.set(point)

def lineTo(p: Point2):
    glBegin(GL_LINES)
    glVertex2f(CP.x, CP.y)
    glVertex2f(p.x, p.y)
    glEnd()
    CP.set(p)

def myInit():
    glClearColor(1.0, 0.0, 0.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 480.0, 0.0, 480.0)

def stellation(N, step, radius):
    if N < 3 or step <= 0:
        return

    pointList = []
    theta = (2.0 * math.pi) / N

    for i in range(N):
        x = radius * math.cos(theta * i)
        y = radius * math.sin(theta * i)
        pointList.append(Point2(x, y))

    for i in range(N):
        j = (i + step) % N
        moveTo(pointList[i])
        lineTo(pointList[j])

def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right - left, top - bottom)

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    setWindow(-1, 1, -1, 1)
    setViewport(0, 480, 0, 480)
    stellation(7, 2, 0.8)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Stellation Diagram")
    myInit()
    glutDisplayFunc(render)
    glutMainLoop()

if __name__ == "__main__":
    main()
