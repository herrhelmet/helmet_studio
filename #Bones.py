#WELCOME TO BONES
name = "world_real.txt"
file = open(name,"r")
world = file.read()
world = world.split("\n")
for i in range(len(world)):
    world[i] = world[i].split(",")
for i in range(len(world)):
    for j in range(len(world[i])):
        world[i][j] = int(world[i][j])
file.close()
import tkinter
import time
from tkinter.constants import *
tk = tkinter.Tk()
tk.title("Bones")
tk.geometry("465x645+100+100")
colour = "#250750"
tk.config(bg=colour)
#x = tkinter.Button(tk,text="x",command=tk.destroy,fg="#ff0000")
#x.place(x=430,y=620,width=20,height=20)
wt = 13
st = 14
soak = 3
def_ = 0
dam = 3
food = 10
water_ = 10
t1 = tkinter.Button(tk,bg=colour)
t2 = tkinter.Button(tk,bg=colour)
t3 = tkinter.Button(tk,bg=colour)
t4 = tkinter.Button(tk,bg=colour)
t1.place(x=410,y=520,width=30,height=30)
t2.place(x=410,y=550,width=30,height=30)
t3.place(x=410,y=580,width=30,height=30)
t4.place(x=410,y=610,width=30,height=30)
m1 = tkinter.Label(tk,bg=colour)
m2 = tkinter.Label(tk,bg=colour)
m3 = tkinter.Label(tk,bg=colour)
m4 = tkinter.Label(tk,bg=colour)
n1 = tkinter.Label(tk,bg=colour,text="0",fg="#ffffff")
n2 = tkinter.Label(tk,bg=colour,text="0",fg="#ffffff")
n3 = tkinter.Label(tk,bg=colour,text="0",fg="#ffffff")
n4 = tkinter.Label(tk,bg=colour,text="0",fg="#ffffff")
m1.place(x=350,y=520,width=30,height=30)
m2.place(x=350,y=550,width=30,height=30)
m3.place(x=350,y=580,width=30,height=30)
m4.place(x=350,y=610,width=30,height=30)
n1.place(x=330,y=525,width=20,height=20)
n2.place(x=330,y=555,width=20,height=20)
n3.place(x=330,y=585,width=20,height=20)
n4.place(x=330,y=615,width=20,height=20)
#
day = True   # goes to night every 256 secs
fish_dir = True #right is true
turtle_dir = True
skeleton1_att = False
skeleton2_att = False
skeleton_l1_att = False
skeleton_l2_att = False
skeleton_i_att = False
skeleton_p_att = False
boat_ = False
inventory = []
craft = False
level = 0
trade = True
rh = 0 #just putting it here too
import random
de = tkinter.Label(tk,bg=colour,fg="#ffffff",text="Defence:")
so = tkinter.Label(tk,bg=colour,fg="#ffffff",text="Soak:")
fo = tkinter.Label(tk,bg=colour,fg="#ffffff",text="Food:")
wa = tkinter.Label(tk,bg=colour,fg="#ffffff",text="Water:")
da = tkinter.Label(tk,bg=colour,fg="#ffffff",text="Damage:")
wT = tkinter.Label(tk,bg=colour,fg="#ffffff",text="WT:")
sT = tkinter.Label(tk,bg=colour,fg="#ffffff",text="ST:")
de.place(x=200,y=540,height=20)
so.place(x=200,y=560,height=20)
da.place(x=200,y=580,height=20)
wa.place(x=270,y=600,height=20)
fo.place(x=270,y=580,height=20)
wT.place(x=270,y=560,height=20)
sT.place(x=270,y=540,height=20)
u = 1
v = 1
w = 1
def reset_trades():
    global u
    global v
    global w
    u = random.randint(1,4)
    v = random.randint(1,3)
    w = random.randint(1,3)
#-------------
#non interactables = 0,10,11,12,13,14,19,20,22,23,24,29
def attack(enemy):
  global moves
  if moves == 1:
    moves = 0
    global dam
    global turtle_hp
    global boar1_hp
    global boar2_hp
    global skeleton1_hp
    global skeleton2_hp
    global skeleton_l1_hp
    global skeleton_l2_hp
    global cube_hp
    global skeleton_i_hp
    global skeleton_p_hp
    y = find_player_y()
    global world
    if enemy == 32:
        e = dam - 6
        if e < 0:
            e = 0
        turtle_hp = turtle_hp - e
        if turtle_hp < 0:
            y2 = find_y_of(32)
            x2 = find_x_of(32,y2)
            world[y2][x2] = 0
    #-----------------------#
    elif enemy == 33:
        e = dam - 3
        if e < 0:
            e = 0
        boar1_hp = boar1_hp - e
        if boar1_hp < 0:
            y2 = find_y_of(33)
            x2 = find_x_of(33,y2)
            world[y2][x2] = 0
            a = random.randint(1,2)
            global ar
            if a == 1 and ar == 0:
                add(5)
    #-----------------------#
    elif enemy == 34:
        e = dam - 3
        if e < 0:
            e = 0
        boar2_hp = boar2_hp - e
        if boar2_hp < 0:
            y2 = find_y_of(34)
            x2 = find_x_of(34,y2)
            world[y2][x2] = 0
    #-----------------------#
    elif enemy == 36:
        e = dam - 3
        if e < 0:
            e = 0
        skeleton1_hp = skeleton1_hp - e
        if skeleton1_hp < 0:
            y2 = find_y_of(36)
            x2 = find_x_of(36,y2)
            world[y2][x2] = 0
            add(10)
    #-----------------------#
    elif enemy == 37:
        e = dam - 3
        if e < 0:
            e = 0
        skeleton2_hp = skeleton2_hp - e
        if skeleton2_hp < 0:
            y2 = find_y_of(37)
            x2 = find_x_of(37,y2)
            world[y2][x2] = 0
            add(10)
    #-----------------------#
    elif enemy == 38:
        e = dam - 4
        if e < 0:
            e = 0
        skeleton_l1_hp = skeleton_l1_hp - e
        if skeleton_l1_hp < 0:
            y2 = find_y_of(38)
            x2 = find_x_of(38,y2)
            world[y2][x2] = 27
            add(10)
    #-----------------------#
    elif enemy == 39:
        e = dam - 4
        if e < 0:
            e = 0
        skeleton_l2_hp = skeleton_l2_hp - e
        if skeleton_l2_hp < 0:
            y2 = find_y_of(39)
            x2 = find_x_of(39,y2)
            world[y2][x2] = 3
            add(10)
    #-----------------------#
    elif enemy == 40:
        e = dam - 5
        if e < 0:
            e = 0
        skeleton_i_hp = skeleton_i_hp - e
        if skeleton_i_hp < 0:
            y2 = find_y_of(40)
            x2 = find_x_of(40,y2)
            world[y2][x2] = 0
            add(10)
            add(10)
    #-----------------------#
    elif enemy == 41:
        e = int(dam * 0.8)
        e = e - 6
        if e < 0:
            e = 0
        skeleton_p_hp = skeleton_p_hp - e
        if skeleton_p_hp < 0:
            y2 = find_y_of(41)
            x2 = find_x_of(41,y2)
            world[y2][x2] = 0
            add(10)
            add(18)
            add(18)
    #-----------------------#
    elif enemy == 45:
        e = dam - 2
        if e < 0:
            e = 0
        cube_hp = cube_hp - e
        if cube_hp < 0:
            y2 = find_y_of(45)
            x2 = find_x_of(45,y2)
            world[y2][x2] = 0
    #-----------------------#
    else:
        pass
def drop(event):
    global rh
    rh = 0
def use_item(event):
    global rh
    global wt
    global st
    global food
    global water_
    global prev_block
    e = rh
    if e == 19:
        rh = 0
        food += 5
        water_ += 2
    elif e == 20:
        rh = 0
        food += 8
    elif e == 21:
        rh = 0
        food += 4
        water_ += 1
    elif e == 23:
        rh = 22
        water_ += 8
    elif e == 24:
        rh = 0
        food += 1
        water_ += 1
    elif e == 25:
        rh = 0
        food += 2
        water_ += 1
        wt += 8
    elif e == 26:
        rh = 0
        food += 2
        water_ += 1
        st = 14
    elif e == 27:
        rh = 0
        food += 2
        water_ += 1
        st += -8
        wt += 2
    elif e == 28:
        rh = 0
        prev_block = 20
    else:
        pass
    update_world()
def return_():
    global rh
    global inventory
    e = rh
    if len(inventory) < 14:
       rh = 0
       add(e)
    update_world()
def put_to_hand(slot):
  try:
    global inventory
    global rh
    global lh
    global ar
    e = inventory[slot]
    if e == 14 or e == 15:
        e = e - 13
        temp = e
        temp_ = lh
        if lh == 1:
            temp_ = 14
        elif lh == 2:
            temp_ = 15
        else:
            pass
        lh = temp
        inventory[slot] = temp_
    elif e == 5 or e == 6 or e == 7 or e == 8 or e == 29:
        if not e == 29:
            e = e - 4
        else:
            e = 5
        ar = e
        del inventory[slot]
    else:
        temp = e
        temp_ = rh
        rh = temp
        if e == 0:
            del inventory[slot]
        else:
            inventory[slot] = temp_
  except:
      pass
  finally:
    update_world()
bnnb = tkinter.Button(tk,bg=colour,fg="#ffffff",text="Drop item",command=lambda:drop(0))
bnnb.place(x=100,y=560)
bnna = tkinter.Button(tk,bg=colour,fg="#ffffff",text="Use item",command=lambda:use_item(0))
bnna.place(x=103,y=586)
block = False
blo = False
def eee():
    global blo
    blo = False
def ee():
    global block
    global blo
    block = False
    blo = True
    tk.after(2000,eee)
def block_(event):
  global blo
  if blo == False:
    global st
    st += -1
    global block
    block = True
    tk.after(1000,ee)
bnnc = tkinter.Button(tk,bg=colour,fg="#ffffff",text="Block",command=lambda:block_(0))
bnnc.place(x=112,y=612)
def down_(obj):
    global world
    y = find_y_of(obj)
    x = find_x_of(obj,y)
    if obj_in_world(obj) == True and world[y+1][x] == 0:
        y = find_y_of(obj)
        x = find_x_of(obj,y)
        world[y][x] = 0
        world[y+1][x] = obj
def gravity_for(obj):
 global world
 if obj_in_world(obj) == True:
    y = find_y_of(obj)
    x = find_x_of(obj,y)
    while world[y+1][x] == 0:
        world[y][x] = 0
        world[y+1][x] = obj
    down_(obj)
def interact(x,y):
  global rh
  global st
  axes = [1,2,3,4,30]
  loot1 = [26,26,26,26,27,27,25,16,16]
  loot2 = [2,2,2,6,6,6,13,13,13]
  loot3 = [18,18,18,18,22,22,22,28,28]
  global world
  global day
  global boat_
  y2 = find_player_y()
  x2 = find_player_x(y2)
  a = y+y2
  b = x+x2
  z = find_player_y()
  place = world[a][b]
  global prev_block
  global trade
  global craft
  if place == 48:
      world[a][b] = 0
  if not(st == 0):
    if place == 0:
        pass
    elif place == 1 and rh == 13:
        world[a][b] = 0
    elif place == 2:
        world[a][b] = 0
    elif place == 3 and rh == 22:
        rh = 23
    elif place == 4:
        world[a][b] = 0
    elif place == 5 and (rh in axes):
        world[a][b] = 0
        add(9)
        add(9)
    elif place == 6 and (rh in axes):
        world[a][b] = 0
        add(9)
    elif place == 7:
        world[a][b] = 0
        add(9)
    elif place == 8:
        add(24)
    elif place == 9:
        add(21)
    elif place == 15 and rh == 13:
        world[a][b] = 27
    elif place == 16 and rh == 13:
        world[a][b] = 0
        add(12)
    elif place == 17 and rh == 13:
        world[a][b] = 0
        add(11)
    elif place == 18:
        world[a][b] = 0
        add(10)
    elif place == 21:
        world[a][b] = 0
    elif place == 25 and rh == 17:
        world[a][b] = 0
    elif place == 46:
        day = True
    elif place == 30:
        world[a][b] = 2
        add(18)
        add(loot1[random.randint(0,8)])
        add(loot2[random.randint(0,8)])
        add(loot3[random.randint(0,8)])
        st += -1
    elif place == 26:
        craft = True
        trade = False
        load_trades()
    elif place == 42:
        craft = False
        trade = True
        load_trades()
    elif place == 31:
        if boat_ == False and z == a:
            world[a][b] = 0
            boat_ = True
    elif place == 35 and rh == 16:
        if prev_block == 27:
            world[a][b] = 27
        else:
            world[a][b] = 3
        add(19)
    elif place == 35:
        if prev_block == 27:
            world[a][b] = 27
        else:
            world[a][b] = 3
    elif place == 43:
        world[a][b] = 3
    elif place == 47:
        world[a][b] = 0
    elif 31 < place and place < 48:
        attack(place)
    elif place == 55:
        world[a][b] = 0
        add(18)
    else:
        pass
    update_world()
#-------------    
blank = tkinter.PhotoImage(file="blank.png") #0      i0  
stone = tkinter.PhotoImage(file="stone.png") #1   
sand = tkinter.PhotoImage(file="sand.png") #2     
water = tkinter.PhotoImage(file="water.png") #3   
dirt = tkinter.PhotoImage(file="dirt.png") #4     
log = tkinter.PhotoImage(file="log.png") #5      
leaves = tkinter.PhotoImage(file="leaves.png") #6  
stick = tkinter.PhotoImage(file="stick.png") #7         #i9
bush = tkinter.PhotoImage(file="bush.png") #8   
potato = tkinter.PhotoImage(file="potato_plant.png") #9   
vine = tkinter.PhotoImage(file="vine.png") #10
coral_red = tkinter.PhotoImage(file="coral_red.png") #11
coral_orange = tkinter.PhotoImage(file="coral_orange.png") #12
coral_green = tkinter.PhotoImage(file="coral_green.png") #13
coral_blue = tkinter.PhotoImage(file="coral_blue.png") #14
space_coral = tkinter.PhotoImage(file="space_coral.png") #15 
iron_ore = tkinter.PhotoImage(file="iron_ore.png") #16   
copper_ore = tkinter.PhotoImage(file="copper_ore.png") #17   
bone = tkinter.PhotoImage(file="bone.png") #18        i10  
lantern = tkinter.PhotoImage(file="lantern_normal.png") #19
ladder = tkinter.PhotoImage(file="ladder.png") #20        i28   
asteroid = tkinter.PhotoImage(file="asteroid.png") #21  
sea_bricks = tkinter.PhotoImage(file="sea_bricks.png") #22
stone_bricks = tkinter.PhotoImage(file="stone_bricks.png") #23
sea_lantern = tkinter.PhotoImage(file="lantern_sea.png") #24
cursed_lantern = tkinter.PhotoImage(file="lantern_special.png") #25  
anvil = tkinter.PhotoImage(file="anvil.png") #26   
space = tkinter.PhotoImage(file="space.png") #27
seaglass = tkinter.PhotoImage(file="seaglass.png") #28
lava = tkinter.PhotoImage(file="lava.png") #29
treasure = tkinter.PhotoImage(file="treasure.png") #30   
#balls
boat = tkinter.PhotoImage(file="boat.png") #31   
turtle_left = tkinter.PhotoImage(file="turtle_left.png") #32
turtle_right = tkinter.PhotoImage(file="turtle_right.png") #32
boar_left = tkinter.PhotoImage(file="wild_boar_left.png") #33/34
boar_right = tkinter.PhotoImage(file="wild_boar_right.png") #33/34
fish_left = tkinter.PhotoImage(file="fish_left.png")#35     i19
fish = tkinter.PhotoImage(file="fish_left.png") # im lazy
fish_right = tkinter.PhotoImage(file="fish_right.png") #35
space_fish_left = tkinter.PhotoImage(file="space_fish_left.png") #35
space_fish_right = tkinter.PhotoImage(file="space_fish_right.png") #35
skeleton_right = tkinter.PhotoImage(file="skeleton_right.png") #36/37
skeleton_left = tkinter.PhotoImage(file="skeleton_left.png") #36/37
skeleton_attack_left = tkinter.PhotoImage(file="skeleton_left_attack.png") #36/37
skeleton_attack_right = tkinter.PhotoImage(file="skeleton_right_attack.png") #36/37
leather_skeleton_right = tkinter.PhotoImage(file="leather_skeleton_right.png") #38/39
leather_skeleton_left = tkinter.PhotoImage(file="leather_skeleton_left.png") #38/39
leather_skeleton_attack_left = tkinter.PhotoImage(file="leather_skeleton_attack_left.png") #38/39
leather_skeleton_attack_right = tkinter.PhotoImage(file="leather_skeleton_attack_right.png") #38/39
bone_skeleton_right = tkinter.PhotoImage(file="bone_skeleton_right.png") #40
bone_skeleton_left = tkinter.PhotoImage(file="bone_skeleton_left.png") #40
bone_skeleton_attack_left = tkinter.PhotoImage(file="bone_skeleton_attack_left.png") #40
bone_skeleton_attack_right = tkinter.PhotoImage(file="bone_skeleton_attack_right.png") #40
pirate_right = tkinter.PhotoImage(file="pirate_right.png") #41
pirate_left = tkinter.PhotoImage(file="pirate_left.png") #41
pirate_attack_left = tkinter.PhotoImage(file="pirate_parry_left.png") #41
pirate_attack_right = tkinter.PhotoImage(file="pirate_parry_right.png") #41
human = tkinter.PhotoImage(file="human.png") #42
pufferfish = tkinter.PhotoImage(file="pufferfish.png") #43
player = tkinter.PhotoImage(file="player.png") #44
player_boat = tkinter.PhotoImage(file="boat_human.png") #44
player_ko = tkinter.PhotoImage(file="player_ko.png") #44
gelatinous_cube = tkinter.PhotoImage(file="gelatinous_cube.png") #45
tent = tkinter.PhotoImage(file="tent.png") #46
bird = tkinter.PhotoImage(file="bird.png") #47
spider = tkinter.PhotoImage(file="jumping_da_spida.png") #48
cloud = tkinter.PhotoImage(file="cloud.png") #49
stem = tkinter.PhotoImage(file="stem.png") #50
shroom_r = tkinter.PhotoImage(file="shroom_r.png") #51
shroom_b = tkinter.PhotoImage(file="shroom_b.png") #52
#balls
boat_pirate = tkinter.PhotoImage(file="boat_pirate.png") #53
bullet = tkinter.PhotoImage(file="bullet.png") #54
g_ore = tkinter.PhotoImage(file="gold_ore.png") #55
book = tkinter.PhotoImage(file="bookshelf.png") #56
grass_g = tkinter.PhotoImage(file="grass_g.png") #57
grass_o = tkinter.PhotoImage(file="grass_o.png") #58
kelp = tkinter.PhotoImage(file="kelp.png") #59
frame = tkinter.PhotoImage(file="iron_frame.png") #60
tower = tkinter.PhotoImage(file="space_tower.png") #61
rasta = tkinter.PhotoImage(file="rasta_skeleton.png") #62
#blank = i0
w_axe = tkinter.PhotoImage(file="wood_axe.png") #i1
b_axe = tkinter.PhotoImage(file="bone_axe.png") #i2
c_axe = tkinter.PhotoImage(file="copper_axe.png") #i3
i_axe = tkinter.PhotoImage(file="iron_axe.png") #i4
l_armour = tkinter.PhotoImage(file="leather_helmet.png") #i5
b_armour = tkinter.PhotoImage(file="bone_helmet.png") #i6
c_armour = tkinter.PhotoImage(file="copper_helmet.png") #i7
i_armour = tkinter.PhotoImage(file="iron_helmet.png") #i8
#stick = i9
#bone = i10
copper = tkinter.PhotoImage(file="copper.png") #i11
iron = tkinter.PhotoImage(file="iron.png") #i12
pickaxe = tkinter.PhotoImage(file="pickaxe.png") #i13
c_shield = tkinter.PhotoImage(file="shield_copper.png") #i14
i_shield = tkinter.PhotoImage(file="shield_iron.png") #i15
bucket = tkinter.PhotoImage(file="bucket.png") #i16
cutlass = tkinter.PhotoImage(file="cutlass.png") #i17
dbloon = tkinter.PhotoImage(file="dbloon.png") #i18
#fish = i19
bread = tkinter.PhotoImage(file="bread.png") #i20
spud = tkinter.PhotoImage(file="spud.png") #i21
empty_pouch = tkinter.PhotoImage(file="pouch_empty.png") #i22
full_pouch = tkinter.PhotoImage(file="pouch_water.png") #i23
berries = tkinter.PhotoImage(file="berries.png") #i24
herb_heal = tkinter.PhotoImage(file="herb_heal.png") #i25
herb_st = tkinter.PhotoImage(file="herb_strain.png") #i26
herb_ko = tkinter.PhotoImage(file="herb_ko.png") #i27
#ladder = i28
d_armour = tkinter.PhotoImage(file="diamond_helmet.png") #i29
d_axe = tkinter.PhotoImage(file="diamond_axe.png") #i30
#suck my balls
a1 = tkinter.Label(tk)
a1.place(x=20,y=20,width=60,height=60)
a2 = tkinter.Label(tk)
a2.place(x=20,y=80,width=60,height=60)
a3 = tkinter.Label(tk)
a3.place(x=20,y=140,width=60,height=60)
a4 = tkinter.Label(tk)
a4.place(x=20,y=200,width=60,height=60)
a5 = tkinter.Label(tk)
a5.place(x=20,y=260,width=60,height=60)
a6 = tkinter.Label(tk)
a6.place(x=20,y=320,width=60,height=60)
a7 = tkinter.Label(tk)
a7.place(x=20,y=380,width=60,height=60)
#
b1 = tkinter.Label(tk)
b1.place(x=80,y=20,width=60,height=60)
b2 = tkinter.Label(tk)
b2.place(x=80,y=80,width=60,height=60)
b3 = tkinter.Label(tk)
b3.place(x=80,y=140,width=60,height=60)
b4 = tkinter.Label(tk)
b4.place(x=80,y=200,width=60,height=60)
b5 = tkinter.Label(tk)
b5.place(x=80,y=260,width=60,height=60)
b6 = tkinter.Label(tk)
b6.place(x=80,y=320,width=60,height=60)
b7 = tkinter.Label(tk)
b7.place(x=80,y=380,width=60,height=60)
#
c1 = tkinter.Label(tk)
c1.place(x=140,y=20,width=60,height=60)
c2 = tkinter.Label(tk)
c2.place(x=140,y=80,width=60,height=60)
c3 = tkinter.Label(tk)
c3.place(x=140,y=140,width=60,height=60)
c4 = tkinter.Button(tk,command=lambda:interact(-1,0))
c4.place(x=140,y=200,width=60,height=60)
c5 = tkinter.Label(tk)
c5.place(x=140,y=260,width=60,height=60)
c6 = tkinter.Label(tk)
c6.place(x=140,y=320,width=60,height=60)
c7 = tkinter.Label(tk)
c7.place(x=140,y=380,width=60,height=60)
#
d1 = tkinter.Label(tk)
d1.place(x=200,y=20,width=60,height=60)
d2 = tkinter.Label(tk)
d2.place(x=200,y=80,width=60,height=60)
d3 = tkinter.Button(tk,command=lambda:interact(0,-1))
d3.place(x=200,y=140,width=60,height=60)
d4 = tkinter.Label(tk)
d4.place(x=200,y=200,width=60,height=60)
d5 = tkinter.Button(tk,command=lambda:interact(0,1))
d5.place(x=200,y=260,width=60,height=60)
d6 = tkinter.Label(tk)
d6.place(x=200,y=320,width=60,height=60)
d7 = tkinter.Label(tk)
d7.place(x=200,y=380,width=60,height=60)
#
e1 = tkinter.Label(tk)
e1.place(x=260,y=20,width=60,height=60)
e2 = tkinter.Label(tk)
e2.place(x=260,y=80,width=60,height=60)
e3 = tkinter.Label(tk)
e3.place(x=260,y=140,width=60,height=60)
e4 = tkinter.Button(tk,command=lambda:interact(1,0))
e4.place(x=260,y=200,width=60,height=60)
e5 = tkinter.Label(tk)
e5.place(x=260,y=260,width=60,height=60)
e6 = tkinter.Label(tk)
e6.place(x=260,y=320,width=60,height=60)
e7 = tkinter.Label(tk)
e7.place(x=260,y=380,width=60,height=60)
#
f1 = tkinter.Label(tk)
f1.place(x=320,y=20,width=60,height=60)
f2 = tkinter.Label(tk)
f2.place(x=320,y=80,width=60,height=60)
f3 = tkinter.Label(tk)
f3.place(x=320,y=140,width=60,height=60)
f4 = tkinter.Label(tk)
f4.place(x=320,y=200,width=60,height=60)
f5 = tkinter.Label(tk)
f5.place(x=320,y=260,width=60,height=60)
f6 = tkinter.Label(tk)
f6.place(x=320,y=320,width=60,height=60)
f7 = tkinter.Label(tk)
f7.place(x=320,y=380,width=60,height=60)
#
g1 = tkinter.Label(tk)
g1.place(x=380,y=20,width=60,height=60)
g2 = tkinter.Label(tk)
g2.place(x=380,y=80,width=60,height=60)
g3 = tkinter.Label(tk)
g3.place(x=380,y=140,width=60,height=60)
g4 = tkinter.Label(tk)
g4.place(x=380,y=200,width=60,height=60)
g5 = tkinter.Label(tk)
g5.place(x=380,y=260,width=60,height=60)
g6 = tkinter.Label(tk)
g6.place(x=380,y=320,width=60,height=60)
g7 = tkinter.Label(tk)
g7.place(x=380,y=380,width=60,height=60)
#
inv = tkinter.Label(tk,bg=colour,text="INVENTORY:",fg="#ffffff")
inv.place(x=200,y=450,height=16)
i1 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(0))
i1.place(x=20,y=470,width=30,height=30)
i2 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(1))
i2.place(x=50,y=470,width=30,height=30)
i3 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(2))
i3.place(x=80,y=470,width=30,height=30)
i4 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(3))
i4.place(x=110,y=470,width=30,height=30)
i5 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(4))
i5.place(x=140,y=470,width=30,height=30)
i6 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(5))
i6.place(x=170,y=470,width=30,height=30)
i7 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(6))
i7.place(x=200,y=470,width=30,height=30)
i8 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(7))
i8.place(x=230,y=470,width=30,height=30)
i9 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(8))
i9.place(x=260,y=470,width=30,height=30)
i10 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(9))
i10.place(x=290,y=470,width=30,height=30)
i11 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(10))
i11.place(x=320,y=470,width=30,height=30)
i12 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(11))
i12.place(x=350,y=470,width=30,height=30)
i13 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(12))
i13.place(x=380,y=470,width=30,height=30)
i14 = tkinter.Button(tk,bg=colour,command=lambda:put_to_hand(13))
i14.place(x=410,y=470,width=30,height=30)
#
def oof():
    global lh
    lh = 0
    update_world()
def oof2():
    global ar
    ar = 0
    update_world()
