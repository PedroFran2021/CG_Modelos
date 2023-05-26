import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -5)
   
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         quit()
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         # read the color of the pixel under the mouse cursor
         pos = pygame.mouse.get_pos()
         color = glReadPixels(pos[0], display[1] - pos[1], 1, 1, GL_RGB, GL_UNSIGNED_BYTE)
         print(f"Color at ({pos[0]}, {pos[1]}): RGB({color[0]}, {color[1]}, {color[2]})")

   #glRotatef(1, 3, 1, 1)
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   
   glBegin(GL_TRIANGLES)
   glColor3f(1.0, 0.0, 0.0)
   glVertex3f(0.0, 1.0, 0.0)
   glColor3f(0.0, 1.0, 0.0)
   glVertex3f(-1.0, -1.0, 0.0)
   glColor3f(0.0, 0.0, 1.0)
   glVertex3f(1.0, -1.0, 0.0)
   glEnd()

   pygame.display.flip()
   pygame.time.wait(10)
