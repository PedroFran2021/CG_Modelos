import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_square(r, g, b, a=0):
   '''desenha um quadrado: repare que a cor esta
   no sistema RGB com canal alfa.
   '''
   glColor4f(r, g, b, a)
   glBegin(GL_QUADS)
   glVertex2f(0, 0)
   glVertex2f(4, 0)
   glVertex2f(4, -4)
   glVertex2f(0, -4)
   glEnd()


def main():
   pygame.init()
   display = (800,600)
   pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

   # cria a campo de visao
   gluPerspective(90, (display[0]/display[1]), 0.1, 100.0)

   # define a cor de fundo (opcional - default: preto)
   glClearColor(1.0, 1.0, 1.0, 0.0)

   # translacao: define o ponto de origem
   glTranslatef(0, 0, -5)

   # habilita transparencia
   glEnable(GL_BLEND)
   glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()

      # desenha quadrado vermelho
      draw_square(1.0, 0.0, 0.0, 0.5)

      # desenha quadrado verde
      '''
      Por causa do PushMatrix(), a rotacao afeta somente este quadrado.
      Usamos Push e Pop, quando queremos isolar um ou mais objetos
      dos demais, ao realizar transformacoes.
      '''
      glPushMatrix()
      glRotatef(45, 0, 0, 1)
      draw_square(0.0, 1.0, 0.0, 0.5)
      glPopMatrix()

      '''
      Apos o PopMatrix(), a posicao de referencia continua sendo
       a origem.
      '''

      # desenha quadrado azul
      glPushMatrix()
      glRotatef(45, 0, 0, 1)
      glTranslatef(-1, 1, 0)
      draw_square(0.0, 0.0, 1.0, 0.5)
      glPopMatrix()

      pygame.display.flip()
      pygame.time.wait(10)

main()