# This file was created by: Aarush

'''
Goals:
When a user click on their choice, the computer randomly chooses and displays the result 

'''

# import package
import turtle
from turtle import *
from random import randint
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1200, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="blue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()

XMark_image = os.path.join(images_folder, 'XMark.gif')
XMark_instance = turtle.Turtle()

CheckMark_image = os.path.join(images_folder, 'CheckMark.gif')
CheckMark_instance = turtle.Turtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)
def ShowXMark(x,y):
    # add the XMark image as a shape
    screen.addshape(XMark_image)
    # attach the XMark_image to the XMark_instance
    XMark_instance.shape(XMark_image)
    # remove the pen option from the XMark_instance so it doesn't draw lines when moved
    XMark_instance.penup()
    # set the position of the XMark_instance
    XMark_instance.setpos(x,y)
# instantiate a turtle for writing text
def ShowCheckMark(x,y):
    # add the checkmark image as a shape
    screen.addshape(CheckMark_image)
    # attach the CheckMark_image to the Check_instance
    CheckMark_instance.shape(CheckMark_image)
    # remove the pen option from the CheckMark_instance so it doesn't draw lines when moved
    CheckMark_instance.penup()
    # set the position of the Checkmark_instance
    CheckMark_instance.setpos(x,y)
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup() 

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick

# def computer_choice():
#     choice = randint(0,2)
#     if choice == 0:
#         show_rock(300,)

def hideCheck ():
    CheckMark_instance.hideturtle
def showCheck ():
    CheckMark_instance.showturtle
def hideX():
    XMark_instance.hideturtle
def showX():
    XMark_instance.hideturtle


def mouse_pos(x, y):
        #assigns rps choices
        rps_choices=["rock","paper","scissors"]
        #randomizes computer choices from previous choices
        computer = rps_choices[randint(0,2)]
        #if click on rock following happens
        if collide(x,y,rock_instance, rock_w, rock_h):
            #prints rock in terminal clears text on screen
            print("rock")
            text.clear()
            #if computer chooses scissors write on screen you chose rock computer chose scissors you win & shows checkmark
            if computer == "scissors":
                text.write("You chose rock computer chose scissor, You Win",False,"left", ("Arial", 18, "normal"))
                ShowCheckMark(0,0)
            #else if computer chooses paper writes on screen You chose rock computer chose paper, You Lose & shows XMark
            elif computer =="paper":
                text.write("You chose rock computer chose paper, You Lose",False,"left", ("Arial", 18, "normal"))
                ShowXMark(0,0)
            #else if both choose rock writes You chose rock computer chose rock, Tie
            elif computer =="rock":
                text.write("You chose rock computer chose rock, Tie",False,"left", ("Arial", 18, "normal"))                                            
        #if click on paper following happens
        elif collide(x,y,paper_instance, rock_w, rock_h):
            #prints paper in terminal clears text on screen
            print("paper")
            text.clear()
            #if computer chooses rock write on screen You chose paper computer chose rock, You Win & shows CheckMark
            if computer == "rock":
                text.write("You chose paper computer chose rock, You Win",False,"left", ("Arial", 18, "normal"))
                ShowCheckMark(0,0)
            #else if computer chooses scissors write on screen You chose paper computer chose scissors, You Lose & shows XMark
            elif computer =="scissors":
                text.write("You chose paper computer chose scissors, You Lose ",False,"left", ("Arial", 18, "normal"))
                ShowXMark(0,0)
            #else if computer chooses paper write on screen You chose paper computer chose paper, Tie
            elif computer =="paper":
                text.write(" You chose paper computer chose paper, Tie ",False,"left", ("Arial", 18, "normal"))  
        #if click on scissors following happens       
        elif collide(x,y,scissors_instance, scissors_w, scissors_h):
            #prints scissors in terminal & clears text on screen
            print("scissors")
            text.clear()
            #if computer chooses rock write on screen You chose rock computer chose rock, You Lose & shows XMark
            if computer == "rock":
                text.write("You chose scissors computer chose rock, You Lose ",False,"left", ("Arial", 18, "normal"))
                ShowXMark(0,0)
            #else if computer chooses paper writes on screen You chose rock computer chose paper, You Win & shows Check Mark
            elif computer =="paper":
                text.write("You chose scissors computer chose paper, You Win",False,"left", ("Arial", 18, "normal"))                                                                                          
                ShowCheckMark(0,0) 
            #else if computer chooses scissors writes on screen You chose rock computer chose scissors, Tie
            elif computer == "scissors":
                text.write(" You chose scissors computer chose scissors, Tie ",False,"left", ("Arial", 18, "normal"))
        exit
text.setpos(0,150)

# user this to get mouse position
#runs func on screen
screen.onclick(mouse_pos)


# runs mainloop for Turtle - required to be last
screen.mainloop()

#referance code not used
def rps():
    #creates variable InfinateRounds = 1 makes while loop so goes on forever while Infinate roands varible is greater than 0
    InfinateRounds =1
    
    while InfinateRounds > 0:
        #player choice is equal to rock, paper or scissors
        player_choice=input("choose rock, paper or scissors, you have infinate rounds ")
        #computer has choices of rock paper or scissors which is randomized by randint
        computer = rps_choices[randint(0,2)]
    
        
        #If player_choice == rock & computer == scissors than player wins
        if player_choice=="rock" :
            if computer == "scissors":
             print("computer choose "+computer )
             print("you win") 
        #If player_choice == scissors & computer == paper than player wins & prints what computer choose
        if player_choice=="scissors" :
            if computer == "paper":
             print("computer choose "+computer )
             print("you win")     
        #If player_choice == paper & computer == rock than player wins & prints what computer choose
        if player_choice=="paper" :
            if computer == "rock":
             print("computer choose "+computer )
             print("you win") 
        #if player choice is equal to computer than it is a tie + prints what computer choose
        elif player_choice == computer:
            print("computer choose "+computer)
            print("tie")
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose
        elif player_choice == "rock":
             if computer =="paper":
                print("computer choose "+computer)
                print("you lose")      
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose
        elif player_choice == "scissors":
             if computer=="rock":
                print("computer choose "+computer)
                print("you lose")   
        #if player chooses rock & computer chooses paper, player lose & prints what computer choose   
        elif player_choice == "paper":
             if computer =="scissors":
                print("computer choose "+computer)
                print("you lose")    
