import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

origem = GLint()

def draw_origin():
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

def draw_points():
   glPointSize(10)
   glBegin(GL_POINTS)
   glColor3f(0.0, 1.0, 0.0)
   glVertex2i(0, 0)

   glColor3f(1.0, 0.0, 0.0)
   glVertex2i(-1, 1)
   glVertex2i(-1, -1)
   glVertex2i(1, -1)
   glVertex2i(1, 1)
   glEnd()

def draw_lines():
   glColor3f(0.0, 0.0, 1.0)
   glBegin(GL_LINES)
   glVertex2i(3, 0)
   glVertex2i(3, 3)

   glVertex2i(5, 0)
   glVertex2i(5, 3)

   glVertex2i(3, 3)
   glVertex2i(5, 3)
   glEnd()

def draw_polygon():
   glColor3f(0.5, 0.5, 0.0)
   glBegin(GL_POLYGON)
   glVertex2i(-4, 0)
   glVertex2i(-4, 3)
   glVertex2i(-3, 2)
   glVertex2i(-3, 1)
   glEnd()

def draw_square():
   glColor3f(0.5, 0.0, 0.5)
   glBegin(GL_QUADS)
   glVertex2i(3, -3)
   glVertex2i(4, -3)
   glVertex2i(4, -4)
   glVertex2i(3, -4)
   glEnd()

def draw_triangle():
   glColor3f(0.0, 0.5, 0.5)
   glBegin(GL_TRIANGLES)
   glVertex2i(-3, -3)
   glVertex2i(-4, -4)
   glVertex2i(-2, -4)
   glEnd()

pygame.init()
display = (640, 480)

'''
Especifica que o opengl sera usado com
doublebuf: há duas imagens em qualquer momento - 
uma que vemos e outra que podemos transformar.
Podemos ver o resultado da transformação quando os
dois buffers são trocados.
'''
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# Especifica o campo de visão: quão longe e largo é o campo de visão
# p1: angulo 
# p2: proporção da tela - taxa entre largura e altura
# p3: distancia mínima para o desenho (em z)
# p4: distancia máxima para o desenho (em z)
gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -5)
draw_origin()
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

      # x = glGetDoublev(GL_MODELVIEW_MATRIX)
      # print(x)

      # limpa a tela para desenhar o proximo frame
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

      glCallList(origem)

      draw_points()

      draw_lines()

      draw_polygon()

      draw_square()

      draw_triangle()

      # prepapa a tela e espera um instante para o próximo frame
      pygame.display.flip()
      pygame.time.wait(10)