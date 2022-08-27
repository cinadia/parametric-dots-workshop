# V3 - ADVANCED, with nested list
# import statements
import simplegui
import time
import math
import random

# set width and height of frame
frame_width = 600
frame_height = 600

# fields for the dots
dot_radius = 5
dot_width = 1

dots = [] # [["colour", (x, y)], ["colour", (x, y)]]
"""
current_dot_colour = '#'
dot_colours = []
#dot_colour = 'Red'

dots = []
"""
    
# returns [x, y] of parametric equation points
def get_dot_coords(t):
    
    # circle
    #return [(math.cos(t) * 100 + (0.5 * frame_width)), (math.sin(t) * 100 + (0.5 * frame_height))]
        
    # star
    #return [((2 * math.cos(t) + 5 * math.cos(2*t/3)) * 10 + (0.5 * frame_width)), 
    #        ((2 * math.sin(t) - 5 * math.sin(2*t/3)) * 10 + (0.5 * frame_height))]
    
    # flower
    return [((math.cos(t) * math.sin(4*t)) * 100 + (0.5 * frame_width)), 
            ((math.sin(t)*math.sin(4*t))*100 + (0.5 * frame_height))] 
    
def generate_dot_colour():
    hex = '#'
    for i in range(6):
        num = random.randint(0, 9)
        hex = hex + num.__str__()
    return hex
    
# creates the next dot: {(x, y), "colour"}
def new_dots(t):
    coords = get_dot_coords(t)
    colour = generate_dot_colour()
    
    dots.append([colour, coords])
        
def draw(canvas):
    t = time.time() # get current time
    new_dots(t)
    
    # draw each dot in 'dots' list onto canvas
    
    for i in range(len(dots)):
        canvas.draw_circle(dots[i][1], # coordinate
                           dot_radius, 
                           dot_width, 
                           dots[i][0], # colour
                           dots[i][0])
       
    

# create a frame 
frame = simplegui.create_frame("Parametric Equations", frame_width, frame_height)

# assign draw handler to frame
frame.set_draw_handler(draw)

# create time Handler
def timer_handler():
    draw
    
# set and start timer
timer = simplegui.create_timer(500, timer_handler)
timer.start()

# start the frame animation
frame.start()




