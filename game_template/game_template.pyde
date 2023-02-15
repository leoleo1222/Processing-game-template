def setup():
    size(1000, 500)
    background(255, 255, 255)
    global kirby, bg, sword
    kirby = loadImage("data/kirby.png")
    bg = loadImage("data/background.jpg")
    sword = loadImage("data/sword.png")
    # draw the floor with line
    global floory, floorx
    floory = height - 100
    floorx = width
    line(0, floory, floorx, floory)
    # initialize the position of the character standing on the floor
    global x, y
    x = 0
    y = floory
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
    g = 10
    # initialize the friction
    global f
    f = 0.1
    # move the character with key input w, a, s, d
    global move
    move = 3
    global swordx, swordy, swordvx, swordvy, swordax, sworday, swordg, swordf, swordmove
    swordx = 100
    swordy = 0
    swordvx = 0
    swordvy = 0
    swordax = 0
    sworday = 0
    swordg = 10
    swordf = 0.1
    swordmove = 3
    swordx = 100
    swordy = 0


def draw():
    global g, f, swordy , floory , swordvy
    # draw the background
    image(bg, 0, 0, width, height)
    image(kirby, x, y - h, w, h)
    image(sword, swordx, swordy, 100, 100)
    drop_weapon()
    textDisplay()
    move_character()

    # draw a rectangle to show the floor, the rectangle size should cover the area under the floor which is the area under floorx and floory
    # when kirby touch the ground, the rectangle will change the color to red
    # when kirby leave the ground, the rectangle will change the color to green
    if y == floory:
        fill(255, 0, 0)
    else:
        fill(0, 255, 0)
    rect(0, floory, floorx, floory)

# in this function if the user press the key '1', the sword will drop from the sky until the floory
def drop_weapon():
    global swordx, swordy, swordvx, swordvy, swordax, sworday, swordg, swordf, swordmove
    if key == '1':
        sworday += swordmove
        swordvx += swordax
        swordvy += sworday
        swordx += swordvx
        swordy += swordvy
        swordvy += swordg
        swordvx *= swordf
        swordvy *= swordf
        swordax = 0
        sworday = 0


def textDisplay():
    fill(0, 0, 0)
    textSize(50)
    text("[1]", 10, 50)

def move_character():
    global x, y, vx, vy, ax, ay, g, f, move
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
    if y <= h:
        y = h
        vy = 0 

    




        
  
    


    
    
    

        



    
    

