import pygame
from pygame.locals import *
# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *

class Llave:
    def __init__(self,x,y,z,tam):
        self.tam = tam
        self.radioColi = 1
        self.obj = OBJ("Key2.obj", swapyz = True)
        self.obj.generate()
        self.x=x
        self.y=y
        self.z =z
        self.ang = 0
        self.Position = []
        self.Position.append(x)
        self.Position.append(y)
        self.Position.append(z)
        
    def update(self):
        if(self.ang>=360):
            self.ang = 0
        self.ang += 5

    def draw(self):
        glPushMatrix()
        glTranslatef(self.Position[0], self.Position[1], self.Position[2])
        glScaled(0.02*self.tam, 0.02*self.tam, 0.02*self.tam) 
        glRotated(-90, 1,0,0)
        glRotated(self.ang, 0,0,1)
        
        self.obj.render()
        glPopMatrix()