lha = tkinter.Button(tk,bg=colour,command=oof)
lha.place(x=20,y=520,width=30,height=30)
rha = tkinter.Button(tk,bg=colour,command=return_)
rha.place(x=140,y=520,width=30,height=30)
arm = tkinter.Button(tk,bg=colour,command=oof2)
arm.place(x=80,y=520,width=30,height=30)
lab = tkinter.Label(tk,bg=colour,fg="#ffffff",text="Left Hand    Armour    Right Hand")
lab.place(x=5,y=500,height=16)
#oh shit
lh = 0
rh = 0
ar = 0
def update_inventory():
    global inventory
    while len(inventory) > 14:
        del inventory[14]
    i = 0
    for j in range(14):
      try:
        if inventory[i] == 0:
            del inventory[i]
      except:
          pass
      finally:
          i += 1
    global lh
    global rh
    global ar
    global soak
    global def_
    global dam
    global food
    global water_
    global wt
    global st
    if food > 15:
        food = 15
    if water_ > 15:
        water_ = 15
    if wt > 13:
        wt = 13
    if st > 20:
        st = 20
    if st < 0:
        st = 0
    soak = 3 + ar
    if lh == 1 or rh == 17:
        def_ = 1
    elif lh == 2:
        def_ = 2
    else:
        def_ = 0
    if rh == 30 or rh == 17:
        dam = 9
    elif rh == 4:
        dam = 8
    elif rh == 3:
        dam = 7
    elif rh == 2:
        dam = 6
    elif rh == 1 or rh == 13:
        dam = 5
    elif rh == 9 or rh == 10 or rh == 16 or lh == 1 or lh == 2:
        dam = 4
    else:
        dam = 3
    if ar == 0:
        arm.config(image=blank)
    elif ar == 1:
        arm.config(image=l_armour)
    elif ar == 2:
        arm.config(image=b_armour)
    elif ar == 3:
        arm.config(image=c_armour)
    elif ar == 4:
        arm.config(image=i_armour)
    elif ar == 5:
        arm.config(image=d_armour)
    if lh == 0:
        lha.config(image=blank)
    elif lh == 1:
        lha.config(image=c_shield)
    elif lh == 2:
        lha.config(image=i_shield)
    if rh == 0:
        rha.config(image=blank)
    elif rh == 1:
        rha.config(image=w_axe)
    elif rh == 2:
        rha.config(image=b_axe)
    elif rh == 3:
        rha.config(image=c_axe)
    elif rh == 4:
        rha.config(image=i_axe)
    elif rh == 5:
        rha.config(image=l_armour)
    elif rh == 6:
        rha.config(image=b_armour)
    elif rh == 7:
        rha.config(image=c_armour)
    elif rh == 8:
        rha.config(image=i_armour)
    elif rh == 9:
        rha.config(image=stick)
    elif rh == 10:
        rha.config(image=bone)
    elif rh == 11:
        rha.config(image=copper)
    elif rh == 12:
        rha.config(image=iron)
    elif rh == 13:
        rha.config(image=pickaxe)
    elif rh == 14:
        rha.config(image=c_shield)
    elif rh == 15:
        rha.config(image=i_shield)
    elif rh == 16:
        rha.config(image=bucket)
    elif rh == 17:
        rha.config(image=cutlass)
    elif rh == 18:
        rha.config(image=dbloon)
    elif rh == 19:
        rha.config(image=fish)
    elif rh == 20:
        rha.config(image=bread)
    elif rh == 21:
        rha.config(image=spud)
    elif rh == 22:
        rha.config(image=empty_pouch)
    elif rh == 23:
        rha.config(image=full_pouch)
    elif rh == 24:
        rha.config(image=berries)
    elif rh == 25:
        rha.config(image=herb_heal)
    elif rh == 26:
        rha.config(image=herb_st)
    elif rh == 27:
        rha.config(image=herb_ko)
    elif rh == 28:
        rha.config(image=ladder)
    elif rh == 29:
        rha.config(image=d_armour)
    elif rh == 30:
        rha.config(image=d_axe)
    else:
        pass
    da.config(text=f"Damage: {dam}")
    so.config(text=f"Soak: {soak}")
    de.config(text=f"Defence: {def_}")
    fo.config(text=f"Food: {food}")
    wa.config(text=f"Water: {water_}")
    sT.config(text=f"ST: {st}")
    wT.config(text=f"WT: {wt}")
    #reee
    try:
        e = inventory[0]
    except:
        e = 0
    finally:
        if e == 0:
            i1.config(image=blank)
        elif e == 1:
            i1.config(image=w_axe)
        elif e == 2:
            i1.config(image=b_axe)
        elif e == 3:
            i1.config(image=c_axe)
        elif e == 4:
            i1.config(image=i_axe)
        elif e == 5:
            i1.config(image=l_armour)
        elif e == 6:
            i1.config(image=b_armour)
        elif e == 7:
            i1.config(image=c_armour)
        elif e == 8:
            i1.config(image=i_armour)
        elif e == 9:
            i1.config(image=stick)
        elif e == 10:
            i1.config(image=bone)
        elif e == 11:
            i1.config(image=copper)
        elif e == 12:
            i1.config(image=iron)
        elif e == 13:
            i1.config(image=pickaxe)
        elif e == 14:
            i1.config(image=c_shield)
        elif e == 15:
            i1.config(image=i_shield)
        elif e == 16:
            i1.config(image=bucket)
        elif e == 17:
            i1.config(image=cutlass)
        elif e == 18:
            i1.config(image=dbloon)
        elif e == 19:
            i1.config(image=fish)
        elif e == 20:
            i1.config(image=bread)
        elif e == 21:
            i1.config(image=spud)
        elif e == 22:
            i1.config(image=empty_pouch)
        elif e == 23:
            i1.config(image=full_pouch)
        elif e == 24:
            i1.config(image=berries)
        elif e == 25:
            i1.config(image=herb_heal)
        elif e == 26:
            i1.config(image=herb_st)
        elif e == 27:
            i1.config(image=herb_ko)
        elif e == 28:
            i1.config(image=ladder)
        elif e == 29:
            i1.config(image=d_armour)
        elif e == 30:
            i1.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[1]
    except:
        e = 0
    finally:
        if e == 0:
            i2.config(image=blank)
        elif e == 1:
            i2.config(image=w_axe)
        elif e == 2:
            i2.config(image=b_axe)
        elif e == 3:
            i2.config(image=c_axe)
        elif e == 4:
            i2.config(image=i_axe)
        elif e == 5:
            i2.config(image=l_armour)
        elif e == 6:
            i2.config(image=b_armour)
        elif e == 7:
            i2.config(image=c_armour)
        elif e == 8:
            i2.config(image=i_armour)
        elif e == 9:
            i2.config(image=stick)
        elif e == 10:
            i2.config(image=bone)
        elif e == 11:
            i2.config(image=copper)
        elif e == 12:
            i2.config(image=iron)
        elif e == 13:
            i2.config(image=pickaxe)
        elif e == 14:
            i2.config(image=c_shield)
        elif e == 15:
            i2.config(image=i_shield)
        elif e == 16:
            i2.config(image=bucket)
        elif e == 17:
            i2.config(image=cutlass)
        elif e == 18:
            i2.config(image=dbloon)
        elif e == 19:
            i2.config(image=fish)
        elif e == 20:
            i2.config(image=bread)
        elif e == 21:
            i2.config(image=spud)
        elif e == 22:
            i2.config(image=empty_pouch)
        elif e == 23:
            i2.config(image=full_pouch)
        elif e == 24:
            i2.config(image=berries)
        elif e == 25:
            i2.config(image=herb_heal)
        elif e == 26:
            i2.config(image=herb_st)
        elif e == 27:
            i2.config(image=herb_ko)
        elif e == 28:
            i2.config(image=ladder)
        elif e == 29:
            i2.config(image=d_armour)
        elif e == 30:
            i2.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[2]
    except:
        e = 0
    finally:
        if e == 0:
            i3.config(image=blank)
        elif e == 1:
            i3.config(image=w_axe)
        elif e == 2:
            i3.config(image=b_axe)
        elif e == 3:
            i3.config(image=c_axe)
        elif e == 4:
            i3.config(image=i_axe)
        elif e == 5:
            i3.config(image=l_armour)
        elif e == 6:
            i3.config(image=b_armour)
        elif e == 7:
            i3.config(image=c_armour)
        elif e == 8:
            i3.config(image=i_armour)
        elif e == 9:
            i3.config(image=stick)
        elif e == 10:
            i3.config(image=bone)
        elif e == 11:
            i3.config(image=copper)
        elif e == 12:
            i3.config(image=iron)
        elif e == 13:
            i3.config(image=pickaxe)
        elif e == 14:
            i3.config(image=c_shield)
        elif e == 15:
            i3.config(image=i_shield)
        elif e == 16:
            i3.config(image=bucket)
        elif e == 17:
            i3.config(image=cutlass)
        elif e == 18:
            i3.config(image=dbloon)
        elif e == 19:
            i3.config(image=fish)
        elif e == 20:
            i3.config(image=bread)
        elif e == 21:
            i3.config(image=spud)
        elif e == 22:
            i3.config(image=empty_pouch)
        elif e == 23:
            i3.config(image=full_pouch)
        elif e == 24:
            i3.config(image=berries)
        elif e == 25:
            i3.config(image=herb_heal)
        elif e == 26:
            i3.config(image=herb_st)
        elif e == 27:
            i3.config(image=herb_ko)
        elif e == 28:
            i3.config(image=ladder)
        elif e == 29:
            i3.config(image=d_armour)
        elif e == 30:
            i3.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[3]
    except:
        e = 0
    finally:
        if e == 0:
            i4.config(image=blank)
        elif e == 1:
            i4.config(image=w_axe)
        elif e == 2:
            i4.config(image=b_axe)
        elif e == 3:
            i4.config(image=c_axe)
        elif e == 4:
            i4.config(image=i_axe)
        elif e == 5:
            i4.config(image=l_armour)
        elif e == 6:
            i4.config(image=b_armour)
        elif e == 7:
            i4.config(image=c_armour)
        elif e == 8:
            i4.config(image=i_armour)
        elif e == 9:
            i4.config(image=stick)
        elif e == 10:
            i4.config(image=bone)
        elif e == 11:
            i4.config(image=copper)
        elif e == 12:
            i4.config(image=iron)
        elif e == 13:
            i4.config(image=pickaxe)
        elif e == 14:
            i4.config(image=c_shield)
        elif e == 15:
            i4.config(image=i_shield)
        elif e == 16:
            i4.config(image=bucket)
        elif e == 17:
            i4.config(image=cutlass)
        elif e == 18:
            i4.config(image=dbloon)
        elif e == 19:
            i4.config(image=fish)
        elif e == 20:
            i4.config(image=bread)
        elif e == 21:
            i4.config(image=spud)
        elif e == 22:
            i4.config(image=empty_pouch)
        elif e == 23:
            i4.config(image=full_pouch)
        elif e == 24:
            i4.config(image=berries)
        elif e == 25:
            i4.config(image=herb_heal)
        elif e == 26:
            i4.config(image=herb_st)
        elif e == 27:
            i4.config(image=herb_ko)
        elif e == 28:
            i4.config(image=ladder)
        elif e == 29:
            i4.config(image=d_armour)
        elif e == 30:
            i4.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[4]
    except:
        e = 0
    finally:
        if e == 0:
            i5.config(image=blank)
        elif e == 1:
            i5.config(image=w_axe)
        elif e == 2:
            i5.config(image=b_axe)
        elif e == 3:
            i5.config(image=c_axe)
        elif e == 4:
            i5.config(image=i_axe)
        elif e == 5:
            i5.config(image=l_armour)
        elif e == 6:
            i5.config(image=b_armour)
        elif e == 7:
            i5.config(image=c_armour)
        elif e == 8:
            i5.config(image=i_armour)
        elif e == 9:
            i5.config(image=stick)
        elif e == 10:
            i5.config(image=bone)
        elif e == 11:
            i5.config(image=copper)
        elif e == 12:
            i5.config(image=iron)
        elif e == 13:
            i5.config(image=pickaxe)
        elif e == 14:
            i5.config(image=c_shield)
        elif e == 15:
            i5.config(image=i_shield)
        elif e == 16:
            i5.config(image=bucket)
        elif e == 17:
            i5.config(image=cutlass)
        elif e == 18:
            i5.config(image=dbloon)
        elif e == 19:
            i5.config(image=fish)
        elif e == 20:
            i5.config(image=bread)
        elif e == 21:
            i5.config(image=spud)
        elif e == 22:
            i5.config(image=empty_pouch)
        elif e == 23:
            i5.config(image=full_pouch)
        elif e == 24:
            i5.config(image=berries)
        elif e == 25:
            i5.config(image=herb_heal)
        elif e == 26:
            i5.config(image=herb_st)
        elif e == 27:
            i5.config(image=herb_ko)
        elif e == 28:
            i5.config(image=ladder)
        elif e == 29:
            i5.config(image=d_armour)
        elif e == 30:
            i5.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[5]
    except:
        e = 0
    finally:
        if e == 0:
            i6.config(image=blank)
        elif e == 1:
            i6.config(image=w_axe)
        elif e == 2:
            i6.config(image=b_axe)
        elif e == 3:
            i6.config(image=c_axe)
        elif e == 4:
            i6.config(image=i_axe)
        elif e == 5:
            i6.config(image=l_armour)
        elif e == 6:
            i6.config(image=b_armour)
        elif e == 7:
            i6.config(image=c_armour)
        elif e == 8:
            i6.config(image=i_armour)
        elif e == 9:
            i6.config(image=stick)
        elif e == 10:
            i6.config(image=bone)
        elif e == 11:
            i6.config(image=copper)
        elif e == 12:
            i6.config(image=iron)
        elif e == 13:
            i6.config(image=pickaxe)
        elif e == 14:
            i6.config(image=c_shield)
        elif e == 15:
            i6.config(image=i_shield)
        elif e == 16:
            i6.config(image=bucket)
        elif e == 17:
            i6.config(image=cutlass)
        elif e == 18:
            i6.config(image=dbloon)
        elif e == 19:
            i6.config(image=fish)
        elif e == 20:
            i6.config(image=bread)
        elif e == 21:
            i6.config(image=spud)
        elif e == 22:
            i6.config(image=empty_pouch)
        elif e == 23:
            i6.config(image=full_pouch)
        elif e == 24:
            i6.config(image=berries)
        elif e == 25:
            i6.config(image=herb_heal)
        elif e == 26:
            i6.config(image=herb_st)
        elif e == 27:
            i6.config(image=herb_ko)
        elif e == 28:
            i6.config(image=ladder)
        elif e == 29:
            i6.config(image=d_armour)
        elif e == 30:
            i6.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[6]
    except:
        e = 0
    finally:
        if e == 0:
            i7.config(image=blank)
        elif e == 1:
            i7.config(image=w_axe)
        elif e == 2:
            i7.config(image=b_axe)
        elif e == 3:
            i7.config(image=c_axe)
        elif e == 4:
            i7.config(image=i_axe)
        elif e == 5:
            i7.config(image=l_armour)
        elif e == 6:
            i7.config(image=b_armour)
        elif e == 7:
            i7.config(image=c_armour)
        elif e == 8:
            i7.config(image=i_armour)
        elif e == 9:
            i7.config(image=stick)
        elif e == 10:
            i7.config(image=bone)
        elif e == 11:
            i7.config(image=copper)
        elif e == 12:
            i7.config(image=iron)
        elif e == 13:
            i7.config(image=pickaxe)
        elif e == 14:
            i7.config(image=c_shield)
        elif e == 15:
            i7.config(image=i_shield)
        elif e == 16:
            i7.config(image=bucket)
        elif e == 17:
            i7.config(image=cutlass)
        elif e == 18:
            i7.config(image=dbloon)
        elif e == 19:
            i7.config(image=fish)
        elif e == 20:
            i7.config(image=bread)
        elif e == 21:
            i7.config(image=spud)
        elif e == 22:
            i7.config(image=empty_pouch)
        elif e == 23:
            i7.config(image=full_pouch)
        elif e == 24:
            i7.config(image=berries)
        elif e == 25:
            i7.config(image=herb_heal)
        elif e == 26:
            i7.config(image=herb_st)
        elif e == 27:
            i7.config(image=herb_ko)
        elif e == 28:
            i7.config(image=ladder)
        elif e == 29:
            i7.config(image=d_armour)
        elif e == 30:
            i7.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[7]
    except:
        e = 0
    finally:
        if e == 0:
            i8.config(image=blank)
        elif e == 1:
            i8.config(image=w_axe)
        elif e == 2:
            i8.config(image=b_axe)
        elif e == 3:
            i8.config(image=c_axe)
        elif e == 4:
            i8.config(image=i_axe)
        elif e == 5:
            i8.config(image=l_armour)
        elif e == 6:
            i8.config(image=b_armour)
        elif e == 7:
            i8.config(image=c_armour)
        elif e == 8:
            i8.config(image=i_armour)
        elif e == 9:
            i8.config(image=stick)
        elif e == 10:
            i8.config(image=bone)
        elif e == 11:
            i8.config(image=copper)
        elif e == 12:
            i8.config(image=iron)
        elif e == 13:
            i8.config(image=pickaxe)
        elif e == 14:
            i8.config(image=c_shield)
        elif e == 15:
            i8.config(image=i_shield)
        elif e == 16:
            i8.config(image=bucket)
        elif e == 17:
            i8.config(image=cutlass)
        elif e == 18:
            i8.config(image=dbloon)
        elif e == 19:
            i8.config(image=fish)
        elif e == 20:
            i8.config(image=bread)
        elif e == 21:
            i8.config(image=spud)
        elif e == 22:
            i8.config(image=empty_pouch)
        elif e == 23:
            i8.config(image=full_pouch)
        elif e == 24:
            i8.config(image=berries)
        elif e == 25:
            i8.config(image=herb_heal)
        elif e == 26:
            i8.config(image=herb_st)
        elif e == 27:
            i8.config(image=herb_ko)
        elif e == 28:
            i8.config(image=ladder)
        elif e == 29:
            i8.config(image=d_armour)
        elif e == 30:
            i8.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[8]
    except:
        e = 0
    finally:
        if e == 0:
            i9.config(image=blank)
        elif e == 1:
            i9.config(image=w_axe)
        elif e == 2:
            i9.config(image=b_axe)
        elif e == 3:
            i9.config(image=c_axe)
        elif e == 4:
            i9.config(image=i_axe)
        elif e == 5:
            i9.config(image=l_armour)
        elif e == 6:
            i9.config(image=b_armour)
        elif e == 7:
            i9.config(image=c_armour)
        elif e == 8:
            i9.config(image=i_armour)
        elif e == 9:
            i9.config(image=stick)
        elif e == 10:
            i9.config(image=bone)
        elif e == 11:
            i9.config(image=copper)
        elif e == 12:
            i9.config(image=iron)
        elif e == 13:
            i9.config(image=pickaxe)
        elif e == 14:
            i9.config(image=c_shield)
        elif e == 15:
            i9.config(image=i_shield)
        elif e == 16:
            i9.config(image=bucket)
        elif e == 17:
            i9.config(image=cutlass)
        elif e == 18:
            i9.config(image=dbloon)
        elif e == 19:
            i9.config(image=fish)
        elif e == 20:
            i9.config(image=bread)
        elif e == 21:
            i9.config(image=spud)
        elif e == 22:
            i9.config(image=empty_pouch)
        elif e == 23:
            i9.config(image=full_pouch)
        elif e == 24:
            i9.config(image=berries)
        elif e == 25:
            i9.config(image=herb_heal)
        elif e == 26:
            i9.config(image=herb_st)
        elif e == 27:
            i9.config(image=herb_ko)
        elif e == 28:
            i9.config(image=ladder)
        elif e == 29:
            i9.config(image=d_armour)
        elif e == 30:
            i9.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[9]
    except:
        e = 0
    finally:
        if e == 0:
            i10.config(image=blank)
        elif e == 1:
            i10.config(image=w_axe)
        elif e == 2:
            i10.config(image=b_axe)
        elif e == 3:
            i10.config(image=c_axe)
        elif e == 4:
            i10.config(image=i_axe)
        elif e == 5:
            i10.config(image=l_armour)
        elif e == 6:
            i10.config(image=b_armour)
        elif e == 7:
            i10.config(image=c_armour)
        elif e == 8:
            i10.config(image=i_armour)
        elif e == 9:
            i10.config(image=stick)
        elif e == 10:
            i10.config(image=bone)
        elif e == 11:
            i10.config(image=copper)
        elif e == 12:
            i10.config(image=iron)
        elif e == 13:
            i10.config(image=pickaxe)
        elif e == 14:
            i10.config(image=c_shield)
        elif e == 15:
            i10.config(image=i_shield)
        elif e == 16:
            i10.config(image=bucket)
        elif e == 17:
            i10.config(image=cutlass)
        elif e == 18:
            i10.config(image=dbloon)
        elif e == 19:
            i10.config(image=fish)
        elif e == 20:
            i10.config(image=bread)
        elif e == 21:
            i10.config(image=spud)
        elif e == 22:
            i10.config(image=empty_pouch)
        elif e == 23:
            i10.config(image=full_pouch)
        elif e == 24:
            i10.config(image=berries)
        elif e == 25:
            i10.config(image=herb_heal)
        elif e == 26:
            i10.config(image=herb_st)
        elif e == 27:
            i10.config(image=herb_ko)
        elif e == 28:
            i10.config(image=ladder)
        elif e == 29:
            i10.config(image=d_armour)
        elif e == 30:
            i10.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[10]
    except:
        e = 0
    finally:
        if e == 0:
            i11.config(image=blank)
        elif e == 1:
            i11.config(image=w_axe)
        elif e == 2:
            i11.config(image=b_axe)
        elif e == 3:
            i11.config(image=c_axe)
        elif e == 4:
            i11.config(image=i_axe)
        elif e == 5:
            i11.config(image=l_armour)
        elif e == 6:
            i11.config(image=b_armour)
        elif e == 7:
            i11.config(image=c_armour)
        elif e == 8:
            i11.config(image=i_armour)
        elif e == 9:
            i11.config(image=stick)
        elif e == 10:
            i11.config(image=bone)
        elif e == 11:
            i11.config(image=copper)
        elif e == 12:
            i11.config(image=iron)
        elif e == 13:
            i11.config(image=pickaxe)
        elif e == 14:
            i11.config(image=c_shield)
        elif e == 15:
            i11.config(image=i_shield)
        elif e == 16:
            i11.config(image=bucket)
        elif e == 17:
            i11.config(image=cutlass)
        elif e == 18:
            i11.config(image=dbloon)
        elif e == 19:
            i11.config(image=fish)
        elif e == 20:
            i11.config(image=bread)
        elif e == 21:
            i11.config(image=spud)
        elif e == 22:
            i11.config(image=empty_pouch)
        elif e == 23:
            i11.config(image=full_pouch)
        elif e == 24:
            i11.config(image=berries)
        elif e == 25:
            i11.config(image=herb_heal)
        elif e == 26:
            i11.config(image=herb_st)
        elif e == 27:
            i11.config(image=herb_ko)
        elif e == 28:
            i11.config(image=ladder)
        elif e == 29:
            i11.config(image=d_armour)
        elif e == 30:
            i11.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[11]
    except:
        e = 0
    finally:
        if e == 0:
            i12.config(image=blank)
        elif e == 1:
            i12.config(image=w_axe)
        elif e == 2:
            i12.config(image=b_axe)
        elif e == 3:
            i12.config(image=c_axe)
        elif e == 4:
            i12.config(image=i_axe)
        elif e == 5:
            i12.config(image=l_armour)
        elif e == 6:
            i12.config(image=b_armour)
        elif e == 7:
            i12.config(image=c_armour)
        elif e == 8:
            i12.config(image=i_armour)
        elif e == 9:
            i12.config(image=stick)
        elif e == 10:
            i12.config(image=bone)
        elif e == 11:
            i12.config(image=copper)
        elif e == 12:
            i12.config(image=iron)
        elif e == 13:
            i12.config(image=pickaxe)
        elif e == 14:
            i12.config(image=c_shield)
        elif e == 15:
            i12.config(image=i_shield)
        elif e == 16:
            i12.config(image=bucket)
        elif e == 17:
            i12.config(image=cutlass)
        elif e == 18:
            i12.config(image=dbloon)
        elif e == 19:
            i12.config(image=fish)
        elif e == 20:
            i12.config(image=bread)
        elif e == 21:
            i12.config(image=spud)
        elif e == 22:
            i12.config(image=empty_pouch)
        elif e == 23:
            i12.config(image=full_pouch)
        elif e == 24:
            i12.config(image=berries)
        elif e == 25:
            i12.config(image=herb_heal)
        elif e == 26:
            i12.config(image=herb_st)
        elif e == 27:
            i12.config(image=herb_ko)
        elif e == 28:
            i12.config(image=ladder)
        elif e == 29:
            i12.config(image=d_armour)
        elif e == 30:
            i12.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[12]
    except:
        e = 0
    finally:
        if e == 0:
            i13.config(image=blank)
        elif e == 1:
            i13.config(image=w_axe)
        elif e == 2:
            i13.config(image=b_axe)
        elif e == 3:
            i13.config(image=c_axe)
        elif e == 4:
            i13.config(image=i_axe)
        elif e == 5:
            i13.config(image=l_armour)
        elif e == 6:
            i13.config(image=b_armour)
        elif e == 7:
            i13.config(image=c_armour)
        elif e == 8:
            i13.config(image=i_armour)
        elif e == 9:
            i13.config(image=stick)
        elif e == 10:
            i13.config(image=bone)
        elif e == 11:
            i13.config(image=copper)
        elif e == 12:
            i13.config(image=iron)
        elif e == 13:
            i13.config(image=pickaxe)
        elif e == 14:
            i13.config(image=c_shield)
        elif e == 15:
            i13.config(image=i_shield)
        elif e == 16:
            i13.config(image=bucket)
        elif e == 17:
            i13.config(image=cutlass)
        elif e == 18:
            i13.config(image=dbloon)
        elif e == 19:
            i13.config(image=fish)
        elif e == 20:
            i13.config(image=bread)
        elif e == 21:
            i13.config(image=spud)
        elif e == 22:
            i13.config(image=empty_pouch)
        elif e == 23:
            i13.config(image=full_pouch)
        elif e == 24:
            i13.config(image=berries)
        elif e == 25:
            i13.config(image=herb_heal)
        elif e == 26:
            i13.config(image=herb_st)
        elif e == 27:
            i13.config(image=herb_ko)
        elif e == 28:
            i13.config(image=ladder)
        elif e == 29:
            i13.config(image=d_armour)
        elif e == 30:
            i13.config(image=d_axe)
        else:
            pass
    #oh jesus
    try:
        e = inventory[13]
    except:
        e = 0
    finally:
        if e == 0:
            i14.config(image=blank)
        elif e == 1:
            i14.config(image=w_axe)
        elif e == 2:
            i14.config(image=b_axe)
        elif e == 3:
            i14.config(image=c_axe)
        elif e == 4:
            i14.config(image=i_axe)
        elif e == 5:
            i14.config(image=l_armour)
        elif e == 6:
            i14.config(image=b_armour)
        elif e == 7:
            i14.config(image=c_armour)
        elif e == 8:
            i14.config(image=i_armour)
        elif e == 9:
            i14.config(image=stick)
        elif e == 10:
            i14.config(image=bone)
        elif e == 11:
            i14.config(image=copper)
        elif e == 12:
            i14.config(image=iron)
        elif e == 13:
            i14.config(image=pickaxe)
        elif e == 14:
            i14.config(image=c_shield)
        elif e == 15:
            i14.config(image=i_shield)
        elif e == 16:
            i14.config(image=bucket)
        elif e == 17:
            i14.config(image=cutlass)
        elif e == 18:
            i14.config(image=dbloon)
        elif e == 19:
            i14.config(image=fish)
        elif e == 20:
            i14.config(image=bread)
        elif e == 21:
            i14.config(image=spud)
        elif e == 22:
            i14.config(image=empty_pouch)
        elif e == 23:
            i14.config(image=full_pouch)
        elif e == 24:
            i14.config(image=berries)
        elif e == 25:
            i14.config(image=herb_heal)
        elif e == 26:
            i14.config(image=herb_st)
        elif e == 27:
            i14.config(image=herb_ko)
        elif e == 28:
            i14.config(image=ladder)
        elif e == 29:
            i14.config(image=d_armour)
        elif e == 30:
            i14.config(image=d_axe)
        else:
            pass
    #oh jesus
import random
seen_world = []
prev_block = 0  #goat variable
#class basics():    #44 is player
def find_player_y():
  try:
    global world
    notfound = True
    i = 0
    while notfound:
        if 44 in world[i]:
            notfound = False
        else:
            i += 1
    return i
  except:
    return 4
def find_player_x(y):
  try:
    global world
    notfound = True
    i = 0
    while notfound:
        if world[y][i] == 44:
            notfound = False
        else:
            i += 1
    return i
  except:
    return 4
def find_y_of(obj):
 if obj_in_world(obj) == True:
    global world
    notfound = True
    i = 0
    while notfound:
        if obj in world[i]:
            notfound = False
        else:
            i += 1
    return i
def find_x_of(obj,y):
 if obj_in_world(obj) == True:
    global world
    notfound = True
    i = 0
    while notfound:
        if world[y][i] == obj:
            notfound = False
        else:
            i += 1
    return i
def obj_near_player(obj):
    y = find_player_y()  
    x = find_player_x(y)
    if world[y][x+1] == obj or world[y][x-1] == obj or world[y+1][x] == obj or world[y-1][x] == obj:
        return True
    else:
        return False
def find_amount_of(obj):
    global world
    k = 0
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == obj:
                k += 1
    return k
def obj_in_world(obj):
    global world
    e = False
    for i in range(len(world)):
        if obj in world[i]:
            e = True
            break
    return e
def obj_in_seen_world(obj):
    global seen_world
    e = False
    for i in range(len(seen_world)):
        if obj in seen_world[i]:
            e = True
            break
    return e
def remove_and_replace(obj,replacement):   
    if obj_in_world(obj) == True and obj_in_seen_world(obj) == False:
        y = find_y_of(obj)
        x = find_x_of(obj,y)
        world[y][x] = replacement
        update_world()
def add(obj):
    global inventory
    if len(inventory) < 14:
        inventory.append(obj)
def rem(obj):
    global inventory
    if obj in inventory:
        e = 0
        while not inventory[e] == obj:
            e += 1
        del inventory[e]
