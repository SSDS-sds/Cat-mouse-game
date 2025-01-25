import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "Cat Game."

score = 0

cat = Actor("cat")
cat.pos = 300,250
rat = Actor("rat")
rat.pos = 400,350

def draw():
    screen.blit("background",(0,0))
    cat.draw()
    rat.draw()
    screen.draw.text("score:"+ str(score), color = "red", fontsize = 30, topleft = (10,10))

pgzrun.go()