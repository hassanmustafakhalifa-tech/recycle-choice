import pgzrun
import random

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X,CENTER_Y)
TITLE = 'Food choice'
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ['fries','chips','burger','pizza']

is_game_over = False
game_comp = False
current_level = 1
items = []
animations = []

def draw():
    global game_comp, items , current_level , is_game_over
    screen.clear()
    screen.blit('bg',(0,0))
    if is_game_over :
        display_message('GAME OVER','Try again')
    elif game_comp:
        display_message('YOU WIN', 'Good job')
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_food(current_level)

def make_food(extra_items):
    new_foods = get_option(extra_items)
    foods_list = create_items(new_foods)
    layout_items(foods_list)
    animate_items(foods_list)
    return foods_list

def get_option(extra_items):
    items_to_create = ['mango']
    for i in range (extra_items):
        random_item = random.choice(ITEMS)

        items_to_create.append(random_item)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + 'img')
        new_items.append(item)
    return new_items 

def layout_items(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / num_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate (items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ('center','bottom')
        animation = animate(item,duration=duration,on_finished = game_over,y = HEIGHT)
        animations.append(animation)

def game_over ():
    global is_game_over
    is_game_over = True

def on_mouse_down (pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if 'mango' in item.image:
                game_complete()
            else:
                game_over()

def game_complete():
    global current_level , items , animations , game_comp
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_comp = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(main_text, sub_text):
    screen.draw.text(main_text,fontsize = 60, center = CENTER, color = 'black')
    screen.draw.text(sub_text, fontsize = 30, center = (CENTER_X,CENTER_Y + 35) , color = 'black')



pgzrun.go()