#end class
seen_world=[[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
weeb = tkinter.Label(tk,bg=colour,fg="#ffffff",text="o")
weeb.place(x=165,y=615)
def update_world():
    global world
    global seen_world
    global inventory
    update_inventory()
    y = find_player_y()
    x = find_player_x(y)
    seen_world[0][0] = world[y-3][x-3]
    seen_world[0][1] = world[y-3][x-2]
    seen_world[0][2] = world[y-3][x-1]
    seen_world[0][3] = world[y-3][x]
    seen_world[0][4] = world[y-3][x+1]
    seen_world[0][5] = world[y-3][x+2]
    seen_world[0][6] = world[y-3][x+3]
    seen_world[1][0] = world[y-2][x-3]
    seen_world[1][1] = world[y-2][x-2]
    seen_world[1][2] = world[y-2][x-1]
    seen_world[1][3] = world[y-2][x]
    seen_world[1][4] = world[y-2][x+1]
    seen_world[1][5] = world[y-2][x+2]
    seen_world[1][6] = world[y-2][x+3]
    seen_world[2][0] = world[y-1][x-3]
    seen_world[2][1] = world[y-1][x-2]
    seen_world[2][2] = world[y-1][x-1]
    seen_world[2][3] = world[y-1][x]
    seen_world[2][4] = world[y-1][x+1]
    seen_world[2][5] = world[y-1][x+2]
    seen_world[2][6] = world[y-1][x+3]
    seen_world[3][0] = world[y][x-3]
    seen_world[3][1] = world[y][x-2]
    seen_world[3][2] = world[y][x-1]
    seen_world[3][3] = world[y][x]
    seen_world[3][4] = world[y][x+1]
    seen_world[3][5] = world[y][x+2]
    seen_world[3][6] = world[y][x+3]
    seen_world[4][0] = world[y+1][x-3]
    seen_world[4][1] = world[y+1][x-2]
    seen_world[4][2] = world[y+1][x-1]
    seen_world[4][3] = world[y+1][x]
    seen_world[4][4] = world[y+1][x+1]
    seen_world[4][5] = world[y+1][x+2]
    seen_world[4][6] = world[y+1][x+3]
    seen_world[5][0] = world[y+2][x-3]
    seen_world[5][1] = world[y+2][x-2]
    seen_world[5][2] = world[y+2][x-1]
    seen_world[5][3] = world[y+2][x]
    seen_world[5][4] = world[y+2][x+1]
    seen_world[5][5] = world[y+2][x+2]
    seen_world[5][6] = world[y+2][x+3]
    seen_world[6][0] = world[y+3][x-3]
    seen_world[6][1] = world[y+3][x-2]
    seen_world[6][2] = world[y+3][x-1]
    seen_world[6][3] = world[y+3][x]
    seen_world[6][4] = world[y+3][x+1]
    seen_world[6][5] = world[y+3][x+2]
    seen_world[6][6] = world[y+3][x+3]
    #damn
    global day
    global wt
    global st
    wt = int(wt)
    st = int(st)
    global block
    if block == True:
        weeb.config(text="x")
    else:
        weeb.config(text="o")
    if y > 24 and x > 900:
        back = "#040404"
    else:
        if prev_block == 3:
            back = "#00bbff"
        elif y > 18 and day == True and y < 51:
            back = "#8ef4ff"
        else:
            back = "#040404"
    if y > 24 and x > 900:
        back2 = "#040404"
    else:
        if y > 18 and day == True and y < 51:
            back2 = "#8ef4ff"
        else:
            back2 = "#040404"
    global fish_dir
    global turtle_dir
    global skeleton1_att
    global skeleton2_att
    global skeleton_l1_att
    global skeleton_l2_att
    global skeleton_i_att
    global skeleton_p_att
    #here we go
    e = seen_world[0][0]
    if e == 0:
        a1.config(bg=back2,image=blank)
    elif e == 1:
        a1.config(bg=back,image=stone)
    elif e == 2:
        a1.config(bg=back,image=sand)
    elif e == 3:
        a1.config(bg=back,image=water)
    elif e == 4:
        a1.config(bg=back,image=dirt)
    elif e == 5:
        a1.config(bg=back,image=log)
    elif e == 6:
        a1.config(bg=back,image=leaves)
    elif e == 7:
        a1.config(bg=back,image=stick)
    elif e == 8:
        a1.config(bg=back,image=bush)
    elif e == 9:
        a1.config(bg=back,image=potato)
    elif e == 10:
        a1.config(bg=back,image=vine)
    elif e == 11:
        a1.config(bg=back,image=coral_red)
    elif e == 12:
        a1.config(bg=back,image=coral_orange)
    elif e == 13:
        a1.config(bg=back,image=coral_green)
    elif e == 14:
        a1.config(bg=back,image=coral_blue)
    elif e == 15:
        a1.config(bg=back,image=space_coral)
    elif e == 16:
        a1.config(bg=back,image=iron_ore)
    elif e == 17:
        a1.config(bg=back,image=copper_ore)
    elif e == 18:
        a1.config(bg=back,image=bone)
    elif e == 19:
        a1.config(bg=back,image=lantern)
    elif e == 20:
        a1.config(bg=back,image=ladder)
    elif e == 21:
        a1.config(bg=back,image=asteroid)
    elif e == 22:
        a1.config(bg=back,image=sea_bricks)
    elif e == 23:
        a1.config(bg=back,image=stone_bricks)
    elif e == 24:
        a1.config(bg=back,image=sea_lantern)
    elif e == 25:
        a1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a1.config(bg=back,image=anvil)
    elif e == 27:
        a1.config(bg=back,image=space)
    elif e == 28:
        a1.config(bg=back,image=seaglass)
    elif e == 29:
        a1.config(bg=back,image=lava)
    elif e == 30:
        a1.config(bg=back,image=treasure)
    elif e == 31:
        a1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a1.config(bg=back,image=turtle_right)
        else:
            a1.config(bg=back,image=turtle_left)
    elif e == 33:
        a1.config(bg=back,image=boar_right)
    elif e == 34:
        a1.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a1.config(bg=back,image=space_fish_right)
            else:
                a1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a1.config(bg=back,image=fish_right)
            else:
                a1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a1.config(bg=back,image=skeleton_attack_right)
        else:
            a1.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a1.config(bg=back,image=skeleton_attack_right)
        else:
            a1.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a1.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a1.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a1.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a1.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a1.config(bg=back,image=pirate_attack_right)
        else:
            a1.config(bg=back,image=pirate_right)
    elif e == 42:
        a1.config(bg=back,image=human)
    elif e == 43:
        a1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a1.config(bg=back,image=tent)
    elif e == 47:
        a1.config(bg=back,image=bird)
    elif e == 48:
        a1.config(bg=back,image=spider)
    elif e == 49:
        a1.config(bg=back,image=cloud)
    elif e == 50:
        a1.config(bg=back,image=stem)
    elif e == 51:
        a1.config(bg=back,image=shroom_r)
    elif e == 52:
        a1.config(bg=back,image=shroom_b)
    elif e == 53:
        a1.config(bg=back,image=boat_pirate)
    elif e == 54:
        a1.config(bg=back,image=bullet)
    elif e == 55:
        a1.config(bg=back,image=g_ore)
    elif e == 56:
        a1.config(bg=back,image=book)
    elif e == 57:
        a1.config(bg=back,image=grass_g)
    elif e == 58:
        a1.config(bg=back,image=grass_o)
    elif e == 59:
        a1.config(bg=back,image=kelp)
    elif e == 60:
        a1.config(bg=back,image=frame)
    elif e == 61:
        a1.config(bg=back,image=tower)
    elif e == 62:
        a1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[0][1]
    if e == 0:
        b1.config(bg=back2,image=blank)
    elif e == 1:
        b1.config(bg=back,image=stone)
    elif e == 2:
        b1.config(bg=back,image=sand)
    elif e == 3:
        b1.config(bg=back,image=water)
    elif e == 4:
        b1.config(bg=back,image=dirt)
    elif e == 5:
        b1.config(bg=back,image=log)
    elif e == 6:
        b1.config(bg=back,image=leaves)
    elif e == 7:
        b1.config(bg=back,image=stick)
    elif e == 8:
        b1.config(bg=back,image=bush)
    elif e == 9:
        b1.config(bg=back,image=potato)
    elif e == 10:
        b1.config(bg=back,image=vine)
    elif e == 11:
        b1.config(bg=back,image=coral_red)
    elif e == 12:
        b1.config(bg=back,image=coral_orange)
    elif e == 13:
        b1.config(bg=back,image=coral_green)
    elif e == 14:
        b1.config(bg=back,image=coral_blue)
    elif e == 15:
        b1.config(bg=back,image=space_coral)
    elif e == 16:
        b1.config(bg=back,image=iron_ore)
    elif e == 17:
        b1.config(bg=back,image=copper_ore)
    elif e == 18:
        b1.config(bg=back,image=bone)
    elif e == 19:
        b1.config(bg=back,image=lantern)
    elif e == 20:
        b1.config(bg=back,image=ladder)
    elif e == 21:
        b1.config(bg=back,image=asteroid)
    elif e == 22:
        b1.config(bg=back,image=sea_bricks)
    elif e == 23:
        b1.config(bg=back,image=stone_bricks)
    elif e == 24:
        b1.config(bg=back,image=sea_lantern)
    elif e == 25:
        b1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b1.config(bg=back,image=anvil)
    elif e == 27:
        b1.config(bg=back,image=space)
    elif e == 28:
        b1.config(bg=back,image=seaglass)
    elif e == 29:
        b1.config(bg=back,image=lava)
    elif e == 30:
        b1.config(bg=back,image=treasure)
    elif e == 31:
        b1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b1.config(bg=back,image=turtle_right)
        else:
            b1.config(bg=back,image=turtle_left)
    elif e == 33:
        b1.config(bg=back,image=boar_right)
    elif e == 34:
        b1.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b1.config(bg=back,image=space_fish_right)
            else:
                b1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b1.config(bg=back,image=fish_right)
            else:
                b1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b1.config(bg=back,image=skeleton_attack_right)
        else:
            b1.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b1.config(bg=back,image=skeleton_attack_right)
        else:
            b1.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b1.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b1.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b1.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b1.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b1.config(bg=back,image=pirate_attack_right)
        else:
            b1.config(bg=back,image=pirate_right)
    elif e == 42:
        b1.config(bg=back,image=human)
    elif e == 43:
        b1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b1.config(bg=back,image=tent)
    elif e == 47:
        b1.config(bg=back,image=bird)
    elif e == 48:
        b1.config(bg=back,image=spider)
    elif e == 49:
        b1.config(bg=back,image=cloud)
    elif e == 50:
        b1.config(bg=back,image=stem)
    elif e == 51:
        b1.config(bg=back,image=shroom_r)
    elif e == 52:
        b1.config(bg=back,image=shroom_b)
    elif e == 53:
        b1.config(bg=back,image=boat_pirate)
    elif e == 54:
        b1.config(bg=back,image=bullet)
    elif e == 55:
        b1.config(bg=back,image=g_ore)
    elif e == 56:
        b1.config(bg=back,image=book)
    elif e == 57:
        b1.config(bg=back,image=grass_g)
    elif e == 58:
        b1.config(bg=back,image=grass_o)
    elif e == 59:
        b1.config(bg=back,image=kelp)
    elif e == 60:
        b1.config(bg=back,image=frame)
    elif e == 61:
        b1.config(bg=back,image=tower)
    elif e == 62:
        b1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[0][2]
    if e == 0:
        c1.config(bg=back2,image=blank)
    elif e == 1:
        c1.config(bg=back,image=stone)
    elif e == 2:
        c1.config(bg=back,image=sand)
    elif e == 3:
        c1.config(bg=back,image=water)
    elif e == 4:
        c1.config(bg=back,image=dirt)
    elif e == 5:
        c1.config(bg=back,image=log)
    elif e == 6:
        c1.config(bg=back,image=leaves)
    elif e == 7:
        c1.config(bg=back,image=stick)
    elif e == 8:
        c1.config(bg=back,image=bush)
    elif e == 9:
        c1.config(bg=back,image=potato)
    elif e == 10:
        c1.config(bg=back,image=vine)
    elif e == 11:
        c1.config(bg=back,image=coral_red)
    elif e == 12:
        c1.config(bg=back,image=coral_orange)
    elif e == 13:
        c1.config(bg=back,image=coral_green)
    elif e == 14:
        c1.config(bg=back,image=coral_blue)
    elif e == 15:
        c1.config(bg=back,image=space_coral)
    elif e == 16:
        c1.config(bg=back,image=iron_ore)
    elif e == 17:
        c1.config(bg=back,image=copper_ore)
    elif e == 18:
        c1.config(bg=back,image=bone)
    elif e == 19:
        c1.config(bg=back,image=lantern)
    elif e == 20:
        c1.config(bg=back,image=ladder)
    elif e == 21:
        c1.config(bg=back,image=asteroid)
    elif e == 22:
        c1.config(bg=back,image=sea_bricks)
    elif e == 23:
        c1.config(bg=back,image=stone_bricks)
    elif e == 24:
        c1.config(bg=back,image=sea_lantern)
    elif e == 25:
        c1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c1.config(bg=back,image=anvil)
    elif e == 27:
        c1.config(bg=back,image=space)
    elif e == 28:
        c1.config(bg=back,image=seaglass)
    elif e == 29:
        c1.config(bg=back,image=lava)
    elif e == 30:
        c1.config(bg=back,image=treasure)
    elif e == 31:
        c1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c1.config(bg=back,image=turtle_right)
        else:
            c1.config(bg=back,image=turtle_left)
    elif e == 33:
        c1.config(bg=back,image=boar_right)
    elif e == 34:
        c1.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c1.config(bg=back,image=space_fish_right)
            else:
                c1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c1.config(bg=back,image=fish_right)
            else:
                c1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c1.config(bg=back,image=skeleton_attack_right)
        else:
            c1.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c1.config(bg=back,image=skeleton_attack_right)
        else:
            c1.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c1.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c1.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c1.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c1.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c1.config(bg=back,image=pirate_attack_right)
        else:
            c1.config(bg=back,image=pirate_right)
    elif e == 42:
        c1.config(bg=back,image=human)
    elif e == 43:
        c1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c1.config(bg=back,image=tent)
    elif e == 47:
        c1.config(bg=back,image=bird)
    elif e == 48:
        c1.config(bg=back,image=spider)
    elif e == 49:
        c1.config(bg=back,image=cloud)
    elif e == 50:
        c1.config(bg=back,image=stem)
    elif e == 51:
        c1.config(bg=back,image=shroom_r)
    elif e == 52:
        c1.config(bg=back,image=shroom_b)
    elif e == 53:
        c1.config(bg=back,image=boat_pirate)
    elif e == 54:
        c1.config(bg=back,image=bullet)
    elif e == 55:
        c1.config(bg=back,image=g_ore)
    elif e == 56:
        c1.config(bg=back,image=book)
    elif e == 57:
        c1.config(bg=back,image=grass_g)
    elif e == 58:
        c1.config(bg=back,image=grass_o)
    elif e == 59:
        c1.config(bg=back,image=kelp)
    elif e == 60:
        c1.config(bg=back,image=frame)
    elif e == 61:
        c1.config(bg=back,image=tower)
    elif e == 62:
        c1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[0][3]
    if e == 0:
        d1.config(bg=back2,image=blank)
    elif e == 1:
        d1.config(bg=back,image=stone)
    elif e == 2:
        d1.config(bg=back,image=sand)
    elif e == 3:
        d1.config(bg=back,image=water)
    elif e == 4:
        d1.config(bg=back,image=dirt)
    elif e == 5:
        d1.config(bg=back,image=log)
    elif e == 6:
        d1.config(bg=back,image=leaves)
    elif e == 7:
        d1.config(bg=back,image=stick)
    elif e == 8:
        d1.config(bg=back,image=bush)
    elif e == 9:
        d1.config(bg=back,image=potato)
    elif e == 10:
        d1.config(bg=back,image=vine)
    elif e == 11:
        d1.config(bg=back,image=coral_red)
    elif e == 12:
        d1.config(bg=back,image=coral_orange)
    elif e == 13:
        d1.config(bg=back,image=coral_green)
    elif e == 14:
        d1.config(bg=back,image=coral_blue)
    elif e == 15:
        d1.config(bg=back,image=space_coral)
    elif e == 16:
        d1.config(bg=back,image=iron_ore)
    elif e == 17:
        d1.config(bg=back,image=copper_ore)
    elif e == 18:
        d1.config(bg=back,image=bone)
    elif e == 19:
        d1.config(bg=back,image=lantern)
    elif e == 20:
        d1.config(bg=back,image=ladder)
    elif e == 21:
        d1.config(bg=back,image=asteroid)
    elif e == 22:
        d1.config(bg=back,image=sea_bricks)
    elif e == 23:
        d1.config(bg=back,image=stone_bricks)
    elif e == 24:
        d1.config(bg=back,image=sea_lantern)
    elif e == 25:
        d1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d1.config(bg=back,image=anvil)
    elif e == 27:
        d1.config(bg=back,image=space)
    elif e == 28:
        d1.config(bg=back,image=seaglass)
    elif e == 29:
        d1.config(bg=back,image=lava)
    elif e == 30:
        d1.config(bg=back,image=treasure)
    elif e == 31:
        d1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d1.config(bg=back,image=turtle_right)
        else:
            d1.config(bg=back,image=turtle_left)
    elif e == 33:
        d1.config(bg=back,image=boar_right)
    elif e == 34:
        d1.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d1.config(bg=back,image=space_fish_right)
            else:
                d1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d1.config(bg=back,image=fish_right)
            else:
                d1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d1.config(bg=back,image=skeleton_attack_right)
        else:
            d1.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d1.config(bg=back,image=skeleton_attack_right)
        else:
            d1.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d1.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d1.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d1.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d1.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d1.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d1.config(bg=back,image=pirate_attack_right)
        else:
            d1.config(bg=back,image=pirate_right)
    elif e == 42:
        d1.config(bg=back,image=human)
    elif e == 43:
        d1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        d1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d1.config(bg=back,image=tent)
    elif e == 47:
        d1.config(bg=back,image=bird)
    elif e == 48:
        d1.config(bg=back,image=spider)
    elif e == 49:
        d1.config(bg=back,image=cloud)
    elif e == 50:
        d1.config(bg=back,image=stem)
    elif e == 51:
        d1.config(bg=back,image=shroom_r)
    elif e == 52:
        d1.config(bg=back,image=shroom_b)
    elif e == 53:
        d1.config(bg=back,image=boat_pirate)
    elif e == 54:
        d1.config(bg=back,image=bullet)
    elif e == 55:
        d1.config(bg=back,image=g_ore)
    elif e == 56:
        d1.config(bg=back,image=book)
    elif e == 57:
        d1.config(bg=back,image=grass_g)
    elif e == 58:
        d1.config(bg=back,image=grass_o)
    elif e == 59:
        d1.config(bg=back,image=kelp)
    elif e == 60:
        d1.config(bg=back,image=frame)
    elif e == 61:
        d1.config(bg=back,image=tower)
    elif e == 62:
        d1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[0][4]
    if e == 0:
        e1.config(bg=back2,image=blank)
    elif e == 1:
        e1.config(bg=back,image=stone)
    elif e == 2:
        e1.config(bg=back,image=sand)
    elif e == 3:
        e1.config(bg=back,image=water)
    elif e == 4:
        e1.config(bg=back,image=dirt)
    elif e == 5:
        e1.config(bg=back,image=log)
    elif e == 6:
        e1.config(bg=back,image=leaves)
    elif e == 7:
        e1.config(bg=back,image=stick)
    elif e == 8:
        e1.config(bg=back,image=bush)
    elif e == 9:
        e1.config(bg=back,image=potato)
    elif e == 10:
        e1.config(bg=back,image=vine)
    elif e == 11:
        e1.config(bg=back,image=coral_red)
    elif e == 12:
        e1.config(bg=back,image=coral_orange)
    elif e == 13:
        e1.config(bg=back,image=coral_green)
    elif e == 14:
        e1.config(bg=back,image=coral_blue)
    elif e == 15:
        e1.config(bg=back,image=space_coral)
    elif e == 16:
        e1.config(bg=back,image=iron_ore)
    elif e == 17:
        e1.config(bg=back,image=copper_ore)
    elif e == 18:
        e1.config(bg=back,image=bone)
    elif e == 19:
        e1.config(bg=back,image=lantern)
    elif e == 20:
        e1.config(bg=back,image=ladder)
    elif e == 21:
        e1.config(bg=back,image=asteroid)
    elif e == 22:
        e1.config(bg=back,image=sea_bricks)
    elif e == 23:
        e1.config(bg=back,image=stone_bricks)
    elif e == 24:
        e1.config(bg=back,image=sea_lantern)
    elif e == 25:
        e1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e1.config(bg=back,image=anvil)
    elif e == 27:
        e1.config(bg=back,image=space)
    elif e == 28:
        e1.config(bg=back,image=seaglass)
    elif e == 29:
        e1.config(bg=back,image=lava)
    elif e == 30:
        e1.config(bg=back,image=treasure)
    elif e == 31:
        e1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e1.config(bg=back,image=turtle_right)
        else:
            e1.config(bg=back,image=turtle_left)
    elif e == 33:
        e1.config(bg=back,image=boar_left)
    elif e == 34:
        e1.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e1.config(bg=back,image=space_fish_right)
            else:
                e1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e1.config(bg=back,image=fish_right)
            else:
                e1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e1.config(bg=back,image=skeleton_attack_left)
        else:
            e1.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e1.config(bg=back,image=skeleton_attack_left)
        else:
            e1.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e1.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e1.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e1.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e1.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e1.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e1.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e1.config(bg=back,image=pirate_attack_left)
        else:
            e1.config(bg=back,image=pirate_left)
    elif e == 42:
        e1.config(bg=back,image=human)
    elif e == 43:
        e1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e1.config(bg=back,image=tent)
    elif e == 47:
        e1.config(bg=back,image=bird)
    elif e == 48:
        e1.config(bg=back,image=spider)
    elif e == 49:
        e1.config(bg=back,image=cloud)
    elif e == 50:
        e1.config(bg=back,image=stem)
    elif e == 51:
        e1.config(bg=back,image=shroom_r)
    elif e == 52:
        e1.config(bg=back,image=shroom_b)
    elif e == 53:
        e1.config(bg=back,image=boat_pirate)
    elif e == 54:
        e1.config(bg=back,image=bullet)
    elif e == 55:
        e1.config(bg=back,image=g_ore)
    elif e == 56:
        e1.config(bg=back,image=book)
    elif e == 57:
        e1.config(bg=back,image=grass_g)
    elif e == 58:
        e1.config(bg=back,image=grass_o)
    elif e == 59:
        e1.config(bg=back,image=kelp)
    elif e == 60:
        e1.config(bg=back,image=frame)
    elif e == 61:
        e1.config(bg=back,image=tower)
    elif e == 62:
        e1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[0][5]
    if e == 0:
        f1.config(bg=back2,image=blank)
    elif e == 1:
        f1.config(bg=back,image=stone)
    elif e == 2:
        f1.config(bg=back,image=sand)
    elif e == 3:
        f1.config(bg=back,image=water)
    elif e == 4:
        f1.config(bg=back,image=dirt)
    elif e == 5:
        f1.config(bg=back,image=log)
    elif e == 6:
        f1.config(bg=back,image=leaves)
    elif e == 7:
        f1.config(bg=back,image=stick)
    elif e == 8:
        f1.config(bg=back,image=bush)
    elif e == 9:
        f1.config(bg=back,image=potato)
    elif e == 10:
        f1.config(bg=back,image=vine)
    elif e == 11:
        f1.config(bg=back,image=coral_red)
    elif e == 12:
        f1.config(bg=back,image=coral_orange)
    elif e == 13:
        f1.config(bg=back,image=coral_green)
    elif e == 14:
        f1.config(bg=back,image=coral_blue)
    elif e == 15:
        f1.config(bg=back,image=space_coral)
    elif e == 16:
        f1.config(bg=back,image=iron_ore)
    elif e == 17:
        f1.config(bg=back,image=copper_ore)
    elif e == 18:
        f1.config(bg=back,image=bone)
    elif e == 19:
        f1.config(bg=back,image=lantern)
    elif e == 20:
        f1.config(bg=back,image=ladder)
    elif e == 21:
        f1.config(bg=back,image=asteroid)
    elif e == 22:
        f1.config(bg=back,image=sea_bricks)
    elif e == 23:
        f1.config(bg=back,image=stone_bricks)
    elif e == 24:
        f1.config(bg=back,image=sea_lantern)
    elif e == 25:
        f1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f1.config(bg=back,image=anvil)
    elif e == 27:
        f1.config(bg=back,image=space)
    elif e == 28:
        f1.config(bg=back,image=seaglass)
    elif e == 29:
        f1.config(bg=back,image=lava)
    elif e == 30:
        f1.config(bg=back,image=treasure)
    elif e == 31:
        f1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f1.config(bg=back,image=turtle_right)
        else:
            f1.config(bg=back,image=turtle_left)
    elif e == 33:
        f1.config(bg=back,image=boar_left)
    elif e == 34:
        f1.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f1.config(bg=back,image=space_fish_right)
            else:
                f1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f1.config(bg=back,image=fish_right)
            else:
                f1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f1.config(bg=back,image=skeleton_attack_left)
        else:
            f1.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f1.config(bg=back,image=skeleton_attack_left)
        else:
            f1.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f1.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f1.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f1.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f1.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f1.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f1.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f1.config(bg=back,image=pirate_attack_left)
        else:
            f1.config(bg=back,image=pirate_left)
    elif e == 42:
        f1.config(bg=back,image=human)
    elif e == 43:
        f1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f1.config(bg=back,image=tent)
    elif e == 47:
        f1.config(bg=back,image=bird)
    elif e == 48:
        f1.config(bg=back,image=spider)
    elif e == 49:
        f1.config(bg=back,image=cloud)
    elif e == 50:
        f1.config(bg=back,image=stem)
    elif e == 51:
        f1.config(bg=back,image=shroom_r)
    elif e == 52:
        f1.config(bg=back,image=shroom_b)
    elif e == 53:
        f1.config(bg=back,image=boat_pirate)
    elif e == 54:
        f1.config(bg=back,image=bullet)
    elif e == 55:
        f1.config(bg=back,image=g_ore)
    elif e == 56:
        f1.config(bg=back,image=book)
    elif e == 57:
        f1.config(bg=back,image=grass_g)
    elif e == 58:
        f1.config(bg=back,image=grass_o)
    elif e == 59:
        f1.config(bg=back,image=kelp)
    elif e == 60:
        f1.config(bg=back,image=frame)
    elif e == 61:
        f1.config(bg=back,image=tower)
    elif e == 62:
        f1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[0][6]
    if e == 0:
        g1.config(bg=back2,image=blank)
    elif e == 1:
        g1.config(bg=back,image=stone)
    elif e == 2:
        g1.config(bg=back,image=sand)
    elif e == 3:
        g1.config(bg=back,image=water)
    elif e == 4:
        g1.config(bg=back,image=dirt)
    elif e == 5:
        g1.config(bg=back,image=log)
    elif e == 6:
        g1.config(bg=back,image=leaves)
    elif e == 7:
        g1.config(bg=back,image=stick)
    elif e == 8:
        g1.config(bg=back,image=bush)
    elif e == 9:
        g1.config(bg=back,image=potato)
    elif e == 10:
        g1.config(bg=back,image=vine)
    elif e == 11:
        g1.config(bg=back,image=coral_red)
    elif e == 12:
        g1.config(bg=back,image=coral_orange)
    elif e == 13:
        g1.config(bg=back,image=coral_green)
    elif e == 14:
        g1.config(bg=back,image=coral_blue)
    elif e == 15:
        g1.config(bg=back,image=space_coral)
    elif e == 16:
        g1.config(bg=back,image=iron_ore)
    elif e == 17:
        g1.config(bg=back,image=copper_ore)
    elif e == 18:
        g1.config(bg=back,image=bone)
    elif e == 19:
        g1.config(bg=back,image=lantern)
    elif e == 20:
        g1.config(bg=back,image=ladder)
    elif e == 21:
        g1.config(bg=back,image=asteroid)
    elif e == 22:
        g1.config(bg=back,image=sea_bricks)
    elif e == 23:
        g1.config(bg=back,image=stone_bricks)
    elif e == 24:
        g1.config(bg=back,image=sea_lantern)
    elif e == 25:
        g1.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g1.config(bg=back,image=anvil)
    elif e == 27:
        g1.config(bg=back,image=space)
    elif e == 28:
        g1.config(bg=back,image=seaglass)
    elif e == 29:
        g1.config(bg=back,image=lava)
    elif e == 30:
        g1.config(bg=back,image=treasure)
    elif e == 31:
        g1.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g1.config(bg=back,image=turtle_right)
        else:
            g1.config(bg=back,image=turtle_left)
    elif e == 33:
        g1.config(bg=back,image=boar_left)
    elif e == 34:
        g1.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g1.config(bg=back,image=space_fish_right)
            else:
                g1.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g1.config(bg=back,image=fish_right)
            else:
                g1.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g1.config(bg=back,image=skeleton_attack_left)
        else:
            g1.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g1.config(bg=back,image=skeleton_attack_left)
        else:
            g1.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g1.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g1.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g1.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g1.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g1.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g1.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g1.config(bg=back,image=pirate_attack_left)
        else:
            g1.config(bg=back,image=pirate_left)
    elif e == 42:
        g1.config(bg=back,image=human)
    elif e == 43:
        g1.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g1.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g1.config(bg=back,image=tent)
    elif e == 47:
        g1.config(bg=back,image=bird)
    elif e == 48:
        g1.config(bg=back,image=spider)
    elif e == 49:
        g1.config(bg=back,image=cloud)
    elif e == 50:
        g1.config(bg=back,image=stem)
    elif e == 51:
        g1.config(bg=back,image=shroom_r)
    elif e == 52:
        g1.config(bg=back,image=shroom_b)
    elif e == 53:
        g1.config(bg=back,image=boat_pirate)
    elif e == 54:
        g1.config(bg=back,image=bullet)
    elif e == 55:
        g1.config(bg=back,image=g_ore)
    elif e == 56:
        g1.config(bg=back,image=book)
    elif e == 57:
        g1.config(bg=back,image=grass_g)
    elif e == 58:
        g1.config(bg=back,image=grass_o)
    elif e == 59:
        g1.config(bg=back,image=kelp)
    elif e == 60:
        g1.config(bg=back,image=frame)
    elif e == 61:
        g1.config(bg=back,image=tower)
    elif e == 62:
        g1.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][0]
    if e == 0:
        a2.config(bg=back2,image=blank)
    elif e == 1:
        a2.config(bg=back,image=stone)
    elif e == 2:
        a2.config(bg=back,image=sand)
    elif e == 3:
        a2.config(bg=back,image=water)
    elif e == 4:
        a2.config(bg=back,image=dirt)
    elif e == 5:
        a2.config(bg=back,image=log)
    elif e == 6:
        a2.config(bg=back,image=leaves)
    elif e == 7:
        a2.config(bg=back,image=stick)
    elif e == 8:
        a2.config(bg=back,image=bush)
    elif e == 9:
        a2.config(bg=back,image=potato)
    elif e == 10:
        a2.config(bg=back,image=vine)
    elif e == 11:
        a2.config(bg=back,image=coral_red)
    elif e == 12:
        a2.config(bg=back,image=coral_orange)
    elif e == 13:
        a2.config(bg=back,image=coral_green)
    elif e == 14:
        a2.config(bg=back,image=coral_blue)
    elif e == 15:
        a2.config(bg=back,image=space_coral)
    elif e == 16:
        a2.config(bg=back,image=iron_ore)
    elif e == 17:
        a2.config(bg=back,image=copper_ore)
    elif e == 18:
        a2.config(bg=back,image=bone)
    elif e == 19:
        a2.config(bg=back,image=lantern)
    elif e == 20:
        a2.config(bg=back,image=ladder)
    elif e == 21:
        a2.config(bg=back,image=asteroid)
    elif e == 22:
        a2.config(bg=back,image=sea_bricks)
    elif e == 23:
        a2.config(bg=back,image=stone_bricks)
    elif e == 24:
        a2.config(bg=back,image=sea_lantern)
    elif e == 25:
        a2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a2.config(bg=back,image=anvil)
    elif e == 27:
        a2.config(bg=back,image=space)
    elif e == 28:
        a2.config(bg=back,image=seaglass)
    elif e == 29:
        a2.config(bg=back,image=lava)
    elif e == 30:
        a2.config(bg=back,image=treasure)
    elif e == 31:
        a2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a2.config(bg=back,image=turtle_right)
        else:
            a2.config(bg=back,image=turtle_left)
    elif e == 33:
        a2.config(bg=back,image=boar_right)
    elif e == 34:
        a2.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a2.config(bg=back,image=space_fish_right)
            else:
                a2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a2.config(bg=back,image=fish_right)
            else:
                a2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a2.config(bg=back,image=skeleton_attack_right)
        else:
            a2.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a2.config(bg=back,image=skeleton_attack_right)
        else:
            a2.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a2.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a2.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a2.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a2.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a2.config(bg=back,image=pirate_attack_right)
        else:
            a2.config(bg=back,image=pirate_right)
    elif e == 42:
        a2.config(bg=back,image=human)
    elif e == 43:
        a2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a2.config(bg=back,image=tent)
    elif e == 47:
        a2.config(bg=back,image=bird)
    elif e == 48:
        a2.config(bg=back,image=spider)
    elif e == 49:
        a2.config(bg=back,image=cloud)
    elif e == 50:
        a2.config(bg=back,image=stem)
    elif e == 51:
        a2.config(bg=back,image=shroom_r)
    elif e == 52:
        a2.config(bg=back,image=shroom_b)
    elif e == 53:
        a2.config(bg=back,image=boat_pirate)
    elif e == 54:
        a2.config(bg=back,image=bullet)
    elif e == 55:
        a2.config(bg=back,image=g_ore)
    elif e == 56:
        a2.config(bg=back,image=book)
    elif e == 57:
        a2.config(bg=back,image=grass_g)
    elif e == 58:
        a2.config(bg=back,image=grass_o)
    elif e == 59:
        a2.config(bg=back,image=kelp)
    elif e == 60:
        a2.config(bg=back,image=frame)
    elif e == 61:
        a2.config(bg=back,image=tower)
    elif e == 62:
        a2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][1]
    if e == 0:
        b2.config(bg=back2,image=blank)
    elif e == 1:
        b2.config(bg=back,image=stone)
    elif e == 2:
        b2.config(bg=back,image=sand)
    elif e == 3:
        b2.config(bg=back,image=water)
    elif e == 4:
        b2.config(bg=back,image=dirt)
    elif e == 5:
        b2.config(bg=back,image=log)
    elif e == 6:
        b2.config(bg=back,image=leaves)
    elif e == 7:
        b2.config(bg=back,image=stick)
    elif e == 8:
        b2.config(bg=back,image=bush)
    elif e == 9:
        b2.config(bg=back,image=potato)
    elif e == 10:
        b2.config(bg=back,image=vine)
    elif e == 11:
        b2.config(bg=back,image=coral_red)
    elif e == 12:
        b2.config(bg=back,image=coral_orange)
    elif e == 13:
        b2.config(bg=back,image=coral_green)
    elif e == 14:
        b2.config(bg=back,image=coral_blue)
    elif e == 15:
        b2.config(bg=back,image=space_coral)
    elif e == 16:
        b2.config(bg=back,image=iron_ore)
    elif e == 17:
        b2.config(bg=back,image=copper_ore)
    elif e == 18:
        b2.config(bg=back,image=bone)
    elif e == 19:
        b2.config(bg=back,image=lantern)
    elif e == 20:
        b2.config(bg=back,image=ladder)
    elif e == 21:
        b2.config(bg=back,image=asteroid)
    elif e == 22:
        b2.config(bg=back,image=sea_bricks)
    elif e == 23:
        b2.config(bg=back,image=stone_bricks)
    elif e == 24:
        b2.config(bg=back,image=sea_lantern)
    elif e == 25:
        b2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b2.config(bg=back,image=anvil)
    elif e == 27:
        b2.config(bg=back,image=space)
    elif e == 28:
        b2.config(bg=back,image=seaglass)
    elif e == 29:
        b2.config(bg=back,image=lava)
    elif e == 30:
        b2.config(bg=back,image=treasure)
    elif e == 31:
        b2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b2.config(bg=back,image=turtle_right)
        else:
            b2.config(bg=back,image=turtle_left)
    elif e == 33:
        b2.config(bg=back,image=boar_right)
    elif e == 34:
        b2.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b2.config(bg=back,image=space_fish_right)
            else:
                b2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b2.config(bg=back,image=fish_right)
            else:
                b2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b2.config(bg=back,image=skeleton_attack_right)
        else:
            b2.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b2.config(bg=back,image=skeleton_attack_right)
        else:
            b2.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b2.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b2.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b2.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b2.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b2.config(bg=back,image=pirate_attack_right)
        else:
            b2.config(bg=back,image=pirate_right)
    elif e == 42:
        b2.config(bg=back,image=human)
    elif e == 43:
        b2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b2.config(bg=back,image=tent)
    elif e == 47:
        b2.config(bg=back,image=bird)
    elif e == 48:
        b2.config(bg=back,image=spider)
    elif e == 49:
        b2.config(bg=back,image=cloud)
    elif e == 50:
        b2.config(bg=back,image=stem)
    elif e == 51:
        b2.config(bg=back,image=shroom_r)
    elif e == 52:
        b2.config(bg=back,image=shroom_b)
    elif e == 53:
        b2.config(bg=back,image=boat_pirate)
    elif e == 54:
        b2.config(bg=back,image=bullet)
    elif e == 55:
        b2.config(bg=back,image=g_ore)
    elif e == 56:
        b2.config(bg=back,image=book)
    elif e == 57:
        b2.config(bg=back,image=grass_g)
    elif e == 58:
        b2.config(bg=back,image=grass_o)
    elif e == 59:
        b2.config(bg=back,image=kelp)
    elif e == 60:
        b2.config(bg=back,image=frame)
    elif e == 61:
        b2.config(bg=back,image=tower)
    elif e == 62:
        b2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][2]
    if e == 0:
        c2.config(bg=back2,image=blank)
    elif e == 1:
        c2.config(bg=back,image=stone)
    elif e == 2:
        c2.config(bg=back,image=sand)
    elif e == 3:
        c2.config(bg=back,image=water)
    elif e == 4:
        c2.config(bg=back,image=dirt)
    elif e == 5:
        c2.config(bg=back,image=log)
    elif e == 6:
        c2.config(bg=back,image=leaves)
    elif e == 7:
        c2.config(bg=back,image=stick)
    elif e == 8:
        c2.config(bg=back,image=bush)
    elif e == 9:
        c2.config(bg=back,image=potato)
    elif e == 10:
        c2.config(bg=back,image=vine)
    elif e == 11:
        c2.config(bg=back,image=coral_red)
    elif e == 12:
        c2.config(bg=back,image=coral_orange)
    elif e == 13:
        c2.config(bg=back,image=coral_green)
    elif e == 14:
        c2.config(bg=back,image=coral_blue)
    elif e == 15:
        c2.config(bg=back,image=space_coral)
    elif e == 16:
        c2.config(bg=back,image=iron_ore)
    elif e == 17:
        c2.config(bg=back,image=copper_ore)
    elif e == 18:
        c2.config(bg=back,image=bone)
    elif e == 19:
        c2.config(bg=back,image=lantern)
    elif e == 20:
        c2.config(bg=back,image=ladder)
    elif e == 21:
        c2.config(bg=back,image=asteroid)
    elif e == 22:
        c2.config(bg=back,image=sea_bricks)
    elif e == 23:
        c2.config(bg=back,image=stone_bricks)
    elif e == 24:
        c2.config(bg=back,image=sea_lantern)
    elif e == 25:
        c2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c2.config(bg=back,image=anvil)
    elif e == 27:
        c2.config(bg=back,image=space)
    elif e == 28:
        c2.config(bg=back,image=seaglass)
    elif e == 29:
        c2.config(bg=back,image=lava)
    elif e == 30:
        c2.config(bg=back,image=treasure)
    elif e == 31:
        c2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c2.config(bg=back,image=turtle_right)
        else:
            c2.config(bg=back,image=turtle_left)
    elif e == 33:
        c2.config(bg=back,image=boar_right)
    elif e == 34:
        c2.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c2.config(bg=back,image=space_fish_right)
            else:
                c2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c2.config(bg=back,image=fish_right)
            else:
                c2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c2.config(bg=back,image=skeleton_attack_right)
        else:
            c2.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c2.config(bg=back,image=skeleton_attack_right)
        else:
            c2.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c2.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c2.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c2.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c2.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c2.config(bg=back,image=pirate_attack_right)
        else:
            c2.config(bg=back,image=pirate_right)
    elif e == 42:
        c2.config(bg=back,image=human)
    elif e == 43:
        c2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c2.config(bg=back,image=tent)
    elif e == 47:
        c2.config(bg=back,image=bird)
    elif e == 48:
        c2.config(bg=back,image=spider)
    elif e == 49:
        c2.config(bg=back,image=cloud)
    elif e == 50:
        c2.config(bg=back,image=stem)
    elif e == 51:
        c2.config(bg=back,image=shroom_r)
    elif e == 52:
        c2.config(bg=back,image=shroom_b)
    elif e == 53:
        c2.config(bg=back,image=boat_pirate)
    elif e == 54:
        c2.config(bg=back,image=bullet)
    elif e == 55:
        c2.config(bg=back,image=g_ore)
    elif e == 56:
        c2.config(bg=back,image=book)
    elif e == 57:
        c2.config(bg=back,image=grass_g)
    elif e == 58:
        c2.config(bg=back,image=grass_o)
    elif e == 59:
        c2.config(bg=back,image=kelp)
    elif e == 60:
        c2.config(bg=back,image=frame)
    elif e == 61:
        c2.config(bg=back,image=tower)
    elif e == 62:
        c2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][3]
    if e == 0:
        d2.config(bg=back2,image=blank)
    elif e == 1:
        d2.config(bg=back,image=stone)
    elif e == 2:
        d2.config(bg=back,image=sand)
    elif e == 3:
        d2.config(bg=back,image=water)
    elif e == 4:
        d2.config(bg=back,image=dirt)
    elif e == 5:
        d2.config(bg=back,image=log)
    elif e == 6:
        d2.config(bg=back,image=leaves)
    elif e == 7:
        d2.config(bg=back,image=stick)
    elif e == 8:
        d2.config(bg=back,image=bush)
    elif e == 9:
        d2.config(bg=back,image=potato)
    elif e == 10:
        d2.config(bg=back,image=vine)
    elif e == 11:
        d2.config(bg=back,image=coral_red)
    elif e == 12:
        d2.config(bg=back,image=coral_orange)
    elif e == 13:
        d2.config(bg=back,image=coral_green)
    elif e == 14:
        d2.config(bg=back,image=coral_blue)
    elif e == 15:
        d2.config(bg=back,image=space_coral)
    elif e == 16:
        d2.config(bg=back,image=iron_ore)
    elif e == 17:
        d2.config(bg=back,image=copper_ore)
    elif e == 18:
        d2.config(bg=back,image=bone)
    elif e == 19:
        d2.config(bg=back,image=lantern)
    elif e == 20:
        d2.config(bg=back,image=ladder)
    elif e == 21:
        d2.config(bg=back,image=asteroid)
    elif e == 22:
        d2.config(bg=back,image=sea_bricks)
    elif e == 23:
        d2.config(bg=back,image=stone_bricks)
    elif e == 24:
        d2.config(bg=back,image=sea_lantern)
    elif e == 25:
        d2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d2.config(bg=back,image=anvil)
    elif e == 27:
        d2.config(bg=back,image=space)
    elif e == 28:
        d2.config(bg=back,image=seaglass)
    elif e == 29:
        d2.config(bg=back,image=lava)
    elif e == 30:
        d2.config(bg=back,image=treasure)
    elif e == 31:
        d2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d2.config(bg=back,image=turtle_right)
        else:
            d2.config(bg=back,image=turtle_left)
    elif e == 33:
        d2.config(bg=back,image=boar_right)
    elif e == 34:
        d2.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d2.config(bg=back,image=space_fish_right)
            else:
                d2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d2.config(bg=back,image=fish_right)
            else:
                d2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d2.config(bg=back,image=skeleton_attack_right)
        else:
            d2.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d2.config(bg=back,image=skeleton_attack_right)
        else:
            d2.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d2.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d2.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d2.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d2.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d2.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d2.config(bg=back,image=pirate_attack_right)
        else:
            d2.config(bg=back,image=pirate_right)
    elif e == 42:
        d2.config(bg=back,image=human)
    elif e == 43:
        d2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        d2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d2.config(bg=back,image=tent)
    elif e == 47:
        d2.config(bg=back,image=bird)
    elif e == 48:
        d2.config(bg=back,image=spider)
    elif e == 49:
        d2.config(bg=back,image=cloud)
    elif e == 50:
        d2.config(bg=back,image=stem)
    elif e == 51:
        d2.config(bg=back,image=shroom_r)
    elif e == 52:
        d2.config(bg=back,image=shroom_b)
    elif e == 53:
        d2.config(bg=back,image=boat_pirate)
    elif e == 54:
        d2.config(bg=back,image=bullet)
    elif e == 55:
        d2.config(bg=back,image=g_ore)
    elif e == 56:
        d2.config(bg=back,image=book)
    elif e == 57:
        d2.config(bg=back,image=grass_g)
    elif e == 58:
        d2.config(bg=back,image=grass_o)
    elif e == 59:
        d2.config(bg=back,image=kelp)
    elif e == 60:
        d2.config(bg=back,image=frame)
    elif e == 61:
        d2.config(bg=back,image=tower)
    elif e == 62:
        d2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][4]
    if e == 0:
        e2.config(bg=back2,image=blank)
    elif e == 1:
        e2.config(bg=back,image=stone)
    elif e == 2:
        e2.config(bg=back,image=sand)
    elif e == 3:
        e2.config(bg=back,image=water)
    elif e == 4:
        e2.config(bg=back,image=dirt)
    elif e == 5:
        e2.config(bg=back,image=log)
    elif e == 6:
        e2.config(bg=back,image=leaves)
    elif e == 7:
        e2.config(bg=back,image=stick)
    elif e == 8:
        e2.config(bg=back,image=bush)
    elif e == 9:
        e2.config(bg=back,image=potato)
    elif e == 10:
        e2.config(bg=back,image=vine)
    elif e == 11:
        e2.config(bg=back,image=coral_red)
    elif e == 12:
        e2.config(bg=back,image=coral_orange)
    elif e == 13:
        e2.config(bg=back,image=coral_green)
    elif e == 14:
        e2.config(bg=back,image=coral_blue)
    elif e == 15:
        e2.config(bg=back,image=space_coral)
    elif e == 16:
        e2.config(bg=back,image=iron_ore)
    elif e == 17:
        e2.config(bg=back,image=copper_ore)
    elif e == 18:
        e2.config(bg=back,image=bone)
    elif e == 19:
        e2.config(bg=back,image=lantern)
    elif e == 20:
        e2.config(bg=back,image=ladder)
    elif e == 21:
        e2.config(bg=back,image=asteroid)
    elif e == 22:
        e2.config(bg=back,image=sea_bricks)
    elif e == 23:
        e2.config(bg=back,image=stone_bricks)
    elif e == 24:
        e2.config(bg=back,image=sea_lantern)
    elif e == 25:
        e2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e2.config(bg=back,image=anvil)
    elif e == 27:
        e2.config(bg=back,image=space)
    elif e == 28:
        e2.config(bg=back,image=seaglass)
    elif e == 29:
        e2.config(bg=back,image=lava)
    elif e == 30:
        e2.config(bg=back,image=treasure)
    elif e == 31:
        e2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e2.config(bg=back,image=turtle_right)
        else:
            e2.config(bg=back,image=turtle_left)
    elif e == 33:
        e2.config(bg=back,image=boar_left)
    elif e == 34:
        e2.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e2.config(bg=back,image=space_fish_right)
            else:
                e2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e2.config(bg=back,image=fish_right)
            else:
                e2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e2.config(bg=back,image=skeleton_attack_left)
        else:
            e2.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e2.config(bg=back,image=skeleton_attack_left)
        else:
            e2.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e2.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e2.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e2.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e2.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e2.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e2.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e2.config(bg=back,image=pirate_attack_left)
        else:
            e2.config(bg=back,image=pirate_left)
    elif e == 42:
        e2.config(bg=back,image=human)
    elif e == 43:
        e2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e2.config(bg=back,image=tent)
    elif e == 47:
        e2.config(bg=back,image=bird)
    elif e == 48:
        e2.config(bg=back,image=spider)
    elif e == 49:
        e2.config(bg=back,image=cloud)
    elif e == 50:
        e2.config(bg=back,image=stem)
    elif e == 51:
        e2.config(bg=back,image=shroom_r)
    elif e == 52:
        e2.config(bg=back,image=shroom_b)
    elif e == 53:
        e2.config(bg=back,image=boat_pirate)
    elif e == 54:
        e2.config(bg=back,image=bullet)
    elif e == 55:
        e2.config(bg=back,image=g_ore)
    elif e == 56:
        e2.config(bg=back,image=book)
    elif e == 57:
        e2.config(bg=back,image=grass_g)
    elif e == 58:
        e2.config(bg=back,image=grass_o)
    elif e == 59:
        e2.config(bg=back,image=kelp)
    elif e == 60:
        e2.config(bg=back,image=frame)
    elif e == 61:
        e2.config(bg=back,image=tower)
    elif e == 62:
        e2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][5]
    if e == 0:
        f2.config(bg=back2,image=blank)
    elif e == 1:
        f2.config(bg=back,image=stone)
    elif e == 2:
        f2.config(bg=back,image=sand)
    elif e == 3:
        f2.config(bg=back,image=water)
    elif e == 4:
        f2.config(bg=back,image=dirt)
    elif e == 5:
        f2.config(bg=back,image=log)
    elif e == 6:
        f2.config(bg=back,image=leaves)
    elif e == 7:
        f2.config(bg=back,image=stick)
    elif e == 8:
        f2.config(bg=back,image=bush)
    elif e == 9:
        f2.config(bg=back,image=potato)
    elif e == 10:
        f2.config(bg=back,image=vine)
    elif e == 11:
        f2.config(bg=back,image=coral_red)
    elif e == 12:
        f2.config(bg=back,image=coral_orange)
    elif e == 13:
        f2.config(bg=back,image=coral_green)
    elif e == 14:
        f2.config(bg=back,image=coral_blue)
    elif e == 15:
        f2.config(bg=back,image=space_coral)
    elif e == 16:
        f2.config(bg=back,image=iron_ore)
    elif e == 17:
        f2.config(bg=back,image=copper_ore)
    elif e == 18:
        f2.config(bg=back,image=bone)
    elif e == 19:
        f2.config(bg=back,image=lantern)
    elif e == 20:
        f2.config(bg=back,image=ladder)
    elif e == 21:
        f2.config(bg=back,image=asteroid)
    elif e == 22:
        f2.config(bg=back,image=sea_bricks)
    elif e == 23:
        f2.config(bg=back,image=stone_bricks)
    elif e == 24:
        f2.config(bg=back,image=sea_lantern)
    elif e == 25:
        f2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f2.config(bg=back,image=anvil)
    elif e == 27:
        f2.config(bg=back,image=space)
    elif e == 28:
        f2.config(bg=back,image=seaglass)
    elif e == 29:
        f2.config(bg=back,image=lava)
    elif e == 30:
        f2.config(bg=back,image=treasure)
    elif e == 31:
        f2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f2.config(bg=back,image=turtle_right)
        else:
            f2.config(bg=back,image=turtle_left)
    elif e == 33:
        f2.config(bg=back,image=boar_left)
    elif e == 34:
        f2.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f2.config(bg=back,image=space_fish_right)
            else:
                f2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f2.config(bg=back,image=fish_right)
            else:
                f2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f2.config(bg=back,image=skeleton_attack_left)
        else:
            f2.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f2.config(bg=back,image=skeleton_attack_left)
        else:
            f2.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f2.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f2.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f2.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f2.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f2.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f2.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f2.config(bg=back,image=pirate_attack_left)
        else:
            f2.config(bg=back,image=pirate_left)
    elif e == 42:
        f2.config(bg=back,image=human)
    elif e == 43:
        f2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f2.config(bg=back,image=tent)
    elif e == 47:
        f2.config(bg=back,image=bird)
    elif e == 48:
        f2.config(bg=back,image=spider)
    elif e == 49:
        f2.config(bg=back,image=cloud)
    elif e == 50:
        f2.config(bg=back,image=stem)
    elif e == 51:
        f2.config(bg=back,image=shroom_r)
    elif e == 52:
        f2.config(bg=back,image=shroom_b)
    elif e == 53:
        f2.config(bg=back,image=boat_pirate)
    elif e == 54:
        f2.config(bg=back,image=bullet)
    elif e == 55:
        f2.config(bg=back,image=g_ore)
    elif e == 56:
        f2.config(bg=back,image=book)
    elif e == 57:
        f2.config(bg=back,image=grass_g)
    elif e == 58:
        f2.config(bg=back,image=grass_o)
    elif e == 59:
        f2.config(bg=back,image=kelp)
    elif e == 60:
        f2.config(bg=back,image=frame)
    elif e == 61:
        f2.config(bg=back,image=tower)
    elif e == 62:
        f2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[1][6]
    if e == 0:
        g2.config(bg=back2,image=blank)
    elif e == 1:
        g2.config(bg=back,image=stone)
    elif e == 2:
        g2.config(bg=back,image=sand)
    elif e == 3:
        g2.config(bg=back,image=water)
    elif e == 4:
        g2.config(bg=back,image=dirt)
    elif e == 5:
        g2.config(bg=back,image=log)
    elif e == 6:
        g2.config(bg=back,image=leaves)
    elif e == 7:
        g2.config(bg=back,image=stick)
    elif e == 8:
        g2.config(bg=back,image=bush)
    elif e == 9:
        g2.config(bg=back,image=potato)
    elif e == 10:
        g2.config(bg=back,image=vine)
    elif e == 11:
        g2.config(bg=back,image=coral_red)
    elif e == 12:
        g2.config(bg=back,image=coral_orange)
    elif e == 13:
        g2.config(bg=back,image=coral_green)
    elif e == 14:
        g2.config(bg=back,image=coral_blue)
    elif e == 15:
        g2.config(bg=back,image=space_coral)
    elif e == 16:
        g2.config(bg=back,image=iron_ore)
    elif e == 17:
        g2.config(bg=back,image=copper_ore)
    elif e == 18:
        g2.config(bg=back,image=bone)
    elif e == 19:
        g2.config(bg=back,image=lantern)
    elif e == 20:
        g2.config(bg=back,image=ladder)
    elif e == 21:
        g2.config(bg=back,image=asteroid)
    elif e == 22:
        g2.config(bg=back,image=sea_bricks)
    elif e == 23:
        g2.config(bg=back,image=stone_bricks)
    elif e == 24:
        g2.config(bg=back,image=sea_lantern)
    elif e == 25:
        g2.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g2.config(bg=back,image=anvil)
    elif e == 27:
        g2.config(bg=back,image=space)
    elif e == 28:
        g2.config(bg=back,image=seaglass)
    elif e == 29:
        g2.config(bg=back,image=lava)
    elif e == 30:
        g2.config(bg=back,image=treasure)
    elif e == 31:
        g2.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g2.config(bg=back,image=turtle_right)
        else:
            g2.config(bg=back,image=turtle_left)
    elif e == 33:
        g2.config(bg=back,image=boar_left)
    elif e == 34:
        g2.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g2.config(bg=back,image=space_fish_right)
            else:
                g2.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g2.config(bg=back,image=fish_right)
            else:
                g2.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g2.config(bg=back,image=skeleton_attack_left)
        else:
            g2.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g2.config(bg=back,image=skeleton_attack_left)
        else:
            g2.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g2.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g2.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g2.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g2.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g2.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g2.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g2.config(bg=back,image=pirate_attack_left)
        else:
            g2.config(bg=back,image=pirate_left)
    elif e == 42:
        g2.config(bg=back,image=human)
    elif e == 43:
        g2.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g2.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g2.config(bg=back,image=tent)
    elif e == 47:
        g2.config(bg=back,image=bird)
    elif e == 48:
        g2.config(bg=back,image=spider)
    elif e == 49:
        g2.config(bg=back,image=cloud)
    elif e == 50:
        g2.config(bg=back,image=stem)
    elif e == 51:
        g2.config(bg=back,image=shroom_r)
    elif e == 52:
        g2.config(bg=back,image=shroom_b)
    elif e == 53:
        g2.config(bg=back,image=boat_pirate)
    elif e == 54:
        g2.config(bg=back,image=bullet)
    elif e == 55:
        g2.config(bg=back,image=g_ore)
    elif e == 56:
        g2.config(bg=back,image=book)
    elif e == 57:
        g2.config(bg=back,image=grass_g)
    elif e == 58:
        g2.config(bg=back,image=grass_o)
    elif e == 59:
        g2.config(bg=back,image=kelp)
    elif e == 60:
        g2.config(bg=back,image=frame)
    elif e == 61:
        g2.config(bg=back,image=tower)
    elif e == 62:
        g2.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][0]
    if e == 0:
        a3.config(bg=back2,image=blank)
    elif e == 1:
        a3.config(bg=back,image=stone)
    elif e == 2:
        a3.config(bg=back,image=sand)
    elif e == 3:
        a3.config(bg=back,image=water)
    elif e == 4:
        a3.config(bg=back,image=dirt)
    elif e == 5:
        a3.config(bg=back,image=log)
    elif e == 6:
        a3.config(bg=back,image=leaves)
    elif e == 7:
        a3.config(bg=back,image=stick)
    elif e == 8:
        a3.config(bg=back,image=bush)
    elif e == 9:
        a3.config(bg=back,image=potato)
    elif e == 10:
        a3.config(bg=back,image=vine)
    elif e == 11:
        a3.config(bg=back,image=coral_red)
    elif e == 12:
        a3.config(bg=back,image=coral_orange)
    elif e == 13:
        a3.config(bg=back,image=coral_green)
    elif e == 14:
        a3.config(bg=back,image=coral_blue)
    elif e == 15:
        a3.config(bg=back,image=space_coral)
    elif e == 16:
        a3.config(bg=back,image=iron_ore)
    elif e == 17:
        a3.config(bg=back,image=copper_ore)
    elif e == 18:
        a3.config(bg=back,image=bone)
    elif e == 19:
        a3.config(bg=back,image=lantern)
    elif e == 20:
        a3.config(bg=back,image=ladder)
    elif e == 21:
        a3.config(bg=back,image=asteroid)
    elif e == 22:
        a3.config(bg=back,image=sea_bricks)
    elif e == 23:
        a3.config(bg=back,image=stone_bricks)
    elif e == 24:
        a3.config(bg=back,image=sea_lantern)
    elif e == 25:
        a3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a3.config(bg=back,image=anvil)
    elif e == 27:
        a3.config(bg=back,image=space)
    elif e == 28:
        a3.config(bg=back,image=seaglass)
    elif e == 29:
        a3.config(bg=back,image=lava)
    elif e == 30:
        a3.config(bg=back,image=treasure)
    elif e == 31:
        a3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a3.config(bg=back,image=turtle_right)
        else:
            a3.config(bg=back,image=turtle_left)
    elif e == 33:
        a3.config(bg=back,image=boar_right)
    elif e == 34:
        a3.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a3.config(bg=back,image=space_fish_right)
            else:
                a3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a3.config(bg=back,image=fish_right)
            else:
                a3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a3.config(bg=back,image=skeleton_attack_right)
        else:
            a3.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a3.config(bg=back,image=skeleton_attack_right)
        else:
            a3.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a3.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a3.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a3.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a3.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a3.config(bg=back,image=pirate_attack_right)
        else:
            a3.config(bg=back,image=pirate_right)
    elif e == 42:
        a3.config(bg=back,image=human)
    elif e == 43:
        a3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a3.config(bg=back,image=tent)
    elif e == 47:
        a3.config(bg=back,image=bird)
    elif e == 48:
        a3.config(bg=back,image=spider)
    elif e == 49:
        a3.config(bg=back,image=cloud)
    elif e == 50:
        a3.config(bg=back,image=stem)
    elif e == 51:
        a3.config(bg=back,image=shroom_r)
    elif e == 52:
        a3.config(bg=back,image=shroom_b)
    elif e == 53:
        a3.config(bg=back,image=boat_pirate)
    elif e == 54:
        a3.config(bg=back,image=bullet)
    elif e == 55:
        a3.config(bg=back,image=g_ore)
    elif e == 56:
        a3.config(bg=back,image=book)
    elif e == 57:
        a3.config(bg=back,image=grass_g)
    elif e == 58:
        a3.config(bg=back,image=grass_o)
    elif e == 59:
        a3.config(bg=back,image=kelp)
    elif e == 60:
        a3.config(bg=back,image=frame)
    elif e == 61:
        a3.config(bg=back,image=tower)
    elif e == 62:
        a3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][1]
    if e == 0:
        b3.config(bg=back2,image=blank)
    elif e == 1:
        b3.config(bg=back,image=stone)
    elif e == 2:
        b3.config(bg=back,image=sand)
    elif e == 3:
        b3.config(bg=back,image=water)
    elif e == 4:
        b3.config(bg=back,image=dirt)
    elif e == 5:
        b3.config(bg=back,image=log)
    elif e == 6:
        b3.config(bg=back,image=leaves)
    elif e == 7:
        b3.config(bg=back,image=stick)
    elif e == 8:
        b3.config(bg=back,image=bush)
    elif e == 9:
        b3.config(bg=back,image=potato)
    elif e == 10:
        b3.config(bg=back,image=vine)
    elif e == 11:
        b3.config(bg=back,image=coral_red)
    elif e == 12:
        b3.config(bg=back,image=coral_orange)
    elif e == 13:
        b3.config(bg=back,image=coral_green)
    elif e == 14:
        b3.config(bg=back,image=coral_blue)
    elif e == 15:
        b3.config(bg=back,image=space_coral)
    elif e == 16:
        b3.config(bg=back,image=iron_ore)
    elif e == 17:
        b3.config(bg=back,image=copper_ore)
    elif e == 18:
        b3.config(bg=back,image=bone)
    elif e == 19:
        b3.config(bg=back,image=lantern)
    elif e == 20:
        b3.config(bg=back,image=ladder)
    elif e == 21:
        b3.config(bg=back,image=asteroid)
    elif e == 22:
        b3.config(bg=back,image=sea_bricks)
    elif e == 23:
        b3.config(bg=back,image=stone_bricks)
    elif e == 24:
        b3.config(bg=back,image=sea_lantern)
    elif e == 25:
        b3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b3.config(bg=back,image=anvil)
    elif e == 27:
        b3.config(bg=back,image=space)
    elif e == 28:
        b3.config(bg=back,image=seaglass)
    elif e == 29:
        b3.config(bg=back,image=lava)
    elif e == 30:
        b3.config(bg=back,image=treasure)
    elif e == 31:
        b3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b3.config(bg=back,image=turtle_right)
        else:
            b3.config(bg=back,image=turtle_left)
    elif e == 33:
        b3.config(bg=back,image=boar_right)
    elif e == 34:
        b3.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b3.config(bg=back,image=space_fish_right)
            else:
                b3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b3.config(bg=back,image=fish_right)
            else:
                b3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b3.config(bg=back,image=skeleton_attack_right)
        else:
            b3.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b3.config(bg=back,image=skeleton_attack_right)
        else:
            b3.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b3.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b3.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b3.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b3.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b3.config(bg=back,image=pirate_attack_right)
        else:
            b3.config(bg=back,image=pirate_right)
    elif e == 42:
        b3.config(bg=back,image=human)
    elif e == 43:
        b3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b3.config(bg=back,image=tent)
    elif e == 47:
        b3.config(bg=back,image=bird)
    elif e == 48:
        b3.config(bg=back,image=spider)
    elif e == 49:
        b3.config(bg=back,image=cloud)
    elif e == 50:
        b3.config(bg=back,image=stem)
    elif e == 51:
        b3.config(bg=back,image=shroom_r)
    elif e == 52:
        b3.config(bg=back,image=shroom_b)
    elif e == 53:
        b3.config(bg=back,image=boat_pirate)
    elif e == 54:
        b3.config(bg=back,image=bullet)
    elif e == 55:
        b3.config(bg=back,image=g_ore)
    elif e == 56:
        b3.config(bg=back,image=book)
    elif e == 57:
        b3.config(bg=back,image=grass_g)
    elif e == 58:
        b3.config(bg=back,image=grass_o)
    elif e == 59:
        b3.config(bg=back,image=kelp)
    elif e == 60:
        b3.config(bg=back,image=frame)
    elif e == 61:
        b3.config(bg=back,image=tower)
    elif e == 62:
        b3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][2]
    if e == 0:
        c3.config(bg=back2,image=blank)
    elif e == 1:
        c3.config(bg=back,image=stone)
    elif e == 2:
        c3.config(bg=back,image=sand)
    elif e == 3:
        c3.config(bg=back,image=water)
    elif e == 4:
        c3.config(bg=back,image=dirt)
    elif e == 5:
        c3.config(bg=back,image=log)
    elif e == 6:
        c3.config(bg=back,image=leaves)
    elif e == 7:
        c3.config(bg=back,image=stick)
    elif e == 8:
        c3.config(bg=back,image=bush)
    elif e == 9:
        c3.config(bg=back,image=potato)
    elif e == 10:
        c3.config(bg=back,image=vine)
    elif e == 11:
        c3.config(bg=back,image=coral_red)
    elif e == 12:
        c3.config(bg=back,image=coral_orange)
    elif e == 13:
        c3.config(bg=back,image=coral_green)
    elif e == 14:
        c3.config(bg=back,image=coral_blue)
    elif e == 15:
        c3.config(bg=back,image=space_coral)
    elif e == 16:
        c3.config(bg=back,image=iron_ore)
    elif e == 17:
        c3.config(bg=back,image=copper_ore)
    elif e == 18:
        c3.config(bg=back,image=bone)
    elif e == 19:
        c3.config(bg=back,image=lantern)
    elif e == 20:
        c3.config(bg=back,image=ladder)
    elif e == 21:
        c3.config(bg=back,image=asteroid)
    elif e == 22:
        c3.config(bg=back,image=sea_bricks)
    elif e == 23:
        c3.config(bg=back,image=stone_bricks)
    elif e == 24:
        c3.config(bg=back,image=sea_lantern)
    elif e == 25:
        c3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c3.config(bg=back,image=anvil)
    elif e == 27:
        c3.config(bg=back,image=space)
    elif e == 28:
        c3.config(bg=back,image=seaglass)
    elif e == 29:
        c3.config(bg=back,image=lava)
    elif e == 30:
        c3.config(bg=back,image=treasure)
    elif e == 31:
        c3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c3.config(bg=back,image=turtle_right)
        else:
            c3.config(bg=back,image=turtle_left)
    elif e == 33:
        c3.config(bg=back,image=boar_right)
    elif e == 34:
        c3.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c3.config(bg=back,image=space_fish_right)
            else:
                c3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c3.config(bg=back,image=fish_right)
            else:
                c3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c3.config(bg=back,image=skeleton_attack_right)
        else:
            c3.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c3.config(bg=back,image=skeleton_attack_right)
        else:
            c3.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c3.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c3.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c3.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c3.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c3.config(bg=back,image=pirate_attack_right)
        else:
            c3.config(bg=back,image=pirate_right)
    elif e == 42:
        c3.config(bg=back,image=human)
    elif e == 43:
        c3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c3.config(bg=back,image=tent)
    elif e == 47:
        c3.config(bg=back,image=bird)
    elif e == 48:
        c3.config(bg=back,image=spider)
    elif e == 49:
        c3.config(bg=back,image=cloud)
    elif e == 50:
        c3.config(bg=back,image=stem)
    elif e == 51:
        c3.config(bg=back,image=shroom_r)
    elif e == 52:
        c3.config(bg=back,image=shroom_b)
    elif e == 53:
        c3.config(bg=back,image=boat_pirate)
    elif e == 54:
        c3.config(bg=back,image=bullet)
    elif e == 55:
        c3.config(bg=back,image=g_ore)
    elif e == 56:
        c3.config(bg=back,image=book)
    elif e == 57:
        c3.config(bg=back,image=grass_g)
    elif e == 58:
        c3.config(bg=back,image=grass_o)
    elif e == 59:
        c3.config(bg=back,image=kelp)
    elif e == 60:
        c3.config(bg=back,image=frame)
    elif e == 61:
        c3.config(bg=back,image=tower)
    elif e == 62:
        c3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][3]
    if e == 0:
        d3.config(bg=back2,image=blank)
    elif e == 1:
        d3.config(bg=back,image=stone)
    elif e == 2:
        d3.config(bg=back,image=sand)
    elif e == 3:
        d3.config(bg=back,image=water)
    elif e == 4:
        d3.config(bg=back,image=dirt)
    elif e == 5:
        d3.config(bg=back,image=log)
    elif e == 6:
        d3.config(bg=back,image=leaves)
    elif e == 7:
        d3.config(bg=back,image=stick)
    elif e == 8:
        d3.config(bg=back,image=bush)
    elif e == 9:
        d3.config(bg=back,image=potato)
    elif e == 10:
        d3.config(bg=back,image=vine)
    elif e == 11:
        d3.config(bg=back,image=coral_red)
    elif e == 12:
        d3.config(bg=back,image=coral_orange)
    elif e == 13:
        d3.config(bg=back,image=coral_green)
    elif e == 14:
        d3.config(bg=back,image=coral_blue)
    elif e == 15:
        d3.config(bg=back,image=space_coral)
    elif e == 16:
        d3.config(bg=back,image=iron_ore)
    elif e == 17:
        d3.config(bg=back,image=copper_ore)
    elif e == 18:
        d3.config(bg=back,image=bone)
    elif e == 19:
        d3.config(bg=back,image=lantern)
    elif e == 20:
        d3.config(bg=back,image=ladder)
    elif e == 21:
        d3.config(bg=back,image=asteroid)
    elif e == 22:
        d3.config(bg=back,image=sea_bricks)
    elif e == 23:
        d3.config(bg=back,image=stone_bricks)
    elif e == 24:
        d3.config(bg=back,image=sea_lantern)
    elif e == 25:
        d3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d3.config(bg=back,image=anvil)
    elif e == 27:
        d3.config(bg=back,image=space)
    elif e == 28:
        d3.config(bg=back,image=seaglass)
    elif e == 29:
        d3.config(bg=back,image=lava)
    elif e == 30:
        d3.config(bg=back,image=treasure)
    elif e == 31:
        d3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d3.config(bg=back,image=turtle_right)
        else:
            d3.config(bg=back,image=turtle_left)
    elif e == 33:
        d3.config(bg=back,image=boar_right)
    elif e == 34:
        d3.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d3.config(bg=back,image=space_fish_right)
            else:
                d3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d3.config(bg=back,image=fish_right)
            else:
                d3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d3.config(bg=back,image=skeleton_attack_right)
        else:
            d3.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d3.config(bg=back,image=skeleton_attack_right)
        else:
            d3.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d3.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d3.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d3.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d3.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d3.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d3.config(bg=back,image=pirate_attack_right)
        else:
            d3.config(bg=back,image=pirate_right)
    elif e == 42:
        d3.config(bg=back,image=human)
    elif e == 43:
        d3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        d3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d3.config(bg=back,image=tent)
    elif e == 47:
        d3.config(bg=back,image=bird)
    elif e == 48:
        d3.config(bg=back,image=spider)
    elif e == 49:
        d3.config(bg=back,image=cloud)
    elif e == 50:
        d3.config(bg=back,image=stem)
    elif e == 51:
        d3.config(bg=back,image=shroom_r)
    elif e == 52:
        d3.config(bg=back,image=shroom_b)
    elif e == 53:
        d3.config(bg=back,image=boat_pirate)
    elif e == 54:
        d3.config(bg=back,image=bullet)
    elif e == 55:
        d3.config(bg=back,image=g_ore)
    elif e == 56:
        d3.config(bg=back,image=book)
    elif e == 57:
        d3.config(bg=back,image=grass_g)
    elif e == 58:
        d3.config(bg=back,image=grass_o)
    elif e == 59:
        d3.config(bg=back,image=kelp)
    elif e == 60:
        d3.config(bg=back,image=frame)
    elif e == 61:
        d3.config(bg=back,image=tower)
    elif e == 62:
        d3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][4]
    if e == 0:
        e3.config(bg=back2,image=blank)
    elif e == 1:
        e3.config(bg=back,image=stone)
    elif e == 2:
        e3.config(bg=back,image=sand)
    elif e == 3:
        e3.config(bg=back,image=water)
    elif e == 4:
        e3.config(bg=back,image=dirt)
    elif e == 5:
        e3.config(bg=back,image=log)
    elif e == 6:
        e3.config(bg=back,image=leaves)
    elif e == 7:
        e3.config(bg=back,image=stick)
    elif e == 8:
        e3.config(bg=back,image=bush)
    elif e == 9:
        e3.config(bg=back,image=potato)
    elif e == 10:
        e3.config(bg=back,image=vine)
    elif e == 11:
        e3.config(bg=back,image=coral_red)
    elif e == 12:
        e3.config(bg=back,image=coral_orange)
    elif e == 13:
        e3.config(bg=back,image=coral_green)
    elif e == 14:
        e3.config(bg=back,image=coral_blue)
    elif e == 15:
        e3.config(bg=back,image=space_coral)
    elif e == 16:
        e3.config(bg=back,image=iron_ore)
    elif e == 17:
        e3.config(bg=back,image=copper_ore)
    elif e == 18:
        e3.config(bg=back,image=bone)
    elif e == 19:
        e3.config(bg=back,image=lantern)
    elif e == 20:
        e3.config(bg=back,image=ladder)
    elif e == 21:
        e3.config(bg=back,image=asteroid)
    elif e == 22:
        e3.config(bg=back,image=sea_bricks)
    elif e == 23:
        e3.config(bg=back,image=stone_bricks)
    elif e == 24:
        e3.config(bg=back,image=sea_lantern)
    elif e == 25:
        e3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e3.config(bg=back,image=anvil)
    elif e == 27:
        e3.config(bg=back,image=space)
    elif e == 28:
        e3.config(bg=back,image=seaglass)
    elif e == 29:
        e3.config(bg=back,image=lava)
    elif e == 30:
        e3.config(bg=back,image=treasure)
    elif e == 31:
        e3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e3.config(bg=back,image=turtle_right)
        else:
            e3.config(bg=back,image=turtle_left)
    elif e == 33:
        e3.config(bg=back,image=boar_left)
    elif e == 34:
        e3.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e3.config(bg=back,image=space_fish_right)
            else:
                e3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e3.config(bg=back,image=fish_right)
            else:
                e3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e3.config(bg=back,image=skeleton_attack_left)
        else:
            e3.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e3.config(bg=back,image=skeleton_attack_left)
        else:
            e3.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e3.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e3.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e3.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e3.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e3.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e3.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e3.config(bg=back,image=pirate_attack_left)
        else:
            e3.config(bg=back,image=pirate_left)
    elif e == 42:
        e3.config(bg=back,image=human)
    elif e == 43:
        e3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e3.config(bg=back,image=tent)
    elif e == 47:
        e3.config(bg=back,image=bird)
    elif e == 48:
        e3.config(bg=back,image=spider)
    elif e == 49:
        e3.config(bg=back,image=cloud)
    elif e == 50:
        e3.config(bg=back,image=stem)
    elif e == 51:
        e3.config(bg=back,image=shroom_r)
    elif e == 52:
        e3.config(bg=back,image=shroom_b)
    elif e == 53:
        e3.config(bg=back,image=boat_pirate)
    elif e == 54:
        e3.config(bg=back,image=bullet)
    elif e == 55:
        e3.config(bg=back,image=g_ore)
    elif e == 56:
        e3.config(bg=back,image=book)
    elif e == 57:
        e3.config(bg=back,image=grass_g)
    elif e == 58:
        e3.config(bg=back,image=grass_o)
    elif e == 59:
        e3.config(bg=back,image=kelp)
    elif e == 60:
        e3.config(bg=back,image=frame)
    elif e == 61:
        e3.config(bg=back,image=tower)
    elif e == 62:
        e3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][5]
    if e == 0:
        f3.config(bg=back2,image=blank)
    elif e == 1:
        f3.config(bg=back,image=stone)
    elif e == 2:
        f3.config(bg=back,image=sand)
    elif e == 3:
        f3.config(bg=back,image=water)
    elif e == 4:
        f3.config(bg=back,image=dirt)
    elif e == 5:
        f3.config(bg=back,image=log)
    elif e == 6:
        f3.config(bg=back,image=leaves)
    elif e == 7:
        f3.config(bg=back,image=stick)
    elif e == 8:
        f3.config(bg=back,image=bush)
    elif e == 9:
        f3.config(bg=back,image=potato)
    elif e == 10:
        f3.config(bg=back,image=vine)
    elif e == 11:
        f3.config(bg=back,image=coral_red)
    elif e == 12:
        f3.config(bg=back,image=coral_orange)
    elif e == 13:
        f3.config(bg=back,image=coral_green)
    elif e == 14:
        f3.config(bg=back,image=coral_blue)
    elif e == 15:
        f3.config(bg=back,image=space_coral)
    elif e == 16:
        f3.config(bg=back,image=iron_ore)
    elif e == 17:
        f3.config(bg=back,image=copper_ore)
    elif e == 18:
        f3.config(bg=back,image=bone)
    elif e == 19:
        f3.config(bg=back,image=lantern)
    elif e == 20:
        f3.config(bg=back,image=ladder)
    elif e == 21:
        f3.config(bg=back,image=asteroid)
    elif e == 22:
        f3.config(bg=back,image=sea_bricks)
    elif e == 23:
        f3.config(bg=back,image=stone_bricks)
    elif e == 24:
        f3.config(bg=back,image=sea_lantern)
    elif e == 25:
        f3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f3.config(bg=back,image=anvil)
    elif e == 27:
        f3.config(bg=back,image=space)
    elif e == 28:
        f3.config(bg=back,image=seaglass)
    elif e == 29:
        f3.config(bg=back,image=lava)
    elif e == 30:
        f3.config(bg=back,image=treasure)
    elif e == 31:
        f3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f3.config(bg=back,image=turtle_right)
        else:
            f3.config(bg=back,image=turtle_left)
    elif e == 33:
        f3.config(bg=back,image=boar_left)
    elif e == 34:
        f3.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f3.config(bg=back,image=space_fish_right)
            else:
                f3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f3.config(bg=back,image=fish_right)
            else:
                f3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f3.config(bg=back,image=skeleton_attack_left)
        else:
            f3.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f3.config(bg=back,image=skeleton_attack_left)
        else:
            f3.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f3.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f3.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f3.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f3.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f3.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f3.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f3.config(bg=back,image=pirate_attack_left)
        else:
            f3.config(bg=back,image=pirate_left)
    elif e == 42:
        f3.config(bg=back,image=human)
    elif e == 43:
        f3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f3.config(bg=back,image=tent)
    elif e == 47:
        f3.config(bg=back,image=bird)
    elif e == 48:
        f3.config(bg=back,image=spider)
    elif e == 49:
        f3.config(bg=back,image=cloud)
    elif e == 50:
        f3.config(bg=back,image=stem)
    elif e == 51:
        f3.config(bg=back,image=shroom_r)
    elif e == 52:
        f3.config(bg=back,image=shroom_b)
    elif e == 53:
        f3.config(bg=back,image=boat_pirate)
    elif e == 54:
        f3.config(bg=back,image=bullet)
    elif e == 55:
        f3.config(bg=back,image=g_ore)
    elif e == 56:
        f3.config(bg=back,image=book)
    elif e == 57:
        f3.config(bg=back,image=grass_g)
    elif e == 58:
        f3.config(bg=back,image=grass_o)
    elif e == 59:
        f3.config(bg=back,image=kelp)
    elif e == 60:
        f3.config(bg=back,image=frame)
    elif e == 61:
        f3.config(bg=back,image=tower)
    elif e == 62:
        f3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[2][6]
    if e == 0:
        g3.config(bg=back2,image=blank)
    elif e == 1:
        g3.config(bg=back,image=stone)
    elif e == 2:
        g3.config(bg=back,image=sand)
    elif e == 3:
        g3.config(bg=back,image=water)
    elif e == 4:
        g3.config(bg=back,image=dirt)
    elif e == 5:
        g3.config(bg=back,image=log)
    elif e == 6:
        g3.config(bg=back,image=leaves)
    elif e == 7:
        g3.config(bg=back,image=stick)
    elif e == 8:
        g3.config(bg=back,image=bush)
    elif e == 9:
        g3.config(bg=back,image=potato)
    elif e == 10:
        g3.config(bg=back,image=vine)
    elif e == 11:
        g3.config(bg=back,image=coral_red)
    elif e == 12:
        g3.config(bg=back,image=coral_orange)
    elif e == 13:
        g3.config(bg=back,image=coral_green)
    elif e == 14:
        g3.config(bg=back,image=coral_blue)
    elif e == 15:
        g3.config(bg=back,image=space_coral)
    elif e == 16:
        g3.config(bg=back,image=iron_ore)
    elif e == 17:
        g3.config(bg=back,image=copper_ore)
    elif e == 18:
        g3.config(bg=back,image=bone)
    elif e == 19:
        g3.config(bg=back,image=lantern)
    elif e == 20:
        g3.config(bg=back,image=ladder)
    elif e == 21:
        g3.config(bg=back,image=asteroid)
    elif e == 22:
        g3.config(bg=back,image=sea_bricks)
    elif e == 23:
        g3.config(bg=back,image=stone_bricks)
    elif e == 24:
        g3.config(bg=back,image=sea_lantern)
    elif e == 25:
        g3.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g3.config(bg=back,image=anvil)
    elif e == 27:
        g3.config(bg=back,image=space)
    elif e == 28:
        g3.config(bg=back,image=seaglass)
    elif e == 29:
        g3.config(bg=back,image=lava)
    elif e == 30:
        g3.config(bg=back,image=treasure)
    elif e == 31:
        g3.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g3.config(bg=back,image=turtle_right)
        else:
            g3.config(bg=back,image=turtle_left)
    elif e == 33:
        g3.config(bg=back,image=boar_left)
    elif e == 34:
        g3.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g3.config(bg=back,image=space_fish_right)
            else:
                g3.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g3.config(bg=back,image=fish_right)
            else:
                g3.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g3.config(bg=back,image=skeleton_attack_left)
        else:
            g3.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g3.config(bg=back,image=skeleton_attack_left)
        else:
            g3.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g3.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g3.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g3.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g3.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g3.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g3.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g3.config(bg=back,image=pirate_attack_left)
        else:
            g3.config(bg=back,image=pirate_left)
    elif e == 42:
        g3.config(bg=back,image=human)
    elif e == 43:
        g3.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g3.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g3.config(bg=back,image=tent)
    elif e == 47:
        g3.config(bg=back,image=bird)
    elif e == 48:
        g3.config(bg=back,image=spider)
    elif e == 49:
        g3.config(bg=back,image=cloud)
    elif e == 50:
        g3.config(bg=back,image=stem)
    elif e == 51:
        g3.config(bg=back,image=shroom_r)
    elif e == 52:
        g3.config(bg=back,image=shroom_b)
    elif e == 53:
        g3.config(bg=back,image=boat_pirate)
    elif e == 54:
        g3.config(bg=back,image=bullet)
    elif e == 55:
        g3.config(bg=back,image=g_ore)
    elif e == 56:
        g3.config(bg=back,image=book)
    elif e == 57:
        g3.config(bg=back,image=grass_g)
    elif e == 58:
        g3.config(bg=back,image=grass_o)
    elif e == 59:
        g3.config(bg=back,image=kelp)
    elif e == 60:
        g3.config(bg=back,image=frame)
    elif e == 61:
        g3.config(bg=back,image=tower)
    elif e == 62:
        g3.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][0]
    if e == 0:
        a4.config(bg=back2,image=blank)
    elif e == 1:
        a4.config(bg=back,image=stone)
    elif e == 2:
        a4.config(bg=back,image=sand)
    elif e == 3:
        a4.config(bg=back,image=water)
    elif e == 4:
        a4.config(bg=back,image=dirt)
    elif e == 5:
        a4.config(bg=back,image=log)
    elif e == 6:
        a4.config(bg=back,image=leaves)
    elif e == 7:
        a4.config(bg=back,image=stick)
    elif e == 8:
        a4.config(bg=back,image=bush)
    elif e == 9:
        a4.config(bg=back,image=potato)
    elif e == 10:
        a4.config(bg=back,image=vine)
    elif e == 11:
        a4.config(bg=back,image=coral_red)
    elif e == 12:
        a4.config(bg=back,image=coral_orange)
    elif e == 13:
        a4.config(bg=back,image=coral_green)
    elif e == 14:
        a4.config(bg=back,image=coral_blue)
    elif e == 15:
        a4.config(bg=back,image=space_coral)
    elif e == 16:
        a4.config(bg=back,image=iron_ore)
    elif e == 17:
        a4.config(bg=back,image=copper_ore)
    elif e == 18:
        a4.config(bg=back,image=bone)
    elif e == 19:
        a4.config(bg=back,image=lantern)
    elif e == 20:
        a4.config(bg=back,image=ladder)
    elif e == 21:
        a4.config(bg=back,image=asteroid)
    elif e == 22:
        a4.config(bg=back,image=sea_bricks)
    elif e == 23:
        a4.config(bg=back,image=stone_bricks)
    elif e == 24:
        a4.config(bg=back,image=sea_lantern)
    elif e == 25:
        a4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a4.config(bg=back,image=anvil)
    elif e == 27:
        a4.config(bg=back,image=space)
    elif e == 28:
        a4.config(bg=back,image=seaglass)
    elif e == 29:
        a4.config(bg=back,image=lava)
    elif e == 30:
        a4.config(bg=back,image=treasure)
    elif e == 31:
        a4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a4.config(bg=back,image=turtle_right)
        else:
            a4.config(bg=back,image=turtle_left)
    elif e == 33:
        a4.config(bg=back,image=boar_right)
    elif e == 34:
        a4.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a4.config(bg=back,image=space_fish_right)
            else:
                a4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a4.config(bg=back,image=fish_right)
            else:
                a4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a4.config(bg=back,image=skeleton_attack_right)
        else:
            a4.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a4.config(bg=back,image=skeleton_attack_right)
        else:
            a4.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a4.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a4.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a4.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a4.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a4.config(bg=back,image=pirate_attack_right)
        else:
            a4.config(bg=back,image=pirate_right)
    elif e == 42:
        a4.config(bg=back,image=human)
    elif e == 43:
        a4.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a4.config(bg=back,image=tent)
    elif e == 47:
        a4.config(bg=back,image=bird)
    elif e == 48:
        a4.config(bg=back,image=spider)
    elif e == 49:
        a4.config(bg=back,image=cloud)
    elif e == 50:
        a4.config(bg=back,image=stem)
    elif e == 51:
        a4.config(bg=back,image=shroom_r)
    elif e == 52:
        a4.config(bg=back,image=shroom_b)
    elif e == 53:
        a4.config(bg=back,image=boat_pirate)
    elif e == 54:
        a4.config(bg=back,image=bullet)
    elif e == 55:
        a4.config(bg=back,image=g_ore)
    elif e == 56:
        a4.config(bg=back,image=book)
    elif e == 57:
        a4.config(bg=back,image=grass_g)
    elif e == 58:
        a4.config(bg=back,image=grass_o)
    elif e == 59:
        a4.config(bg=back,image=kelp)
    elif e == 60:
        a4.config(bg=back,image=frame)
    elif e == 61:
        a4.config(bg=back,image=tower)
    elif e == 62:
        a4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][1]
    if e == 0:
        b4.config(bg=back2,image=blank)
    elif e == 1:
        b4.config(bg=back,image=stone)
    elif e == 2:
        b4.config(bg=back,image=sand)
    elif e == 3:
        b4.config(bg=back,image=water)
    elif e == 4:
        b4.config(bg=back,image=dirt)
    elif e == 5:
        b4.config(bg=back,image=log)
    elif e == 6:
        b4.config(bg=back,image=leaves)
    elif e == 7:
        b4.config(bg=back,image=stick)
    elif e == 8:
        b4.config(bg=back,image=bush)
    elif e == 9:
        b4.config(bg=back,image=potato)
    elif e == 10:
        b4.config(bg=back,image=vine)
    elif e == 11:
        b4.config(bg=back,image=coral_red)
    elif e == 12:
        b4.config(bg=back,image=coral_orange)
    elif e == 13:
        b4.config(bg=back,image=coral_green)
    elif e == 14:
        b4.config(bg=back,image=coral_blue)
    elif e == 15:
        b4.config(bg=back,image=space_coral)
    elif e == 16:
        b4.config(bg=back,image=iron_ore)
    elif e == 17:
        b4.config(bg=back,image=copper_ore)
    elif e == 18:
        b4.config(bg=back,image=bone)
    elif e == 19:
        b4.config(bg=back,image=lantern)
    elif e == 20:
        b4.config(bg=back,image=ladder)
    elif e == 21:
        b4.config(bg=back,image=asteroid)
    elif e == 22:
        b4.config(bg=back,image=sea_bricks)
    elif e == 23:
        b4.config(bg=back,image=stone_bricks)
    elif e == 24:
        b4.config(bg=back,image=sea_lantern)
    elif e == 25:
        b4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b4.config(bg=back,image=anvil)
    elif e == 27:
        b4.config(bg=back,image=space)
    elif e == 28:
        b4.config(bg=back,image=seaglass)
    elif e == 29:
        b4.config(bg=back,image=lava)
    elif e == 30:
        b4.config(bg=back,image=treasure)
    elif e == 31:
        b4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b4.config(bg=back,image=turtle_right)
        else:
            b4.config(bg=back,image=turtle_left)
    elif e == 33:
        b4.config(bg=back,image=boar_right)
    elif e == 34:
        b4.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b4.config(bg=back,image=space_fish_right)
            else:
                b4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b4.config(bg=back,image=fish_right)
            else:
                b4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b4.config(bg=back,image=skeleton_attack_right)
        else:
            b4.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b4.config(bg=back,image=skeleton_attack_right)
        else:
            b4.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b4.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b4.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b4.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b4.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b4.config(bg=back,image=pirate_attack_right)
        else:
            b4.config(bg=back,image=pirate_right)
    elif e == 42:
        b4.config(bg=back,image=human)
    elif e == 43:
        b4.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b4.config(bg=back,image=tent)
    elif e == 47:
        b4.config(bg=back,image=bird)
    elif e == 48:
        b4.config(bg=back,image=spider)
    elif e == 49:
        b4.config(bg=back,image=cloud)
    elif e == 50:
        b4.config(bg=back,image=stem)
    elif e == 51:
        b4.config(bg=back,image=shroom_r)
    elif e == 52:
        b4.config(bg=back,image=shroom_b)
    elif e == 53:
        b4.config(bg=back,image=boat_pirate)
    elif e == 54:
        b4.config(bg=back,image=bullet)
    elif e == 55:
        b4.config(bg=back,image=g_ore)
    elif e == 56:
        b4.config(bg=back,image=book)
    elif e == 57:
        b4.config(bg=back,image=grass_g)
    elif e == 58:
        b4.config(bg=back,image=grass_o)
    elif e == 59:
        b4.config(bg=back,image=kelp)
    elif e == 60:
        b4.config(bg=back,image=frame)
    elif e == 61:
        b4.config(bg=back,image=tower)
    elif e == 62:
        b4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][2]
    if e == 0:
        c4.config(bg=back2,image=blank)
    elif e == 1:
        c4.config(bg=back,image=stone)
    elif e == 2:
        c4.config(bg=back,image=sand)
    elif e == 3:
        c4.config(bg=back,image=water)
    elif e == 4:
        c4.config(bg=back,image=dirt)
    elif e == 5:
        c4.config(bg=back,image=log)
    elif e == 6:
        c4.config(bg=back,image=leaves)
    elif e == 7:
        c4.config(bg=back,image=stick)
    elif e == 8:
        c4.config(bg=back,image=bush)
    elif e == 9:
        c4.config(bg=back,image=potato)
    elif e == 10:
        c4.config(bg=back,image=vine)
    elif e == 11:
        c4.config(bg=back,image=coral_red)
    elif e == 12:
        c4.config(bg=back,image=coral_orange)
    elif e == 13:
        c4.config(bg=back,image=coral_green)
    elif e == 14:
        c4.config(bg=back,image=coral_blue)
    elif e == 15:
        c4.config(bg=back,image=space_coral)
    elif e == 16:
        c4.config(bg=back,image=iron_ore)
    elif e == 17:
        c4.config(bg=back,image=copper_ore)
    elif e == 18:
        c4.config(bg=back,image=bone)
    elif e == 19:
        c4.config(bg=back,image=lantern)
    elif e == 20:
        c4.config(bg=back,image=ladder)
    elif e == 21:
        c4.config(bg=back,image=asteroid)
    elif e == 22:
        c4.config(bg=back,image=sea_bricks)
    elif e == 23:
        c4.config(bg=back,image=stone_bricks)
    elif e == 24:
        c4.config(bg=back,image=sea_lantern)
    elif e == 25:
        c4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c4.config(bg=back,image=anvil)
    elif e == 27:
        c4.config(bg=back,image=space)
    elif e == 28:
        c4.config(bg=back,image=seaglass)
    elif e == 29:
        c4.config(bg=back,image=lava)
    elif e == 30:
        c4.config(bg=back,image=treasure)
    elif e == 31:
        c4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c4.config(bg=back,image=turtle_right)
        else:
            c4.config(bg=back,image=turtle_left)
    elif e == 33:
        c4.config(bg=back,image=boar_right)
    elif e == 34:
        c4.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c4.config(bg=back,image=space_fish_right)
            else:
                c4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c4.config(bg=back,image=fish_right)
            else:
                c4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c4.config(bg=back,image=skeleton_attack_right)
        else:
            c4.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c4.config(bg=back,image=skeleton_attack_right)
        else:
            c4.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c4.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c4.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c4.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c4.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c4.config(bg=back,image=pirate_attack_right)
        else:
            c4.config(bg=back,image=pirate_right)
    elif e == 42:
        c4.config(bg=back,image=human)
    elif e == 43:
        c4.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c4.config(bg=back,image=tent)
    elif e == 47:
        c4.config(bg=back,image=bird)
    elif e == 48:
        c4.config(bg=back,image=spider)
    elif e == 49:
        c4.config(bg=back,image=cloud)
    elif e == 50:
        c4.config(bg=back,image=stem)
    elif e == 51:
        c4.config(bg=back,image=shroom_r)
    elif e == 52:
        c4.config(bg=back,image=shroom_b)
    elif e == 53:
        c4.config(bg=back,image=boat_pirate)
    elif e == 54:
        c4.config(bg=back,image=bullet)
    elif e == 55:
        c4.config(bg=back,image=g_ore)
    elif e == 56:
        c4.config(bg=back,image=book)
    elif e == 57:
        c4.config(bg=back,image=grass_g)
    elif e == 58:
        c4.config(bg=back,image=grass_o)
    elif e == 59:
        c4.config(bg=back,image=kelp)
    elif e == 60:
        c4.config(bg=back,image=frame)
    elif e == 61:
        c4.config(bg=back,image=tower)
    elif e == 62:
        c4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][3]
    if e == 0:
        d4.config(bg=back2,image=blank)
    elif e == 1:
        d4.config(bg=back,image=stone)
    elif e == 2:
        d4.config(bg=back,image=sand)
    elif e == 3:
        d4.config(bg=back,image=water)
    elif e == 4:
        d4.config(bg=back,image=dirt)
    elif e == 5:
        d4.config(bg=back,image=log)
    elif e == 6:
        d4.config(bg=back,image=leaves)
    elif e == 7:
        d4.config(bg=back,image=stick)
    elif e == 8:
        d4.config(bg=back,image=bush)
    elif e == 9:
        d4.config(bg=back,image=potato)
    elif e == 10:
        d4.config(bg=back,image=vine)
    elif e == 11:
        d4.config(bg=back,image=coral_red)
    elif e == 12:
        d4.config(bg=back,image=coral_orange)
    elif e == 13:
        d4.config(bg=back,image=coral_green)
    elif e == 14:
        d4.config(bg=back,image=coral_blue)
    elif e == 15:
        d4.config(bg=back,image=space_coral)
    elif e == 16:
        d4.config(bg=back,image=iron_ore)
    elif e == 17:
        d4.config(bg=back,image=copper_ore)
    elif e == 18:
        d4.config(bg=back,image=bone)
    elif e == 19:
        d4.config(bg=back,image=lantern)
    elif e == 20:
        d4.config(bg=back,image=ladder)
    elif e == 21:
        d4.config(bg=back,image=asteroid)
    elif e == 22:
        d4.config(bg=back,image=sea_bricks)
    elif e == 23:
        d4.config(bg=back,image=stone_bricks)
    elif e == 24:
        d4.config(bg=back,image=sea_lantern)
    elif e == 25:
        d4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d4.config(bg=back,image=anvil)
    elif e == 27:
        d4.config(bg=back,image=space)
    elif e == 28:
        d4.config(bg=back,image=seaglass)
    elif e == 29:
        d4.config(bg=back,image=lava)
    elif e == 30:
        d4.config(bg=back,image=treasure)
    elif e == 31:
        d4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d4.config(bg=back,image=turtle_right)
        else:
            d4.config(bg=back,image=turtle_left)
    elif e == 33:
        d4.config(bg=back,image=boar_right)
    elif e == 34:
        d4.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d4.config(bg=back,image=space_fish_right)
            else:
                d4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d4.config(bg=back,image=fish_right)
            else:
                d4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d4.config(bg=back,image=skeleton_attack_right)
        else:
            d4.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d4.config(bg=back,image=skeleton_attack_right)
        else:
            d4.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d4.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d4.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d4.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d4.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d4.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d4.config(bg=back,image=pirate_attack_right)
        else:
            d4.config(bg=back,image=pirate_right)
    elif e == 42:
        d4.config(bg=back,image=human)
    elif e == 43:
        d4.config(bg=back,image=pufferfish)
    elif e == 44:
        global boat_
        if boat_ == True:
            d4.config(bg=back,image=player_boat)
        else:
            if st == 0:
                d4.config(bg=back,image=player_ko)
            else:
                d4.config(bg=back,image=player)
    elif e == 45:
        d4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d4.config(bg=back,image=tent)
    elif e == 47:
        d4.config(bg=back,image=bird)
    elif e == 48:
        d4.config(bg=back,image=spider)
    elif e == 49:
        d4.config(bg=back,image=cloud)
    elif e == 50:
        d4.config(bg=back,image=stem)
    elif e == 51:
        d4.config(bg=back,image=shroom_r)
    elif e == 52:
        d4.config(bg=back,image=shroom_b)
    elif e == 53:
        d4.config(bg=back,image=boat_pirate)
    elif e == 54:
        d4.config(bg=back,image=bullet)
    elif e == 55:
        d4.config(bg=back,image=g_ore)
    elif e == 56:
        d4.config(bg=back,image=book)
    elif e == 57:
        d4.config(bg=back,image=grass_g)
    elif e == 58:
        d4.config(bg=back,image=grass_o)
    elif e == 59:
        d4.config(bg=back,image=kelp)
    elif e == 60:
        d4.config(bg=back,image=frame)
    elif e == 61:
        d4.config(bg=back,image=tower)
    elif e == 62:
        d4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][4]
    if e == 0:
        e4.config(bg=back2,image=blank)
    elif e == 1:
        e4.config(bg=back,image=stone)
    elif e == 2:
        e4.config(bg=back,image=sand)
    elif e == 3:
        e4.config(bg=back,image=water)
    elif e == 4:
        e4.config(bg=back,image=dirt)
    elif e == 5:
        e4.config(bg=back,image=log)
    elif e == 6:
        e4.config(bg=back,image=leaves)
    elif e == 7:
        e4.config(bg=back,image=stick)
    elif e == 8:
        e4.config(bg=back,image=bush)
    elif e == 9:
        e4.config(bg=back,image=potato)
    elif e == 10:
        e4.config(bg=back,image=vine)
    elif e == 11:
        e4.config(bg=back,image=coral_red)
    elif e == 12:
        e4.config(bg=back,image=coral_orange)
    elif e == 13:
        e4.config(bg=back,image=coral_green)
    elif e == 14:
        e4.config(bg=back,image=coral_blue)
    elif e == 15:
        e4.config(bg=back,image=space_coral)
    elif e == 16:
        e4.config(bg=back,image=iron_ore)
    elif e == 17:
        e4.config(bg=back,image=copper_ore)
    elif e == 18:
        e4.config(bg=back,image=bone)
    elif e == 19:
        e4.config(bg=back,image=lantern)
    elif e == 20:
        e4.config(bg=back,image=ladder)
    elif e == 21:
        e4.config(bg=back,image=asteroid)
    elif e == 22:
        e4.config(bg=back,image=sea_bricks)
    elif e == 23:
        e4.config(bg=back,image=stone_bricks)
    elif e == 24:
        e4.config(bg=back,image=sea_lantern)
    elif e == 25:
        e4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e4.config(bg=back,image=anvil)
    elif e == 27:
        e4.config(bg=back,image=space)
    elif e == 28:
        e4.config(bg=back,image=seaglass)
    elif e == 29:
        e4.config(bg=back,image=lava)
    elif e == 30:
        e4.config(bg=back,image=treasure)
    elif e == 31:
        e4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e4.config(bg=back,image=turtle_right)
        else:
            e4.config(bg=back,image=turtle_left)
    elif e == 33:
        e4.config(bg=back,image=boar_left)
    elif e == 34:
        e4.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e4.config(bg=back,image=space_fish_right)
            else:
                e4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e4.config(bg=back,image=fish_right)
            else:
                e4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e4.config(bg=back,image=skeleton_attack_left)
        else:
            e4.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e4.config(bg=back,image=skeleton_attack_left)
        else:
            e4.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e4.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e4.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e4.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e4.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e4.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e4.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e4.config(bg=back,image=pirate_attack_left)
        else:
            e4.config(bg=back,image=pirate_left)
    elif e == 42:
        e4.config(bg=back,image=human)
    elif e == 43:
        e4.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e4.config(bg=back,image=tent)
    elif e == 47:
        e4.config(bg=back,image=bird)
    elif e == 48:
        e4.config(bg=back,image=spider)
    elif e == 49:
        e4.config(bg=back,image=cloud)
    elif e == 50:
        e4.config(bg=back,image=stem)
    elif e == 51:
        e4.config(bg=back,image=shroom_r)
    elif e == 52:
        e4.config(bg=back,image=shroom_b)
    elif e == 53:
        e4.config(bg=back,image=boat_pirate)
    elif e == 54:
        e4.config(bg=back,image=bullet)
    elif e == 55:
        e4.config(bg=back,image=g_ore)
    elif e == 56:
        e4.config(bg=back,image=book)
    elif e == 57:
        e4.config(bg=back,image=grass_g)
    elif e == 58:
        e4.config(bg=back,image=grass_o)
    elif e == 59:
        e4.config(bg=back,image=kelp)
    elif e == 60:
        e4.config(bg=back,image=frame)
    elif e == 61:
        e4.config(bg=back,image=tower)
    elif e == 62:
        e4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][5]
    if e == 0:
        f4.config(bg=back2,image=blank)
    elif e == 1:
        f4.config(bg=back,image=stone)
    elif e == 2:
        f4.config(bg=back,image=sand)
    elif e == 3:
        f4.config(bg=back,image=water)
    elif e == 4:
        f4.config(bg=back,image=dirt)
    elif e == 5:
        f4.config(bg=back,image=log)
    elif e == 6:
        f4.config(bg=back,image=leaves)
    elif e == 7:
        f4.config(bg=back,image=stick)
    elif e == 8:
        f4.config(bg=back,image=bush)
    elif e == 9:
        f4.config(bg=back,image=potato)
    elif e == 10:
        f4.config(bg=back,image=vine)
    elif e == 11:
        f4.config(bg=back,image=coral_red)
    elif e == 12:
        f4.config(bg=back,image=coral_orange)
    elif e == 13:
        f4.config(bg=back,image=coral_green)
    elif e == 14:
        f4.config(bg=back,image=coral_blue)
    elif e == 15:
        f4.config(bg=back,image=space_coral)
    elif e == 16:
        f4.config(bg=back,image=iron_ore)
    elif e == 17:
        f4.config(bg=back,image=copper_ore)
    elif e == 18:
        f4.config(bg=back,image=bone)
    elif e == 19:
        f4.config(bg=back,image=lantern)
    elif e == 20:
        f4.config(bg=back,image=ladder)
    elif e == 21:
        f4.config(bg=back,image=asteroid)
    elif e == 22:
        f4.config(bg=back,image=sea_bricks)
    elif e == 23:
        f4.config(bg=back,image=stone_bricks)
    elif e == 24:
        f4.config(bg=back,image=sea_lantern)
    elif e == 25:
        f4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f4.config(bg=back,image=anvil)
    elif e == 27:
        f4.config(bg=back,image=space)
    elif e == 28:
        f4.config(bg=back,image=seaglass)
    elif e == 29:
        f4.config(bg=back,image=lava)
    elif e == 30:
        f4.config(bg=back,image=treasure)
    elif e == 31:
        f4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f4.config(bg=back,image=turtle_right)
        else:
            f4.config(bg=back,image=turtle_left)
    elif e == 33:
        f4.config(bg=back,image=boar_left)
    elif e == 34:
        f4.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f4.config(bg=back,image=space_fish_right)
            else:
                f4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f4.config(bg=back,image=fish_right)
            else:
                f4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f4.config(bg=back,image=skeleton_attack_left)
        else:
            f4.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f4.config(bg=back,image=skeleton_attack_left)
        else:
            f4.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f4.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f4.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f4.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f4.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f4.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f4.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f4.config(bg=back,image=pirate_attack_left)
        else:
            f4.config(bg=back,image=pirate_left)
    elif e == 42:
        f4.config(bg=back,image=human)
    elif e == 43:
        f4.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f4.config(bg=back,image=tent)
    elif e == 47:
        f4.config(bg=back,image=bird)
    elif e == 48:
        f4.config(bg=back,image=spider)
    elif e == 49:
        f4.config(bg=back,image=cloud)
    elif e == 50:
        f4.config(bg=back,image=stem)
    elif e == 51:
        f4.config(bg=back,image=shroom_r)
    elif e == 52:
        f4.config(bg=back,image=shroom_b)
    elif e == 53:
        f4.config(bg=back,image=boat_pirate)
    elif e == 54:
        f4.config(bg=back,image=bullet)
    elif e == 55:
        f4.config(bg=back,image=g_ore)
    elif e == 56:
        f4.config(bg=back,image=book)
    elif e == 57:
        f4.config(bg=back,image=grass_g)
    elif e == 58:
        f4.config(bg=back,image=grass_o)
    elif e == 59:
        f4.config(bg=back,image=kelp)
    elif e == 60:
        f4.config(bg=back,image=frame)
    elif e == 61:
        f4.config(bg=back,image=tower)
    elif e == 62:
        f4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[3][6]
    if e == 0:
        g4.config(bg=back2,image=blank)
    elif e == 1:
        g4.config(bg=back,image=stone)
    elif e == 2:
        g4.config(bg=back,image=sand)
    elif e == 3:
        g4.config(bg=back,image=water)
    elif e == 4:
        g4.config(bg=back,image=dirt)
    elif e == 5:
        g4.config(bg=back,image=log)
    elif e == 6:
        g4.config(bg=back,image=leaves)
    elif e == 7:
        g4.config(bg=back,image=stick)
    elif e == 8:
        g4.config(bg=back,image=bush)
    elif e == 9:
        g4.config(bg=back,image=potato)
    elif e == 10:
        g4.config(bg=back,image=vine)
    elif e == 11:
        g4.config(bg=back,image=coral_red)
    elif e == 12:
        g4.config(bg=back,image=coral_orange)
    elif e == 13:
        g4.config(bg=back,image=coral_green)
    elif e == 14:
        g4.config(bg=back,image=coral_blue)
    elif e == 15:
        g4.config(bg=back,image=space_coral)
    elif e == 16:
        g4.config(bg=back,image=iron_ore)
    elif e == 17:
        g4.config(bg=back,image=copper_ore)
    elif e == 18:
        g4.config(bg=back,image=bone)
    elif e == 19:
        g4.config(bg=back,image=lantern)
    elif e == 20:
        g4.config(bg=back,image=ladder)
    elif e == 21:
        g4.config(bg=back,image=asteroid)
    elif e == 22:
        g4.config(bg=back,image=sea_bricks)
    elif e == 23:
        g4.config(bg=back,image=stone_bricks)
    elif e == 24:
        g4.config(bg=back,image=sea_lantern)
    elif e == 25:
        g4.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g4.config(bg=back,image=anvil)
    elif e == 27:
        g4.config(bg=back,image=space)
    elif e == 28:
        g4.config(bg=back,image=seaglass)
    elif e == 29:
        g4.config(bg=back,image=lava)
    elif e == 30:
        g4.config(bg=back,image=treasure)
    elif e == 31:
        g4.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g4.config(bg=back,image=turtle_right)
        else:
            g4.config(bg=back,image=turtle_left)
    elif e == 33:
        g4.config(bg=back,image=boar_left)
    elif e == 34:
        g4.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g4.config(bg=back,image=space_fish_right)
            else:
                g4.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g4.config(bg=back,image=fish_right)
            else:
                g4.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g4.config(bg=back,image=skeleton_attack_left)
        else:
            g4.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g4.config(bg=back,image=skeleton_attack_left)
        else:
            g4.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g4.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g4.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g4.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g4.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g4.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g4.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g4.config(bg=back,image=pirate_attack_left)
        else:
            g4.config(bg=back,image=pirate_left)
    elif e == 42:
        g4.config(bg=back,image=human)
    elif e == 43:
        g4.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g4.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g4.config(bg=back,image=tent)
    elif e == 47:
        g4.config(bg=back,image=bird)
    elif e == 48:
        g4.config(bg=back,image=spider)
    elif e == 49:
        g4.config(bg=back,image=cloud)
    elif e == 50:
        g4.config(bg=back,image=stem)
    elif e == 51:
        g4.config(bg=back,image=shroom_r)
    elif e == 52:
        g4.config(bg=back,image=shroom_b)
    elif e == 53:
        g4.config(bg=back,image=boat_pirate)
    elif e == 54:
        g4.config(bg=back,image=bullet)
    elif e == 55:
        g4.config(bg=back,image=g_ore)
    elif e == 56:
        g4.config(bg=back,image=book)
    elif e == 57:
        g4.config(bg=back,image=grass_g)
    elif e == 58:
        g4.config(bg=back,image=grass_o)
    elif e == 59:
        g4.config(bg=back,image=kelp)
    elif e == 60:
        g4.config(bg=back,image=frame)
    elif e == 61:
        g4.config(bg=back,image=tower)
    elif e == 62:
        g4.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][0]
    if e == 0:
        a5.config(bg=back2,image=blank)
    elif e == 1:
        a5.config(bg=back,image=stone)
    elif e == 2:
        a5.config(bg=back,image=sand)
    elif e == 3:
        a5.config(bg=back,image=water)
    elif e == 4:
        a5.config(bg=back,image=dirt)
    elif e == 5:
        a5.config(bg=back,image=log)
    elif e == 6:
        a5.config(bg=back,image=leaves)
    elif e == 7:
        a5.config(bg=back,image=stick)
    elif e == 8:
        a5.config(bg=back,image=bush)
    elif e == 9:
        a5.config(bg=back,image=potato)
    elif e == 10:
        a5.config(bg=back,image=vine)
    elif e == 11:
        a5.config(bg=back,image=coral_red)
    elif e == 12:
        a5.config(bg=back,image=coral_orange)
    elif e == 13:
        a5.config(bg=back,image=coral_green)
    elif e == 14:
        a5.config(bg=back,image=coral_blue)
    elif e == 15:
        a5.config(bg=back,image=space_coral)
    elif e == 16:
        a5.config(bg=back,image=iron_ore)
    elif e == 17:
        a5.config(bg=back,image=copper_ore)
    elif e == 18:
        a5.config(bg=back,image=bone)
    elif e == 19:
        a5.config(bg=back,image=lantern)
    elif e == 20:
        a5.config(bg=back,image=ladder)
    elif e == 21:
        a5.config(bg=back,image=asteroid)
    elif e == 22:
        a5.config(bg=back,image=sea_bricks)
    elif e == 23:
        a5.config(bg=back,image=stone_bricks)
    elif e == 24:
        a5.config(bg=back,image=sea_lantern)
    elif e == 25:
        a5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a5.config(bg=back,image=anvil)
    elif e == 27:
        a5.config(bg=back,image=space)
    elif e == 28:
        a5.config(bg=back,image=seaglass)
    elif e == 29:
        a5.config(bg=back,image=lava)
    elif e == 30:
        a5.config(bg=back,image=treasure)
    elif e == 31:
        a5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a5.config(bg=back,image=turtle_right)
        else:
            a5.config(bg=back,image=turtle_left)
    elif e == 33:
        a5.config(bg=back,image=boar_right)
    elif e == 34:
        a5.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a5.config(bg=back,image=space_fish_right)
            else:
                a5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a5.config(bg=back,image=fish_right)
            else:
                a5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a5.config(bg=back,image=skeleton_attack_right)
        else:
            a5.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a5.config(bg=back,image=skeleton_attack_right)
        else:
            a5.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a5.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a5.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a5.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a5.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a5.config(bg=back,image=pirate_attack_right)
        else:
            a5.config(bg=back,image=pirate_right)
    elif e == 42:
        a5.config(bg=back,image=human)
    elif e == 43:
        a5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a5.config(bg=back,image=tent)
    elif e == 47:
        a5.config(bg=back,image=bird)
    elif e == 48:
        a5.config(bg=back,image=spider)
    elif e == 49:
        a5.config(bg=back,image=cloud)
    elif e == 50:
        a5.config(bg=back,image=stem)
    elif e == 51:
        a5.config(bg=back,image=shroom_r)
    elif e == 52:
        a5.config(bg=back,image=shroom_b)
    elif e == 53:
        a5.config(bg=back,image=boat_pirate)
    elif e == 54:
        a5.config(bg=back,image=bullet)
    elif e == 55:
        a5.config(bg=back,image=g_ore)
    elif e == 56:
        a5.config(bg=back,image=book)
    elif e == 57:
        a5.config(bg=back,image=grass_g)
    elif e == 58:
        a5.config(bg=back,image=grass_o)
    elif e == 59:
        a5.config(bg=back,image=kelp)
    elif e == 60:
        a5.config(bg=back,image=frame)
    elif e == 61:
        a5.config(bg=back,image=tower)
    elif e == 62:
        a5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][1]
    if e == 0:
        b5.config(bg=back2,image=blank)
    elif e == 1:
        b5.config(bg=back,image=stone)
    elif e == 2:
        b5.config(bg=back,image=sand)
    elif e == 3:
        b5.config(bg=back,image=water)
    elif e == 4:
        b5.config(bg=back,image=dirt)
    elif e == 5:
        b5.config(bg=back,image=log)
    elif e == 6:
        b5.config(bg=back,image=leaves)
    elif e == 7:
        b5.config(bg=back,image=stick)
    elif e == 8:
        b5.config(bg=back,image=bush)
    elif e == 9:
        b5.config(bg=back,image=potato)
    elif e == 10:
        b5.config(bg=back,image=vine)
    elif e == 11:
        b5.config(bg=back,image=coral_red)
    elif e == 12:
        b5.config(bg=back,image=coral_orange)
    elif e == 13:
        b5.config(bg=back,image=coral_green)
    elif e == 14:
        b5.config(bg=back,image=coral_blue)
    elif e == 15:
        b5.config(bg=back,image=space_coral)
    elif e == 16:
        b5.config(bg=back,image=iron_ore)
    elif e == 17:
        b5.config(bg=back,image=copper_ore)
    elif e == 18:
        b5.config(bg=back,image=bone)
    elif e == 19:
        b5.config(bg=back,image=lantern)
    elif e == 20:
        b5.config(bg=back,image=ladder)
    elif e == 21:
        b5.config(bg=back,image=asteroid)
    elif e == 22:
        b5.config(bg=back,image=sea_bricks)
    elif e == 23:
        b5.config(bg=back,image=stone_bricks)
    elif e == 24:
        b5.config(bg=back,image=sea_lantern)
    elif e == 25:
        b5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b5.config(bg=back,image=anvil)
    elif e == 27:
        b5.config(bg=back,image=space)
    elif e == 28:
        b5.config(bg=back,image=seaglass)
    elif e == 29:
        b5.config(bg=back,image=lava)
    elif e == 30:
        b5.config(bg=back,image=treasure)
    elif e == 31:
        b5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b5.config(bg=back,image=turtle_right)
        else:
            b5.config(bg=back,image=turtle_left)
    elif e == 33:
        b5.config(bg=back,image=boar_right)
    elif e == 34:
        b5.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b5.config(bg=back,image=space_fish_right)
            else:
                b5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b5.config(bg=back,image=fish_right)
            else:
                b5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b5.config(bg=back,image=skeleton_attack_right)
        else:
            b5.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b5.config(bg=back,image=skeleton_attack_right)
        else:
            b5.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b5.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b5.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b5.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b5.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b5.config(bg=back,image=pirate_attack_right)
        else:
            b5.config(bg=back,image=pirate_right)
    elif e == 42:
        b5.config(bg=back,image=human)
    elif e == 43:
        b5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b5.config(bg=back,image=tent)
    elif e == 47:
        b5.config(bg=back,image=bird)
    elif e == 48:
        b5.config(bg=back,image=spider)
    elif e == 49:
        b5.config(bg=back,image=cloud)
    elif e == 50:
        b5.config(bg=back,image=stem)
    elif e == 51:
        b5.config(bg=back,image=shroom_r)
    elif e == 52:
        b5.config(bg=back,image=shroom_b)
    elif e == 53:
        b5.config(bg=back,image=boat_pirate)
    elif e == 54:
        b5.config(bg=back,image=bullet)
    elif e == 55:
        b5.config(bg=back,image=g_ore)
    elif e == 56:
        b5.config(bg=back,image=book)
    elif e == 57:
        b5.config(bg=back,image=grass_g)
    elif e == 58:
        b5.config(bg=back,image=grass_o)
    elif e == 59:
        b5.config(bg=back,image=kelp)
    elif e == 60:
        b5.config(bg=back,image=frame)
    elif e == 61:
        b5.config(bg=back,image=tower)
    elif e == 62:
        b5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][2]
    if e == 0:
        c5.config(bg=back2,image=blank)
    elif e == 1:
        c5.config(bg=back,image=stone)
    elif e == 2:
        c5.config(bg=back,image=sand)
    elif e == 3:
        c5.config(bg=back,image=water)
    elif e == 4:
        c5.config(bg=back,image=dirt)
    elif e == 5:
        c5.config(bg=back,image=log)
    elif e == 6:
        c5.config(bg=back,image=leaves)
    elif e == 7:
        c5.config(bg=back,image=stick)
    elif e == 8:
        c5.config(bg=back,image=bush)
    elif e == 9:
        c5.config(bg=back,image=potato)
    elif e == 10:
        c5.config(bg=back,image=vine)
    elif e == 11:
        c5.config(bg=back,image=coral_red)
    elif e == 12:
        c5.config(bg=back,image=coral_orange)
    elif e == 13:
        c5.config(bg=back,image=coral_green)
    elif e == 14:
        c5.config(bg=back,image=coral_blue)
    elif e == 15:
        c5.config(bg=back,image=space_coral)
    elif e == 16:
        c5.config(bg=back,image=iron_ore)
    elif e == 17:
        c5.config(bg=back,image=copper_ore)
    elif e == 18:
        c5.config(bg=back,image=bone)
    elif e == 19:
        c5.config(bg=back,image=lantern)
    elif e == 20:
        c5.config(bg=back,image=ladder)
    elif e == 21:
        c5.config(bg=back,image=asteroid)
    elif e == 22:
        c5.config(bg=back,image=sea_bricks)
    elif e == 23:
        c5.config(bg=back,image=stone_bricks)
    elif e == 24:
        c5.config(bg=back,image=sea_lantern)
    elif e == 25:
        c5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c5.config(bg=back,image=anvil)
    elif e == 27:
        c5.config(bg=back,image=space)
    elif e == 28:
        c5.config(bg=back,image=seaglass)
    elif e == 29:
        c5.config(bg=back,image=lava)
    elif e == 30:
        c5.config(bg=back,image=treasure)
    elif e == 31:
        c5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c5.config(bg=back,image=turtle_right)
        else:
            c5.config(bg=back,image=turtle_left)
    elif e == 33:
        c5.config(bg=back,image=boar_right)
    elif e == 34:
        c5.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c5.config(bg=back,image=space_fish_right)
            else:
                c5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c5.config(bg=back,image=fish_right)
            else:
                c5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c5.config(bg=back,image=skeleton_attack_right)
        else:
            c5.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c5.config(bg=back,image=skeleton_attack_right)
        else:
            c5.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c5.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c5.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c5.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c5.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c5.config(bg=back,image=pirate_attack_right)
        else:
            c5.config(bg=back,image=pirate_right)
    elif e == 42:
        c5.config(bg=back,image=human)
    elif e == 43:
        c5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c5.config(bg=back,image=tent)
    elif e == 47:
        c5.config(bg=back,image=bird)
    elif e == 48:
        c5.config(bg=back,image=spider)
    elif e == 49:
        c5.config(bg=back,image=cloud)
    elif e == 50:
        c5.config(bg=back,image=stem)
    elif e == 51:
        c5.config(bg=back,image=shroom_r)
    elif e == 52:
        c5.config(bg=back,image=shroom_b)
    elif e == 53:
        c5.config(bg=back,image=boat_pirate)
    elif e == 54:
        c5.config(bg=back,image=bullet)
    elif e == 55:
        c5.config(bg=back,image=g_ore)
    elif e == 56:
        c5.config(bg=back,image=book)
    elif e == 57:
        c5.config(bg=back,image=grass_g)
    elif e == 58:
        c5.config(bg=back,image=grass_o)
    elif e == 59:
        c5.config(bg=back,image=kelp)
    elif e == 60:
        c5.config(bg=back,image=frame)
    elif e == 61:
        c5.config(bg=back,image=tower)
    elif e == 62:
        c5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][3]
    if e == 0:
        d5.config(bg=back2,image=blank)
    elif e == 1:
        d5.config(bg=back,image=stone)
    elif e == 2:
        d5.config(bg=back,image=sand)
    elif e == 3:
        d5.config(bg=back,image=water)
    elif e == 4:
        d5.config(bg=back,image=dirt)
    elif e == 5:
        d5.config(bg=back,image=log)
    elif e == 6:
        d5.config(bg=back,image=leaves)
    elif e == 7:
        d5.config(bg=back,image=stick)
    elif e == 8:
        d5.config(bg=back,image=bush)
    elif e == 9:
        d5.config(bg=back,image=potato)
    elif e == 10:
        d5.config(bg=back,image=vine)
    elif e == 11:
        d5.config(bg=back,image=coral_red)
    elif e == 12:
        d5.config(bg=back,image=coral_orange)
    elif e == 13:
        d5.config(bg=back,image=coral_green)
    elif e == 14:
        d5.config(bg=back,image=coral_blue)
    elif e == 15:
        d5.config(bg=back,image=space_coral)
    elif e == 16:
        d5.config(bg=back,image=iron_ore)
    elif e == 17:
        d5.config(bg=back,image=copper_ore)
    elif e == 18:
        d5.config(bg=back,image=bone)
    elif e == 19:
        d5.config(bg=back,image=lantern)
    elif e == 20:
        d5.config(bg=back,image=ladder)
    elif e == 21:
        d5.config(bg=back,image=asteroid)
    elif e == 22:
        d5.config(bg=back,image=sea_bricks)
    elif e == 23:
        d5.config(bg=back,image=stone_bricks)
    elif e == 24:
        d5.config(bg=back,image=sea_lantern)
    elif e == 25:
        d5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d5.config(bg=back,image=anvil)
    elif e == 27:
        d5.config(bg=back,image=space)
    elif e == 28:
        d5.config(bg=back,image=seaglass)
    elif e == 29:
        d5.config(bg=back,image=lava)
    elif e == 30:
        d5.config(bg=back,image=treasure)
    elif e == 31:
        d5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d5.config(bg=back,image=turtle_right)
        else:
            d5.config(bg=back,image=turtle_left)
    elif e == 33:
        d5.config(bg=back,image=boar_right)
    elif e == 34:
        d5.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d5.config(bg=back,image=space_fish_right)
            else:
                d5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d5.config(bg=back,image=fish_right)
            else:
                d5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d5.config(bg=back,image=skeleton_attack_right)
        else:
            d5.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d5.config(bg=back,image=skeleton_attack_right)
        else:
            d5.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d5.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d5.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d5.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d5.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d5.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d5.config(bg=back,image=pirate_attack_right)
        else:
            d5.config(bg=back,image=pirate_right)
    elif e == 42:
        d5.config(bg=back,image=human)
    elif e == 43:
        d5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        d5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d5.config(bg=back,image=tent)
    elif e == 47:
        d5.config(bg=back,image=bird)
    elif e == 48:
        d5.config(bg=back,image=spider)
    elif e == 49:
        d5.config(bg=back,image=cloud)
    elif e == 50:
        d5.config(bg=back,image=stem)
    elif e == 51:
        d5.config(bg=back,image=shroom_r)
    elif e == 52:
        d5.config(bg=back,image=shroom_b)
    elif e == 53:
        d5.config(bg=back,image=boat_pirate)
    elif e == 54:
        d5.config(bg=back,image=bullet)
    elif e == 55:
        d5.config(bg=back,image=g_ore)
    elif e == 56:
        d5.config(bg=back,image=book)
    elif e == 57:
        d5.config(bg=back,image=grass_g)
    elif e == 58:
        d5.config(bg=back,image=grass_o)
    elif e == 59:
        d5.config(bg=back,image=kelp)
    elif e == 60:
        d5.config(bg=back,image=frame)
    elif e == 61:
        d5.config(bg=back,image=tower)
    elif e == 62:
        d5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][4]
    if e == 0:
        e5.config(bg=back2,image=blank)
    elif e == 1:
        e5.config(bg=back,image=stone)
    elif e == 2:
        e5.config(bg=back,image=sand)
    elif e == 3:
        e5.config(bg=back,image=water)
    elif e == 4:
        e5.config(bg=back,image=dirt)
    elif e == 5:
        e5.config(bg=back,image=log)
    elif e == 6:
        e5.config(bg=back,image=leaves)
    elif e == 7:
        e5.config(bg=back,image=stick)
    elif e == 8:
        e5.config(bg=back,image=bush)
    elif e == 9:
        e5.config(bg=back,image=potato)
    elif e == 10:
        e5.config(bg=back,image=vine)
    elif e == 11:
        e5.config(bg=back,image=coral_red)
    elif e == 12:
        e5.config(bg=back,image=coral_orange)
    elif e == 13:
        e5.config(bg=back,image=coral_green)
    elif e == 14:
        e5.config(bg=back,image=coral_blue)
    elif e == 15:
        e5.config(bg=back,image=space_coral)
    elif e == 16:
        e5.config(bg=back,image=iron_ore)
    elif e == 17:
        e5.config(bg=back,image=copper_ore)
    elif e == 18:
        e5.config(bg=back,image=bone)
    elif e == 19:
        e5.config(bg=back,image=lantern)
    elif e == 20:
        e5.config(bg=back,image=ladder)
    elif e == 21:
        e5.config(bg=back,image=asteroid)
    elif e == 22:
        e5.config(bg=back,image=sea_bricks)
    elif e == 23:
        e5.config(bg=back,image=stone_bricks)
    elif e == 24:
        e5.config(bg=back,image=sea_lantern)
    elif e == 25:
        e5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e5.config(bg=back,image=anvil)
    elif e == 27:
        e5.config(bg=back,image=space)
    elif e == 28:
        e5.config(bg=back,image=seaglass)
    elif e == 29:
        e5.config(bg=back,image=lava)
    elif e == 30:
        e5.config(bg=back,image=treasure)
    elif e == 31:
        e5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e5.config(bg=back,image=turtle_right)
        else:
            e5.config(bg=back,image=turtle_left)
    elif e == 33:
        e5.config(bg=back,image=boar_left)
    elif e == 34:
        e5.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e5.config(bg=back,image=space_fish_right)
            else:
                e5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e5.config(bg=back,image=fish_right)
            else:
                e5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e5.config(bg=back,image=skeleton_attack_left)
        else:
            e5.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e5.config(bg=back,image=skeleton_attack_left)
        else:
            e5.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e5.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e5.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e5.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e5.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e5.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e5.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e5.config(bg=back,image=pirate_attack_left)
        else:
            e5.config(bg=back,image=pirate_left)
    elif e == 42:
        e5.config(bg=back,image=human)
    elif e == 43:
        e5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e5.config(bg=back,image=tent)
    elif e == 47:
        e5.config(bg=back,image=bird)
    elif e == 48:
        e5.config(bg=back,image=spider)
    elif e == 49:
        e5.config(bg=back,image=cloud)
    elif e == 50:
        e5.config(bg=back,image=stem)
    elif e == 51:
        e5.config(bg=back,image=shroom_r)
    elif e == 52:
        e5.config(bg=back,image=shroom_b)
    elif e == 53:
        e5.config(bg=back,image=boat_pirate)
    elif e == 54:
        e5.config(bg=back,image=bullet)
    elif e == 55:
        e5.config(bg=back,image=g_ore)
    elif e == 56:
        e5.config(bg=back,image=book)
    elif e == 57:
        e5.config(bg=back,image=grass_g)
    elif e == 58:
        e5.config(bg=back,image=grass_o)
    elif e == 59:
        e5.config(bg=back,image=kelp)
    elif e == 60:
        e5.config(bg=back,image=frame)
    elif e == 61:
        e5.config(bg=back,image=tower)
    elif e == 62:
        e5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][5]
    if e == 0:
        f5.config(bg=back2,image=blank)
    elif e == 1:
        f5.config(bg=back,image=stone)
    elif e == 2:
        f5.config(bg=back,image=sand)
    elif e == 3:
        f5.config(bg=back,image=water)
    elif e == 4:
        f5.config(bg=back,image=dirt)
    elif e == 5:
        f5.config(bg=back,image=log)
    elif e == 6:
        f5.config(bg=back,image=leaves)
    elif e == 7:
        f5.config(bg=back,image=stick)
    elif e == 8:
        f5.config(bg=back,image=bush)
    elif e == 9:
        f5.config(bg=back,image=potato)
    elif e == 10:
        f5.config(bg=back,image=vine)
    elif e == 11:
        f5.config(bg=back,image=coral_red)
    elif e == 12:
        f5.config(bg=back,image=coral_orange)
    elif e == 13:
        f5.config(bg=back,image=coral_green)
    elif e == 14:
        f5.config(bg=back,image=coral_blue)
    elif e == 15:
        f5.config(bg=back,image=space_coral)
    elif e == 16:
        f5.config(bg=back,image=iron_ore)
    elif e == 17:
        f5.config(bg=back,image=copper_ore)
    elif e == 18:
        f5.config(bg=back,image=bone)
    elif e == 19:
        f5.config(bg=back,image=lantern)
    elif e == 20:
        f5.config(bg=back,image=ladder)
    elif e == 21:
        f5.config(bg=back,image=asteroid)
    elif e == 22:
        f5.config(bg=back,image=sea_bricks)
    elif e == 23:
        f5.config(bg=back,image=stone_bricks)
    elif e == 24:
        f5.config(bg=back,image=sea_lantern)
    elif e == 25:
        f5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f5.config(bg=back,image=anvil)
    elif e == 27:
        f5.config(bg=back,image=space)
    elif e == 28:
        f5.config(bg=back,image=seaglass)
    elif e == 29:
        f5.config(bg=back,image=lava)
    elif e == 30:
        f5.config(bg=back,image=treasure)
    elif e == 31:
        f5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f5.config(bg=back,image=turtle_right)
        else:
            f5.config(bg=back,image=turtle_left)
    elif e == 33:
        f5.config(bg=back,image=boar_left)
    elif e == 34:
        f5.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f5.config(bg=back,image=space_fish_right)
            else:
                f5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f5.config(bg=back,image=fish_right)
            else:
                f5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f5.config(bg=back,image=skeleton_attack_left)
        else:
            f5.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f5.config(bg=back,image=skeleton_attack_left)
        else:
            f5.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f5.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f5.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f5.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f5.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f5.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f5.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f5.config(bg=back,image=pirate_attack_left)
        else:
            f5.config(bg=back,image=pirate_left)
    elif e == 42:
        f5.config(bg=back,image=human)
    elif e == 43:
        f5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f5.config(bg=back,image=tent)
    elif e == 47:
        f5.config(bg=back,image=bird)
    elif e == 48:
        f5.config(bg=back,image=spider)
    elif e == 49:
        f5.config(bg=back,image=cloud)
    elif e == 50:
        f5.config(bg=back,image=stem)
    elif e == 51:
        f5.config(bg=back,image=shroom_r)
    elif e == 52:
        f5.config(bg=back,image=shroom_b)
    elif e == 53:
        f5.config(bg=back,image=boat_pirate)
    elif e == 54:
        f5.config(bg=back,image=bullet)
    elif e == 55:
        f5.config(bg=back,image=g_ore)
    elif e == 56:
        f5.config(bg=back,image=book)
    elif e == 57:
        f5.config(bg=back,image=grass_g)
    elif e == 58:
        f5.config(bg=back,image=grass_o)
    elif e == 59:
        f5.config(bg=back,image=kelp)
    elif e == 60:
        f5.config(bg=back,image=frame)
    elif e == 61:
        f5.config(bg=back,image=tower)
    elif e == 62:
        f5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[4][6]
    if e == 0:
        g5.config(bg=back2,image=blank)
    elif e == 1:
        g5.config(bg=back,image=stone)
    elif e == 2:
        g5.config(bg=back,image=sand)
    elif e == 3:
        g5.config(bg=back,image=water)
    elif e == 4:
        g5.config(bg=back,image=dirt)
    elif e == 5:
        g5.config(bg=back,image=log)
    elif e == 6:
        g5.config(bg=back,image=leaves)
    elif e == 7:
        g5.config(bg=back,image=stick)
    elif e == 8:
        g5.config(bg=back,image=bush)
    elif e == 9:
        g5.config(bg=back,image=potato)
    elif e == 10:
        g5.config(bg=back,image=vine)
    elif e == 11:
        g5.config(bg=back,image=coral_red)
    elif e == 12:
        g5.config(bg=back,image=coral_orange)
    elif e == 13:
        g5.config(bg=back,image=coral_green)
    elif e == 14:
        g5.config(bg=back,image=coral_blue)
    elif e == 15:
        g5.config(bg=back,image=space_coral)
    elif e == 16:
        g5.config(bg=back,image=iron_ore)
    elif e == 17:
        g5.config(bg=back,image=copper_ore)
    elif e == 18:
        g5.config(bg=back,image=bone)
    elif e == 19:
        g5.config(bg=back,image=lantern)
    elif e == 20:
        g5.config(bg=back,image=ladder)
    elif e == 21:
        g5.config(bg=back,image=asteroid)
    elif e == 22:
        g5.config(bg=back,image=sea_bricks)
    elif e == 23:
        g5.config(bg=back,image=stone_bricks)
    elif e == 24:
        g5.config(bg=back,image=sea_lantern)
    elif e == 25:
        g5.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g5.config(bg=back,image=anvil)
    elif e == 27:
        g5.config(bg=back,image=space)
    elif e == 28:
        g5.config(bg=back,image=seaglass)
    elif e == 29:
        g5.config(bg=back,image=lava)
    elif e == 30:
        g5.config(bg=back,image=treasure)
    elif e == 31:
        g5.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g5.config(bg=back,image=turtle_right)
        else:
            g5.config(bg=back,image=turtle_left)
    elif e == 33:
        g5.config(bg=back,image=boar_left)
    elif e == 34:
        g5.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g5.config(bg=back,image=space_fish_right)
            else:
                g5.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g5.config(bg=back,image=fish_right)
            else:
                g5.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g5.config(bg=back,image=skeleton_attack_left)
        else:
            g5.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g5.config(bg=back,image=skeleton_attack_left)
        else:
            g5.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g5.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g5.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g5.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g5.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g5.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g5.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g5.config(bg=back,image=pirate_attack_left)
        else:
            g5.config(bg=back,image=pirate_left)
    elif e == 42:
        g5.config(bg=back,image=human)
    elif e == 43:
        g5.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g5.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g5.config(bg=back,image=tent)
    elif e == 47:
        g5.config(bg=back,image=bird)
    elif e == 48:
        g5.config(bg=back,image=spider)
    elif e == 49:
        g5.config(bg=back,image=cloud)
    elif e == 50:
        g5.config(bg=back,image=stem)
    elif e == 51:
        g5.config(bg=back,image=shroom_r)
    elif e == 52:
        g5.config(bg=back,image=shroom_b)
    elif e == 53:
        g5.config(bg=back,image=boat_pirate)
    elif e == 54:
        g5.config(bg=back,image=bullet)
    elif e == 55:
        g5.config(bg=back,image=g_ore)
    elif e == 56:
        g5.config(bg=back,image=book)
    elif e == 57:
        g5.config(bg=back,image=grass_g)
    elif e == 58:
        g5.config(bg=back,image=grass_o)
    elif e == 59:
        g5.config(bg=back,image=kelp)
    elif e == 60:
        g5.config(bg=back,image=frame)
    elif e == 61:
        g5.config(bg=back,image=tower)
    elif e == 62:
        g5.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][0]
    if e == 0:
        a6.config(bg=back2,image=blank)
    elif e == 1:
        a6.config(bg=back,image=stone)
    elif e == 2:
        a6.config(bg=back,image=sand)
    elif e == 3:
        a6.config(bg=back,image=water)
    elif e == 4:
        a6.config(bg=back,image=dirt)
    elif e == 5:
        a6.config(bg=back,image=log)
    elif e == 6:
        a6.config(bg=back,image=leaves)
    elif e == 7:
        a6.config(bg=back,image=stick)
    elif e == 8:
        a6.config(bg=back,image=bush)
    elif e == 9:
        a6.config(bg=back,image=potato)
    elif e == 10:
        a6.config(bg=back,image=vine)
    elif e == 11:
        a6.config(bg=back,image=coral_red)
    elif e == 12:
        a6.config(bg=back,image=coral_orange)
    elif e == 13:
        a6.config(bg=back,image=coral_green)
    elif e == 14:
        a6.config(bg=back,image=coral_blue)
    elif e == 15:
        a6.config(bg=back,image=space_coral)
    elif e == 16:
        a6.config(bg=back,image=iron_ore)
    elif e == 17:
        a6.config(bg=back,image=copper_ore)
    elif e == 18:
        a6.config(bg=back,image=bone)
    elif e == 19:
        a6.config(bg=back,image=lantern)
    elif e == 20:
        a6.config(bg=back,image=ladder)
    elif e == 21:
        a6.config(bg=back,image=asteroid)
    elif e == 22:
        a6.config(bg=back,image=sea_bricks)
    elif e == 23:
        a6.config(bg=back,image=stone_bricks)
    elif e == 24:
        a6.config(bg=back,image=sea_lantern)
    elif e == 25:
        a6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a6.config(bg=back,image=anvil)
    elif e == 27:
        a6.config(bg=back,image=space)
    elif e == 28:
        a6.config(bg=back,image=seaglass)
    elif e == 29:
        a6.config(bg=back,image=lava)
    elif e == 30:
        a6.config(bg=back,image=treasure)
    elif e == 31:
        a6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a6.config(bg=back,image=turtle_right)
        else:
            a6.config(bg=back,image=turtle_left)
    elif e == 33:
        a6.config(bg=back,image=boar_right)
    elif e == 34:
        a6.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a6.config(bg=back,image=space_fish_right)
            else:
                a6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a6.config(bg=back,image=fish_right)
            else:
                a6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a6.config(bg=back,image=skeleton_attack_right)
        else:
            a6.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a6.config(bg=back,image=skeleton_attack_right)
        else:
            a6.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a6.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a6.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a6.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a6.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a6.config(bg=back,image=pirate_attack_right)
        else:
            a6.config(bg=back,image=pirate_right)
    elif e == 42:
        a6.config(bg=back,image=human)
    elif e == 43:
        a6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a6.config(bg=back,image=tent)
    elif e == 47:
        a6.config(bg=back,image=bird)
    elif e == 48:
        a6.config(bg=back,image=spider)
    elif e == 49:
        a6.config(bg=back,image=cloud)
    elif e == 50:
        a6.config(bg=back,image=stem)
    elif e == 51:
        a6.config(bg=back,image=shroom_r)
    elif e == 52:
        a6.config(bg=back,image=shroom_b)
    elif e == 53:
        a6.config(bg=back,image=boat_pirate)
    elif e == 54:
        a6.config(bg=back,image=bullet)
    elif e == 55:
        a6.config(bg=back,image=g_ore)
    elif e == 56:
        a6.config(bg=back,image=book)
    elif e == 57:
        a6.config(bg=back,image=grass_g)
    elif e == 58:
        a6.config(bg=back,image=grass_o)
    elif e == 59:
        a6.config(bg=back,image=kelp)
    elif e == 60:
        a6.config(bg=back,image=frame)
    elif e == 61:
        a6.config(bg=back,image=tower)
    elif e == 62:
        a6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][1]
    if e == 0:
        b6.config(bg=back2,image=blank)
    elif e == 1:
        b6.config(bg=back,image=stone)
    elif e == 2:
        b6.config(bg=back,image=sand)
    elif e == 3:
        b6.config(bg=back,image=water)
    elif e == 4:
        b6.config(bg=back,image=dirt)
    elif e == 5:
        b6.config(bg=back,image=log)
    elif e == 6:
        b6.config(bg=back,image=leaves)
    elif e == 7:
        b6.config(bg=back,image=stick)
    elif e == 8:
        b6.config(bg=back,image=bush)
    elif e == 9:
        b6.config(bg=back,image=potato)
    elif e == 10:
        b6.config(bg=back,image=vine)
    elif e == 11:
        b6.config(bg=back,image=coral_red)
    elif e == 12:
        b6.config(bg=back,image=coral_orange)
    elif e == 13:
        b6.config(bg=back,image=coral_green)
    elif e == 14:
        b6.config(bg=back,image=coral_blue)
    elif e == 15:
        b6.config(bg=back,image=space_coral)
    elif e == 16:
        b6.config(bg=back,image=iron_ore)
    elif e == 17:
        b6.config(bg=back,image=copper_ore)
    elif e == 18:
        b6.config(bg=back,image=bone)
    elif e == 19:
        b6.config(bg=back,image=lantern)
    elif e == 20:
        b6.config(bg=back,image=ladder)
    elif e == 21:
        b6.config(bg=back,image=asteroid)
    elif e == 22:
        b6.config(bg=back,image=sea_bricks)
    elif e == 23:
        b6.config(bg=back,image=stone_bricks)
    elif e == 24:
        b6.config(bg=back,image=sea_lantern)
    elif e == 25:
        b6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b6.config(bg=back,image=anvil)
    elif e == 27:
        b6.config(bg=back,image=space)
    elif e == 28:
        b6.config(bg=back,image=seaglass)
    elif e == 29:
        b6.config(bg=back,image=lava)
    elif e == 30:
        b6.config(bg=back,image=treasure)
    elif e == 31:
        b6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b6.config(bg=back,image=turtle_right)
        else:
            b6.config(bg=back,image=turtle_left)
    elif e == 33:
        b6.config(bg=back,image=boar_right)
    elif e == 34:
        b6.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b6.config(bg=back,image=space_fish_right)
            else:
                b6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b6.config(bg=back,image=fish_right)
            else:
                b6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b6.config(bg=back,image=skeleton_attack_right)
        else:
            b6.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b6.config(bg=back,image=skeleton_attack_right)
        else:
            b6.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b6.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b6.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b6.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b6.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b6.config(bg=back,image=pirate_attack_right)
        else:
            b6.config(bg=back,image=pirate_right)
    elif e == 42:
        b6.config(bg=back,image=human)
    elif e == 43:
        b6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b6.config(bg=back,image=tent)
    elif e == 47:
        b6.config(bg=back,image=bird)
    elif e == 48:
        b6.config(bg=back,image=spider)
    elif e == 49:
        b6.config(bg=back,image=cloud)
    elif e == 50:
        b6.config(bg=back,image=stem)
    elif e == 51:
        b6.config(bg=back,image=shroom_r)
    elif e == 52:
        b6.config(bg=back,image=shroom_b)
    elif e == 53:
        b6.config(bg=back,image=boat_pirate)
    elif e == 54:
        b6.config(bg=back,image=bullet)
    elif e == 55:
        b6.config(bg=back,image=g_ore)
    elif e == 56:
        b6.config(bg=back,image=book)
    elif e == 57:
        b6.config(bg=back,image=grass_g)
    elif e == 58:
        b6.config(bg=back,image=grass_o)
    elif e == 59:
        b6.config(bg=back,image=kelp)
    elif e == 60:
        b6.config(bg=back,image=frame)
    elif e == 61:
        b6.config(bg=back,image=tower)
    elif e == 62:
        b6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][2]
    if e == 0:
        c6.config(bg=back2,image=blank)
    elif e == 1:
        c6.config(bg=back,image=stone)
    elif e == 2:
        c6.config(bg=back,image=sand)
    elif e == 3:
        c6.config(bg=back,image=water)
    elif e == 4:
        c6.config(bg=back,image=dirt)
    elif e == 5:
        c6.config(bg=back,image=log)
    elif e == 6:
        c6.config(bg=back,image=leaves)
    elif e == 7:
        c6.config(bg=back,image=stick)
    elif e == 8:
        c6.config(bg=back,image=bush)
    elif e == 9:
        c6.config(bg=back,image=potato)
    elif e == 10:
        c6.config(bg=back,image=vine)
    elif e == 11:
        c6.config(bg=back,image=coral_red)
    elif e == 12:
        c6.config(bg=back,image=coral_orange)
    elif e == 13:
        c6.config(bg=back,image=coral_green)
    elif e == 14:
        c6.config(bg=back,image=coral_blue)
    elif e == 15:
        c6.config(bg=back,image=space_coral)
    elif e == 16:
        c6.config(bg=back,image=iron_ore)
    elif e == 17:
        c6.config(bg=back,image=copper_ore)
    elif e == 18:
        c6.config(bg=back,image=bone)
    elif e == 19:
        c6.config(bg=back,image=lantern)
    elif e == 20:
        c6.config(bg=back,image=ladder)
    elif e == 21:
        c6.config(bg=back,image=asteroid)
    elif e == 22:
        c6.config(bg=back,image=sea_bricks)
    elif e == 23:
        c6.config(bg=back,image=stone_bricks)
    elif e == 24:
        c6.config(bg=back,image=sea_lantern)
    elif e == 25:
        c6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c6.config(bg=back,image=anvil)
    elif e == 27:
        c6.config(bg=back,image=space)
    elif e == 28:
        c6.config(bg=back,image=seaglass)
    elif e == 29:
        c6.config(bg=back,image=lava)
    elif e == 30:
        c6.config(bg=back,image=treasure)
    elif e == 31:
        c6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c6.config(bg=back,image=turtle_right)
        else:
            c6.config(bg=back,image=turtle_left)
    elif e == 33:
        c6.config(bg=back,image=boar_right)
    elif e == 34:
        c6.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c6.config(bg=back,image=space_fish_right)
            else:
                c6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c6.config(bg=back,image=fish_right)
            else:
                c6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c6.config(bg=back,image=skeleton_attack_right)
        else:
            c6.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c6.config(bg=back,image=skeleton_attack_right)
        else:
            c6.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c6.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c6.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c6.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c6.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c6.config(bg=back,image=pirate_attack_right)
        else:
            c6.config(bg=back,image=pirate_right)
    elif e == 42:
        c6.config(bg=back,image=human)
    elif e == 43:
        c6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c6.config(bg=back,image=tent)
    elif e == 47:
        c6.config(bg=back,image=bird)
    elif e == 48:
        c6.config(bg=back,image=spider)
    elif e == 49:
        c6.config(bg=back,image=cloud)
    elif e == 50:
        c6.config(bg=back,image=stem)
    elif e == 51:
        c6.config(bg=back,image=shroom_r)
    elif e == 52:
        c6.config(bg=back,image=shroom_b)
    elif e == 53:
        c6.config(bg=back,image=boat_pirate)
    elif e == 54:
        c6.config(bg=back,image=bullet)
    elif e == 55:
        c6.config(bg=back,image=g_ore)
    elif e == 56:
        c6.config(bg=back,image=book)
    elif e == 57:
        c6.config(bg=back,image=grass_g)
    elif e == 58:
        c6.config(bg=back,image=grass_o)
    elif e == 59:
        c6.config(bg=back,image=kelp)
    elif e == 60:
        c6.config(bg=back,image=frame)
    elif e == 61:
        c6.config(bg=back,image=tower)
    elif e == 62:
        c6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][3]
    if e == 0:
        d6.config(bg=back2,image=blank)
    elif e == 1:
        d6.config(bg=back,image=stone)
    elif e == 2:
        d6.config(bg=back,image=sand)
    elif e == 3:
        d6.config(bg=back,image=water)
    elif e == 4:
        d6.config(bg=back,image=dirt)
    elif e == 5:
        d6.config(bg=back,image=log)
    elif e == 6:
        d6.config(bg=back,image=leaves)
    elif e == 7:
        d6.config(bg=back,image=stick)
    elif e == 8:
        d6.config(bg=back,image=bush)
    elif e == 9:
        d6.config(bg=back,image=potato)
    elif e == 10:
        d6.config(bg=back,image=vine)
    elif e == 11:
        d6.config(bg=back,image=coral_red)
    elif e == 12:
        d6.config(bg=back,image=coral_orange)
    elif e == 13:
        d6.config(bg=back,image=coral_green)
    elif e == 14:
        d6.config(bg=back,image=coral_blue)
    elif e == 15:
        d6.config(bg=back,image=space_coral)
    elif e == 16:
        d6.config(bg=back,image=iron_ore)
    elif e == 17:
        d6.config(bg=back,image=copper_ore)
    elif e == 18:
        d6.config(bg=back,image=bone)
    elif e == 19:
        d6.config(bg=back,image=lantern)
    elif e == 20:
        d6.config(bg=back,image=ladder)
    elif e == 21:
        d6.config(bg=back,image=asteroid)
    elif e == 22:
        d6.config(bg=back,image=sea_bricks)
    elif e == 23:
        d6.config(bg=back,image=stone_bricks)
    elif e == 24:
        d6.config(bg=back,image=sea_lantern)
    elif e == 25:
        d6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d6.config(bg=back,image=anvil)
    elif e == 27:
        d6.config(bg=back,image=space)
    elif e == 28:
        d6.config(bg=back,image=seaglass)
    elif e == 29:
        d6.config(bg=back,image=lava)
    elif e == 30:
        d6.config(bg=back,image=treasure)
    elif e == 31:
        d6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d6.config(bg=back,image=turtle_right)
        else:
            d6.config(bg=back,image=turtle_left)
    elif e == 33:
        d6.config(bg=back,image=boar_right)
    elif e == 34:
        d6.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d6.config(bg=back,image=space_fish_right)
            else:
                d6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d6.config(bg=back,image=fish_right)
            else:
                d6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d6.config(bg=back,image=skeleton_attack_right)
        else:
            d6.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d6.config(bg=back,image=skeleton_attack_right)
        else:
            d6.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d6.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d6.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d6.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d6.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d6.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d6.config(bg=back,image=pirate_attack_right)
        else:
            d6.config(bg=back,image=pirate_right)
    elif e == 42:
        d6.config(bg=back,image=human)
    elif e == 43:
        d6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        d6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d6.config(bg=back,image=tent)
    elif e == 47:
        d6.config(bg=back,image=bird)
    elif e == 48:
        d6.config(bg=back,image=spider)
    elif e == 49:
        d6.config(bg=back,image=cloud)
    elif e == 50:
        d6.config(bg=back,image=stem)
    elif e == 51:
        d6.config(bg=back,image=shroom_r)
    elif e == 52:
        d6.config(bg=back,image=shroom_b)
    elif e == 53:
        d6.config(bg=back,image=boat_pirate)
    elif e == 54:
        d6.config(bg=back,image=bullet)
    elif e == 55:
        d6.config(bg=back,image=g_ore)
    elif e == 56:
        d6.config(bg=back,image=book)
    elif e == 57:
        d6.config(bg=back,image=grass_g)
    elif e == 58:
        d6.config(bg=back,image=grass_o)
    elif e == 59:
        d6.config(bg=back,image=kelp)
    elif e == 60:
        d6.config(bg=back,image=frame)
    elif e == 61:
        d6.config(bg=back,image=tower)
    elif e == 62:
        d6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][4]
    if e == 0:
        e6.config(bg=back2,image=blank)
    elif e == 1:
        e6.config(bg=back,image=stone)
    elif e == 2:
        e6.config(bg=back,image=sand)
    elif e == 3:
        e6.config(bg=back,image=water)
    elif e == 4:
        e6.config(bg=back,image=dirt)
    elif e == 5:
        e6.config(bg=back,image=log)
    elif e == 6:
        e6.config(bg=back,image=leaves)
    elif e == 7:
        e6.config(bg=back,image=stick)
    elif e == 8:
        e6.config(bg=back,image=bush)
    elif e == 9:
        e6.config(bg=back,image=potato)
    elif e == 10:
        e6.config(bg=back,image=vine)
    elif e == 11:
        e6.config(bg=back,image=coral_red)
    elif e == 12:
        e6.config(bg=back,image=coral_orange)
    elif e == 13:
        e6.config(bg=back,image=coral_green)
    elif e == 14:
        e6.config(bg=back,image=coral_blue)
    elif e == 15:
        e6.config(bg=back,image=space_coral)
    elif e == 16:
        e6.config(bg=back,image=iron_ore)
    elif e == 17:
        e6.config(bg=back,image=copper_ore)
    elif e == 18:
        e6.config(bg=back,image=bone)
    elif e == 19:
        e6.config(bg=back,image=lantern)
    elif e == 20:
        e6.config(bg=back,image=ladder)
    elif e == 21:
        e6.config(bg=back,image=asteroid)
    elif e == 22:
        e6.config(bg=back,image=sea_bricks)
    elif e == 23:
        e6.config(bg=back,image=stone_bricks)
    elif e == 24:
        e6.config(bg=back,image=sea_lantern)
    elif e == 25:
        e6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e6.config(bg=back,image=anvil)
    elif e == 27:
        e6.config(bg=back,image=space)
    elif e == 28:
        e6.config(bg=back,image=seaglass)
    elif e == 29:
        e6.config(bg=back,image=lava)
    elif e == 30:
        e6.config(bg=back,image=treasure)
    elif e == 31:
        e6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e6.config(bg=back,image=turtle_right)
        else:
            e6.config(bg=back,image=turtle_left)
    elif e == 33:
        e6.config(bg=back,image=boar_left)
    elif e == 34:
        e6.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e6.config(bg=back,image=space_fish_right)
            else:
                e6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e6.config(bg=back,image=fish_right)
            else:
                e6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e6.config(bg=back,image=skeleton_attack_left)
        else:
            e6.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e6.config(bg=back,image=skeleton_attack_left)
        else:
            e6.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e6.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e6.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e6.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e6.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e6.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e6.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e6.config(bg=back,image=pirate_attack_left)
        else:
            e6.config(bg=back,image=pirate_left)
    elif e == 42:
        e6.config(bg=back,image=human)
    elif e == 43:
        e6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e6.config(bg=back,image=tent)
    elif e == 47:
        e6.config(bg=back,image=bird)
    elif e == 48:
        e6.config(bg=back,image=spider)
    elif e == 49:
        e6.config(bg=back,image=cloud)
    elif e == 50:
        e6.config(bg=back,image=stem)
    elif e == 51:
        e6.config(bg=back,image=shroom_r)
    elif e == 52:
        e6.config(bg=back,image=shroom_b)
    elif e == 53:
        e6.config(bg=back,image=boat_pirate)
    elif e == 54:
        e6.config(bg=back,image=bullet)
    elif e == 55:
        e6.config(bg=back,image=g_ore)
    elif e == 56:
        e6.config(bg=back,image=book)
    elif e == 57:
        e6.config(bg=back,image=grass_g)
    elif e == 58:
        e6.config(bg=back,image=grass_o)
    elif e == 59:
        e6.config(bg=back,image=kelp)
    elif e == 60:
        e6.config(bg=back,image=frame)
    elif e == 61:
        e6.config(bg=back,image=tower)
    elif e == 62:
        e6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][5]
    if e == 0:
        f6.config(bg=back2,image=blank)
    elif e == 1:
        f6.config(bg=back,image=stone)
    elif e == 2:
        f6.config(bg=back,image=sand)
    elif e == 3:
        f6.config(bg=back,image=water)
    elif e == 4:
        f6.config(bg=back,image=dirt)
    elif e == 5:
        f6.config(bg=back,image=log)
    elif e == 6:
        f6.config(bg=back,image=leaves)
    elif e == 7:
        f6.config(bg=back,image=stick)
    elif e == 8:
        f6.config(bg=back,image=bush)
    elif e == 9:
        f6.config(bg=back,image=potato)
    elif e == 10:
        f6.config(bg=back,image=vine)
    elif e == 11:
        f6.config(bg=back,image=coral_red)
    elif e == 12:
        f6.config(bg=back,image=coral_orange)
    elif e == 13:
        f6.config(bg=back,image=coral_green)
    elif e == 14:
        f6.config(bg=back,image=coral_blue)
    elif e == 15:
        f6.config(bg=back,image=space_coral)
    elif e == 16:
        f6.config(bg=back,image=iron_ore)
    elif e == 17:
        f6.config(bg=back,image=copper_ore)
    elif e == 18:
        f6.config(bg=back,image=bone)
    elif e == 19:
        f6.config(bg=back,image=lantern)
    elif e == 20:
        f6.config(bg=back,image=ladder)
    elif e == 21:
        f6.config(bg=back,image=asteroid)
    elif e == 22:
        f6.config(bg=back,image=sea_bricks)
    elif e == 23:
        f6.config(bg=back,image=stone_bricks)
    elif e == 24:
        f6.config(bg=back,image=sea_lantern)
    elif e == 25:
        f6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f6.config(bg=back,image=anvil)
    elif e == 27:
        f6.config(bg=back,image=space)
    elif e == 28:
        f6.config(bg=back,image=seaglass)
    elif e == 29:
        f6.config(bg=back,image=lava)
    elif e == 30:
        f6.config(bg=back,image=treasure)
    elif e == 31:
        f6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f6.config(bg=back,image=turtle_right)
        else:
            f6.config(bg=back,image=turtle_left)
    elif e == 33:
        f6.config(bg=back,image=boar_left)
    elif e == 34:
        f6.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f6.config(bg=back,image=space_fish_right)
            else:
                f6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f6.config(bg=back,image=fish_right)
            else:
                f6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f6.config(bg=back,image=skeleton_attack_left)
        else:
            f6.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f6.config(bg=back,image=skeleton_attack_left)
        else:
            f6.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f6.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f6.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f6.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f6.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f6.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f6.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f6.config(bg=back,image=pirate_attack_left)
        else:
            f6.config(bg=back,image=pirate_left)
    elif e == 42:
        f6.config(bg=back,image=human)
    elif e == 43:
        f6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f6.config(bg=back,image=tent)
    elif e == 47:
        f6.config(bg=back,image=bird)
    elif e == 48:
        f6.config(bg=back,image=spider)
    elif e == 49:
        f6.config(bg=back,image=cloud)
    elif e == 50:
        f6.config(bg=back,image=stem)
    elif e == 51:
        f6.config(bg=back,image=shroom_r)
    elif e == 52:
        f6.config(bg=back,image=shroom_b)
    elif e == 53:
        f6.config(bg=back,image=boat_pirate)
    elif e == 54:
        f6.config(bg=back,image=bullet)
    elif e == 55:
        f6.config(bg=back,image=g_ore)
    elif e == 56:
        f6.config(bg=back,image=book)
    elif e == 57:
        f6.config(bg=back,image=grass_g)
    elif e == 58:
        f6.config(bg=back,image=grass_o)
    elif e == 59:
        f6.config(bg=back,image=kelp)
    elif e == 60:
        f6.config(bg=back,image=frame)
    elif e == 61:
        f6.config(bg=back,image=tower)
    elif e == 62:
        f6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[5][6]
    if e == 0:
        g6.config(bg=back2,image=blank)
    elif e == 1:
        g6.config(bg=back,image=stone)
    elif e == 2:
        g6.config(bg=back,image=sand)
    elif e == 3:
        g6.config(bg=back,image=water)
    elif e == 4:
        g6.config(bg=back,image=dirt)
    elif e == 5:
        g6.config(bg=back,image=log)
    elif e == 6:
        g6.config(bg=back,image=leaves)
    elif e == 7:
        g6.config(bg=back,image=stick)
    elif e == 8:
        g6.config(bg=back,image=bush)
    elif e == 9:
        g6.config(bg=back,image=potato)
    elif e == 10:
        g6.config(bg=back,image=vine)
    elif e == 11:
        g6.config(bg=back,image=coral_red)
    elif e == 12:
        g6.config(bg=back,image=coral_orange)
    elif e == 13:
        g6.config(bg=back,image=coral_green)
    elif e == 14:
        g6.config(bg=back,image=coral_blue)
    elif e == 15:
        g6.config(bg=back,image=space_coral)
    elif e == 16:
        g6.config(bg=back,image=iron_ore)
    elif e == 17:
        g6.config(bg=back,image=copper_ore)
    elif e == 18:
        g6.config(bg=back,image=bone)
    elif e == 19:
        g6.config(bg=back,image=lantern)
    elif e == 20:
        g6.config(bg=back,image=ladder)
    elif e == 21:
        g6.config(bg=back,image=asteroid)
    elif e == 22:
        g6.config(bg=back,image=sea_bricks)
    elif e == 23:
        g6.config(bg=back,image=stone_bricks)
    elif e == 24:
        g6.config(bg=back,image=sea_lantern)
    elif e == 25:
        g6.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g6.config(bg=back,image=anvil)
    elif e == 27:
        g6.config(bg=back,image=space)
    elif e == 28:
        g6.config(bg=back,image=seaglass)
    elif e == 29:
        g6.config(bg=back,image=lava)
    elif e == 30:
        g6.config(bg=back,image=treasure)
    elif e == 31:
        g6.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g6.config(bg=back,image=turtle_right)
        else:
            g6.config(bg=back,image=turtle_left)
    elif e == 33:
        g6.config(bg=back,image=boar_left)
    elif e == 34:
        g6.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g6.config(bg=back,image=space_fish_right)
            else:
                g6.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g6.config(bg=back,image=fish_right)
            else:
                g6.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g6.config(bg=back,image=skeleton_attack_left)
        else:
            g6.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g6.config(bg=back,image=skeleton_attack_left)
        else:
            g6.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g6.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g6.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g6.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g6.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g6.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g6.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g6.config(bg=back,image=pirate_attack_left)
        else:
            g6.config(bg=back,image=pirate_left)
    elif e == 42:
        g6.config(bg=back,image=human)
    elif e == 43:
        g6.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g6.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g6.config(bg=back,image=tent)
    elif e == 47:
        g6.config(bg=back,image=bird)
    elif e == 48:
        g6.config(bg=back,image=spider)
    elif e == 49:
        g6.config(bg=back,image=cloud)
    elif e == 50:
        g6.config(bg=back,image=stem)
    elif e == 51:
        g6.config(bg=back,image=shroom_r)
    elif e == 52:
        g6.config(bg=back,image=shroom_b)
    elif e == 53:
        g6.config(bg=back,image=boat_pirate)
    elif e == 54:
        g6.config(bg=back,image=bullet)
    elif e == 55:
        g6.config(bg=back,image=g_ore)
    elif e == 56:
        g6.config(bg=back,image=book)
    elif e == 57:
        g6.config(bg=back,image=grass_g)
    elif e == 58:
        g6.config(bg=back,image=grass_o)
    elif e == 59:
        g6.config(bg=back,image=kelp)
    elif e == 60:
        g6.config(bg=back,image=frame)
    elif e == 61:
        g6.config(bg=back,image=tower)
    elif e == 62:
        g6.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][0]
    if e == 0:
        a7.config(bg=back2,image=blank)
    elif e == 1:
        a7.config(bg=back,image=stone)
    elif e == 2:
        a7.config(bg=back,image=sand)
    elif e == 3:
        a7.config(bg=back,image=water)
    elif e == 4:
        a7.config(bg=back,image=dirt)
    elif e == 5:
        a7.config(bg=back,image=log)
    elif e == 6:
        a7.config(bg=back,image=leaves)
    elif e == 7:
        a7.config(bg=back,image=stick)
    elif e == 8:
        a7.config(bg=back,image=bush)
    elif e == 9:
        a7.config(bg=back,image=potato)
    elif e == 10:
        a7.config(bg=back,image=vine)
    elif e == 11:
        a7.config(bg=back,image=coral_red)
    elif e == 12:
        a7.config(bg=back,image=coral_orange)
    elif e == 13:
        a7.config(bg=back,image=coral_green)
    elif e == 14:
        a7.config(bg=back,image=coral_blue)
    elif e == 15:
        a7.config(bg=back,image=space_coral)
    elif e == 16:
        a7.config(bg=back,image=iron_ore)
    elif e == 17:
        a7.config(bg=back,image=copper_ore)
    elif e == 18:
        a7.config(bg=back,image=bone)
    elif e == 19:
        a7.config(bg=back,image=lantern)
    elif e == 20:
        a7.config(bg=back,image=ladder)
    elif e == 21:
        a7.config(bg=back,image=asteroid)
    elif e == 22:
        a7.config(bg=back,image=sea_bricks)
    elif e == 23:
        a7.config(bg=back,image=stone_bricks)
    elif e == 24:
        a7.config(bg=back,image=sea_lantern)
    elif e == 25:
        a7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        a7.config(bg=back,image=anvil)
    elif e == 27:
        a7.config(bg=back,image=space)
    elif e == 28:
        a7.config(bg=back,image=seaglass)
    elif e == 29:
        a7.config(bg=back,image=lava)
    elif e == 30:
        a7.config(bg=back,image=treasure)
    elif e == 31:
        a7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            a7.config(bg=back,image=turtle_right)
        else:
            a7.config(bg=back,image=turtle_left)
    elif e == 33:
        a7.config(bg=back,image=boar_right)
    elif e == 34:
        a7.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                a7.config(bg=back,image=space_fish_right)
            else:
                a7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                a7.config(bg=back,image=fish_right)
            else:
                a7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            a7.config(bg=back,image=skeleton_attack_right)
        else:
            a7.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            a7.config(bg=back,image=skeleton_attack_right)
        else:
            a7.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            a7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a7.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            a7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            a7.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            a7.config(bg=back,image=bone_skeleton_attack_right)
        else:
            a7.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            a7.config(bg=back,image=pirate_attack_right)
        else:
            a7.config(bg=back,image=pirate_right)
    elif e == 42:
        a7.config(bg=back,image=human)
    elif e == 43:
        a7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        a7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        a7.config(bg=back,image=tent)
    elif e == 47:
        a7.config(bg=back,image=bird)
    elif e == 48:
        a7.config(bg=back,image=spider)
    elif e == 49:
        a7.config(bg=back,image=cloud)
    elif e == 50:
        a7.config(bg=back,image=stem)
    elif e == 51:
        a7.config(bg=back,image=shroom_r)
    elif e == 52:
        a7.config(bg=back,image=shroom_b)
    elif e == 53:
        a7.config(bg=back,image=boat_pirate)
    elif e == 54:
        a7.config(bg=back,image=bullet)
    elif e == 55:
        a7.config(bg=back,image=g_ore)
    elif e == 56:
        a7.config(bg=back,image=book)
    elif e == 57:
        a7.config(bg=back,image=grass_g)
    elif e == 58:
        a7.config(bg=back,image=grass_o)
    elif e == 59:
        a7.config(bg=back,image=kelp)
    elif e == 60:
        a7.config(bg=back,image=frame)
    elif e == 61:
        a7.config(bg=back,image=tower)
    elif e == 62:
        a7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][1]
    if e == 0:
        b7.config(bg=back2,image=blank)
    elif e == 1:
        b7.config(bg=back,image=stone)
    elif e == 2:
        b7.config(bg=back,image=sand)
    elif e == 3:
        b7.config(bg=back,image=water)
    elif e == 4:
        b7.config(bg=back,image=dirt)
    elif e == 5:
        b7.config(bg=back,image=log)
    elif e == 6:
        b7.config(bg=back,image=leaves)
    elif e == 7:
        b7.config(bg=back,image=stick)
    elif e == 8:
        b7.config(bg=back,image=bush)
    elif e == 9:
        b7.config(bg=back,image=potato)
    elif e == 10:
        b7.config(bg=back,image=vine)
    elif e == 11:
        b7.config(bg=back,image=coral_red)
    elif e == 12:
        b7.config(bg=back,image=coral_orange)
    elif e == 13:
        b7.config(bg=back,image=coral_green)
    elif e == 14:
        b7.config(bg=back,image=coral_blue)
    elif e == 15:
        b7.config(bg=back,image=space_coral)
    elif e == 16:
        b7.config(bg=back,image=iron_ore)
    elif e == 17:
        b7.config(bg=back,image=copper_ore)
    elif e == 18:
        b7.config(bg=back,image=bone)
    elif e == 19:
        b7.config(bg=back,image=lantern)
    elif e == 20:
        b7.config(bg=back,image=ladder)
    elif e == 21:
        b7.config(bg=back,image=asteroid)
    elif e == 22:
        b7.config(bg=back,image=sea_bricks)
    elif e == 23:
        b7.config(bg=back,image=stone_bricks)
    elif e == 24:
        b7.config(bg=back,image=sea_lantern)
    elif e == 25:
        b7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        b7.config(bg=back,image=anvil)
    elif e == 27:
        b7.config(bg=back,image=space)
    elif e == 28:
        b7.config(bg=back,image=seaglass)
    elif e == 29:
        b7.config(bg=back,image=lava)
    elif e == 30:
        b7.config(bg=back,image=treasure)
    elif e == 31:
        b7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            b7.config(bg=back,image=turtle_right)
        else:
            b7.config(bg=back,image=turtle_left)
    elif e == 33:
        b7.config(bg=back,image=boar_right)
    elif e == 34:
        b7.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                b7.config(bg=back,image=space_fish_right)
            else:
                b7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                b7.config(bg=back,image=fish_right)
            else:
                b7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            b7.config(bg=back,image=skeleton_attack_right)
        else:
            b7.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            b7.config(bg=back,image=skeleton_attack_right)
        else:
            b7.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            b7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b7.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            b7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            b7.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            b7.config(bg=back,image=bone_skeleton_attack_right)
        else:
            b7.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            b7.config(bg=back,image=pirate_attack_right)
        else:
            b7.config(bg=back,image=pirate_right)
    elif e == 42:
        b7.config(bg=back,image=human)
    elif e == 43:
        b7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        b7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        b7.config(bg=back,image=tent)
    elif e == 47:
        b7.config(bg=back,image=bird)
    elif e == 48:
        b7.config(bg=back,image=spider)
    elif e == 49:
        b7.config(bg=back,image=cloud)
    elif e == 50:
        b7.config(bg=back,image=stem)
    elif e == 51:
        b7.config(bg=back,image=shroom_r)
    elif e == 52:
        b7.config(bg=back,image=shroom_b)
    elif e == 53:
        b7.config(bg=back,image=boat_pirate)
    elif e == 54:
        b7.config(bg=back,image=bullet)
    elif e == 55:
        b7.config(bg=back,image=g_ore)
    elif e == 56:
        b7.config(bg=back,image=book)
    elif e == 57:
        b7.config(bg=back,image=grass_g)
    elif e == 58:
        b7.config(bg=back,image=grass_o)
    elif e == 59:
        b7.config(bg=back,image=kelp)
    elif e == 60:
        b7.config(bg=back,image=frame)
    elif e == 61:
        b7.config(bg=back,image=tower)
    elif e == 62:
        b7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][2]
    if e == 0:
        c7.config(bg=back2,image=blank)
    elif e == 1:
        c7.config(bg=back,image=stone)
    elif e == 2:
        c7.config(bg=back,image=sand)
    elif e == 3:
        c7.config(bg=back,image=water)
    elif e == 4:
        c7.config(bg=back,image=dirt)
    elif e == 5:
        c7.config(bg=back,image=log)
    elif e == 6:
        c7.config(bg=back,image=leaves)
    elif e == 7:
        c7.config(bg=back,image=stick)
    elif e == 8:
        c7.config(bg=back,image=bush)
    elif e == 9:
        c7.config(bg=back,image=potato)
    elif e == 10:
        c7.config(bg=back,image=vine)
    elif e == 11:
        c7.config(bg=back,image=coral_red)
    elif e == 12:
        c7.config(bg=back,image=coral_orange)
    elif e == 13:
        c7.config(bg=back,image=coral_green)
    elif e == 14:
        c7.config(bg=back,image=coral_blue)
    elif e == 15:
        c7.config(bg=back,image=space_coral)
    elif e == 16:
        c7.config(bg=back,image=iron_ore)
    elif e == 17:
        c7.config(bg=back,image=copper_ore)
    elif e == 18:
        c7.config(bg=back,image=bone)
    elif e == 19:
        c7.config(bg=back,image=lantern)
    elif e == 20:
        c7.config(bg=back,image=ladder)
    elif e == 21:
        c7.config(bg=back,image=asteroid)
    elif e == 22:
        c7.config(bg=back,image=sea_bricks)
    elif e == 23:
        c7.config(bg=back,image=stone_bricks)
    elif e == 24:
        c7.config(bg=back,image=sea_lantern)
    elif e == 25:
        c7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        c7.config(bg=back,image=anvil)
    elif e == 27:
        c7.config(bg=back,image=space)
    elif e == 28:
        c7.config(bg=back,image=seaglass)
    elif e == 29:
        c7.config(bg=back,image=lava)
    elif e == 30:
        c7.config(bg=back,image=treasure)
    elif e == 31:
        c7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            c7.config(bg=back,image=turtle_right)
        else:
            c7.config(bg=back,image=turtle_left)
    elif e == 33:
        c7.config(bg=back,image=boar_right)
    elif e == 34:
        c7.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                c7.config(bg=back,image=space_fish_right)
            else:
                c7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                c7.config(bg=back,image=fish_right)
            else:
                c7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            c7.config(bg=back,image=skeleton_attack_right)
        else:
            c7.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            c7.config(bg=back,image=skeleton_attack_right)
        else:
            c7.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            c7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c7.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            c7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            c7.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            c7.config(bg=back,image=bone_skeleton_attack_right)
        else:
            c7.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            c7.config(bg=back,image=pirate_attack_right)
        else:
            c7.config(bg=back,image=pirate_right)
    elif e == 42:
        c7.config(bg=back,image=human)
    elif e == 43:
        c7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        c7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        c7.config(bg=back,image=tent)
    elif e == 47:
        c7.config(bg=back,image=bird)
    elif e == 48:
        c7.config(bg=back,image=spider)
    elif e == 49:
        c7.config(bg=back,image=cloud)
    elif e == 50:
        c7.config(bg=back,image=stem)
    elif e == 51:
        c7.config(bg=back,image=shroom_r)
    elif e == 52:
        c7.config(bg=back,image=shroom_b)
    elif e == 53:
        c7.config(bg=back,image=boat_pirate)
    elif e == 54:
        c7.config(bg=back,image=bullet)
    elif e == 55:
        c7.config(bg=back,image=g_ore)
    elif e == 56:
        c7.config(bg=back,image=book)
    elif e == 57:
        c7.config(bg=back,image=grass_g)
    elif e == 58:
        c7.config(bg=back,image=grass_o)
    elif e == 59:
        c7.config(bg=back,image=kelp)
    elif e == 60:
        c7.config(bg=back,image=frame)
    elif e == 61:
        c7.config(bg=back,image=tower)
    elif e == 62:
        c7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][3]
    if e == 0:
        d7.config(bg=back2,image=blank)
    elif e == 1:
        d7.config(bg=back,image=stone)
    elif e == 2:
        d7.config(bg=back,image=sand)
    elif e == 3:
        d7.config(bg=back,image=water)
    elif e == 4:
        d7.config(bg=back,image=dirt)
    elif e == 5:
        d7.config(bg=back,image=log)
    elif e == 6:
        d7.config(bg=back,image=leaves)
    elif e == 7:
        d7.config(bg=back,image=stick)
    elif e == 8:
        d7.config(bg=back,image=bush)
    elif e == 9:
        d7.config(bg=back,image=potato)
    elif e == 10:
        d7.config(bg=back,image=vine)
    elif e == 11:
        d7.config(bg=back,image=coral_red)
    elif e == 12:
        d7.config(bg=back,image=coral_orange)
    elif e == 13:
        d7.config(bg=back,image=coral_green)
    elif e == 14:
        d7.config(bg=back,image=coral_blue)
    elif e == 15:
        d7.config(bg=back,image=space_coral)
    elif e == 16:
        d7.config(bg=back,image=iron_ore)
    elif e == 17:
        d7.config(bg=back,image=copper_ore)
    elif e == 18:
        d7.config(bg=back,image=bone)
    elif e == 19:
        d7.config(bg=back,image=lantern)
    elif e == 20:
        d7.config(bg=back,image=ladder)
    elif e == 21:
        d7.config(bg=back,image=asteroid)
    elif e == 22:
        d7.config(bg=back,image=sea_bricks)
    elif e == 23:
        d7.config(bg=back,image=stone_bricks)
    elif e == 24:
        d7.config(bg=back,image=sea_lantern)
    elif e == 25:
        d7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        d7.config(bg=back,image=anvil)
    elif e == 27:
        d7.config(bg=back,image=space)
    elif e == 28:
        d7.config(bg=back,image=seaglass)
    elif e == 29:
        d7.config(bg=back,image=lava)
    elif e == 30:
        d7.config(bg=back,image=treasure)
    elif e == 31:
        d7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            d7.config(bg=back,image=turtle_right)
        else:
            d7.config(bg=back,image=turtle_left)
    elif e == 33:
        d7.config(bg=back,image=boar_right)
    elif e == 34:
        d7.config(bg=back,image=boar_right)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                d7.config(bg=back,image=space_fish_right)
            else:
                d7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                d7.config(bg=back,image=fish_right)
            else:
                d7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            d7.config(bg=back,image=skeleton_attack_right)
        else:
            d7.config(bg=back,image=skeleton_right)
    elif e == 37:
        if skeleton2_att == True:
            d7.config(bg=back,image=skeleton_attack_right)
        else:
            d7.config(bg=back,image=skeleton_right)
    elif e == 38:
        if skeleton_l1_att == True:
            d7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d7.config(bg=back,image=leather_skeleton_right)
    elif e == 39:
        if skeleton_l2_att == True:
            d7.config(bg=back,image=leather_skeleton_attack_right)
        else:
            d7.config(bg=back,image=leather_skeleton_right)
    elif e == 40:
        if skeleton_i_att == True:
            d7.config(bg=back,image=bone_skeleton_attack_right)
        else:
            d7.config(bg=back,image=bone_skeleton_right)
    elif e == 41:
        if skeleton2_att == True:
            d7.config(bg=back,image=pirate_attack_right)
        else:
            d7.config(bg=back,image=pirate_right)
    elif e == 42:
        d7.config(bg=back,image=human)
    elif e == 43:
        d7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        d7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        d7.config(bg=back,image=tent)
    elif e == 47:
        d7.config(bg=back,image=bird)
    elif e == 48:
        d7.config(bg=back,image=spider)
    elif e == 49:
        d7.config(bg=back,image=cloud)
    elif e == 50:
        d7.config(bg=back,image=stem)
    elif e == 51:
        d7.config(bg=back,image=shroom_r)
    elif e == 52:
        d7.config(bg=back,image=shroom_b)
    elif e == 53:
        d7.config(bg=back,image=boat_pirate)
    elif e == 54:
        d7.config(bg=back,image=bullet)
    elif e == 55:
        d7.config(bg=back,image=g_ore)
    elif e == 56:
        d7.config(bg=back,image=book)
    elif e == 57:
        d7.config(bg=back,image=grass_g)
    elif e == 58:
        d7.config(bg=back,image=grass_o)
    elif e == 59:
        d7.config(bg=back,image=kelp)
    elif e == 60:
        d7.config(bg=back,image=frame)
    elif e == 61:
        d7.config(bg=back,image=tower)
    elif e == 62:
        d7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][4]
    if e == 0:
        e7.config(bg=back2,image=blank)
    elif e == 1:
        e7.config(bg=back,image=stone)
    elif e == 2:
        e7.config(bg=back,image=sand)
    elif e == 3:
        e7.config(bg=back,image=water)
    elif e == 4:
        e7.config(bg=back,image=dirt)
    elif e == 5:
        e7.config(bg=back,image=log)
    elif e == 6:
        e7.config(bg=back,image=leaves)
    elif e == 7:
        e7.config(bg=back,image=stick)
    elif e == 8:
        e7.config(bg=back,image=bush)
    elif e == 9:
        e7.config(bg=back,image=potato)
    elif e == 10:
        e7.config(bg=back,image=vine)
    elif e == 11:
        e7.config(bg=back,image=coral_red)
    elif e == 12:
        e7.config(bg=back,image=coral_orange)
    elif e == 13:
        e7.config(bg=back,image=coral_green)
    elif e == 14:
        e7.config(bg=back,image=coral_blue)
    elif e == 15:
        e7.config(bg=back,image=space_coral)
    elif e == 16:
        e7.config(bg=back,image=iron_ore)
    elif e == 17:
        e7.config(bg=back,image=copper_ore)
    elif e == 18:
        e7.config(bg=back,image=bone)
    elif e == 19:
        e7.config(bg=back,image=lantern)
    elif e == 20:
        e7.config(bg=back,image=ladder)
    elif e == 21:
        e7.config(bg=back,image=asteroid)
    elif e == 22:
        e7.config(bg=back,image=sea_bricks)
    elif e == 23:
        e7.config(bg=back,image=stone_bricks)
    elif e == 24:
        e7.config(bg=back,image=sea_lantern)
    elif e == 25:
        e7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        e7.config(bg=back,image=anvil)
    elif e == 27:
        e7.config(bg=back,image=space)
    elif e == 28:
        e7.config(bg=back,image=seaglass)
    elif e == 29:
        e7.config(bg=back,image=lava)
    elif e == 30:
        e7.config(bg=back,image=treasure)
    elif e == 31:
        e7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            e7.config(bg=back,image=turtle_right)
        else:
            e7.config(bg=back,image=turtle_left)
    elif e == 33:
        e7.config(bg=back,image=boar_left)
    elif e == 34:
        e7.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                e7.config(bg=back,image=space_fish_right)
            else:
                e7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                e7.config(bg=back,image=fish_right)
            else:
                e7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            e7.config(bg=back,image=skeleton_attack_left)
        else:
            e7.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            e7.config(bg=back,image=skeleton_attack_left)
        else:
            e7.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            e7.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e7.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            e7.config(bg=back,image=leather_skeleton_attack_left)
        else:
            e7.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            e7.config(bg=back,image=bone_skeleton_attack_left)
        else:
            e7.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            e7.config(bg=back,image=pirate_attack_left)
        else:
            e7.config(bg=back,image=pirate_left)
    elif e == 42:
        e7.config(bg=back,image=human)
    elif e == 43:
        e7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        e7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        e7.config(bg=back,image=tent)
    elif e == 47:
        e7.config(bg=back,image=bird)
    elif e == 48:
        e7.config(bg=back,image=spider)
    elif e == 49:
        e7.config(bg=back,image=cloud)
    elif e == 50:
        e7.config(bg=back,image=stem)
    elif e == 51:
        e7.config(bg=back,image=shroom_r)
    elif e == 52:
        e7.config(bg=back,image=shroom_b)
    elif e == 53:
        e7.config(bg=back,image=boat_pirate)
    elif e == 54:
        e7.config(bg=back,image=bullet)
    elif e == 55:
        e7.config(bg=back,image=g_ore)
    elif e == 56:
        e7.config(bg=back,image=book)
    elif e == 57:
        e7.config(bg=back,image=grass_g)
    elif e == 58:
        e7.config(bg=back,image=grass_o)
    elif e == 59:
        e7.config(bg=back,image=kelp)
    elif e == 60:
        e7.config(bg=back,image=frame)
    elif e == 61:
        e7.config(bg=back,image=tower)
    elif e == 62:
        e7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][5]
    if e == 0:
        f7.config(bg=back2,image=blank)
    elif e == 1:
        f7.config(bg=back,image=stone)
    elif e == 2:
        f7.config(bg=back,image=sand)
    elif e == 3:
        f7.config(bg=back,image=water)
    elif e == 4:
        f7.config(bg=back,image=dirt)
    elif e == 5:
        f7.config(bg=back,image=log)
    elif e == 6:
        f7.config(bg=back,image=leaves)
    elif e == 7:
        f7.config(bg=back,image=stick)
    elif e == 8:
        f7.config(bg=back,image=bush)
    elif e == 9:
        f7.config(bg=back,image=potato)
    elif e == 10:
        f7.config(bg=back,image=vine)
    elif e == 11:
        f7.config(bg=back,image=coral_red)
    elif e == 12:
        f7.config(bg=back,image=coral_orange)
    elif e == 13:
        f7.config(bg=back,image=coral_green)
    elif e == 14:
        f7.config(bg=back,image=coral_blue)
    elif e == 15:
        f7.config(bg=back,image=space_coral)
    elif e == 16:
        f7.config(bg=back,image=iron_ore)
    elif e == 17:
        f7.config(bg=back,image=copper_ore)
    elif e == 18:
        f7.config(bg=back,image=bone)
    elif e == 19:
        f7.config(bg=back,image=lantern)
    elif e == 20:
        f7.config(bg=back,image=ladder)
    elif e == 21:
        f7.config(bg=back,image=asteroid)
    elif e == 22:
        f7.config(bg=back,image=sea_bricks)
    elif e == 23:
        f7.config(bg=back,image=stone_bricks)
    elif e == 24:
        f7.config(bg=back,image=sea_lantern)
    elif e == 25:
        f7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        f7.config(bg=back,image=anvil)
    elif e == 27:
        f7.config(bg=back,image=space)
    elif e == 28:
        f7.config(bg=back,image=seaglass)
    elif e == 29:
        f7.config(bg=back,image=lava)
    elif e == 30:
        f7.config(bg=back,image=treasure)
    elif e == 31:
        f7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            f7.config(bg=back,image=turtle_right)
        else:
            f7.config(bg=back,image=turtle_left)
    elif e == 33:
        f7.config(bg=back,image=boar_left)
    elif e == 34:
        f7.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                f7.config(bg=back,image=space_fish_right)
            else:
                f7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                f7.config(bg=back,image=fish_right)
            else:
                f7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            f7.config(bg=back,image=skeleton_attack_left)
        else:
            f7.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            f7.config(bg=back,image=skeleton_attack_left)
        else:
            f7.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            f7.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f7.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            f7.config(bg=back,image=leather_skeleton_attack_left)
        else:
            f7.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            f7.config(bg=back,image=bone_skeleton_attack_left)
        else:
            f7.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            f7.config(bg=back,image=pirate_attack_left)
        else:
            f7.config(bg=back,image=pirate_left)
    elif e == 42:
        f7.config(bg=back,image=human)
    elif e == 43:
        f7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        f7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        f7.config(bg=back,image=tent)
    elif e == 47:
        f7.config(bg=back,image=bird)
    elif e == 48:
        f7.config(bg=back,image=spider)
    elif e == 49:
        f7.config(bg=back,image=cloud)
    elif e == 50:
        f7.config(bg=back,image=stem)
    elif e == 51:
        f7.config(bg=back,image=shroom_r)
    elif e == 52:
        f7.config(bg=back,image=shroom_b)
    elif e == 53:
        f7.config(bg=back,image=boat_pirate)
    elif e == 54:
        f7.config(bg=back,image=bullet)
    elif e == 55:
        f7.config(bg=back,image=g_ore)
    elif e == 56:
        f7.config(bg=back,image=book)
    elif e == 57:
        f7.config(bg=back,image=grass_g)
    elif e == 58:
        f7.config(bg=back,image=grass_o)
    elif e == 59:
        f7.config(bg=back,image=kelp)
    elif e == 60:
        f7.config(bg=back,image=frame)
    elif e == 61:
        f7.config(bg=back,image=tower)
    elif e == 62:
        f7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    e = seen_world[6][6]
    if e == 0:
        g7.config(bg=back2,image=blank)
    elif e == 1:
        g7.config(bg=back,image=stone)
    elif e == 2:
        g7.config(bg=back,image=sand)
    elif e == 3:
        g7.config(bg=back,image=water)
    elif e == 4:
        g7.config(bg=back,image=dirt)
    elif e == 5:
        g7.config(bg=back,image=log)
    elif e == 6:
        g7.config(bg=back,image=leaves)
    elif e == 7:
        g7.config(bg=back,image=stick)
    elif e == 8:
        g7.config(bg=back,image=bush)
    elif e == 9:
        g7.config(bg=back,image=potato)
    elif e == 10:
        g7.config(bg=back,image=vine)
    elif e == 11:
        g7.config(bg=back,image=coral_red)
    elif e == 12:
        g7.config(bg=back,image=coral_orange)
    elif e == 13:
        g7.config(bg=back,image=coral_green)
    elif e == 14:
        g7.config(bg=back,image=coral_blue)
    elif e == 15:
        g7.config(bg=back,image=space_coral)
    elif e == 16:
        g7.config(bg=back,image=iron_ore)
    elif e == 17:
        g7.config(bg=back,image=copper_ore)
    elif e == 18:
        g7.config(bg=back,image=bone)
    elif e == 19:
        g7.config(bg=back,image=lantern)
    elif e == 20:
        g7.config(bg=back,image=ladder)
    elif e == 21:
        g7.config(bg=back,image=asteroid)
    elif e == 22:
        g7.config(bg=back,image=sea_bricks)
    elif e == 23:
        g7.config(bg=back,image=stone_bricks)
    elif e == 24:
        g7.config(bg=back,image=sea_lantern)
    elif e == 25:
        g7.config(bg=back,image=cursed_lantern)
    elif e == 26:
        g7.config(bg=back,image=anvil)
    elif e == 27:
        g7.config(bg=back,image=space)
    elif e == 28:
        g7.config(bg=back,image=seaglass)
    elif e == 29:
        g7.config(bg=back,image=lava)
    elif e == 30:
        g7.config(bg=back,image=treasure)
    elif e == 31:
        g7.config(bg=back,image=boat)
    elif e == 32:
        if turtle_dir == True:
            g7.config(bg=back,image=turtle_right)
        else:
            g7.config(bg=back,image=turtle_left)
    elif e == 33:
        g7.config(bg=back,image=boar_left)
    elif e == 34:
        g7.config(bg=back,image=boar_left)
    elif e == 35:
        if y < 19:
            if fish_dir == True:
                g7.config(bg=back,image=space_fish_right)
            else:
                g7.config(bg=back,image=space_fish_left)
        else:
            if fish_dir == True:
                g7.config(bg=back,image=fish_right)
            else:
                g7.config(bg=back,image=fish_left)
    elif e == 36:
        if skeleton1_att == True:
            g7.config(bg=back,image=skeleton_attack_left)
        else:
            g7.config(bg=back,image=skeleton_left)
    elif e == 37:
        if skeleton2_att == True:
            g7.config(bg=back,image=skeleton_attack_left)
        else:
            g7.config(bg=back,image=skeleton_left)
    elif e == 38:
        if skeleton_l1_att == True:
            g7.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g7.config(bg=back,image=leather_skeleton_left)
    elif e == 39:
        if skeleton_l2_att == True:
            g7.config(bg=back,image=leather_skeleton_attack_left)
        else:
            g7.config(bg=back,image=leather_skeleton_left)
    elif e == 40:
        if skeleton_i_att == True:
            g7.config(bg=back,image=bone_skeleton_attack_left)
        else:
            g7.config(bg=back,image=bone_skeleton_left)
    elif e == 41:
        if skeleton2_att == True:
            g7.config(bg=back,image=pirate_attack_left)
        else:
            g7.config(bg=back,image=pirate_left)
    elif e == 42:
        g7.config(bg=back,image=human)
    elif e == 43:
        g7.config(bg=back,image=pufferfish)
    elif e == 44:
        pass  # this is the player, we only need to care about it in d4
    elif e == 45:
        g7.config(bg=back,image=gelatinous_cube)
    elif e == 46:
        g7.config(bg=back,image=tent)
    elif e == 47:
        g7.config(bg=back,image=bird)
    elif e == 48:
        g7.config(bg=back,image=spider)
    elif e == 49:
        g7.config(bg=back,image=cloud)
    elif e == 50:
        g7.config(bg=back,image=stem)
    elif e == 51:
        g7.config(bg=back,image=shroom_r)
    elif e == 52:
        g7.config(bg=back,image=shroom_b)
    elif e == 53:
        g7.config(bg=back,image=boat_pirate)
    elif e == 54:
        g7.config(bg=back,image=bullet)
    elif e == 55:
        g7.config(bg=back,image=g_ore)
    elif e == 56:
        g7.config(bg=back,image=book)
    elif e == 57:
        g7.config(bg=back,image=grass_g)
    elif e == 58:
        g7.config(bg=back,image=grass_o)
    elif e == 59:
        g7.config(bg=back,image=kelp)
    elif e == 60:
        g7.config(bg=back,image=frame)
    elif e == 61:
        g7.config(bg=back,image=tower)
    elif e == 62:
        g7.config(bg=back,image=rasta)
    else:
        pass
    #another one bites the dust
    global jump
    if not(world[y+1][x] == 0):
        jump = False
    gfhg.config(text=(str(find_amount_of(25))+" lanterns remaining."))
    gravity_for(32)
    gravity_for(33)
    gravity_for(34)
    gravity_for(36)
    gravity_for(37)
    gravity_for(38)
    gravity_for(39)
    gravity_for(40)
    gravity_for(41)
    gravity_for(45)
    gravity_for(48)
    gravity_for(48)
    global trade
    global craft
    if trade == False and craft == False:
        n1.config(text="0")
        m1.config(image=blank)
        t1.config(image=blank,command=n)
        n2.config(text="0")
        m2.config(image=blank)
        t2.config(image=blank,command=n)
        n3.config(text="0")
        m3.config(image=blank)
        t3.config(image=blank,command=n)
        n4.config(text="0")
        m4.config(image=blank)
        t4.config(image=blank,command=n)
    if not obj_near_player(26) == True:
        craft = False
    if not obj_near_player(42) == True:
        trade = False
    global moves
    if st == 0:
        moves = 0
