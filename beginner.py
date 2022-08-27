# V1 - BEGINNER 
# import statements
import simplegui
import time
import math

# set width and height of frame
frame_width = 600
frame_height = 600

# fields for the dots
dot_radius = 5
dot_width = 1
dot_colour = 'Red'

dots = []
    
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
    

# creates the next dot: (x, y)
def new_dots(t):
    coords = get_dot_coords(t) # <-- function call
    dots.append(coords)
        
def draw(canvas):
    t = time.time() # get current time
    new_dots(t) # <-- function call, passes time 't' to function
    for i in range(len(dots)):
        canvas.draw_circle(dots[i],
                           dot_radius, 
                           dot_width, 
                           dot_colour,
                           dot_colour)
       
    
# create a frame 
frame = simplegui.create_frame("Parametric Equations", frame_width, frame_height)

# assign draw handler to frame
frame.set_draw_handler(draw)

# create time Handler
def timer_handler():
    draw
    
    
# set and start the timer
timer = simplegui.create_timer(500, timer_handler)
timer.start()

# start the frame animation
frame.start()
