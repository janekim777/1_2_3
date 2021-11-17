"""
import turtle as trtl
import random as rand






#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
background_image ="background.gif"
wn.setup(width=1.0, height=1.0)
wn.addshape(background_image)
apple = trtl.Turtle()

letters = ["a","b","c","d","e","f","g","h","i","j"]

apple_list = []
apple_letters = []


for i in range (5):
  apple_list.append(trtl.Turtle())
  apple_letters.append(rand.choice(letters))



#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

  
def drop_apple():
  apple.clear()
  apple.penup()
  apple.goto(apple.xcor(),-170)
  apple.hideturtle()

drawer = trtl.Turtle()

# This function takes care of font and color.
def draw_an_A():
  drawer.penup()
  drawer.color("white")
  drawer.goto(-20,-30) 
  drawer.write("A", font=("Arial", 74, "bold")) 
  drawer.hideturtle()

#-----function calls-----
wn.bgpic("background.gif")
draw_apple(apple)
draw_an_A()
drop_apple()
drawer.clear()
trtl.onkeypress(letters)
wn.listen()

wn.mainloop()
""" 