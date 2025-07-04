from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(1.5)

def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def setViewport(left, right, bottom, top):
    glViewport(int(left), int(bottom), int(right - left), int(top - bottom))

def drawDino(filePath):
    with open(filePath, 'r') as f:
        numpolys = int(f.readline())
        for _ in range(numpolys):
            numLines = int(f.readline())
            glBegin(GL_LINE_STRIP)
            for _ in range(numLines):
                x, y = map(int, f.readline().split())
                glVertex2i(x, y)
            glEnd()

def initCT():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def scale2D(sx, sy):
    glMatrixMode(GL_MODELVIEW)
    glScaled(sx, sy, 1)

def translate2D(tx, ty):
    glMatrixMode(GL_MODELVIEW)
    glTranslated(tx, ty, 0.0)

def rotate2D(angle):
    glMatrixMode(GL_MODELVIEW)
    glRotated(angle, 0, 0, 1)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

    # Set viewport and logical window
    setViewport(0, 640, 0, 480)
    setWindow(-2.0, 2.0, -2.0, 2.0)

    numMotifs = 12
    for i in range(numMotifs):
        initCT()
        rotate2D(i * 360 / numMotifs)
        translate2D(0.0, 0.80)
        scale2D(0.001, 0.001)
        drawDino("data/dino.dat")

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b"Drawing dino in a circular motif using viewport and window")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()
