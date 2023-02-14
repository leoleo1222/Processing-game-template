def setup():
    size(500, 500)
    background(255, 255, 255)
    global kirby
    kirby = loadImage("data/kirby.png")
    global background
    background = loadImage("data/background.jpg")
    # draw the floor with line
    global floory, floorx
    floory = 400
    floorx = 500
    line(0, floory, floorx, floory)
    # initialize the position of the character standing on the floor
    global x, y
    x = 0
    y = 400
    # character size
    global w, h
    w = 100
    h = 100
    # initialize the velocity of the character
    global vx, vy
    vx = 0
    vy = 0
    # initialize the acceleration of the character
    global ax, ay
    ax = 0
    ay = 0
    # initialize the gravity
    global g
    g = 0.5
    # initialize the friction
    global f
    f = 0.1
    # move the character with key input w, a, s, d
    global move
    move = 1

def draw():
    global x, y, vx, vy, ax, ay, g, f, move
    # draw the character
    image(kirby, x, y - h, w, h)
    # draw the background
    # image(background, 0, 0, 500, 500)
    # move the character with key input w, a, s, d
    if key == 'w':
        ay = -move
    if key == 'a':
        ax = -move
    if key == 's':
        ay = move
    if key == 'd':
        ax = move
    # apply the acceleration to the velocity
    vx += ax
    vy += ay
    # apply the velocity to the position
    x += vx
    y += vy
    # apply the gravity to the velocity
    vy += g
    # apply the friction to the velocity
    vx *= f
    vy *= f
    # reset the acceleration
    ax = 0
    ay = 0
    # check if the character is on the floor
    if y >= floory:
        y = floory
        vy = 0
    # check if the character is on the left wall
    if x <= 0:
        x = 0
        vx = 0
    # check if the character is on the right wall
    if x >= floorx - w:
        x = floorx - w
        vx = 0
    # check if the character is on the ceiling
    if y <= 0:
        y = 0
        vy = 0

    # draw a rectangle to show the floor, the rectangle size should cover the area under the floor which is the area under floorx and floory
    # when kirby touch the ground, the rectangle will change the color to red
    # when kirby leave the ground, the rectangle will change the color to green
    if y == floory:
        fill(255, 0, 0)
    else:
        fill(0, 255, 0)
    rect(0, floory, floorx, floory)



        
  
    


    
    
    

        



    
    

