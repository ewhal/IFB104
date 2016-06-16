#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9446800 
#    Student name: Eliot Whalan 
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#


# Draw the grass as a big green rectangle
def draw_grass():
    
    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()


# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0) 
  
        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)


# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0) 

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)


# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))
                
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.

portrait_00 = []

# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.
#
def person(person, scale, crown):
    if person == 'Person A':
        draw_person_a(scale, crown)
    elif person == 'Person B':
        draw_person_b(scale, crown)
    elif person== 'Person C':
        draw_person_c(scale, crown)
    elif person == 'Person D':
        draw_person_d(scale, crown)
    elif person == 'Pet':
        draw_pet(scale, crown)

def goto_pos(pos):
    if pos == 0:
        goto(-300, 0)
    elif pos == 1:
        goto(-150, 0)
    elif pos == 2:
        goto(0, 0)
    elif pos == 3:
        goto(150, 0)
    elif pos == 4:
        goto(300, 0)
    else:
        pass



def draw_person_a(scale, crown):
    #adjust turtle height to brown line
    setheading(90)
    forward(5 * scale)

    #move to left foot
    setheading(180)
    forward(30)

    #draw left foot
    pendown()
    shape("circle")
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    #draw left leg
    setheading(70)
    forward(5 * scale)
    pensize(3)
    forward(80 * scale)

    #move to right foot
    penup()
    pendown()
    setheading(295)
    forward(80 * scale)
    penup()
    #draw right foot
    forward(5 * scale)
    setheading(0)
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    stamp()
    penup()

    setheading(90)
    forward(3)
    penup()


    fillcolor("green")
    begin_fill()
    setheading(0)
    forward(10)
    setheading(110)
    forward(100 * scale)
    setheading(180)
    forward(20)
    setheading(250)
    forward(100 * scale)
    setheading(0)
    forward(20)
    setheading(75)
    forward(60 * scale)
    setheading(0)
    forward(15)
    setheading(290)
    forward(60 * scale)
    setheading(0)
    forward(10)
    end_fill()

    penup()
    #move to shirt position
    setheading(90)
    forward(90 * scale)
    setheading(180)
    forward(20)

    #draw shirt
    fillcolor("orange")
    begin_fill()
    pendown()
    forward(40)

    setheading(90)
    forward(70 * scale)

    setheading(230)
    forward(30)
    setheading(90)
    forward(25 * scale)
    setheading(45)
    forward(30)

    setheading(0)
    forward(40)
    setheading(320)
    forward(30)
    setheading(270)
    forward(25 * scale)
    setheading(140)
    forward(30)

    penup()
    setheading(270)
    forward(70)
    end_fill()

    pendown()
    setheading(90)
    forward(70)

    penup()
    forward(10)
    setheading(320)
    forward(30)

     #right hand
    pendown()
    forward(20)
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(140)
    forward(50)

    setheading(180)
    forward(40)
    
    setheading(220)
    forward(30)
    pendown()
    forward(20)

    #left hand
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(45)
    forward(50)
    setheading(0)
    forward(25)

    #move to head position
    setheading(90)
    forward(40 * scale) 

    #draw head
    shape("circle")
    resizemode("user")
    shapesize(3 * scale)
    fillcolor("white")
    pendown()
    stamp()
    penup()
    pendown()
    
    #right eye
    setheading(0)
    forward(10)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()

    #left eye
    setheading(180)
    forward(16)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()

    penup()
    setheading(0)
    forward(6 * scale)

    setheading(90)
    forward(20 * scale)
    if crown == '*':
        setheading(0)
        forward(35)
        setheading(90)
        forward(10 * scale)
        draw_crown(scale)
        setheading(180)
        forward(30)
        setheading(270)
        forward(10 * scale)
    penup()

