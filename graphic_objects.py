# -*- coding: utf-8 -*-

from tkinter import *

  
class Player(object):
    """ Classe quadrado"""
    
    def __init__(self, width, height, xpos, ypos, color):
        """ Recebe largura, altura, posição e cor do quadrado"""
        self.size = [width, height]
        self.pos = [xpos, ypos]
        self.color = color
        self.form = 'square'
        
        self.yspeed = 0
        self.xspeed = 0
        self.accel = 0.6 

        self.state = '' 
        self.lives = 5
        self.points = 0         
           
        
    def update(self, last_key, player):
        """ Faz as atualizações do objeto"""
        self.getkey (last_key)
        
        self.pos[0] += self.xspeed 
        self.pos[1] += self.yspeed
        
        self.yspeed += self.accel
        
        if self.xspeed < 0:
            self.xspeed += self.accel
        if self.xspeed > 0:
            self.xspeed -= self.accel        
        
        if self.pos[1] > 250:
            self.yspeed = 0
            self.pos[1] = 250
            
            
    def getkey (self, last_key):
        """ Recebe e lê input """
        xaxis = {'Right':8, 'Left':-8}
        yaxis = {'Up':-5, 'Down':5}
        
        if last_key == 'space':
            self.yspeed = -12
        if last_key in xaxis:
            self.xspeed = xaxis[last_key]
        if last_key in yaxis:
            self.deltay = yaxis[last_key]
            
            
        
class Square (object):
    
    def __init__ (self, width, height, xpos, ypos, color, state):
        self.size = [width, height]
        self.pos = [xpos, ypos]
        self.xpos0 = xpos
        
        self.color = color
        self.state = state
        self.form = 'square'
    
    def update (self):
        
        if self.state == 'static':
            pass
        
        if self.state == 'dynamic':
            
            self.pos[0] -= 3            
    
            if self.pos[0]+self.size[0] < 1:
                self.pos[0] = self.xpos0 
                

class Circle (object):
    
    def __init__ (self, radius, color, state):
        self.radius = radius
        self.pos = [200,300]
        
        self.color = color
        self.state = state
        self.form = 'circle'
    
    def update (self):
        if self.state == 'static':
            pass
        
        else:
            self.pos[0] -= 3
            
            if self.pos[0]+self.radius < 1:
                self.pos[0] = 510
        
    
    

class GUI (object):
    
    def __init__ (self, xpos, ypos, text, fill):
        self.pos = [xpos, ypos]
        self.text = text
        self.fill = fill
            
    def update (self, text):
        self.text = text
        

class Ground (object):
    
    def __init__ (self):
        self.size = [5, 110]        
        self.pos = [500, 410-self.size[1]]
        
        self.form = 'square'
        self.color = 'black'
        
    def update (self):
                
        self.pos[1] = 410-self.size[1]
        
        self.pos[0] -= 5
        if self.pos[0] < 1:
            self.pos[0] = 500
    
    
        
        
        
            

           

            