#holy shit
def n():
    pass
go_through = [0,3,8,9,10,20,27,28,29,31,46,49,50,57,58,59] #blocks the player can go through
go_through2 = [0,3,53,54,62,57,58,59,8,9,10,20,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
moves = 0
pause = False
fly = [3,10,20,27,50,49,57,58,59] #blocks that the gravity doesnt care about
jump = False
gfhg = tkinter.Label(tk,bg=colour,fg="#ff00ff")
gfhg.place(x=200,y=510)
def move_timer():
    global pause
    global moves
    global st
    if pause == False:
        if st != 0:
            moves = 1
        tk.after(200,move_timer)
    else:
        moves = 0
move_timer()
#use prev_block
def up(event): #up is world [y-1][x]
  try:
    global jump
    global world
    global prev_block
    global moves
    global fly
    global boat_
    global go_through
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y-1][x] in go_through) and (moves == 1) and (jump == False or prev_block in fly):    
        world[y][x] = prev_block
        prev_block = world[y-1][x]
        world[y-1][x] = 44
    else:
        pass
    moves = 0
    gravity()
    jump = True
    if boat_ == True:
        boat_ = False
        world[y][x] = 31
    update_world()
  except:
    pass
def down(event): #down is world [y+1][x]
  try:
    global world
    global prev_block
    global moves
    global go_through
    global jump
    global boat_
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y+1][x] in go_through) and (moves == 1):    
        world[y][x] = prev_block
        prev_block = world[y+1][x]
        world[y+1][x] = 44
    else:
        pass
    moves = 0
    jump = True
    gravity()
    if boat_ == True:
        boat_ = False
        world[y][x] = 31
    update_world()
  except:
    pass
