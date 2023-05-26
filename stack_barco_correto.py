import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def boat():

   glColor3f(1.0, 0.0, 0.0)
   glBegin(GL_POLYGON)
   glVertex2f(0, 0)
   glVertex2f(-4, 0)
   glVertex2f(-3, -1.5)
   glVertex2f(-1, -1.5)
   glEnd()

   glColor3f(0.0, 1.0, 0.0)
   glBegin(GL_QUADS)
   glVertex2f(-2, 0)
   glVertex2f(-2, 1)
   glVertex2f(-2.1, 1)
   glVertex2f(-2.1, 0)
   glEnd()

   glColor3f(1.0, 0.0, 1.0)
   glBegin(GL_TRIANGLES)
   glVertex2f(-2, 1)
   glVertex2f(-1.8, 0.8)
   glVertex2f(-2, 0.6)
   glEnd()

def water():
   glColor3f(0.0, 0.0, 1.0)
   glBegin(GL_QUADS)
   glVertex2f(10, -1)
   glVertex2f(10, -10)
   glVertex2f(-10, -10)
   glVertex2f(-10, -1)
   glEnd()


def main():
   pygame.init()
   display = (800,600)
   pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

   gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

   glClearColor(1.0, 1.0, 1.0, 0.0)

   glTranslatef(0, 0, -3)

   mov_barco = 0
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               mov_barco = mov_barco - 0.5
            if event.key == pygame.K_RIGHT:
               mov_barco = mov_barco + 0.5
            if event.key == pygame.K_UP:
                  glTranslatef(0, 0, 0.5)
            if event.key == pygame.K_DOWN:
                  glTranslatef(0, 0, -0.5)

      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

      water()

      glPushMatrix()
      glTranslatef(mov_barco,0,0)
      boat()
      glPopMatrix()

      pygame.display.flip()
      pygame.time.wait(10)

main()