from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 

bg = (1.0,1.0,1.0,1.0)
angle = 0.0

class Raindrop:
    def __init__(self, cor_x, cor_y, speed):
        self.x = cor_x
        self.y = cor_y
        self.speed = speed

raindrops = []
for i in range(300):
    l = random.uniform(0, 600)
    r = random.uniform(0, 500)
    speed = random.uniform(3, 8)  
    raindrops.append(Raindrop(l, r, speed))

def drawRaindrop(x1, y1): 
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x1, y1 + 8)  
    glEnd()

def rain_drops() : 
    global angle 
    for raindrop in raindrops:

        raindrop.x += angle 
        raindrop.y -= raindrop.speed
        
        if (raindrop.y < 0):
            raindrop.y = random.uniform(0, 500)
            raindrop.x = random.uniform(0, 500)

def draw_house(): 
    glColor3f(0.75,0.75, 0.75) 
    glPointSize(5) 
    glLineWidth(10)
    glColor3f(0.75,0.75,0.75)
    glBegin(GL_LINES)

    #roof 
    glVertex2f(400,300)
    glVertex2f(100,300)
    glVertex2f(400,300)
    glVertex2f(250,400)
    glVertex2f(100,300)
    glVertex2f(250,400)

    #body
    glVertex2f(380,300)
    glVertex2f(380,100)
    glVertex2f(120,300)
    glVertex2f(120,100)
    glVertex2f(115,100)
    glVertex2f(385,100)
    glEnd()

    glPointSize(5)
    glLineWidth(2)
    glBegin(GL_LINES)

    # door 
    glVertex2f(140,100) 
    glVertex2f(140,200)
    glVertex2f(200,100)
    glVertex2f(200,200)
    glVertex2f(140,200)
    glVertex2f(200,200)

    #window 
    glVertex2f(350,200)
    glVertex2f(350,250)
    glVertex2f(300,200)
    glVertex2f(300,250)
    glVertex2f(350,250)
    glVertex2f(300,250)
    glVertex2f(350,200)
    glVertex2f(300,200)
    glVertex2f(300,225)
    glVertex2f(350,225)
    glVertex2f(325,250)
    glVertex2f(325,200)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    # door lock 
    glVertex2f(190,120)
    glEnd()

def specialKeyListener(key, x, y): 
    global angle 
    if key==GLUT_KEY_RIGHT:
        angle += 1.0 
        print("Tilt Right")
    if key== GLUT_KEY_LEFT:		
        angle -= 1.0  
        print("Tilt Left")
    
    glutPostRedisplay()

def keyboardListener(key, x, y): 
    global bg

    if (key == b'n'): 
        bg = (0.0,0.0,0.0,0.0)
        print("It's night")
    if (key == b'm'):
        bg = (1.0,1.0,1.0,1.0)
        print("It's morning")
         
    glutPostRedisplay()

def animation() :
    rain_drops()
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():

    glClearColor(*bg)
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()

   
    for raindrop in raindrops:
        drawRaindrop(raindrop.x, raindrop.y)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"CSE423 Assignment 1 Part 1") 
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)
glutMainLoop()