def draw_person_b(scale, crown):
    setheading(90)
    forward(5 * scale)

    setheading(180)
    forward(30)

    pendown()
    shape("circle")
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()
    setheading(75)
    forward(5 * scale)
    pensize(3)
    forward(50 * scale)
    penup()
    setheading(0)
    forward(30)
    pendown()
    setheading(290)
    forward(50 * scale)
    penup()
    forward(5 * scale)
    setheading(0)
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    stamp()
    penup()
    setheading(90)
    forward(7)

    setheading(0)
    forward(10)
    setheading(110)
    forward(40 * scale)
    pendown()
    
    fillcolor("purple")
    begin_fill()
    forward(50 * scale)
    setheading(180)
    forward(20)
    setheading(250)
    forward(50 * scale)
    setheading(0)
    forward(50)
    end_fill()
    penup()

    #move to shirt position
    setheading(90)
    forward(45 * scale)
    setheading(180)
    forward(5)

    #draw shirt
    fillcolor("red")
    begin_fill()
    pendown()
    forward(40)

    setheading(90)
    forward(70 * scale)

    setheading(230)
    forward(30)
    setheading(90)
    forward(25 * scale)
    setheading(45)
    forward(30)

    setheading(0)
    forward(40)
    setheading(320)
    forward(30)
    setheading(270)
    forward(25 * scale)
    setheading(140)
    forward(30)

    penup()
    setheading(270)
    forward(70)
    end_fill()

    pendown()
    setheading(90)
    forward(70)

    penup()
    forward(10)
    setheading(320)
    forward(30)

    #right hand
    pendown()
    forward(20)
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(140)
    forward(50)

    setheading(180)
    forward(40)
    
    setheading(220)
    forward(30)
    pendown()
    forward(20)

    #left hand
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(45)
    forward(50)
    setheading(0)
    forward(25)

    #move to head position
    setheading(90)
    forward(40)

    #draw head
    shape("circle")
    resizemode("user")
    shapesize(3 * scale)
    fillcolor("brown")
    pendown()
    stamp()
    penup()
    pendown()
    
    #right eye
    setheading(0)
    forward(10)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()

    #left eye
    setheading(180)
    forward(16)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()
    penup()
    if crown == '*':
        setheading(0)
        forward(35)
        setheading(90)
        forward(10 * scale)
        draw_crown(scale)
        setheading(180)
        forward(30)
        setheading(270)
        forward(10 * scale)
    penup()


def draw_person_c(scale, crown):
    setheading(90)
    forward(5 * scale)

    setheading(180)
    forward(20)
    pendown()


    shape("circle")
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("green")
    stamp()

    setheading(75)
    forward(5 * scale)
    pensize(3)
    forward(40 * scale)
    penup()

    setheading(0)
    forward(20)
    pendown()
    setheading(290)
    forward(40 * scale)
    penup()

    forward(5 * scale)
    setheading(0)
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    stamp()


    setheading(90)
    forward(70 * scale)
    setheading(180)
    forward(25)
    penup()

    setheading(90)
    pendown()
    shape("triangle")
    resizemode("user")
    shapesize(5* scale, 9*scale, 1*scale)
    fillcolor("pink")
    stamp()
    forward(50)
    penup()

    #move to head position
    setheading(90)
    forward(40)

    #draw head
    shape("circle")
    resizemode("user")
    shapesize(3 * scale)
    fillcolor("brown")
    pendown()
    stamp()

    #right eye
    setheading(0)
    forward(10)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()

    #left eye
    setheading(180)
    forward(16)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()


    penup()
    if crown == '*':
        setheading(0)
        forward(35)
        setheading(90)
        forward(10 * scale)
        draw_crown(scale)
        setheading(180)
        forward(30)
        setheading(270)
        forward(10 * scale)


    setheading(270)
    forward(50)
    
    setheading(45)
    forward(25)
    pendown()
    forward(35)

    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(225)
    forward(60)
    pendown()
    forward(40)

    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()


    penup()

