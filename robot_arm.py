import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

shoulder, elbow = 0, 0
ang, first_finger, second_finger = 0, 0, 0
origem = GLint()

def init(display):
   glutInit([])

   glClearColor(0.0, 0.0, 0.0, 0.0) # define a cor de fundo

   # Define a transformação de projeção (caracteristicas da camera)
   gluPerspective(30, (display[0]/display[1]), 0.1, 50.0)

   glTranslatef(0.0, 0.0, -15)

   drawOrigin()

def drawOrigin():
   global origem
   
   origem = glGenLists(1)
   glNewList(origem, GL_COMPILE)
   glBegin(GL_LINES)
   glColor3f(1,0,0) # x
   glVertex3i(0,0,0)
   glVertex3i(1,0,0)

   glColor3f(0,1,0) # y
   glVertex3i(0,0,0)
   glVertex3i(0,1,0)

   glColor3f(0,0,1) # z
   glVertex3i(0,0,0)
   glVertex3i(0,0,1)
   glEnd()
   glEndList()

def desenha():
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glLineWidth(1)

   glPushMatrix()
   glRotatef(ang, 0, 1, 0)
   glCallList(origem)
   
   glTranslatef(-1.0, 0.0, 0.0)
   glRotatef(shoulder, 0.0, 0.0, 1.0)
   glTranslatef(1.0, 0.0, 0.0)
   glPushMatrix()
   glScalef(2.0, 0.4, 1.0)
   glutWireCube(1.0)
   glPopMatrix()

   glTranslatef(1.0, 0.0, 0.0)
   glRotatef(elbow, 0.0, 0.0, 1.0)
   glTranslatef(1.0, 0.0, 0.0)
   glPushMatrix()
   glScalef(2.0, 0.4, 1.0)
   glutWireCube(1.0)
   glPopMatrix()

   glTranslatef(1.0, 0.0, 0.0)
   glPushMatrix()
   glRotatef(first_finger, 0.0, 0.0, 1.0)
   glTranslatef(0.0, 0.2, 0.0)
   glColor3f(0.0, 1.0, 0.0)
   glLineWidth(5)
   glBegin(GL_LINES)
   glVertex2f(0, 0)
   glVertex2f(0.4, 0)
   glEnd()
   glPopMatrix()

   glPushMatrix()
   glRotatef(second_finger, 0.0, 0.0, 1.0)
   glTranslatef(0.0, -0.2, 0.0)
   glBegin(GL_LINES)
   glVertex2f(0, 0)
   glVertex2f(0.4, 0)
   glEnd()
   glPopMatrix()

   glPopMatrix()

def teclado(tecla):
   global shoulder, elbow, ang, first_finger, second_finger

   if tecla == pygame.QUIT:
      pygame.quit()
      quit()
   if tecla[pygame.K_a]:
      shoulder = (shoulder + 5) % 360
   if tecla[pygame.K_f]:
      shoulder = (shoulder - 5) % 360
   if tecla[pygame.K_s]:
      elbow = (elbow + 5) % 360
   if tecla[pygame.K_d]:
      elbow = (elbow - 5) % 360
   if tecla[pygame.K_RIGHT]:
      ang = (ang + 5) % 360
   if tecla[pygame.K_LEFT]:
      ang = (ang - 5) % 360
   if tecla[pygame.K_UP]:
      first_finger = -20
      second_finger = 20
   if tecla[pygame.K_DOWN]:
      first_finger = 0
      second_finger = 0

def main():
   pygame.init()
   display = (800,600)
   pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

   glutInit([])

   init(display)

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            teclado(pygame.QUIT) 
         if pygame.key.get_focused():
            key = pygame.key.get_pressed()
            teclado(key)        

      desenha()

      pygame.display.flip()
      pygame.time.wait(10)

main()
