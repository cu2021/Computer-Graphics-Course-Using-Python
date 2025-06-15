from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT  import *

def myInit():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)

def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left ,right ,bottom ,top)

def setViewport(left, right, bottom, top):
    glViewport(int(left), int(bottom), int(right-left), int(top-bottom))

def drawDino(filePath):

    with open(filePath, 'r') as f:
        numpolys = int(f.readline())
        for _ in range(numpolys):
            numLines = int(f.readline())

            glBegin(GL_LINE_STRIP)
            for _ in range(numLines):
                x, y = map(int, f.readline().split())
                glVertex2i(GLint(x), GLint(y))
            glEnd()

        glFlush()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(10):
        for j in range(10):
            if (i+j)  % 2 == 0:
                setWindow(0, 640, 0, 480)
            else:
                setWindow(0, 640, 480, 0)

            glViewport(int(i*64),int(j*48),64,48)
            drawDino(r"data/dino.dat")
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutCreateWindow(b"Drawing dino from file and inside a viewport")
    myInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()