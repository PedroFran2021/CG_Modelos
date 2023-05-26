import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1, 1,-1))

arestas = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))

def cubo():
   glBegin(GL_LINES)
   for aresta in arestas:
      for v in aresta:
         glVertex3f(*vertices[v])
   glEnd()

def main():

   pygame.init()

   # configuracoes da IU
   display = (800,600)
   pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

   # cria a campo de visao
   gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

   # translacao: define o ponto de origem
   glTranslatef(0, 0, -5)

   r_x, r_y, r_z = 0, 0, 0
   ang = 0
   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               glTranslatef(-0.5,0,0)
            if event.key == pygame.K_RIGHT:
               glTranslatef(0.5,0,0)
            if event.key == pygame.K_UP:
               glTranslatef(0,1,0)
            if event.key == pygame.K_DOWN:
               glTranslatef(0,-1,0)
            if event.key == pygame.K_w:
               ang = (ang - 5) % 360
               r_x = 1 # gira somente sobre X
               r_y = 0 
            if event.key == pygame.K_s:
               ang = (ang + 5) % 360
               r_x = 1 # gira somente sobre X
               r_y = 0 
            if event.key == pygame.K_a:
               ang = (ang - 5) % 360
               r_x = 0
               r_y = 1 # gira somente sobre Y
            if event.key == pygame.K_d:
               ang = (ang + 5) % 360
               r_x = 0
               r_y = 1 # gira somente sobre Y
         if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
               glTranslatef(0,0,1.0)
            if event.button == 5:
               glTranslatef(0,0,-1.0)

      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

      # desenha o cubo
      glPushMatrix()
      glRotatef(ang, r_x, r_y, 0)
      cubo()
      glPopMatrix()

      pygame.display.flip()
      pygame.time.wait(10)

main()