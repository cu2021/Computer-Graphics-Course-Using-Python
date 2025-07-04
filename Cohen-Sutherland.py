from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys



def myInit():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,640,0,480)

class Point2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class RealRect:
    def __init__(self,l,t,r,b):
        self.l = l
        self.t = t
        self.r = r
        self.b = b

def clipSegment(p1: Point2, p2:Point2, w:RealRect):
    m = (p2.y - p1.y) / (p2.x - p1.x)

    while(True):
        print("p1.x= ", p1.x, "p1.y= ", p1.y)
        print("p2.x= ", p2.x, "p2.y= ", p2.y)

        p1_code = outCodes(p1, w)
        p2_code = outCodes(p2, w)


        if(trivialAccept(p1_code,p2_code)):
            return 1

        if(trivialReject(p1_code,p2_code)):
            return 0

        if p1_code != 0:

            if p1_code & 8:
                x0 = p1.x
                y0 = p1.y
                p1.x = w.l
                p1.y = (m * (p1.x - x0)) + y0

            elif p1_code & 4:
                x0 = p1.x
                y0 = p1.y
                p1.y = w.t
                p1.x = ((p1.y - y0) / m) + x0

            elif p1_code & 2:
                x0 = p1.x
                y0 = p1.y
                p1.x = w.r
                p1.y = (m * (p1.x - x0)) + y0

            elif p1_code & 1:
                x0 = p1.x
                y0 = p1.y
                p1.y = w.b
                p1.x = ((p1.y - y0) / m) + x0

        else:

            if p2_code & 8:
                x0 = p2.x
                y0 = p2.y
                p2.x = w.l
                p2.y = m * (p2.x - x0) + y0

            elif p2_code & 4:
                x0 = p2.x
                y0 = p2.y
                p2.y = w.t
                p2.x = ((p2.y - y0) / m) + x0

            elif p2_code & 2:
                x0 = p2.x
                y0 = p2.y
                p2.x = w.r
                p2.y = m * (p2.x - x0) + y0

            elif p2_code & 1:
                x0 = p2.x
                y0 = p2.y
                p2.y = w.b
                p2.x = ((p2.y - y0) / m) + x0

def outCodes(p:Point2, window: RealRect):
    code = 0
    if p.x < window.l:
        code |= 8
    if p.y > window.t:
        code |= 4
    if p.x > window.r:
        code |= 2
    if p.y < window.b:
        code |= 1
    return code

def trivialAccept(p1_code, p2_code):
    if p1_code == 0 and p2_code == 0:
        return True
    return False

def trivialReject(p1_code, p2_code):
    if p1_code & p2_code != 0:
        return True
    return False



def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

    w = RealRect(50,200,200,200)

    p1 = Point2(20,120)
    p2 = Point2(220,300)

    clipSegment(p1,p2,w)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Cohen-Sutherland Algorithm")
    myInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
