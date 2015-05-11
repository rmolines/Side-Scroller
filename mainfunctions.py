# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:21:56 2015

@author: Rafael
"""

from tkinter import *


def wait_and_delete(component):
    component.after(15) # espera 20ms
    component.update()
    component.delete(ALL) # deleta tudo que estava na tela para começar o novo frame   
    

def draw(element, canvas):
    """ Recebe um canvas e nele desenha a forma"""
    xpos = element.pos [0]
    ypos = element.pos [1]
        
    if element.form == 'square':
        width = element.size [0]
        height = element.size [1]
        canvas.create_polygon (xpos+width, ypos+height, xpos, ypos+height, xpos, ypos, xpos+width, ypos, fill=element.color)
        
    elif element.form == 'circle': 
        radius = element.radius
        canvas.create_oval (xpos-radius, ypos-radius, xpos+radius, ypos+radius, fill= element.color)


def drawtext (element, canvas):
    """ Escreve texto na tela """
    x = element.pos[0]
    y = element.pos[1]
    fill = element.fill
    text = element.text
    canvas.create_text (x, y, text=text, fill=fill)
    

def collision (e1, e2):
    """ Cria um collider"""
    x1, y1 = e1.pos[0], e1.pos[1]
    x2, y2 = e2.pos[0], e2.pos[1]
    w1, h1 = e1.size[0], e1.size[1]
    w2, h2 = e2.size[0], e2.size[1]
    v = e2.yspeed 
    
    if x1 > x2-w1 and x1 < x2+w2 and y1 > y2-h1 and y1 < y2+h2:
        return True            
    else:      
        return False


    