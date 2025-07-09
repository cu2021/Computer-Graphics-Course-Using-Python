from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Global variables
clickedPoints = []
linesToDraw = []  # stores tuples of (color, p1, p2)
w = None  # clipping window

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RealRect:
    def __init__(self, l, t, r, b):
        self.l = l
        self.t = t
        self.r = r
        self.b = b

def outCodes(p: Point2, window: RealRect):
    code = 0
    if p.x < window.l: code |= 8
    if p.y > window.t: code |= 4
    if p.x > window.r: code |= 2
    if p.y < window.b: code |= 1
    return code

def trivialAccept(c1, c2):
    return c1 == 0 and c2 == 0

def trivialReject(c1, c2):
    return (c1 & c2) != 0

def clipSegment(p1: Point2, p2: Point2, w: RealRect):
    p1 = Point2(p1.x, p1.y)
    p2 = Point2(p2.x, p2.y)

    while True:
        code1 = outCodes(p1, w)
        code2 = outCodes(p2, w)

        if trivialAccept(code1, code2):
            return True, p1, p2

        if trivialReject(code1, code2):
            return False, None, None

        if abs(p2.x - p1.x) < 1e-6:
            m = None
        else:
            m = (p2.y - p1.y) / (p2.x - p1.x)

        if code1 != 0:
            x0, y0 = p1.x, p1.y
            if code1 & 8:
                p1.x = w.l
                p1.y = m * (p1.x - x0) + y0 if m is not None else y0
            elif code1 & 4:
                p1.y = w.t
                p1.x = ((p1.y - y0) / m) + x0 if m not in (None, 0) else x0
            elif code1 & 2:
                p1.x = w.r
                p1.y = m * (p1.x - x0) + y0 if m is not None else y0
            elif code1 & 1:
                p1.y = w.b
                p1.x = ((p1.y - y0) / m) + x0 if m not in (None, 0) else x0
        else:
            x0, y0 = p2.x, p2.y
            if code2 & 8:
                p2.x = w.l
                p2.y = m * (p2.x - x0) + y0 if m is not None else y0
            elif code2 & 4:
                p2.y = w.t
                p2.x = ((p2.y - y0) / m) + x0 if m not in (None, 0) else x0
            elif code2 & 2:
                p2.x = w.r
                p2.y = m * (p2.x - x0) + y0 if m is not None else y0
            elif code2 & 1:
                p2.y = w.b
                p2.x = ((p2.y - y0) / m) + x0 if m not in (None, 0) else x0

def drawRect(rect: RealRect):
    glBegin(GL_LINE_LOOP)
    glVertex2f(rect.l, rect.b)
    glVertex2f(rect.r, rect.b)
    glVertex2f(rect.r, rect.t)
    glVertex2f(rect.l, rect.t)
    glEnd()

def drawLine(p1: Point2, p2: Point2):
    glBegin(GL_LINES)
    glVertex2f(p1.x, p1.y)
    glVertex2f(p2.x, p2.y)
    glEnd()

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    drawRect(w)

    for color, p1, p2 in linesToDraw:
        glColor3f(color[0], color[1], color[2])
        drawLine(p1, p2)

    glFlush()

def myMouse(button, state, x, y):
    global clickedPoints, linesToDraw  # Include both variables here

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = 480 - y
        clickedPoints.append(Point2(x, y))

        if len(clickedPoints) == 2:
            p1, p2 = clickedPoints
            red = (1.0, 0.0, 0.0)
            linesToDraw.append((red, p1, p2))

            accept, cp1, cp2 = clipSegment(p1, p2, w)
            if accept:
                green = (0.0, 1.0, 0.0)
                linesToDraw.append((green, cp1, cp2))

            clickedPoints = []

            # Redraw everything manually here
            glClear(GL_COLOR_BUFFER_BIT)
            glColor3f(0.0, 0.0, 1.0)
            drawRect(w)

            for color, p1, p2 in linesToDraw:
                glColor3f(*color)
                drawLine(p1, p2)

            glFlush()

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        linesToDraw = []
        clickedPoints = []

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 0.0, 1.0)
        drawRect(w)
        glFlush()


def main():
    global w
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cohen-Sutherland Line Clipping (Mouse Input)")
    myInit()
    w = RealRect(100, 350, 350, 100)
    glutDisplayFunc(myDisplay)
    glutMouseFunc(myMouse)
    glutMainLoop()

if __name__ == "__main__":
    main()
