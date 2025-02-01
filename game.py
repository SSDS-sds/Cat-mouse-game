import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "Cat Game."

game_over = False
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

    if game_over:
        screen.fill("red")
        screen.draw.text("YOUR TIME IS OVER.", color = "white", fontsize = 50, midtop = (WIDTH/2,10))
        screen.draw.text(f"Your score is {score}", color = "white", fontsize = 35, midtop = (WIDTH/2,40))


def timer_is_up():
    global game_over
    game_over = True

def move_cat():
    rat.x = randint(0,600)
    rat.y = randint(0,500)

def update():
    global score
    if keyboard.left:
        cat.x = cat.x - 5
    if keyboard.right:
        cat.x = cat.x + 5
    if keyboard.up:
        cat.y = cat.y - 5
    if keyboard.down:
        cat.y = cat.y + 5

    if cat.colliderect(rat):
        move_cat()
        score = score + 10

clock.schedule(timer_is_up, 20)

pgzrun.go()