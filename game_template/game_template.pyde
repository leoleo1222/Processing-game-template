def setup():
    size(1000, 500)
    background(255, 255, 255)
    global kirby, bg, sword, got_sword, floor
    kirby = loadImage("data/kirby.png")
    bg = loadImage("data/background.jpg")
    sword = loadImage("data/sword.png")
    floor = loadImage("data/ground.png")
    # draw the floor with line
    global floory, floorx
    floory = height - 100
    floorx = width
    # got sword is a boolean variable to check if the character got the sword
    got_sword = False
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
    move = 5
    global swordx, swordy, swordvx, swordvy, swordax, sworday, swordg, swordf, swordmove
    swordx = 100
    swordy = 0
    swordvx = 0
    swordvy = 0
    swordax = 0
    sworday = 0
    swordg = 10
    swordf = 0.1
    swordmove = 7
    swordx = 100
    swordy = 0


def draw():
    global g, f, swordy , floory , swordvy
    # draw the background
    image(bg, 0, 0, width, height)
    image(kirby, x, y - h, w, h)
    image(sword, swordx, swordy, 100, 100)
    image(floor, 0, floory, floorx, floory)
    drop_weapon()
    textDisplay()
    move_character()
    get_weapon()

def get_weapon():
    global got_sword
    # if the sword touched the character, the sword will stay on the character
    if swordx >= x and swordx <= x + w and swordy >= y - h and swordy <= y:
        got_sword = True

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
    global x, y, vx, vy, ax, ay, g, f, move, got_sword, swordx, swordy
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
    if got_sword:
        swordx = x+ 50
        swordy = y - 120

    




        
  
    


    
    
    

        



    
    

