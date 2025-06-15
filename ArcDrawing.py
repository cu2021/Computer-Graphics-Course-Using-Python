from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

class Point2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def setPointXY(self, x,y):
        self.x = x
        self.y = y

    def set(self, p):
        self.x = p.x
        self.y = p.y

currPosition = Point2()
CP = Point2()

def moveTo(p):
    CP.set(p)

def lineTo(p):
    glBegin(GL_LINES)
    glVertex2f(CP.x, CP.y)
    glVertex2f(p.x, p.y)
    glEnd()
    glFlush()
    CP.set(p)

def myInit():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glLineWidth(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)

def drawArc(center, radius, startAngle, sweep):

    # Number of intermediate segments in Arc
    n = 200

    # converting start angle to be in radians value
    angle = (startAngle * 3.14159265) / 180

    angleIncrement = (sweep * 3.14159265) / (180*n)

    cx = center.x
    cy = center.y

    x = cx + radius*math.cos(angle)

    y = cy + radius*math.sin(angle)

    moveTo(Point2(x, y))

    for k in range(1,n):
        x = (cx + radius * math.cos(angle))
        y = (cy + radius * math.sin(angle))
        p = Point2(x,y)
        lineTo(p)
        angle += angleIncrement

def setWindow(left,right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom ,top)

def setViewport(left,right, bottom, top):
    glViewport(left,bottom, (right - left), (top - bottom))


def drawCircle(center, radius):
    glColor3f(0.0,0.0,1.0)
    drawArc(center, radius, 0,360)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    setWindow(0,400,0,400)
    setViewport(0,480,0,480)
    # drawArc(Point2(210,150), 20, 120, 180)
    # drawCircle(Point2(200,150), 50)

    # big circle
    drawCircle(Point2(200,200),200)

    # medium circles (0.5 * radius)
    drawCircle(Point2(100,200),100)
    drawCircle(Point2(300,200),100)

    # small circles 1/5 * medium radius
    drawCircle(Point2(100,200),20)
    drawCircle(Point2(300,200),20)


    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutCreateWindow(b"Drawing Arc")
    myInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