def left(event): #left is world [y][x-1]
  try:
    global world
    global prev_block
    global moves
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x-1] in go_through) and (moves == 1):
        world[y][x] = prev_block
        prev_block = world[y][x-1]
        world[y][x-1] = 44
    else:
        pass
    moves = 0
    jump = True
    gravity()
    update_world()
  except:
    pass
def d_left(event):
  try:
    global world
    global prev_block
    global moves
    global go_through2
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x-1] in go_through2) and (moves == 1) and (world[y][x-2] in go_through):
        world[y][x] = prev_block
        prev_block = world[y][x-2]
        world[y][x-2] = 44
    else:
        pass
    moves = 0
    jump = True
    global st
    st += -1
    gravity()
    update_world()
  except:
    pass
def d_right(event):
  try:
    global world
    global prev_block
    global moves
    global go_through2
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x+1] in go_through2) and (moves == 1) and (world[y][x+2] in go_through):
        world[y][x] = prev_block
        prev_block = world[y][x+2]
        world[y][x+2] = 44
    else:
        pass
    moves = 0
    jump = True
    global st
    st += -1
    gravity()
    update_world()
  except:
    pass
def right(event): #right is world [y][x+1]
  try:
    global world
    global prev_block
    global moves
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x+1] in go_through) and (moves == 1):
        world[y][x] = prev_block
        prev_block = world[y][x+1]
        world[y][x+1] = 44
    else:
        pass
    moves = 0
    jump = True
    gravity()
    update_world()
  except:
    pass
