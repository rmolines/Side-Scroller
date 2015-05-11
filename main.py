# -*- coding: utf-8 -*-


from tkinter import *
from graphic_objects import *
from mainfunctions import * 


window = Tk() # Janela do app
canvas = Canvas(window, width = 500, height = 400) # área para desenha
canvas.pack()

last_key = ""
game = True

player = Player (50, 50, 225, 250, 'black')
player_shadow = Square (46, 46, player.pos[0]+2, player.pos[1]+2, 'red', 'static')
ground = Square (500, 200, 2, 300, 'black', 'static')
box = Square (20, 20, 530, 280, 'black', 'dynamic')
life = GUI (30, 20, 'Lives: 0', 'black')
points = GUI (470, 20, 'Points: 0', 'black')
gameover = GUI (250, 200, 'GAME OVER', 'black')
ball = Circle (25, 'black', 'dynamic')
mground = Ground ()

objetos = [box, player_shadow, ground]
players = [player]
GUI = [life, points]

# Para que possamos detectar teclas pressionadas
def key_pressed(event):
    global last_key
    last_key = event.keysym

# Para que a janela possa ter o foco do teclado
def get_focus(event):
    canvas.focus_set()    
    
canvas.bind("<Key>", key_pressed)
canvas.bind("<1>", get_focus)

    
while game:
    
    global last_key      
        
    
    canvas.create_text(50,50, text=last_key, fill="black")
    
    if player.pos[1]-player.yspeed+player.size[1] < box.pos[1]:
        player.state = 'up'
    else:
        player.state = 'down'
        
    if collision (box, player):
        if player.state == 'up':
            player.pos[1] = box.pos[1] - player.size[1]
            last_key = 'space'
            box.pos[0] = box.xpos0
            player.points += 1
        else:
            box.pos[0] = box.xpos0
            player.lives -= 1
                
    player.update (last_key, player)               
    draw (player, canvas)   
        
    player_shadow.pos = [player.pos[0]+2, player.pos[1]+2]
    
    for elemento in objetos:
        elemento.update()
        draw (elemento, canvas)        
   
    if player.lives == 0:
        game = False
        
    drawtext (life, canvas)
    drawtext (points, canvas)
    life.update ('Lives: ' + str(player.lives)) 
    points.update ('Points: ' + str(player.points))
    
    last_key =''
    
    wait_and_delete(canvas) # Apaga a tela antes do próximo frame

drawtext (gameover, canvas)  

window.mainloop()