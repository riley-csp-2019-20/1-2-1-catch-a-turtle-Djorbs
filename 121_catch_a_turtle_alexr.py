#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
shape = "turtle"
size = 2
color = "brown"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 20
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
wack = trtl.Turtle(shape = shape)
wack.color(color)
wack.shapesize(size)
wack.penup()
wack.speed(0)
scorer = trtl.Turtle(shape = shape)
scorer.ht()
scorer.penup()
scorer.speed(0)
scorer.goto(-420, 350)
counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(340, 350)
#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    runturtlerun()
    leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def turtlebooped(x,y):
  change_position()
  score_count()
  wack.color(random_color())
def change_position():
  wack.ht()
  new_positx = random.randint(-240, 240)
  new_posity = random.randint(-240, 240)
  wack.goto(new_positx, new_posity)
  wack.st()
def score_count(): 
  global score
  score += 100
  font = ("Arial", 30)
  scorer.clear()
  scorer.write(score, font = font)
def leaderboard(): #This is my customization. It brings your score to the middle of the screen
  global score
  scorer.clear()
  scorer.goto(-150,0)
  font = ("Arial", 30)
  scorer.write("Your score: " + str(score), font = font)

def runturtlerun():
  wn.bgcolor(random_color())#This is my customization. The background changes to a random color when the game ends.
  wack.ht
  wack.goto(999, 999)
def random_color(): #This is my customization. The turtle changes color everytime it is clicked.
  r = random.random()
  g = random.random()
  b = random.random()
  return (r,g,b)
#-----events----------------
wack.onclick(turtlebooped)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()