def gravity():
    global prev_block
    global world
    global jump
    global fly
    global boat_
    y = find_player_y()  
    x = find_player_x(y)
    if world[y+1][x] == 0 and jump == True and (not prev_block in fly):
        if boat_ == False:
            world[y][x] = prev_block
            prev_block = world[y+1][x]
            world[y+1][x] = 44
            down(0)
        else:
            boat_ = False
            add(9)
            add(9)
            add(9)
    else:
        pass
    jump = False
    update_world()
update_world()
l = tkinter.Button(tk,bg=colour,fg="#ffffff",text=">",command=lambda:right(0))
r = tkinter.Button(tk,bg=colour,fg="#ffffff",text="<",command=lambda:left(0))
d = tkinter.Button(tk,bg=colour,fg="#ffffff",text="v",command=lambda:down(0))
u = tkinter.Button(tk,bg=colour,fg="#ffffff",text="^",command=lambda:up(0))
l.place(x=60,y=600,width=20,height=20)
r.place(x=20,y=600,width=20,height=20)
d.place(x=40,y=620,width=20,height=20)
u.place(x=40,y=580,width=20,height=20)
l2 = tkinter.Button(tk,bg=colour,fg="#ffffff",text=">>",command=lambda:d_right(0))
r2 = tkinter.Button(tk,bg=colour,fg="#ffffff",text="<<",command=lambda:d_left(0))
l2.place(x=50,y=560,width=30,height=20)
r2.place(x=20,y=560,width=30,height=20)
turtle_hp = 12
skeleton1_hp = 7
skeleton2_hp = 7
skeleton_l1_hp = 10
skeleton_l2_hp = 10
skeleton_i_hp = 13
skeleton_p_hp = 16
boar1_hp = 4
boar2_hp = 4
cube_hp = 32
#-----------------------------------#
def spawn_fish(fih): #35 or 43
    global prev_block
    global world
    global fish_dir
    if obj_in_world(35) == True:
        y = find_y_of(35)
    else:
        y = 50
    if y < 19:
        rep = 27
    else:
        rep = 3
    remove_and_replace(43,3)
    remove_and_replace(35,rep)
    remove_and_replace(35,rep)
    remove_and_replace(35,rep)
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    if fih == 35:
        if (world[y+a][x+b] == 3 or world[y+a][x+b] == 27) and find_amount_of(35) < 3:
            world[y+a][x+b] = fih
        if (world[y+b][x+a] == 3 or world[y+b][x+a] == 27) and find_amount_of(35) < 3:
            world[y+b][x+a] = fih
            fish_dir = True
    elif fih == 43:
        if world[y+a][x+b] == 3 and find_amount_of(43) == 0:
            world[y+a][x+b] = fih
    update_world()
