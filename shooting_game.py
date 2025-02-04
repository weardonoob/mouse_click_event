import pgzrun,os
from random import randint
TITLE = "shooter"
WIDTH = 500
HEIGHT = 500

msg = ""
score = 0
alien= Actor("alien.png")
alien.pos= WIDTH / 2, HEIGHT / 2
print("hello")
def draw():
  screen.clear()
  screen.fill("blue")
  alien.draw()
  print("hi")
  screen.draw.text(msg,center = (WIDTH / 2, 20),fontsize = 30)
  screen.draw.text("score =" + str(score),center = (WIDTH / 2, 40), fontsize= 25)

def on_mouse_down(pos):
  global msg,score
  print(pos)
  if alien.collidepoint(pos):
    score += 10
    msg = "good shot"
    # alien.pos=pos
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)
  else:
    score -= 5
    msg = "oops you missed"




pgzrun.go()