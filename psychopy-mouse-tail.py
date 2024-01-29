# -*- coding: utf-8 -*-
# psychopy-mouse-tail
# Python 3.9 and PsychoPy v2023.2.3 (Coder)
# Copyright (c) 2024, Aurélien Antoine

# Change pointer image, select pointer image according to xy coordinates, and create a mouse/pointer tail for
# experiments in PsychoPy v2023.2.3 (Coder).

from psychopy import visual, core, event

# Create a window to draw in
win = visual.Window((600.0, 600.0), allowGUI=True)

# Initialize some stimuli
background = visual.ImageStim(win, image='./IMG/background.png') # Define your background image.
myMouse = event.Mouse()  #  will use win by default
mouse_pointer = visual.ImageStim(win, image='./IMG/mouseNeu.png', size=(0.1, 0.1)) # Create a pointer object, define image source, and size.
tail = visual.ImageStim(win, image='./IMG/mouseNeu.png', pos=(0,0), size=(0.05, 0.05)) # Create an ImageStim object for pointer tail, define image source, position, and size.
tail_size = 30 # Define the size of the mouse tail (in number of frames)
tail_buffer = []
text = visual.TextStim(win, text="Press a key to exit exp", pos=(-0.5, 0.8), height=0.05, color="black")
mouse_pointer.setAutoDraw(True)

# Continue running until keypress
while not event.getKeys():
    background.draw()
    myMouse.setVisible(0)
    text.draw()

    # Handle the mouse pointer image and select according to x coordinates (y coordinates not used here, use myMouse.getPos()[1]).
    if myMouse.getPos()[0] >= 0.15:
        mouse_pointer.setImage('./IMG/mousePos.png')
    elif myMouse.getPos()[0] <= -0.15: 
        mouse_pointer.setImage('./IMG/mouseNeg.png')
    else:  
        mouse_pointer.setImage('./IMG/mouseNeu.png')
    mouse_pointer.setPos(myMouse.getPos())
    
    ## Create the mouse tail
    # Create mouse tail buffer
    if len(tail_buffer) >= tail_size:
        tail_buffer.pop(0)
        tail_buffer.append(myMouse.getPos())
    else:
        tail_buffer.append(myMouse.getPos())
    # Set image position and draw tail
    for position in tail_buffer:
        tail.setPos(position)
        tail.draw()

    win.flip()

win.close()
core.quit()