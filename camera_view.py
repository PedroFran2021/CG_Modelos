import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init(display):
   glClearColor(0.0, 0.0, 0.0, 1.0)
   glMatrixMode(GL_PROJECTION)
   gluPerspective(45.0, (display[0]/display[1]), 0.1, 50.0)

   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()

def draw():
   glColor3f(1.0, 0.5, 1.0)
   glutWireTeapot(1.0)

def main():
   pygame.init()
   display = (800, 600)
   pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
   glutInit([])
   init(display)
   #glTranslatef(0, 0, -5)
   # Define initial camera position
   camera_pos = [0, 0, 5]
   while True:
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            quit()
         elif pygame.key.get_pressed():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                camera_pos[0] -= 0.1
            elif keys[pygame.K_e]:
                camera_pos[0] += 0.1
            elif keys[pygame.K_w]:
                camera_pos[2] -= 0.1
            elif keys[pygame.K_s]:
                camera_pos[2] += 0.1
      
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

      # Set up camera transformation
      glLoadIdentity()
      
      gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], # camera (x,y,z)
                camera_pos[0], 0, -5,                        # centro (pra onde olha) (x,y,z)
                0, 1, 0)                                     # up (orientacao vertical) (x,y,z) 
      # up: orienta a camera para o topo da imagem

      draw()

      pygame.display.flip()
      pygame.time.wait(10)

if __name__ == '__main__':
    main()