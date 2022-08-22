import time

import wrap

from wrap import  sprite

wrap.world.create_world(1000,900)

dots=[]
platforms=[]

mario=wrap.sprite.add("mario-1-big",800,350,"stand")
platforma=wrap.sprite.add("mario-items",800,500,"cloud_platform")
platforms.append(platforma)

@wrap.on_key_always(wrap.K_d,wrap.K_a,delay=10)
def actions_mario(keys):

    x_mario=sprite.get_x(mario)
    y_mario=sprite.get_y(mario)

    if wrap.K_d in keys:
        sprite.set_reverse_x(mario,False)
        sprite.move(mario,3,0)

    if wrap.K_a in keys:
        sprite.set_reverse_x(mario,True)
        sprite.move(mario,-3,0)


    costum_mario=sprite.get_costume(mario)
    if costum_mario=="stand":
        sprite.set_costume(mario,"walk3")
    else: sprite.set_costume(mario,"stand")

def dot(id,list):

    left=sprite.get_left(id)
    right=sprite.get_right(id)
    y=sprite.get_y(id)
    angle=sprite.get_angle(id)


    if angle==90:
        dot=sprite.add("pacman", right,y,"dot")

    if angle==-90:
        dot=sprite.add("pacman", left,y,"dot")

    sprite.set_angle(dot,angle)
    list.append(dot)


@wrap.on_key_down(key=wrap.K_SPACE)
def shoot():
    dot(mario,dots)

@wrap.always(delay=10)
def fly_dot():
    global fly_dot
    for fly_dot in dots:
        sprite.move_at_angle_dir(fly_dot, 5)


@wrap.on_key_down(key=wrap.K_w)
def jump():
    global a
    a=-20




a=0
@wrap.always()
def droping():
    global a
    q=sprite.get_bottom(mario)
    print(a,q)
    a=a+1



    for platforma_in_list in platforms:


        x=sprite.get_x(mario)
        y=sprite.get_y(mario)
        left_mario=sprite.get_left(mario)
        right_mario=sprite.get_right(mario)


        x_plat=sprite.get_x(platforma_in_list)
        y_plat=sprite.get_y(platforma_in_list)
        top_plat=sprite.get_top(platforma_in_list)
        left_plat=sprite.get_left(platforma_in_list)
        right_plat=sprite.get_right(platforma_in_list)



    wrap.sprite.move(mario,0,a)

    bot_m = sprite.get_bottom(mario)
    if bot_m>=top_plat:
        wrap.sprite.move_bottom_to(mario, top_plat)