def draw_person_d(scale, crown):
    setheading(90)
    forward(5 * scale)

    setheading(180)
    forward(30)

    pendown()
    shape("circle")
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("green")
    stamp()
    setheading(75)
    forward(5 * scale)
    pensize(3)
    forward(50 * scale)
    penup()
    setheading(0)
    forward(30)
    pendown()
    setheading(290)
    forward(50 * scale)
    penup()
    forward(5 * scale)
    setheading(0)
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    stamp()
    penup()
    setheading(90)
    forward(7)

    pendown()
    fillcolor("blue")


    #pants
    penup()
    setheading(0)
    forward(10)
    setheading(110)
    forward(40 * scale)

    pendown()
    begin_fill()
    forward(50 * scale)
    setheading(180)
    forward(20)
    setheading(250)
    forward(50 * scale)
    setheading(0)
    forward(15)
    setheading(75)
    forward(20 * scale)
    setheading(0)
    forward(10)
    setheading(290)
    forward(20 * scale)
    setheading(0)
    forward(15)
    end_fill()
    penup()

    #move to shirt position
    setheading(90)
    forward(45 * scale)
    setheading(180)
    forward(5)

    #draw shirt
    fillcolor("green")
    begin_fill()
    pendown()
    forward(40)

    setheading(90)
    forward(30 * scale)

    setheading(230)
    forward(30)
    setheading(90)
    forward(25 * scale)
    setheading(45)
    forward(30)

    setheading(0)
    forward(40)
    setheading(320)
    forward(30)
    setheading(270)
    forward(25 * scale)
    setheading(140)
    forward(30)

    penup()
    setheading(270)
    forward(70)
    end_fill()

    pendown()
    setheading(90)
    forward(70)

    penup()
    forward(10)
    setheading(320)
    forward(30)

    #right hand
    pendown()
    forward(20)
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(140)
    forward(50)

    setheading(180)
    forward(40)
    
    setheading(220)
    forward(30)
    pendown()
    forward(20)

    #left hand
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()
    setheading(45)
    forward(50)
    setheading(0)
    forward(25)

    #move to head position
    setheading(90)
    forward(40 * scale)

    #draw head
    shape("circle")
    resizemode("user")
    shapesize(3 * scale)
    fillcolor("brown")
    pendown()
    stamp()
    penup()
    pendown()
    
    #right eye
    setheading(0)
    forward(10)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()

    #left eye
    setheading(180)
    forward(16)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("blue")
    stamp()

    penup()
    if crown == '*':
        setheading(0)
        forward(35)
        setheading(90)
        forward(10 * scale)
        draw_crown(scale)
        setheading(180)
        forward(30)
        setheading(270)
        forward(10 * scale)

    penup()



def draw_pet(scale, crown):
    setheading(90)
    forward(10 * scale)

    #draw left foot
    setheading(180)
    forward(20)
    pendown()
    shape("square")
    resizemode("user")
    shapesize(2*scale, 1, 1)
    fillcolor("grey")
    stamp()
    penup()

    #draw right foot
    setheading(0)
    forward(40)
    pendown()
    shape("square")
    resizemode("user")
    shapesize(2*scale, 1, 1)
    fillcolor("grey")
    stamp()
    penup()

    setheading(180)
    forward(20)
    #draw body 
    setheading(90)
    forward(40 * scale)
    setheading(0)
    pendown()
    shape("square")
    resizemode("user")
    shapesize(5 * scale, 4, 1)
    fillcolor("grey")
    stamp()

    #draw head 
    setheading(90)
    forward(50 * scale)
    setheading(0)
    pendown()
    shape("square")
    resizemode("user")
    shapesize(2 * scale, 3, 1)
    fillcolor("grey")
    stamp()
    penup()

    #draw eyes 
    setheading(0)
    forward(5)
    setheading(0)
    pendown()
    shape("square")
    resizemode("user")
    shapesize(0.75 * scale, 0.5, 1)
    fillcolor("black")
    stamp()
    penup()

    setheading(180)
    forward(15)
    setheading(0)
    pendown()
    shape("square")
    resizemode("user")
    shapesize(0.75 * scale, 0.5, 1)
    fillcolor("black")
    stamp()
    penup()


    setheading(270)
    forward(40)
    #right hand
    setheading(0)
    forward(40)
    pendown()

    forward(30)
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()
    penup()

    setheading(180)
    forward(80)
    
    setheading(220)
    forward(10)
    pendown()
    forward(50)

    #left hand
    setheading(270)
    resizemode("user")
    shapesize(0.75 * scale, 1*scale, 0.25*scale)
    fillcolor("brown")
    stamp()

    penup()

    if crown == '*':
        setheading(0)
        forward(90)
        setheading(90)
        forward(70)
        forward(20 * scale)
        draw_crown(scale)

    penup()


def draw_crown(scale):
    pendown()
    fillcolor("yellow")
    begin_fill()
    setheading(90)
    forward(30 * scale)
    for i in range(3):
        setheading(230)
        forward(15 * scale)
        setheading(130)
        forward(15 * scale)

    setheading(270)
    forward(30 * scale)
    setheading(0)
    forward(60 * scale)
    end_fill()
    penup()

# Draw the stick figures as per the provided data set
def draw_portrait(portrait):
    for character, position, scale, crown in portrait:
        goto_pos(position)
        person(character, scale, crown)

    

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
draw_grass()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Family (Describe your theme and the individuals here)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the locations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False
draw_locations(True)
draw_labels(True)
mark_coords(True)

# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False
tracer(True)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_11)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

