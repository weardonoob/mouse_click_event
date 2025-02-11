import pgzrun,os
from random import randint

TITLE = "shooter"
WIDTH = 500
HEIGHT = 500

balloon_pops = 3
msg = ""
score = 0
alien= Actor("alien.png")
alien.alien_pos= WIDTH / 2, HEIGHT / 2
balloon = Actor("balloon.png")
balloon.pos = WIDTH / 2, HEIGHT / 2


def draw():
  screen.clear()
  screen.fill("blue")
  alien.draw()
  balloon.draw()
  print("hi")
  screen.draw.text(msg,center = (WIDTH / 2, 20),fontsize = 30)
  screen.draw.text("score =" + str(score),center = (WIDTH / 2, 40), fontsize= 25)
  
  screen.draw.text("Balloonpops left =" + str(balloon_pops),center = (WIDTH / 2, 50), fontsize= 25)

def on_mouse_down(pos):
  global msg,score, balloon_pops
  print(pos)

  if alien.collidepoint(pos):
    score += 10
    msg = "good shot"
    #alien.pos=pos
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)
    balloon.x = randint(50,WIDTH-50)
    balloon.y = randint(50,HEIGHT-50)

  
  elif balloon.collidepoint(pos):
   balloon_pops -= 1
   msg = "don't hit the poor balloons"
   balloon.x = randint(50,WIDTH-50)
   balloon.y = randint(50,HEIGHT-50)
  else:
    score -= 5
    msg = "oops you missed"
    balloon.x = randint(50,WIDTH-50)
    balloon.y = randint(50,HEIGHT-50)
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)

pgzrun.go()