def spawn_turtle():
    global prev_block
    global world
    global turtle_dir
    remove_and_replace(32,0)
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    if world[y+a][x+b] == 0 and find_amount_of(32) == 0:
        world[y+a][x+b] = 32
        turtle_dir = True
    gravity_for(32)
    gravity_for(32)
def spawn_boat():
    global prev_block
    global world
    remove_and_replace(53,0)
    y = find_player_y()
    x = find_player_x(y)
    b = random.randint(1,3)
    if world[y][x+b] == 0 and world[y+1][x] == 3 and find_amount_of(53) == 0:
        world[y][x+b] = 53
    update_world()
def move_bullet():
    global world
    global wt
    if obj_in_world(54) == True:
        remove_and_replace(54,0)
        y = find_y_of(54)
        x = find_x_of(54,y)
        if world[y][x-1] == 0:
            world[y][x-1] = 54
            world[y][x] = 0
        elif world[y][x-1] == 44:
            world[y][x] = 0
            e = calc(5)
            wt = wt - e
        else:
            world[y][x] = 0
    update_world()
def spawn_bullet():
    global world
    remove_and_replace(54,0)
    if obj_in_world(53) == True and find_amount_of(54) == 0:
        y = find_y_of(53)
        x = find_x_of(53,y)
        if world[y][x-1] == 0:
            world[y][x-1] = 54
            update_world()
        x = find_x_of(54,y)
        if world[y][x+1] == 0:
            world[y][x] = 0
            world[y][x+1] = 54
    update_world()
