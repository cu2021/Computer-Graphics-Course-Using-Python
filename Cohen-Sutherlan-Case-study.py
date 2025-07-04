from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # White background
    glColor3f(0.0, 0.0, 0.0)  # Black drawing color
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)  # Coordinate system: (0,0) bottom-left, (640,480) top-right


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
    if p.x < window.l:
        code |= 8  # Left
    if p.y > window.t:
        code |= 4  # Top
    if p.x > window.r:
        code |= 2  # Right
    if p.y < window.b:
        code |= 1  # Bottom
    return code


def trivialAccept(p1_code, p2_code):
    return p1_code == 0 and p2_code == 0


def trivialReject(p1_code, p2_code):
    return p1_code & p2_code != 0


def clipSegment(p1: Point2, p2: Point2, w: RealRect):
    # Create copies to avoid modifying original points
    p1 = Point2(p1.x, p1.y)
    p2 = Point2(p2.x, p2.y)

    while True:
        print("p1: x:", p1.x, "| y: ", p1.y)
        print("p2: x:", p2.x, "| y: ", p2.y)

        p1_code = outCodes(p1, w)
        p2_code = outCodes(p2, w)

        # Trivial accept: both points inside
        if trivialAccept(p1_code, p2_code):
            print("p1: x:", p1.x, "| y: ", p1.y)
            print("p2: x:", p2.x, "| y: ", p2.y)

            return True, p1, p2

        # Trivial reject: both points on the same side of a boundary
        if trivialReject(p1_code, p2_code):
            print("p1: x:", p1.x, "| y: ", p1.y)
            print("p2: x:", p2.x, "| y: ", p2.y)

            return False, None, None

        # Check for vertical line to avoid division by zero
        if abs(p2.x - p1.x) < 1e-6:  # Vertical line
            m = None  # Slope undefined
        else:
            m = (p2.y - p1.y) / (p2.x - p1.x)

        # Process p1 if it's outside
        if p1_code != 0:
            x0, y0 = p1.x, p1.y
            if p1_code & 8:  # Left
                p1.x = w.l
                if m is not None:
                    p1.y = m * (p1.x - x0) + y0
                else:
                    p1.y = y0
            elif p1_code & 4:  # Top
                p1.y = w.t
                if m is not None:
                    p1.x = ((p1.y - y0) / m) + x0 if m != 0 else x0
                else:
                    p1.x = x0
            elif p1_code & 2:  # Right
                p1.x = w.r
                if m is not None:
                    p1.y = m * (p1.x - x0) + y0
                else:
                    p1.y = y0
            elif p1_code & 1:  # Bottom
                p1.y = w.b
                if m is not None:
                    p1.x = ((p1.y - y0) / m) + x0 if m != 0 else x0
                else:
                    p1.x = x0
        # Process p2 if it's outside
        else:
            x0, y0 = p2.x, p2.y
            if p2_code & 8:  # Left
                p2.x = w.l
                if m is not None:
                    p2.y = m * (p2.x - x0) + y0
                else:
                    p2.y = y0
            elif p2_code & 4:  # Top
                p2.y = w.t
                if m is not None:
                    p2.x = ((p2.y - y0) / m) + x0 if m != 0 else x0
                else:
                    p2.x = x0
            elif p2_code & 2:  # Right
                p2.x = w.r
                if m is not None:
                    p2.y = m * (p2.x - x0) + y0
                else:
                    p2.y = y0
            elif p2_code & 1:  # Bottom
                p2.y = w.b
                if m is not None:
                    p2.x = ((p2.y - y0) / m) + x0 if m != 0 else x0
                else:
                    p2.x = x0


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

    # Define clipping window (adjusted to have height)
    w = RealRect(100, 350, 350, 100)

    # Define line segment
    p1 = Point2(20, 120)
    p2 = Point2(380, 380)

    # Draw clipping window in blue
    glColor3f(0.0, 0.0, 1.0)
    drawRect(w)

    # Draw original line in red (before clipping)
    glColor3f(1.0, 0.0, 0.0)
    drawLine(p1, p2)

    # Perform clipping
    accept, clipped_p1, clipped_p2 = clipSegment(p1, p2, w)

    # Draw clipped line in green if accepted
    if accept:
        glColor3f(0.0, 1.0, 0.0)
        drawLine(clipped_p1, clipped_p2)

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Cohen-Sutherland Line Clipping")
    myInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()


if __name__ == "__main__":
    main()