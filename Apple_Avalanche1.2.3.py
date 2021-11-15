import turtle as trtl







#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

background_image ="background.gif"
wn.setup(width=1.0, height=1.0)
wn.addshape(background_image)
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
tree = trtl.Turtle()
def draw_background(tree):
  tree.shape(background_image)
  wn.update()

drawer = trtl.Turtle()

# This function takes care of font and color.
def draw_an_A():
  drawer.penup()
  drawer.color("white")
  drawer.goto(-20,-30) 
  drawer.write("A", font=("Arial", 74, "bold")) 

#-----function calls-----

draw_background(tree)
draw_an_A()
draw_apple(apple)
drop_apple()

wn.onkeypress(draw_an_A, "a")
wn.listen()
wn.mainloop()
wn.bgpic("background.gif")