def spawn_skeleton(): #36/37      
 global world
 global prev_block  
 global day
 global level
 try:
  if (prev_block == 3):
    raise SyntaxError
  else:
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    c = random.randint(-3,3)
    d = random.randint(-3,3)
    global skeleton1_hp
    global skeleton2_hp
    global skeleton1_att
    global skeleton2_att
    if y > 24 and x > 900:
        back = "#040404"
    else:
        if prev_block == 3:
            back = "#00bbff"
        elif y > 18 and day == True and y < 51:
            back = "#8ef4ff"
        else:
            back = "#040404"
    if back == "#040404" or (obj_in_seen_world(23) == True and level > 4):
        #-----------------------#
        if world[y+a][x+b] == 0 and find_amount_of(36) == 0:
            world[y+a][x+b] = 36
            gravity_for(36)
            skeleton1_hp = 7
            skeleton1_att = False
        #------------------------#
        if world[y+c][x+d] == 0 and find_amount_of(37) == 0:
            world[y+c][x+d] = 37
            gravity_for(37)
            skeleton2_hp = 7
            skeleton2_att = False
 except:
  pass
 finally:
  update_world()
def spawn_dungeon(entity): #40/45
 global world   
 if find_amount_of(entity) == 0 and obj_in_seen_world(23) == True:
    global cube_hp
    global skeleton_i_hp
    global skeleton_i_att
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    remove_and_replace(entity,0)
    if entity == 40:
        if world[y+a][x+b] == 0:
            world[y+a][x+b] = 40
            skeleton_i_hp = 13
            skeleton_i_att = False
            gravity_for(40)
    elif entity == 45:
        if world[y+a][x+b] == 0:
            world[y+a][x+b] = 45
            cube_hp = 32
            gravity_for(45)
def spawn_spider():
    global world
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    c = random.randint(-3,3)
    d = random.randint(-3,3)
    remove_and_replace(48,0)
    remove_and_replace(48,0)
    global day
    if (obj_in_seen_world(6) == True or obj_in_seen_world(5) == True or obj_in_seen_world(10) == True or day == False) and find_amount_of(47) < 2:
        if world[y+a][x+b] == 0:
            world[y+a][x+b] = 48
        if world[y+c][x+d] == 0:
            world[y+c][x+d] = 48
def spawn_bird():
    global world
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    c = random.randint(-3,3)
    d = random.randint(-3,3)
    remove_and_replace(47,0)
    remove_and_replace(47,0)
    if (obj_in_seen_world(6) == True or obj_in_seen_world(5) == True or obj_in_seen_world(10) == True) and find_amount_of(47) < 2:
        if world[y+a][x+b] == 0:
            world[y+a][x+b] = 47
        if world[y+c][x+d] == 0:
            world[y+c][x+d] = 47
def spawn_boar():
    global world
    y = find_player_y()
    x = find_player_x(y)
    remove_and_replace(33,0)
    remove_and_replace(34,0)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    c = random.randint(-3,3)
    d = random.randint(-3,3)
    global boar1_hp
    global boar2_hp
    if world[y+a][x+b] == 0 and find_amount_of(33) == 0 and obj_in_seen_world(4) == True:
        world[y+a][x+b] = 33
        boar1_hp = 4
        gravity_for(33)
    if world[y+c][x+d] == 0 and find_amount_of(34) == 0 and obj_in_seen_world(4) == True:
        world[y+c][x+d] = 34
        boar2_hp = 4
        gravity_for(34)
    gravity_for(33)
    gravity_for(34)
def spawn_pirate():
    global world
    global skeleton_p_hp
    global skeleton_p_att
    remove_and_replace(41,0)
    y = find_player_y()
    x = find_player_x(y)
    a = random.randint(-3,3)
    b = random.randint(-3,3)
    if obj_in_seen_world(23) == True and world[y+a][x+b] == 0 and find_amount_of(41) == 0:
        world[y+a][x+b] = 41
        skeleton_p_hp = 16
        skeleton_p_att = False
def spawn_39():
    global world
    global skeleton_l2_att
    global skeleton_l2_hp
    global prev_block
    remove_and_replace(39,3)
    y = find_player_y()
    x = find_player_x(y)
    c = random.randint(-3,3)
    d = random.randint(-3,3)
    if world[y+c][x+d] == 3 and prev_block == 3 and find_amount_of(39) == 0:
        world[y+c][x+d] = 39
        gravity_for(39)
        skeleton_l2_hp = 10
        skeleton_l2_att = False
def spawn_38():
    global world
    global skeleton_l1_att
    global skeleton_l1_hp
    global prev_block
    remove_and_replace(38,27)
    y = find_player_y()
    x = find_player_x(y)
    c = random.randint(-3,3)
    d = random.randint(-3,3)
    #print(world[y+c][x+d] == 27 and prev_block == 27 and find_amount_of(38) == 0 and (obj_in_world(38) == False))
    if world[y+c][x+d] == 27 and prev_block == 27 and find_amount_of(38) == 0 and (obj_in_world(38) == False):
        world[y+c][x+d] = 38
        gravity_for(38)
        skeleton_l1_hp = 10
        skeleton_l1_att = False
        world[y+c][x+d] = 38
        update_world()
#---------------------------------------#
def move_fish():
    global world
    global fish_dir
    if obj_in_world(35) == True:
        a = random.randint(1,4)
        y = find_y_of(35)
        x = find_x_of(35,y)
        if y < 19:
            rep = 27
        else:
            rep = 3
        remove_and_replace(35,rep)
        if a == 1 and world[y+1][x] == 3:
            world[y+1][x] = 35
            world[y][x] = 3
            fish_dir = False
        elif a == 2 and world[y-1][x] == 3:
            world[y-1][x] = 35
            world[y][x] = 3
            fish_dir = True
        elif a == 3 and world[y][x+1] == 3:
            world[y][x+1] = 35
            world[y][x] = 3
            fish_dir = True
        elif a == 4 and world[y][x-1] == 3:
            world[y][x-1] = 35
            world[y][x] = 3
            fish_dir = False
def move_turtle():
    global world
    global turtle_dir
    if obj_in_world(32) == True:
        a = random.randint(1,2)
        y = find_y_of(32)
        x = find_x_of(32,y)
        remove_and_replace(32,0)
        if a == 1 and world[y][x+1] == 0:
            world[y][x+1] = 32
            world[y][x] = 0
            turtle_dir = True
        elif a == 2 and world[y][x-1] == 0:
            world[y][x-1] = 32
            world[y][x] = 0
            turtle_dir = False
    update_world()
    gravity_for(32)
def move_puff():
    global world
    if obj_in_world(43) == True:
        a = random.randint(1,4)
        y = find_y_of(43)
        x = find_x_of(43,y)
        remove_and_replace(43,3)
        if a == 1 and world[y+1][x] == 3:
            world[y+1][x] = 43
            world[y][x] = 3
        elif a == 2 and world[y-1][x] == 3:
            world[y-1][x] = 43
            world[y][x] = 3
        elif a == 3 and world[y][x+1] == 3:
            world[y][x+1] = 43
            world[y][x] = 3
        elif a == 4 and world[y][x-1] == 3:
            world[y][x-1] = 43
            world[y][x] = 3
def move_bird():
    global world
    if obj_in_world(47) == True:
        a = random.randint(1,4)
        y = find_y_of(47)
        x = find_x_of(47,y)
        remove_and_replace(47,0)
        if a == 1 and world[y+1][x] == 0:
            world[y+1][x] = 47
            world[y][x] = 0
        elif a == 2 and world[y-1][x] == 0:
            world[y-1][x] = 47
            world[y][x] = 0
        elif a == 3 and world[y][x+1] == 0:
            world[y][x+1] = 47
            world[y][x] = 0
        elif a == 4 and world[y][x-1] == 0:
            world[y][x-1] = 47
            world[y][x] = 0
    gravity_for(47)
    gravity_for(47)
def move_39():
    global world
    if obj_in_world(39) == True:
        a = random.randint(1,4)
        y = find_y_of(39)
        x = find_x_of(39,y)
        y2 = find_player_y()
        x2 = find_player_x(y2)
        remove_and_replace(39,3)
        if x < x2:
            if world[y][x+1] == 3:
                world[y][x+1] = 39
                world[y][x] = 3
            else:
                if world[y-1][x] == 3:
                    world[y-1][x] = 39
                    world[y][x] = 3
                    if world[y][x+1] == 3:
                        world[y][x+1] = 39
                        world[y][x] = 3
        elif x > x2:
            if world[y][x-1] == 3:
                world[y][x-1] = 39
                world[y][x] = 3
                if world[y-1][x] == 3:
                    world[y-1][x] = 39
                    world[y][x] = 3
                    if world[y][x-1] == 3:
                        world[y][x-1] = 39
                        world[y][x] = 3
        elif y > y2:
            if world[y-1][x] == 3:
                world[y-1][x] = 39
                world[y][x] = 3
        elif y < y2:
            if world[y+1][x] == 3:
                world[y+1][x] = 39
                world[y][x] = 3
        else:
            pass #?
        gravity_for(39)
def move_38():
    global world
    if obj_in_world(38) == True:
        a = random.randint(1,4)
        y = find_y_of(38)
        x = find_x_of(38,y)
        y2 = find_player_y()
        x2 = find_player_x(y2)
        remove_and_replace(38,27)
        if x < x2:
            if world[y][x+1] == 27:
                world[y][x+1] = 38
                world[y][x] = 27
            else:
                if world[y-1][x] == 27:
                    world[y-1][x] = 38
                    world[y][x] = 27
                    if world[y][x+1] == 27:
                        world[y][x+1] = 38
                        world[y][x] = 27
        elif x > x2:
            if world[y][x-1] == 27:
                world[y][x-1] = 38
                world[y][x] = 27
                if world[y-1][x] == 27:
                    world[y-1][x] = 38
                    world[y][x] = 27
                    if world[y][x-1] == 27:
                        world[y][x-1] = 38
                        world[y][x] = 27
        elif y > y2:
            if world[y-1][x] == 27:
                world[y-1][x] = 38
                world[y][x] = 27
        elif y < y2:
            if world[y+1][x] == 27:
                world[y+1][x] = 38
                world[y][x] = 27
        else:
            pass #?
        gravity_for(38)
def move_enemy(enemy):
    global world
    if obj_in_world(enemy) == True:
        a = random.randint(1,4)
        y = find_y_of(enemy)
        x = find_x_of(enemy,y)
        y2 = find_player_y()
        x2 = find_player_x(y2)
        remove_and_replace(enemy,0)
        if obj_in_world(enemy) == True and obj_in_seen_world(enemy) == False:
            world[y][x] = 0
        if x < x2:
            if world[y][x+1] == 0:
                world[y][x+1] = enemy
                world[y][x] = 0
            else:
                if world[y-1][x] == 0:
                    world[y-1][x] = enemy
                    world[y][x] = 0
                    if world[y][x+1] == 0:
                        world[y][x+1] = enemy
                        world[y][x] = 0
        elif x > x2:
            if world[y][x-1] == 0:
                world[y][x-1] = enemy
                world[y][x] = 0
            else:
                if world[y-1][x] == 0:
                    world[y-1][x] = enemy
                    world[y][x] = 0
                    if world[y][x-1] == 0:
                        world[y][x-1] = enemy
                        world[y][x] = 0
        elif y > y2:
            if world[y-1][x] == 0:
                world[y-1][x] = enemy
                world[y][x] = 0
        elif y < y2:
            if world[y+1][x] == 0:
                world[y+1][x] = enemy
                world[y][x] = 0
        else:
            pass #?
        gravity_for(enemy)
#---------------------------------
def calc(dam):
    global soak
    global def_
    global block
    g = def_
    if block == False:
        g = 0
    e = g * 0.25
    e = 1 - e
    f = dam * e
    f = f - soak
    if f < 0:
        f = 0
    return f
def get_attacked_by(enemy):
    global wt
    global st
    global soak
    global def_
    if obj_near_player(enemy) == True:
        if enemy == 33:
            e = calc(5)
            wt = wt - e
        elif enemy == 34:
            e = calc(5)
            wt = wt - e
        elif enemy == 43:
            st = st-3
        elif enemy == 45:
            e = calc(4)
            wt = wt - e
            a = random.randint(1,2)
            if a == 1:
                d_left(0)
            else:
                d_right(0)
        elif enemy == 48:
            st = st - 4
def get_attacked_by_36():
  if obj_in_world(36) == True:
    global wt
    global skeleton1_att
    global world
    y = find_y_of(36)
    x = find_x_of(36,y)
    y2 = find_player_y()
    x2 = find_player_x(y2)
    if skeleton1_att == False:
        skeleton1_att = True
    else:
        skeleton1_att = False
        if x < x2:  #player is to the right [x+1]
           if world[y][x+1] == 44:
               e = calc(7)
               wt = wt - e
        elif x > x2:  #player is to the left [x-1]
           if world[y][x-1] == 44:
               e = calc(7)
               wt = wt - e
def get_attacked_by_37():
  if obj_in_world(37) == True:
    global wt
    global skeleton2_att
    global world
    y = find_y_of(37)
    x = find_x_of(37,y)
    y2 = find_player_y()
    x2 = find_player_x(y2)
    if skeleton2_att == False:
        skeleton2_att = True
    else:
        skeleton2_att = False
        if x < x2:  #player is to the right [x+1]
           if world[y][x+1] == 44:
               e = calc(7)
               wt = wt - e
        elif x > x2:  #player is to the left [x-1]
           if world[y][x-1] == 44:
               e = calc(7)
               wt = wt - e
def get_attacked_by_38():
  if obj_in_world(38) == True:
    global wt
    global skeleton_l1_att
    global world
    y = find_y_of(38)
    x = find_x_of(38,y)
    y2 = find_player_y()
    x2 = find_player_x(y2)
    if skeleton_l1_att == False:
        skeleton_l1_att = True
    else:
        skeleton_l1_att = False
        if x < x2:  #player is to the right [x+1]
           if world[y][x+1] == 44:
               e = calc(7)
               wt = wt - e
        elif x > x2:  #player is to the left [x-1]
           if world[y][x-1] == 44:
               e = calc(7)
               wt = wt - e
def get_attacked_by_39():
  if obj_in_world(39) == True:
    global wt
    global skeleton_l2_att
    global world
    y = find_y_of(39)
    x = find_x_of(39,y)
    y2 = find_player_y()
    x2 = find_player_x(y2)
    if skeleton_l2_att == False:
        skeleton_l2_att = True
    else:
        skeleton_l2_att = False
        if x < x2:  #player is to the right [x+1]
           if world[y][x+1] == 44:
               e = calc(7)
               wt = wt - e
        elif x > x2:  #player is to the left [x-1]
           if world[y][x-1] == 44:
               e = calc(7)
               wt = wt - e
def get_attacked_by_40():
  if obj_in_world(40) == True:
    global wt
    global skeleton_i_att
    global world
    y = find_y_of(40)
    x = find_x_of(40,y)
    y2 = find_player_y()
    x2 = find_player_x(y2)
    if skeleton_i_att == False:
        skeleton_i_att = True
    else:
        skeleton_i_att = False
        if x < x2:  #player is to the right [x+1]
           if world[y][x+1] == 44:
               e = calc(7)
               wt = wt - e
        elif x > x2:  #player is to the left [x-1]
           if world[y][x-1] == 44:
               e = calc(7)
               wt = wt - e
def get_attacked_by_41():
  if obj_in_world(41) == True:
    global wt
    global skeleton_p_att
    global world
    y = find_y_of(41)
    x = find_x_of(41,y)
    y2 = find_player_y()
    x2 = find_player_x(y2)
    if skeleton_p_att == False:
        skeleton_p_att = True
    else:
        skeleton_p_att = False
        if x < x2:  #player is to the right [x+1]
           if world[y][x+1] == 44:
               e = calc(9)
               wt = wt - e
        elif x > x2:  #player is to the left [x-1]
           if world[y][x-1] == 44:
               e = calc(9)
               wt = wt - e   
#---------------------------------
time = 0
pause = False
def pause_():
    global pause
    global time
    if pause == True:
        pause = False
        puase.config(text="Pause")
        time_()
        move_timer()
    elif pause == False:
        pause = True
        puase.config(text="Unpause")
        time = 13
puase = tkinter.Button(tk,bg=colour,fg="#ffffff",text="Pause",command=pause_)
puase.place(x=200,y=600)
def time_():
    global time
    global pause
    #print(time)
    if pause == False:
        time += 1
        move_world()
        tk.after(250,time_)
import sys
def move_world():
    global world
    global time
    global day
    global food
    global water_
    global wt
    global st
    global prev_block
    global block
    global boat_
    if time % 1024 == 0:
        if day == True:
            day = False
        else:
            day = True
        wt += 4
        reset_trades()
    elif time % 128 == 0:
        food += -1
        water_ += -1
    elif time % 96 == 0:
        spawn_boar()
        spawn_boar()
        spawn_spider()
        spawn_38()
        spawn_39()
        spawn_38()
        spawn_39()
        spawn_boat()
        st += 1
        if prev_block == 3:
            st += -1
    elif time % 64 == 0:
        spawn_fish(43)
        spawn_pirate()
        spawn_38()
        spawn_39()
        spawn_38()
        spawn_39()
        spawn_dungeon(45)
        spawn_dungeon(40)
        spawn_dungeon(45)
        spawn_dungeon(40)
        st += 1
        remove_and_replace(32,0)
        remove_and_replace(33,0)
        remove_and_replace(34,0)
        remove_and_replace(36,0)
        remove_and_replace(37,0)
        remove_and_replace(38,27)
        remove_and_replace(39,3)
        remove_and_replace(40,0)
        remove_and_replace(41,0)
        remove_and_replace(45,0)
        remove_and_replace(48,0)
        remove_and_replace(48,0)
    elif time % 32 == 0:
        spawn_38()
        spawn_39()
        spawn_38()
        spawn_39()
        spawn_bird()
        spawn_bullet()
        spawn_pirate()
        st += 1
        remove_and_replace(32,0)
        remove_and_replace(33,0)
        remove_and_replace(34,0)
        remove_and_replace(36,0)
        remove_and_replace(37,0)
        remove_and_replace(38,27)
        remove_and_replace(39,3)
        remove_and_replace(40,0)
        remove_and_replace(41,0)
        remove_and_replace(45,0)
        remove_and_replace(48,0)
        remove_and_replace(48,0)
        remove_and_replace(53,0)
        remove_and_replace(54,0)
        if prev_block == 3:
            st += -1
    elif time % 24 == 0:
        spawn_skeleton()
        spawn_dungeon(45)
        spawn_dungeon(40)
        spawn_dungeon(45)
        spawn_dungeon(40)
        spawn_boat()
        if prev_block == 3:
            st += -1
    elif time % 16 == 0:
        spawn_turtle()
        spawn_fish(35)
        get_attacked_by(45)
        get_attacked_by(43)
        get_attacked_by(48)
        spawn_bullet()
        get_attacked_by_41()
        if prev_block == 3:
            st += -1
    elif time % 8 == 0:
        move_turtle()
        move_puff()
        move_bird()
        move_enemy(45)
        move_enemy(36)
        move_enemy(37)
        move_38()
        move_39()
        spawn_bullet()
        move_enemy(40)
        move_enemy(41)
        get_attacked_by(45)
        get_attacked_by(43)
        get_attacked_by(48)
        get_attacked_by_41()
        if prev_block == 3:
            st += -1
    elif time % 4 == 0:
        move_fish()
        move_enemy(45)
        move_enemy(36)
        move_enemy(37)
        move_39()
        move_enemy(40)
        move_enemy(41)
        get_attacked_by_41()
        get_attacked_by(45)
        get_attacked_by(43)
        get_attacked_by(48)
        move_38()
    elif time % 3 == 0:
        move_enemy(34)
        move_enemy(33)
        move_enemy(48)
        move_enemy(48)
        get_attacked_by_36()
        get_attacked_by_37()
        get_attacked_by_38()
        get_attacked_by_39()
        get_attacked_by_40()
        get_attacked_by(33)
        get_attacked_by(34)
    elif time % 2 == 0:
        move_enemy(36)
        move_enemy(37)
        move_39()
        move_38()
        move_enemy(40)
        move_enemy(41)
        get_attacked_by_41()
    else:
        pass
    move_bullet()
    if prev_block == 3 and st == 0:
        wt += -1
    if food == 0 or water_ == 0:
        wt += -1
    if obj_near_player(29) == True:
        wt += -1
    if find_amount_of(25) == 0:
        pause = True
        prev_block = 0
        boat_ = True
        world = [[27,27,27,27,27,27,27],
                 [27,27,27,27,27,27,27],
                 [27,27,27,27,27,27,27],
                 [27,53,27,44,27,27,27],
                 [3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3],
                 [2,2,2,2,2,2,2]]
        print("YAR! ME NAME IS CAPTAIN BONES. WE BE FRIENDS NOW.")
        update_world()
        sys.exit()
    if wt == 0 or wt < 0:
        pause = True
        prev_block = 0
        world = [[23,23,23,23,23,23,23],
                 [23,0,0,0,0,0,23],
                 [23,0,0,23,0,0,23],
                 [23,0,23,44,23,0,23],
                 [23,0,0,23,0,0,23],
                 [23,0,0,0,0,0,23],
                 [23,23,23,23,23,23,23]]
        st = 0
        print("GAME OVER")
        update_world()
        sys.exit()
        #raise SyntaxError("GAME OVER  Restart the game to retry.")
    update_world()
#---------------------------------------------#
trads = tkinter.Label(tk,text="TRADES/RECIPES:",bg=colour,fg="#ffffff")
trads.place(x=348,y=499)
reee = tkinter.Label(tk,text=">\n\n>\n\n>\n\n>",bg=colour,fg="#ffffff")
reee.place(x=390,y=525)
reset_trades()
time_()
#18 is mula
def find_number_of(obj):
    global inventory
    j = 0
    e = 0
    for i in range(len(inventory)):
        if inventory[j] == obj:
            e += 1
        j += 1
    return e
def trade1(): #herb
    global inventory
    if find_number_of(18) >= 2:
        rem(18)
        rem(18)
        add(random.randint(1,3)+24)
def trade2(): #ladder
    global inventory
    if 18 in inventory:
        rem(18)
        add(28)
        add(28)
def trade3(): #bread
    global inventory
    if 18 in inventory:
        rem(18)
        add(20)
        add(20)
def trade4(): #bucket
    global inventory
    if find_number_of(18) >= 2:
        rem(18)
        rem(18)
        add(16)
def trade5(): #pickaxe
    global inventory
    if find_number_of(18) >= 2:
        rem(18)
        rem(18)
        add(13)
def trade6(): #pouch
    global inventory
    if 18 in inventory:
        rem(18)
        add(22)
def craft1(): #ladder
    global inventory
    if find_number_of(9) >= 3:
        rem(9)
        rem(9)
        rem(9)
        add(28)
def craft2(): #i_shield
    global inventory
    if find_number_of(12) >= 4:
        for i in range(4):
            rem(12)
        add(15)
def craft3(): #c_shield
    global inventory
    if find_number_of(11) >= 4:
        for i in range(4):
            rem(11)
        add(14)
def craft4(): #b_armour
    global inventory
    if find_number_of(10) >= 4:
        for i in range(4):
            rem(10)
        add(6)
def sell1():  #fish
    global inventory
    if find_number_of(19) >= 5:
        for i in range(5):
            rem(19)
        add(18)
def sell2():  #copper
    global inventory
    if find_number_of(11) >= 5:
        for i in range(5):
            rem(11)
        add(18)
def sell3():  #bones
    global inventory
    if find_number_of(10) >= 5:
        for i in range(5):
            rem(10)
        add(18)
def sell4():  #iron
    global inventory
    if find_number_of(12) >= 2:
        rem(12)
        rem(12)
        add(18)
#here we go
def spec1(): #tier 1
    global inventory
    global level
    if find_number_of(18) >= 2:
        for i in range(2):
            rem(18)
        add(1)
        level = 1
def spec2(): #tier 1
    global inventory
    global level
    if find_number_of(18) >= 2:
        for i in range(2):
            rem(18)
        add(5)
        level = 2
#----#
def spec3(): #tier 2
    global inventory
    global level
    if find_number_of(18) >= 2:
        for i in range(2):
            rem(18)
        add(2)
        level = 3
def spec4(): #tier 2
    global inventory
    global level
    if find_number_of(18) >= 2:
        for i in range(2):
            rem(18)
        add(6)
        level = 4
#----#
def spec5(): #tier 3
    global inventory
    global level
    if find_number_of(18) >= 3:
        for i in range(3):
            rem(18)
        add(3)
        level = 5
def spec6(): #tier 3
    global inventory
    global level
    if find_number_of(18) >= 3:
        for i in range(3):
            rem(18)
        add(7)
        level = 6
#----#
def spec7(): #tier 4
    global inventory
    global level
    if find_number_of(18) >= 4:
        for i in range(4):
            rem(18)
        add(4)
        level = 7
def spec8(): #tier 4
    global inventory
    global level
    if find_number_of(18) >= 4:
        for i in range(4):
            rem(18)
        add(8)
        level = 8
#----#
def spec9(): #tier 5
    global inventory
    global level
    if find_number_of(18) >= 5:
        for i in range(5):
            rem(18)
        add(30)
        level = 9
def spec10(): #tier 5
    global inventory
    global level
    if find_number_of(18) >= 5:
        for i in range(5):
            rem(18)
        add(29)
        level = 10
#----#
def spec11(): #cutlass
    global inventory
    if find_number_of(18) >= 5:
        for i in range(5):
            rem(18)
        add(17)
#-----#
def load_trades():
    global craft
    global trade
    global u
    global v
    global w
    global level
    if craft == True:
        n1.config(text="3")
        m1.config(image=stick)
        t1.config(image=ladder,command=craft1)
        n2.config(text="4")
        m2.config(image=iron)
        t2.config(image=i_shield,command=craft2)
        n3.config(text="4")
        m3.config(image=copper)
        t3.config(image=c_shield,command=craft3)
        n4.config(text="4")
        m4.config(image=bone)
        t4.config(image=b_armour,command=craft4)
    elif trade == True:
        if u == 1:
            n1.config(text="5")
            m1.config(image=fish_left)
            t1.config(image=dbloon,command=sell1)
        elif u == 2:
            n1.config(text="5")
            m1.config(image=copper)
            t1.config(image=dbloon,command=sell2)
        elif u == 3:
            n1.config(text="5")
            m1.config(image=bone)
            t1.config(image=dbloon,command=sell3)
        elif u == 4:
            n1.config(text="2")
            m1.config(image=iron)
            t1.config(image=dbloon,command=sell4)
        if v == 1:
            n2.config(text="2")
            m2.config(image=dbloon)
            t2.config(image=herb_ko,command=trade1)
        elif v == 2:
            n2.config(text="1")
            m2.config(image=dbloon)
            t2.config(image=ladder,command=trade2)
        elif v == 3:
            n2.config(text="1")
            m2.config(image=dbloon)
            t2.config(image=bread,command=trade3)
        if w == 1:
            n3.config(text="2")
            m3.config(image=dbloon)
            t3.config(image=bucket,command=trade4)
        elif w == 2:
            n3.config(text="2")
            m3.config(image=dbloon)
            t3.config(image=pickaxe,command=trade5)
        elif w == 3:
            n3.config(text="1")
            m3.config(image=dbloon)
            t3.config(image=empty_pouch,command=trade6)
        #---------#
        if level == 0:
            n4.config(text="2")
            m4.config(image=dbloon)
            t4.config(image=w_axe,command=spec1)
        elif level == 1:
            n4.config(text="2")
            m4.config(image=dbloon)
            t4.config(image=l_armour,command=spec2)
        elif level == 2:
            n4.config(text="2")
            m4.config(image=dbloon)
            t4.config(image=b_axe,command=spec3)
        elif level == 3:
            n4.config(text="2")
            m4.config(image=dbloon)
            t4.config(image=b_armour,command=spec4)
        elif level == 4:
            n4.config(text="3")
            m4.config(image=dbloon)
            t4.config(image=c_axe,command=spec5)
        elif level == 5:
            n4.config(text="3")
            m4.config(image=dbloon)
            t4.config(image=c_armour,command=spec6)
        elif level == 6:
            n4.config(text="4")
            m4.config(image=dbloon)
            t4.config(image=i_axe,command=spec7)
        elif level == 7:
            n4.config(text="4")
            m4.config(image=dbloon)
            t4.config(image=i_armour,command=spec8)
        elif level == 8:
            n4.config(text="5")
            m4.config(image=dbloon)
            t4.config(image=d_axe,command=spec9)
        elif level == 9:
            n4.config(text="5")
            m4.config(image=dbloon)
            t4.config(image=d_armour,command=spec10)
        elif level == 10:
            n4.config(text="5")
            m4.config(image=dbloon)
            t4.config(image=cutlass,command=spec11)
#------------------------------------------#
tk.bind("<KeyRelease-a>",left)
tk.bind("<KeyRelease-d>",right)
tk.bind("<KeyRelease-w>",up)
tk.bind("<KeyRelease-s>",down)
tk.bind("<KeyRelease-m>",use_item)
tk.bind("<KeyRelease-n>",block_)
tk.bind("<KeyRelease-u>",drop)
tk.bind("<KeyRelease-q>",d_left)
tk.bind("<KeyRelease-e>",d_right)
#+++
tkinter.mainloop()
