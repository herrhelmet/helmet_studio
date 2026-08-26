#┼┼┼
import tkinter
from tkinter.constants import *
ree = tkinter.Tk()
ree.geometry("60x60")
ree.title("PLEASE DONT DESTROY")
blank = tkinter.PhotoImage(file="air.png") #0
water = tkinter.PhotoImage(file="water.png") #1
brick = tkinter.PhotoImage(file="brick.png") #2
ground = tkinter.PhotoImage(file="ground.png") #3
blue_brick = tkinter.PhotoImage(file="blue_brick.png") #4
water_block = tkinter.PhotoImage(file="water_block.png") #5
coral = tkinter.PhotoImage(file="coral.png") #6
pipe = tkinter.PhotoImage(file="pipe.png") #7
shroom = tkinter.PhotoImage(file="shroom.png") #8
stem = tkinter.PhotoImage(file="stem.png") #9
flagpole = tkinter.PhotoImage(file="flagpole.png") #10
platform = tkinter.PhotoImage(file="platform.png") #11
coin = tkinter.PhotoImage(file="coin.png") #12
lava = tkinter.PhotoImage(file="lava.png") #13
castle_brick = tkinter.PhotoImage(file="castle_brick.png") #14
spec_block = tkinter.PhotoImage(file="spec_block.png") #15
goomba = tkinter.PhotoImage(file="goomba.png") #16
beetle = tkinter.PhotoImage(file="beetle.png") #17
beetle_shell = tkinter.PhotoImage(file="beetle_shell.png") #18
green_koopa = tkinter.PhotoImage(file="green_koopa.png") #19
green_shell = tkinter.PhotoImage(file="green_shell.png") #20
red_koopa = tkinter.PhotoImage(file="red_koopa.png") #21
red_shell = tkinter.PhotoImage(file="red_shell.png") #22
p_plant = tkinter.PhotoImage(file="p_plant.png") #23
squid = tkinter.PhotoImage(file="squid.png") #24
red_fish = tkinter.PhotoImage(file="red_fish.png") #25
green_fish = tkinter.PhotoImage(file="green_fish.png") #26
spiny = tkinter.PhotoImage(file="spiny.png") #27
cannon = tkinter.PhotoImage(file="cannon.png") #28
bullet = tkinter.PhotoImage(file="bullet.png") #29
firewall = tkinter.PhotoImage(file="firewall.png") #30
peen_snatcher = tkinter.PhotoImage(file="peen_snatcher.png") #31
power_up = tkinter.PhotoImage(file="power_up.png") #32
mario_right = tkinter.PhotoImage(file="mario_right.png") #33
mario_left = tkinter.PhotoImage(file="mario_left.png") #33
super_mario_right = tkinter.PhotoImage(file="super_mario_right.png") #33
super_mario_left = tkinter.PhotoImage(file="super_mario_left.png") #33
bro = tkinter.PhotoImage(file="bro.png") #34
lakitu = tkinter.PhotoImage(file="lakitu.png") #35
#
print("Welcome to micro mario!")
print("Controls:\n w - high jump\n a - left\n d - right\n q - dash left\n e - dash right\n s - jump\n x - down")
class level():
  def l1():
    file = open("#l1-1.txt","r")
    l1 = file.read()
    l1 = l1.split("\n")
    for i in range(len(l1)):
        l1[i] = l1[i].split(",")
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            l1[i][j] = int(l1[i][j])
    file.close()
    return l1
    #eee
  def l2():
    file = open("#l1-2.txt","r")
    l2 = file.read()
    l2 = l2.split("\n")
    for i in range(len(l2)):
        l2[i] = l2[i].split(",")
    for i in range(len(l2)):
        for j in range(len(l2[i])):
            l2[i][j] = int(l2[i][j])
    file.close()
    return l2
    #eee
  def l3():
    file = open("#l1-3.txt","r")
    l3 = file.read()
    l3 = l3.split("\n")
    for i in range(len(l3)):
        l3[i] = l3[i].split(",")
    for i in range(len(l3)):
        for j in range(len(l3[i])):
            l3[i][j] = int(l3[i][j])
    file.close()
    return l3
    #eee
  def l4():
    file = open("#l1-4.txt","r")
    l4 = file.read()
    l4 = l4.split("\n")
    for i in range(len(l4)):
        l4[i] = l4[i].split(",")
    for i in range(len(l4)):
        for j in range(len(l4[i])):
            l4[i][j] = int(l4[i][j])
    file.close()
    return l4
    #eee
  def l5():
    file = open("#l1-5.txt","r")
    l5 = file.read()
    l5 = l5.split("\n")
    for i in range(len(l5)):
        l5[i] = l5[i].split(",")
    for i in range(len(l5)):
        for j in range(len(l5[i])):
            l5[i][j] = int(l5[i][j])
    file.close()
    return l5
    #eee
  def l6():
    file = open("#l2-1.txt","r")
    l6 = file.read()
    l6 = l6.split("\n")
    for i in range(len(l6)):
        l6[i] = l6[i].split(",")
    for i in range(len(l6)):
        for j in range(len(l6[i])):
            l6[i][j] = int(l6[i][j])
    file.close()
    return l6
    #eee
  def l7():
    file = open("#l2-2.txt","r")
    l7 = file.read()
    l7 = l7.split("\n")
    for i in range(len(l7)):
        l7[i] = l7[i].split(",")
    for i in range(len(l7)):
        for j in range(len(l7[i])):
            l7[i][j] = int(l7[i][j])
    file.close()
    return l7
    #eee
  def l8():
    file = open("#l2-3.txt","r")
    l8 = file.read()
    l8 = l8.split("\n")
    for i in range(len(l8)):
        l8[i] = l8[i].split(",")
    for i in range(len(l8)):
        for j in range(len(l8[i])):
            l8[i][j] = int(l8[i][j])
    file.close()
    return l8
    #eee
  def l9():
    file = open("#l2-4.txt","r")
    l9 = file.read()
    l9 = l9.split("\n")
    for i in range(len(l9)):
        l9[i] = l9[i].split(",")
    for i in range(len(l9)):
        for j in range(len(l9[i])):
            l9[i][j] = int(l9[i][j])
    file.close()
    return l9
    #eee
  def l10():
    file = open("#l2-5.txt","r")
    l10 = file.read()
    l10 = l10.split("\n")
    for i in range(len(l10)):
        l10[i] = l10[i].split(",")
    for i in range(len(l10)):
        for j in range(len(l10[i])):
            l10[i][j] = int(l10[i][j])
    file.close()
    return l10
    #eee
  def l11():
    file = open("#l3-1.txt","r")
    l11 = file.read()
    l11 = l11.split("\n")
    for i in range(len(l11)):
        l11[i] = l11[i].split(",")
    for i in range(len(l11)):
        for j in range(len(l11[i])):
            l11[i][j] = int(l11[i][j])
    file.close()
    return l11
    #eee
  def l12():
    file = open("#l3-2.txt","r")
    l12 = file.read()
    l12 = l12.split("\n")
    for i in range(len(l12)):
        l12[i] = l12[i].split(",")
    for i in range(len(l12)):
        for j in range(len(l12[i])):
            l12[i][j] = int(l12[i][j])
    file.close()
    return l12
    #eee
  def l13():
    file = open("#l3-3.txt","r")
    l13 = file.read()
    l13 = l13.split("\n")
    for i in range(len(l13)):
        l13[i] = l13[i].split(",")
    for i in range(len(l13)):
        for j in range(len(l13[i])):
            l13[i][j] = int(l13[i][j])
    file.close()
    return l13
    #eee
  def l14():
    file = open("#l3-4.txt","r")
    l13 = file.read()
    l13 = l13.split("\n")
    for i in range(len(l13)):
        l13[i] = l13[i].split(",")
    for i in range(len(l13)):
        for j in range(len(l13[i])):
            l13[i][j] = int(l13[i][j])
    file.close()
    return l13
  def l15():
    file = open("#l3-5.txt","r")
    l13 = file.read()
    l13 = l13.split("\n")
    for i in range(len(l13)):
        l13[i] = l13[i].split(",")
    for i in range(len(l13)):
        for j in range(len(l13[i])):
            l13[i][j] = int(l13[i][j])
    file.close()
    return l13
    #eee
  def l16():
    file = open("#l3-6.txt","r")
    l13 = file.read()
    l13 = l13.split("\n")
    for i in range(len(l13)):
        l13[i] = l13[i].split(",")
    for i in range(len(l13)):
        for j in range(len(l13[i])):
            l13[i][j] = int(l13[i][j])
    file.close()
    return l13
    #eee
  def l17():
    file = open("#l3-7.txt","r")
    l13 = file.read()
    l13 = l13.split("\n")
    for i in range(len(l13)):
        l13[i] = l13[i].split(",")
    for i in range(len(l13)):
        for j in range(len(l13[i])):
            l13[i][j] = int(l13[i][j])
    file.close()
    return l13
    #eee
print("Map:")
#┌─┐│└┘┼
print("    ┌o┐\n ┌o┐o │\n o o│ o  o┐\no┘ │o └┐  │\n ┌o┘│  o  o\n o  o ┌┼o─┘\n └─o┘ o┘")
stage = 1
world = []
running = False
peen = True  #trust me on this
hp = 1
import sys
def select_world():
  global world
  global stage
  global running
  global prev_block
  global hp
  global tk
  if running == False:
    if stage == 1:
        world = level.l1()
        prev_block = 0
    elif stage == 2:
        world = level.l2()
        prev_block = 0
    elif stage == 3:
        world = level.l3()
        prev_block = 1
    elif stage == 4:
        world = level.l4()
        prev_block = 0
    elif stage == 5:
        world = level.l5()
        prev_block = 0
    elif stage == 6:
        world = level.l6()
        prev_block = 1
    elif stage == 7:
        world = level.l7()
        prev_block = 0
    elif stage == 8:
        world = level.l8()
        prev_block = 0
    elif stage == 9:
        world = level.l9()
        prev_block = 0
    elif stage == 10:
        world = level.l10()
        prev_block = 0
    elif stage == 11:
        world = level.l11()
        prev_block = 0
    elif stage == 12:
        world = level.l12()
        prev_block = 1
    elif stage == 13:
        world = level.l13()
        prev_block = 0
    elif stage == 14:
        world = level.l14()
        prev_block = 0
    elif stage == 15:
        world = level.l15()
        prev_block = 1
    elif stage == 16:
        world = level.l16()
        prev_block = 0
    elif stage == 17:
        world = level.l17()
        prev_block = 0
    elif stage == 18:
        print("YOU HAVE COMPLETED YOUR QUEST")
        tk.destroy()
        ree.destroy()
        sys.exit()
    running = True
    hp = 1
#################################
def find_player_y():
  try:
    global world
    notfound = True
    i = 0
    while notfound:
        if 33 in world[i]:
            notfound = False
        else:
            i += 1
    return i
  except:
    return 0
def find_player_x(y):
  try:
    global world
    notfound = True
    i = 0
    while notfound:
        if world[y][i] == 33:
            notfound = False
        else:
            i += 1
    return i
  except:
    return 0
def find_y_of(obj):
 if obj_in_seen_world(obj) == True:
    global seen_world
    notfound = True
    i = 0
    while notfound:
        if obj in seen_world[i]:
            notfound = False
        else:
            i += 1
    return i
def find_x_of(obj,y):
 if obj_in_seen_world(obj) == True:
    global seen_world
    notfound = True
    i = 6
    while notfound:
        if seen_world[y][i] == obj:
            notfound = False
        else:
            i += -1
    return i
def obj_near_player(obj):
    y = find_player_y()  
    x = find_player_x(y)
    if world[y][x+1] == obj or world[y][x-1] == obj or world[y+1][x] == obj or world[y-1][x] == obj:
        return True
    else:
        return False
def find_amount_of(obj):
    global seen_world
    k = 0
    for i in range(len(seen_world)):
        for j in range(len(seen_world[i])):
            if seen_world[i][j] == obj:
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
seen_world=[[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
tk = ""
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
b1 = ""
b2 = ""
b3 = ""
b4 = ""
b5 = ""
b6 = ""
b7 = ""
c1 = ""
c2 = ""
c3 = ""
c4 = ""
c5 = ""
c6 = ""
c7 = ""
d1 = ""
d2 = ""
d3 = ""
d4 = ""
d5 = ""
d6 = ""
d7 = ""
e1 = ""
e2 = ""
e3 = ""
e4 = ""
e5 = ""
e6 = ""
e7 = ""
f1 = ""
f2 = ""
f3 = ""
f4 = ""
f5 = ""
f6 = ""
f7 = ""
g1 = ""
g2 = ""
g3 = ""
g4 = ""
g5 = ""
g6 = ""
g7 = ""
def create_world():
    global running
    global world
    select_world()
    running = True
    #this is why you dont create tkinter windows in functions
    global tk
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global d1
    global d2
    global d3
    global d4
    global d5
    global d6
    global d7
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global f7
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    tk = tkinter.Toplevel(ree)
    tk.geometry("147x147+200+400")
    tk.config(bg="#5f97ff")
    tk.title("mini mario")
    #
    a1=tkinter.Label(tk)
    a1.place(x=0,y=0,width=21,height=21)
    a2=tkinter.Label(tk)
    a2.place(x=0,y=21,width=21,height=21)
    a3=tkinter.Label(tk)
    a3.place(x=0,y=42,width=21,height=21)
    a4=tkinter.Label(tk)
    a4.place(x=0,y=63,width=21,height=21)
    a5=tkinter.Label(tk)
    a5.place(x=0,y=84,width=21,height=21)
    a6=tkinter.Label(tk)
    a6.place(x=0,y=105,width=21,height=21)
    a7=tkinter.Label(tk)
    a7.place(x=0,y=126,width=21,height=21)
    #
    b1=tkinter.Label(tk)
    b1.place(x=21,y=0,width=21,height=21)
    b2=tkinter.Label(tk)
    b2.place(x=21,y=21,width=21,height=21)
    b3=tkinter.Label(tk)
    b3.place(x=21,y=42,width=21,height=21)
    b4=tkinter.Label(tk)
    b4.place(x=21,y=63,width=21,height=21)
    b5=tkinter.Label(tk)
    b5.place(x=21,y=84,width=21,height=21)
    b6=tkinter.Label(tk)
    b6.place(x=21,y=105,width=21,height=21)
    b7=tkinter.Label(tk)
    b7.place(x=21,y=126,width=21,height=21)
    #
    c1=tkinter.Label(tk)
    c1.place(x=42,y=0,width=21,height=21)
    c2=tkinter.Label(tk)
    c2.place(x=42,y=21,width=21,height=21)
    c3=tkinter.Label(tk)
    c3.place(x=42,y=42,width=21,height=21)
    c4=tkinter.Label(tk)
    c4.place(x=42,y=63,width=21,height=21)
    c5=tkinter.Label(tk)
    c5.place(x=42,y=84,width=21,height=21)
    c6=tkinter.Label(tk)
    c6.place(x=42,y=105,width=21,height=21)
    c7=tkinter.Label(tk)
    c7.place(x=42,y=126,width=21,height=21)
    #
    d1=tkinter.Label(tk)
    d1.place(x=63,y=0,width=21,height=21)
    d2=tkinter.Label(tk)
    d2.place(x=63,y=21,width=21,height=21)
    d3=tkinter.Label(tk)
    d3.place(x=63,y=42,width=21,height=21)
    d4=tkinter.Label(tk)
    d4.place(x=63,y=63,width=21,height=21)
    d5=tkinter.Label(tk)
    d5.place(x=63,y=84,width=21,height=21)
    d6=tkinter.Label(tk)
    d6.place(x=63,y=105,width=21,height=21)
    d7=tkinter.Label(tk)
    d7.place(x=63,y=126,width=21,height=21)
    #
    e1=tkinter.Label(tk)
    e1.place(x=84,y=0,width=21,height=21)
    e2=tkinter.Label(tk)
    e2.place(x=84,y=21,width=21,height=21)
    e3=tkinter.Label(tk)
    e3.place(x=84,y=42,width=21,height=21)
    e4=tkinter.Label(tk)
    e4.place(x=84,y=63,width=21,height=21)
    e5=tkinter.Label(tk)
    e5.place(x=84,y=84,width=21,height=21)
    e6=tkinter.Label(tk)
    e6.place(x=84,y=105,width=21,height=21)
    e7=tkinter.Label(tk)
    e7.place(x=84,y=126,width=21,height=21)
    #
    f1=tkinter.Label(tk)
    f1.place(x=105,y=0,width=21,height=21)
    f2=tkinter.Label(tk)
    f2.place(x=105,y=21,width=21,height=21)
    f3=tkinter.Label(tk)
    f3.place(x=105,y=42,width=21,height=21)
    f4=tkinter.Label(tk)
    f4.place(x=105,y=63,width=21,height=21)
    f5=tkinter.Label(tk)
    f5.place(x=105,y=84,width=21,height=21)
    f6=tkinter.Label(tk)
    f6.place(x=105,y=105,width=21,height=21)
    f7=tkinter.Label(tk)
    f7.place(x=105,y=126,width=21,height=21)
    #
    g1=tkinter.Label(tk)
    g1.place(x=126,y=0,width=21,height=21)
    g2=tkinter.Label(tk)
    g2.place(x=126,y=21,width=21,height=21)
    g3=tkinter.Label(tk)
    g3.place(x=126,y=42,width=21,height=21)
    g4=tkinter.Label(tk)
    g4.place(x=126,y=63,width=21,height=21)
    g5=tkinter.Label(tk)
    g5.place(x=126,y=84,width=21,height=21)
    g6=tkinter.Label(tk)
    g6.place(x=126,y=105,width=21,height=21)
    g7=tkinter.Label(tk)
    g7.place(x=126,y=126,width=21,height=21)
    #
    tk.bind("<KeyRelease-a>",left)
    tk.bind("<KeyRelease-d>",right)
    tk.bind("<KeyRelease-w>",d_up)
    tk.bind("<KeyRelease-s>",up)
    tk.bind("<KeyRelease-x>",down)
    tk.bind("<KeyRelease-q>",d_left)
    tk.bind("<KeyRelease-e>",d_right)
    update_world()
    move_timer()
    time_()
    tkinter.mainloop()
prev_block = 0
hp = 1
score = 0
mario_dir = True
invincible = False
jump = False
##################################
def update_world():
 global running
 global peen
 if running == True:
  #fml
  global a1
  global a2
  global a3
  global a4
  global a5
  global a6
  global a7
  global b1
  global b2
  global b3
  global b4
  global b5
  global b6
  global b7
  global c1
  global c2
  global c3
  global c4
  global c5
  global c6
  global c7
  global d1
  global d2
  global d3
  global d4
  global d5
  global d6
  global d7
  global e1
  global e2
  global e3
  global e4
  global e5
  global e6
  global e7
  global f1
  global f2
  global f3
  global f4
  global f5
  global f6
  global f7
  global g1
  global g2
  global g3
  global g4
  global g5
  global g6
  global g7
  global hp
  global mario_dir
  try:
    global world
    global seen_world
    y = find_player_y()
    x = find_player_x(y)
    if obj_near_player(10) == True:
        raise SyntaxError
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
    cwater = "#443cff"
    cdark = "#050505"
    cair = "#5f97ff"
    global stage
    global prev_block
    if prev_block == 1:
        back = cwater
    elif stage == 2 or stage == 5 or stage == 8 or stage == 10 or stage == 11 or stage == 14 or stage == 16 or stage == 17:
        back = cdark
    else:
        back = cair
    e = seen_world[0][0]
    if e == 0:
        a1.config(bg=back,image=blank)
    elif e == 1:
        a1.config(bg=back,image=water)
    elif e == 2:
        a1.config(bg=back,image=brick)
    elif e == 3:
        a1.config(bg=back,image=ground)
    elif e == 4:
        a1.config(bg=back,image=blue_brick)
    elif e == 5:
        a1.config(bg=back,image=water_block)
    elif e == 6:
        a1.config(bg=back,image=coral)
    elif e == 7:
        a1.config(bg=back,image=pipe)
    elif e == 8:
        a1.config(bg=back,image=shroom)
    elif e == 9:
        a1.config(bg=back,image=stem)
    elif e == 10:
        a1.config(bg=back,image=flagpole)
    elif e == 11:
        a1.config(bg=back,image=platform)
    elif e == 12:
        a1.config(bg=back,image=coin)
    elif e == 13:
        a1.config(bg=back,image=lava)
    elif e == 14:
        a1.config(bg=back,image=castle_brick)
    elif e == 15:
        a1.config(bg=back,image=spec_block)
    elif e == 16:
        a1.config(bg=back,image=goomba)
    elif e == 17:
        a1.config(bg=back,image=beetle)
    elif e == 18:
        a1.config(bg=back,image=beetle_shell)
    elif e == 19:
        a1.config(bg=back,image=green_koopa)
    elif e == 20:
        a1.config(bg=back,image=green_shell)
    elif e == 21:
        a1.config(bg=back,image=red_koopa)
    elif e == 22:
        a1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a1.config(bg=back,image=blank)
    elif e == 24:
        a1.config(bg=back,image=squid)
    elif e == 25:
        a1.config(bg=back,image=red_fish)
    elif e == 26:
        a1.config(bg=back,image=green_fish)
    elif e == 27:
        a1.config(bg=back,image=spiny)
    elif e == 28:
        a1.config(bg=back,image=cannon)
    elif e == 29:
        a1.config(bg=back,image=bullet)
    elif e == 30:
        a1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a1.config(bg=back,image=blank)
    elif e == 32:
        a1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a1.config(bg=back,image=mario_left)
            else:
                a1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a1.config(bg=back,image=super_mario_left)
            else:
                a1.config(bg=back,image=super_mario_right)
        else:
            a1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a1.config(bg=back,image=bro)
    elif e == 35:
        a1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[0][1]
    if e == 0:
        b1.config(bg=back,image=blank)
    elif e == 1:
        b1.config(bg=back,image=water)
    elif e == 2:
        b1.config(bg=back,image=brick)
    elif e == 3:
        b1.config(bg=back,image=ground)
    elif e == 4:
        b1.config(bg=back,image=blue_brick)
    elif e == 5:
        b1.config(bg=back,image=water_block)
    elif e == 6:
        b1.config(bg=back,image=coral)
    elif e == 7:
        b1.config(bg=back,image=pipe)
    elif e == 8:
        b1.config(bg=back,image=shroom)
    elif e == 9:
        b1.config(bg=back,image=stem)
    elif e == 10:
        b1.config(bg=back,image=flagpole)
    elif e == 11:
        b1.config(bg=back,image=platform)
    elif e == 12:
        b1.config(bg=back,image=coin)
    elif e == 13:
        b1.config(bg=back,image=lava)
    elif e == 14:
        b1.config(bg=back,image=castle_brick)
    elif e == 15:
        b1.config(bg=back,image=spec_block)
    elif e == 16:
        b1.config(bg=back,image=goomba)
    elif e == 17:
        b1.config(bg=back,image=beetle)
    elif e == 18:
        b1.config(bg=back,image=beetle_shell)
    elif e == 19:
        b1.config(bg=back,image=green_koopa)
    elif e == 20:
        b1.config(bg=back,image=green_shell)
    elif e == 21:
        b1.config(bg=back,image=red_koopa)
    elif e == 22:
        b1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b1.config(bg=back,image=blank)
    elif e == 24:
        b1.config(bg=back,image=squid)
    elif e == 25:
        b1.config(bg=back,image=red_fish)
    elif e == 26:
        b1.config(bg=back,image=green_fish)
    elif e == 27:
        b1.config(bg=back,image=spiny)
    elif e == 28:
        b1.config(bg=back,image=cannon)
    elif e == 29:
        b1.config(bg=back,image=bullet)
    elif e == 30:
        b1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b1.config(bg=back,image=blank)
    elif e == 32:
        b1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b1.config(bg=back,image=mario_left)
            else:
                b1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b1.config(bg=back,image=super_mario_left)
            else:
                b1.config(bg=back,image=super_mario_right)
        else:
            b1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b1.config(bg=back,image=bro)
    elif e == 35:
        b1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[0][2]
    if e == 0:
        c1.config(bg=back,image=blank)
    elif e == 1:
        c1.config(bg=back,image=water)
    elif e == 2:
        c1.config(bg=back,image=brick)
    elif e == 3:
        c1.config(bg=back,image=ground)
    elif e == 4:
        c1.config(bg=back,image=blue_brick)
    elif e == 5:
        c1.config(bg=back,image=water_block)
    elif e == 6:
        c1.config(bg=back,image=coral)
    elif e == 7:
        c1.config(bg=back,image=pipe)
    elif e == 8:
        c1.config(bg=back,image=shroom)
    elif e == 9:
        c1.config(bg=back,image=stem)
    elif e == 10:
        c1.config(bg=back,image=flagpole)
    elif e == 11:
        c1.config(bg=back,image=platform)
    elif e == 12:
        c1.config(bg=back,image=coin)
    elif e == 13:
        c1.config(bg=back,image=lava)
    elif e == 14:
        c1.config(bg=back,image=castle_brick)
    elif e == 15:
        c1.config(bg=back,image=spec_block)
    elif e == 16:
        c1.config(bg=back,image=goomba)
    elif e == 17:
        c1.config(bg=back,image=beetle)
    elif e == 18:
        c1.config(bg=back,image=beetle_shell)
    elif e == 19:
        c1.config(bg=back,image=green_koopa)
    elif e == 20:
        c1.config(bg=back,image=green_shell)
    elif e == 21:
        c1.config(bg=back,image=red_koopa)
    elif e == 22:
        c1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c1.config(bg=back,image=blank)
    elif e == 24:
        c1.config(bg=back,image=squid)
    elif e == 25:
        c1.config(bg=back,image=red_fish)
    elif e == 26:
        c1.config(bg=back,image=green_fish)
    elif e == 27:
        c1.config(bg=back,image=spiny)
    elif e == 28:
        c1.config(bg=back,image=cannon)
    elif e == 29:
        c1.config(bg=back,image=bullet)
    elif e == 30:
        c1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c1.config(bg=back,image=blank)
    elif e == 32:
        c1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c1.config(bg=back,image=mario_left)
            else:
                c1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c1.config(bg=back,image=super_mario_left)
            else:
                c1.config(bg=back,image=super_mario_right)
        else:
            c1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c1.config(bg=back,image=bro)
    elif e == 35:
        c1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[0][3]
    if e == 0:
        d1.config(bg=back,image=blank)
    elif e == 1:
        d1.config(bg=back,image=water)
    elif e == 2:
        d1.config(bg=back,image=brick)
    elif e == 3:
        d1.config(bg=back,image=ground)
    elif e == 4:
        d1.config(bg=back,image=blue_brick)
    elif e == 5:
        d1.config(bg=back,image=water_block)
    elif e == 6:
        d1.config(bg=back,image=coral)
    elif e == 7:
        d1.config(bg=back,image=pipe)
    elif e == 8:
        d1.config(bg=back,image=shroom)
    elif e == 9:
        d1.config(bg=back,image=stem)
    elif e == 10:
        d1.config(bg=back,image=flagpole)
    elif e == 11:
        d1.config(bg=back,image=platform)
    elif e == 12:
        d1.config(bg=back,image=coin)
    elif e == 13:
        d1.config(bg=back,image=lava)
    elif e == 14:
        d1.config(bg=back,image=castle_brick)
    elif e == 15:
        d1.config(bg=back,image=spec_block)
    elif e == 16:
        d1.config(bg=back,image=goomba)
    elif e == 17:
        d1.config(bg=back,image=beetle)
    elif e == 18:
        d1.config(bg=back,image=beetle_shell)
    elif e == 19:
        d1.config(bg=back,image=green_koopa)
    elif e == 20:
        d1.config(bg=back,image=green_shell)
    elif e == 21:
        d1.config(bg=back,image=red_koopa)
    elif e == 22:
        d1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d1.config(bg=back,image=blank)
    elif e == 24:
        d1.config(bg=back,image=squid)
    elif e == 25:
        d1.config(bg=back,image=red_fish)
    elif e == 26:
        d1.config(bg=back,image=green_fish)
    elif e == 27:
        d1.config(bg=back,image=spiny)
    elif e == 28:
        d1.config(bg=back,image=cannon)
    elif e == 29:
        d1.config(bg=back,image=bullet)
    elif e == 30:
        d1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d1.config(bg=back,image=blank)
    elif e == 32:
        d1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d1.config(bg=back,image=mario_left)
            else:
                d1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d1.config(bg=back,image=super_mario_left)
            else:
                d1.config(bg=back,image=super_mario_right)
        else:
            d1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d1.config(bg=back,image=bro)
    elif e == 35:
        d1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[0][4]
    if e == 0:
        e1.config(bg=back,image=blank)
    elif e == 1:
        e1.config(bg=back,image=water)
    elif e == 2:
        e1.config(bg=back,image=brick)
    elif e == 3:
        e1.config(bg=back,image=ground)
    elif e == 4:
        e1.config(bg=back,image=blue_brick)
    elif e == 5:
        e1.config(bg=back,image=water_block)
    elif e == 6:
        e1.config(bg=back,image=coral)
    elif e == 7:
        e1.config(bg=back,image=pipe)
    elif e == 8:
        e1.config(bg=back,image=shroom)
    elif e == 9:
        e1.config(bg=back,image=stem)
    elif e == 10:
        e1.config(bg=back,image=flagpole)
    elif e == 11:
        e1.config(bg=back,image=platform)
    elif e == 12:
        e1.config(bg=back,image=coin)
    elif e == 13:
        e1.config(bg=back,image=lava)
    elif e == 14:
        e1.config(bg=back,image=castle_brick)
    elif e == 15:
        e1.config(bg=back,image=spec_block)
    elif e == 16:
        e1.config(bg=back,image=goomba)
    elif e == 17:
        e1.config(bg=back,image=beetle)
    elif e == 18:
        e1.config(bg=back,image=beetle_shell)
    elif e == 19:
        e1.config(bg=back,image=green_koopa)
    elif e == 20:
        e1.config(bg=back,image=green_shell)
    elif e == 21:
        e1.config(bg=back,image=red_koopa)
    elif e == 22:
        e1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e1.config(bg=back,image=blank)
    elif e == 24:
        e1.config(bg=back,image=squid)
    elif e == 25:
        e1.config(bg=back,image=red_fish)
    elif e == 26:
        e1.config(bg=back,image=green_fish)
    elif e == 27:
        e1.config(bg=back,image=spiny)
    elif e == 28:
        e1.config(bg=back,image=cannon)
    elif e == 29:
        e1.config(bg=back,image=bullet)
    elif e == 30:
        e1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e1.config(bg=back,image=blank)
    elif e == 32:
        e1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e1.config(bg=back,image=mario_left)
            else:
                e1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e1.config(bg=back,image=super_mario_left)
            else:
                e1.config(bg=back,image=super_mario_right)
        else:
            e1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e1.config(bg=back,image=bro)
    elif e == 35:
        e1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[0][5]
    if e == 0:
        f1.config(bg=back,image=blank)
    elif e == 1:
        f1.config(bg=back,image=water)
    elif e == 2:
        f1.config(bg=back,image=brick)
    elif e == 3:
        f1.config(bg=back,image=ground)
    elif e == 4:
        f1.config(bg=back,image=blue_brick)
    elif e == 5:
        f1.config(bg=back,image=water_block)
    elif e == 6:
        f1.config(bg=back,image=coral)
    elif e == 7:
        f1.config(bg=back,image=pipe)
    elif e == 8:
        f1.config(bg=back,image=shroom)
    elif e == 9:
        f1.config(bg=back,image=stem)
    elif e == 10:
        f1.config(bg=back,image=flagpole)
    elif e == 11:
        f1.config(bg=back,image=platform)
    elif e == 12:
        f1.config(bg=back,image=coin)
    elif e == 13:
        f1.config(bg=back,image=lava)
    elif e == 14:
        f1.config(bg=back,image=castle_brick)
    elif e == 15:
        f1.config(bg=back,image=spec_block)
    elif e == 16:
        f1.config(bg=back,image=goomba)
    elif e == 17:
        f1.config(bg=back,image=beetle)
    elif e == 18:
        f1.config(bg=back,image=beetle_shell)
    elif e == 19:
        f1.config(bg=back,image=green_koopa)
    elif e == 20:
        f1.config(bg=back,image=green_shell)
    elif e == 21:
        f1.config(bg=back,image=red_koopa)
    elif e == 22:
        f1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f1.config(bg=back,image=blank)
    elif e == 24:
        f1.config(bg=back,image=squid)
    elif e == 25:
        f1.config(bg=back,image=red_fish)
    elif e == 26:
        f1.config(bg=back,image=green_fish)
    elif e == 27:
        f1.config(bg=back,image=spiny)
    elif e == 28:
        f1.config(bg=back,image=cannon)
    elif e == 29:
        f1.config(bg=back,image=bullet)
    elif e == 30:
        f1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f1.config(bg=back,image=blank)
    elif e == 32:
        f1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f1.config(bg=back,image=mario_left)
            else:
                f1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f1.config(bg=back,image=super_mario_left)
            else:
                f1.config(bg=back,image=super_mario_right)
        else:
            f1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f1.config(bg=back,image=bro)
    elif e == 35:
        f1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[0][6]
    if e == 0:
        g1.config(bg=back,image=blank)
    elif e == 1:
        g1.config(bg=back,image=water)
    elif e == 2:
        g1.config(bg=back,image=brick)
    elif e == 3:
        g1.config(bg=back,image=ground)
    elif e == 4:
        g1.config(bg=back,image=blue_brick)
    elif e == 5:
        g1.config(bg=back,image=water_block)
    elif e == 6:
        g1.config(bg=back,image=coral)
    elif e == 7:
        g1.config(bg=back,image=pipe)
    elif e == 8:
        g1.config(bg=back,image=shroom)
    elif e == 9:
        g1.config(bg=back,image=stem)
    elif e == 10:
        g1.config(bg=back,image=flagpole)
    elif e == 11:
        g1.config(bg=back,image=platform)
    elif e == 12:
        g1.config(bg=back,image=coin)
    elif e == 13:
        g1.config(bg=back,image=lava)
    elif e == 14:
        g1.config(bg=back,image=castle_brick)
    elif e == 15:
        g1.config(bg=back,image=spec_block)
    elif e == 16:
        g1.config(bg=back,image=goomba)
    elif e == 17:
        g1.config(bg=back,image=beetle)
    elif e == 18:
        g1.config(bg=back,image=beetle_shell)
    elif e == 19:
        g1.config(bg=back,image=green_koopa)
    elif e == 20:
        g1.config(bg=back,image=green_shell)
    elif e == 21:
        g1.config(bg=back,image=red_koopa)
    elif e == 22:
        g1.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g1.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g1.config(bg=back,image=blank)
    elif e == 24:
        g1.config(bg=back,image=squid)
    elif e == 25:
        g1.config(bg=back,image=red_fish)
    elif e == 26:
        g1.config(bg=back,image=green_fish)
    elif e == 27:
        g1.config(bg=back,image=spiny)
    elif e == 28:
        g1.config(bg=back,image=cannon)
    elif e == 29:
        g1.config(bg=back,image=bullet)
    elif e == 30:
        g1.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g1.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g1.config(bg=back,image=blank)
    elif e == 32:
        g1.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g1.config(bg=back,image=mario_left)
            else:
                g1.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g1.config(bg=back,image=super_mario_left)
            else:
                g1.config(bg=back,image=super_mario_right)
        else:
            g1.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g1.config(bg=back,image=bro)
    elif e == 35:
        g1.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][0]
    if e == 0:
        a2.config(bg=back,image=blank)
    elif e == 1:
        a2.config(bg=back,image=water)
    elif e == 2:
        a2.config(bg=back,image=brick)
    elif e == 3:
        a2.config(bg=back,image=ground)
    elif e == 4:
        a2.config(bg=back,image=blue_brick)
    elif e == 5:
        a2.config(bg=back,image=water_block)
    elif e == 6:
        a2.config(bg=back,image=coral)
    elif e == 7:
        a2.config(bg=back,image=pipe)
    elif e == 8:
        a2.config(bg=back,image=shroom)
    elif e == 9:
        a2.config(bg=back,image=stem)
    elif e == 10:
        a2.config(bg=back,image=flagpole)
    elif e == 11:
        a2.config(bg=back,image=platform)
    elif e == 12:
        a2.config(bg=back,image=coin)
    elif e == 13:
        a2.config(bg=back,image=lava)
    elif e == 14:
        a2.config(bg=back,image=castle_brick)
    elif e == 15:
        a2.config(bg=back,image=spec_block)
    elif e == 16:
        a2.config(bg=back,image=goomba)
    elif e == 17:
        a2.config(bg=back,image=beetle)
    elif e == 18:
        a2.config(bg=back,image=beetle_shell)
    elif e == 19:
        a2.config(bg=back,image=green_koopa)
    elif e == 20:
        a2.config(bg=back,image=green_shell)
    elif e == 21:
        a2.config(bg=back,image=red_koopa)
    elif e == 22:
        a2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a2.config(bg=back,image=blank)
    elif e == 24:
        a2.config(bg=back,image=squid)
    elif e == 25:
        a2.config(bg=back,image=red_fish)
    elif e == 26:
        a2.config(bg=back,image=green_fish)
    elif e == 27:
        a2.config(bg=back,image=spiny)
    elif e == 28:
        a2.config(bg=back,image=cannon)
    elif e == 29:
        a2.config(bg=back,image=bullet)
    elif e == 30:
        a2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a2.config(bg=back,image=blank)
    elif e == 32:
        a2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a2.config(bg=back,image=mario_left)
            else:
                a2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a2.config(bg=back,image=super_mario_left)
            else:
                a2.config(bg=back,image=super_mario_right)
        else:
            a2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a2.config(bg=back,image=bro)
    elif e == 35:
        a2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][1]
    if e == 0:
        b2.config(bg=back,image=blank)
    elif e == 1:
        b2.config(bg=back,image=water)
    elif e == 2:
        b2.config(bg=back,image=brick)
    elif e == 3:
        b2.config(bg=back,image=ground)
    elif e == 4:
        b2.config(bg=back,image=blue_brick)
    elif e == 5:
        b2.config(bg=back,image=water_block)
    elif e == 6:
        b2.config(bg=back,image=coral)
    elif e == 7:
        b2.config(bg=back,image=pipe)
    elif e == 8:
        b2.config(bg=back,image=shroom)
    elif e == 9:
        b2.config(bg=back,image=stem)
    elif e == 10:
        b2.config(bg=back,image=flagpole)
    elif e == 11:
        b2.config(bg=back,image=platform)
    elif e == 12:
        b2.config(bg=back,image=coin)
    elif e == 13:
        b2.config(bg=back,image=lava)
    elif e == 14:
        b2.config(bg=back,image=castle_brick)
    elif e == 15:
        b2.config(bg=back,image=spec_block)
    elif e == 16:
        b2.config(bg=back,image=goomba)
    elif e == 17:
        b2.config(bg=back,image=beetle)
    elif e == 18:
        b2.config(bg=back,image=beetle_shell)
    elif e == 19:
        b2.config(bg=back,image=green_koopa)
    elif e == 20:
        b2.config(bg=back,image=green_shell)
    elif e == 21:
        b2.config(bg=back,image=red_koopa)
    elif e == 22:
        b2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b2.config(bg=back,image=blank)
    elif e == 24:
        b2.config(bg=back,image=squid)
    elif e == 25:
        b2.config(bg=back,image=red_fish)
    elif e == 26:
        b2.config(bg=back,image=green_fish)
    elif e == 27:
        b2.config(bg=back,image=spiny)
    elif e == 28:
        b2.config(bg=back,image=cannon)
    elif e == 29:
        b2.config(bg=back,image=bullet)
    elif e == 30:
        b2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b2.config(bg=back,image=blank)
    elif e == 32:
        b2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b2.config(bg=back,image=mario_left)
            else:
                b2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b2.config(bg=back,image=super_mario_left)
            else:
                b2.config(bg=back,image=super_mario_right)
        else:
            b2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b2.config(bg=back,image=bro)
    elif e == 35:
        b2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][2]
    if e == 0:
        c2.config(bg=back,image=blank)
    elif e == 1:
        c2.config(bg=back,image=water)
    elif e == 2:
        c2.config(bg=back,image=brick)
    elif e == 3:
        c2.config(bg=back,image=ground)
    elif e == 4:
        c2.config(bg=back,image=blue_brick)
    elif e == 5:
        c2.config(bg=back,image=water_block)
    elif e == 6:
        c2.config(bg=back,image=coral)
    elif e == 7:
        c2.config(bg=back,image=pipe)
    elif e == 8:
        c2.config(bg=back,image=shroom)
    elif e == 9:
        c2.config(bg=back,image=stem)
    elif e == 10:
        c2.config(bg=back,image=flagpole)
    elif e == 11:
        c2.config(bg=back,image=platform)
    elif e == 12:
        c2.config(bg=back,image=coin)
    elif e == 13:
        c2.config(bg=back,image=lava)
    elif e == 14:
        c2.config(bg=back,image=castle_brick)
    elif e == 15:
        c2.config(bg=back,image=spec_block)
    elif e == 16:
        c2.config(bg=back,image=goomba)
    elif e == 17:
        c2.config(bg=back,image=beetle)
    elif e == 18:
        c2.config(bg=back,image=beetle_shell)
    elif e == 19:
        c2.config(bg=back,image=green_koopa)
    elif e == 20:
        c2.config(bg=back,image=green_shell)
    elif e == 21:
        c2.config(bg=back,image=red_koopa)
    elif e == 22:
        c2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c2.config(bg=back,image=blank)
    elif e == 24:
        c2.config(bg=back,image=squid)
    elif e == 25:
        c2.config(bg=back,image=red_fish)
    elif e == 26:
        c2.config(bg=back,image=green_fish)
    elif e == 27:
        c2.config(bg=back,image=spiny)
    elif e == 28:
        c2.config(bg=back,image=cannon)
    elif e == 29:
        c2.config(bg=back,image=bullet)
    elif e == 30:
        c2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c2.config(bg=back,image=blank)
    elif e == 32:
        c2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c2.config(bg=back,image=mario_left)
            else:
                c2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c2.config(bg=back,image=super_mario_left)
            else:
                c2.config(bg=back,image=super_mario_right)
        else:
            c2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c2.config(bg=back,image=bro)
    elif e == 35:
        c2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][3]
    if e == 0:
        d2.config(bg=back,image=blank)
    elif e == 1:
        d2.config(bg=back,image=water)
    elif e == 2:
        d2.config(bg=back,image=brick)
    elif e == 3:
        d2.config(bg=back,image=ground)
    elif e == 4:
        d2.config(bg=back,image=blue_brick)
    elif e == 5:
        d2.config(bg=back,image=water_block)
    elif e == 6:
        d2.config(bg=back,image=coral)
    elif e == 7:
        d2.config(bg=back,image=pipe)
    elif e == 8:
        d2.config(bg=back,image=shroom)
    elif e == 9:
        d2.config(bg=back,image=stem)
    elif e == 10:
        d2.config(bg=back,image=flagpole)
    elif e == 11:
        d2.config(bg=back,image=platform)
    elif e == 12:
        d2.config(bg=back,image=coin)
    elif e == 13:
        d2.config(bg=back,image=lava)
    elif e == 14:
        d2.config(bg=back,image=castle_brick)
    elif e == 15:
        d2.config(bg=back,image=spec_block)
    elif e == 16:
        d2.config(bg=back,image=goomba)
    elif e == 17:
        d2.config(bg=back,image=beetle)
    elif e == 18:
        d2.config(bg=back,image=beetle_shell)
    elif e == 19:
        d2.config(bg=back,image=green_koopa)
    elif e == 20:
        d2.config(bg=back,image=green_shell)
    elif e == 21:
        d2.config(bg=back,image=red_koopa)
    elif e == 22:
        d2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d2.config(bg=back,image=blank)
    elif e == 24:
        d2.config(bg=back,image=squid)
    elif e == 25:
        d2.config(bg=back,image=red_fish)
    elif e == 26:
        d2.config(bg=back,image=green_fish)
    elif e == 27:
        d2.config(bg=back,image=spiny)
    elif e == 28:
        d2.config(bg=back,image=cannon)
    elif e == 29:
        d2.config(bg=back,image=bullet)
    elif e == 30:
        d2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d2.config(bg=back,image=blank)
    elif e == 32:
        d2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d2.config(bg=back,image=mario_left)
            else:
                d2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d2.config(bg=back,image=super_mario_left)
            else:
                d2.config(bg=back,image=super_mario_right)
        else:
            d2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d2.config(bg=back,image=bro)
    elif e == 35:
        d2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][4]
    if e == 0:
        e2.config(bg=back,image=blank)
    elif e == 1:
        e2.config(bg=back,image=water)
    elif e == 2:
        e2.config(bg=back,image=brick)
    elif e == 3:
        e2.config(bg=back,image=ground)
    elif e == 4:
        e2.config(bg=back,image=blue_brick)
    elif e == 5:
        e2.config(bg=back,image=water_block)
    elif e == 6:
        e2.config(bg=back,image=coral)
    elif e == 7:
        e2.config(bg=back,image=pipe)
    elif e == 8:
        e2.config(bg=back,image=shroom)
    elif e == 9:
        e2.config(bg=back,image=stem)
    elif e == 10:
        e2.config(bg=back,image=flagpole)
    elif e == 11:
        e2.config(bg=back,image=platform)
    elif e == 12:
        e2.config(bg=back,image=coin)
    elif e == 13:
        e2.config(bg=back,image=lava)
    elif e == 14:
        e2.config(bg=back,image=castle_brick)
    elif e == 15:
        e2.config(bg=back,image=spec_block)
    elif e == 16:
        e2.config(bg=back,image=goomba)
    elif e == 17:
        e2.config(bg=back,image=beetle)
    elif e == 18:
        e2.config(bg=back,image=beetle_shell)
    elif e == 19:
        e2.config(bg=back,image=green_koopa)
    elif e == 20:
        e2.config(bg=back,image=green_shell)
    elif e == 21:
        e2.config(bg=back,image=red_koopa)
    elif e == 22:
        e2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e2.config(bg=back,image=blank)
    elif e == 24:
        e2.config(bg=back,image=squid)
    elif e == 25:
        e2.config(bg=back,image=red_fish)
    elif e == 26:
        e2.config(bg=back,image=green_fish)
    elif e == 27:
        e2.config(bg=back,image=spiny)
    elif e == 28:
        e2.config(bg=back,image=cannon)
    elif e == 29:
        e2.config(bg=back,image=bullet)
    elif e == 30:
        e2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e2.config(bg=back,image=blank)
    elif e == 32:
        e2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e2.config(bg=back,image=mario_left)
            else:
                e2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e2.config(bg=back,image=super_mario_left)
            else:
                e2.config(bg=back,image=super_mario_right)
        else:
            e2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e2.config(bg=back,image=bro)
    elif e == 35:
        e2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][5]
    if e == 0:
        f2.config(bg=back,image=blank)
    elif e == 1:
        f2.config(bg=back,image=water)
    elif e == 2:
        f2.config(bg=back,image=brick)
    elif e == 3:
        f2.config(bg=back,image=ground)
    elif e == 4:
        f2.config(bg=back,image=blue_brick)
    elif e == 5:
        f2.config(bg=back,image=water_block)
    elif e == 6:
        f2.config(bg=back,image=coral)
    elif e == 7:
        f2.config(bg=back,image=pipe)
    elif e == 8:
        f2.config(bg=back,image=shroom)
    elif e == 9:
        f2.config(bg=back,image=stem)
    elif e == 10:
        f2.config(bg=back,image=flagpole)
    elif e == 11:
        f2.config(bg=back,image=platform)
    elif e == 12:
        f2.config(bg=back,image=coin)
    elif e == 13:
        f2.config(bg=back,image=lava)
    elif e == 14:
        f2.config(bg=back,image=castle_brick)
    elif e == 15:
        f2.config(bg=back,image=spec_block)
    elif e == 16:
        f2.config(bg=back,image=goomba)
    elif e == 17:
        f2.config(bg=back,image=beetle)
    elif e == 18:
        f2.config(bg=back,image=beetle_shell)
    elif e == 19:
        f2.config(bg=back,image=green_koopa)
    elif e == 20:
        f2.config(bg=back,image=green_shell)
    elif e == 21:
        f2.config(bg=back,image=red_koopa)
    elif e == 22:
        f2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f2.config(bg=back,image=blank)
    elif e == 24:
        f2.config(bg=back,image=squid)
    elif e == 25:
        f2.config(bg=back,image=red_fish)
    elif e == 26:
        f2.config(bg=back,image=green_fish)
    elif e == 27:
        f2.config(bg=back,image=spiny)
    elif e == 28:
        f2.config(bg=back,image=cannon)
    elif e == 29:
        f2.config(bg=back,image=bullet)
    elif e == 30:
        f2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f2.config(bg=back,image=blank)
    elif e == 32:
        f2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f2.config(bg=back,image=mario_left)
            else:
                f2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f2.config(bg=back,image=super_mario_left)
            else:
                f2.config(bg=back,image=super_mario_right)
        else:
            f2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f2.config(bg=back,image=bro)
    elif e == 35:
        f2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[1][6]
    if e == 0:
        g2.config(bg=back,image=blank)
    elif e == 1:
        g2.config(bg=back,image=water)
    elif e == 2:
        g2.config(bg=back,image=brick)
    elif e == 3:
        g2.config(bg=back,image=ground)
    elif e == 4:
        g2.config(bg=back,image=blue_brick)
    elif e == 5:
        g2.config(bg=back,image=water_block)
    elif e == 6:
        g2.config(bg=back,image=coral)
    elif e == 7:
        g2.config(bg=back,image=pipe)
    elif e == 8:
        g2.config(bg=back,image=shroom)
    elif e == 9:
        g2.config(bg=back,image=stem)
    elif e == 10:
        g2.config(bg=back,image=flagpole)
    elif e == 11:
        g2.config(bg=back,image=platform)
    elif e == 12:
        g2.config(bg=back,image=coin)
    elif e == 13:
        g2.config(bg=back,image=lava)
    elif e == 14:
        g2.config(bg=back,image=castle_brick)
    elif e == 15:
        g2.config(bg=back,image=spec_block)
    elif e == 16:
        g2.config(bg=back,image=goomba)
    elif e == 17:
        g2.config(bg=back,image=beetle)
    elif e == 18:
        g2.config(bg=back,image=beetle_shell)
    elif e == 19:
        g2.config(bg=back,image=green_koopa)
    elif e == 20:
        g2.config(bg=back,image=green_shell)
    elif e == 21:
        g2.config(bg=back,image=red_koopa)
    elif e == 22:
        g2.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g2.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g2.config(bg=back,image=blank)
    elif e == 24:
        g2.config(bg=back,image=squid)
    elif e == 25:
        g2.config(bg=back,image=red_fish)
    elif e == 26:
        g2.config(bg=back,image=green_fish)
    elif e == 27:
        g2.config(bg=back,image=spiny)
    elif e == 28:
        g2.config(bg=back,image=cannon)
    elif e == 29:
        g2.config(bg=back,image=bullet)
    elif e == 30:
        g2.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g2.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g2.config(bg=back,image=blank)
    elif e == 32:
        g2.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g2.config(bg=back,image=mario_left)
            else:
                g2.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g2.config(bg=back,image=super_mario_left)
            else:
                g2.config(bg=back,image=super_mario_right)
        else:
            g2.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g2.config(bg=back,image=bro)
    elif e == 35:
        g2.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][0]
    if e == 0:
        a3.config(bg=back,image=blank)
    elif e == 1:
        a3.config(bg=back,image=water)
    elif e == 2:
        a3.config(bg=back,image=brick)
    elif e == 3:
        a3.config(bg=back,image=ground)
    elif e == 4:
        a3.config(bg=back,image=blue_brick)
    elif e == 5:
        a3.config(bg=back,image=water_block)
    elif e == 6:
        a3.config(bg=back,image=coral)
    elif e == 7:
        a3.config(bg=back,image=pipe)
    elif e == 8:
        a3.config(bg=back,image=shroom)
    elif e == 9:
        a3.config(bg=back,image=stem)
    elif e == 10:
        a3.config(bg=back,image=flagpole)
    elif e == 11:
        a3.config(bg=back,image=platform)
    elif e == 12:
        a3.config(bg=back,image=coin)
    elif e == 13:
        a3.config(bg=back,image=lava)
    elif e == 14:
        a3.config(bg=back,image=castle_brick)
    elif e == 15:
        a3.config(bg=back,image=spec_block)
    elif e == 16:
        a3.config(bg=back,image=goomba)
    elif e == 17:
        a3.config(bg=back,image=beetle)
    elif e == 18:
        a3.config(bg=back,image=beetle_shell)
    elif e == 19:
        a3.config(bg=back,image=green_koopa)
    elif e == 20:
        a3.config(bg=back,image=green_shell)
    elif e == 21:
        a3.config(bg=back,image=red_koopa)
    elif e == 22:
        a3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a3.config(bg=back,image=blank)
    elif e == 24:
        a3.config(bg=back,image=squid)
    elif e == 25:
        a3.config(bg=back,image=red_fish)
    elif e == 26:
        a3.config(bg=back,image=green_fish)
    elif e == 27:
        a3.config(bg=back,image=spiny)
    elif e == 28:
        a3.config(bg=back,image=cannon)
    elif e == 29:
        a3.config(bg=back,image=bullet)
    elif e == 30:
        a3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a3.config(bg=back,image=blank)
    elif e == 32:
        a3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a3.config(bg=back,image=mario_left)
            else:
                a3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a3.config(bg=back,image=super_mario_left)
            else:
                a3.config(bg=back,image=super_mario_right)
        else:
            a3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a3.config(bg=back,image=bro)
    elif e == 35:
        a3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][1]
    if e == 0:
        b3.config(bg=back,image=blank)
    elif e == 1:
        b3.config(bg=back,image=water)
    elif e == 2:
        b3.config(bg=back,image=brick)
    elif e == 3:
        b3.config(bg=back,image=ground)
    elif e == 4:
        b3.config(bg=back,image=blue_brick)
    elif e == 5:
        b3.config(bg=back,image=water_block)
    elif e == 6:
        b3.config(bg=back,image=coral)
    elif e == 7:
        b3.config(bg=back,image=pipe)
    elif e == 8:
        b3.config(bg=back,image=shroom)
    elif e == 9:
        b3.config(bg=back,image=stem)
    elif e == 10:
        b3.config(bg=back,image=flagpole)
    elif e == 11:
        b3.config(bg=back,image=platform)
    elif e == 12:
        b3.config(bg=back,image=coin)
    elif e == 13:
        b3.config(bg=back,image=lava)
    elif e == 14:
        b3.config(bg=back,image=castle_brick)
    elif e == 15:
        b3.config(bg=back,image=spec_block)
    elif e == 16:
        b3.config(bg=back,image=goomba)
    elif e == 17:
        b3.config(bg=back,image=beetle)
    elif e == 18:
        b3.config(bg=back,image=beetle_shell)
    elif e == 19:
        b3.config(bg=back,image=green_koopa)
    elif e == 20:
        b3.config(bg=back,image=green_shell)
    elif e == 21:
        b3.config(bg=back,image=red_koopa)
    elif e == 22:
        b3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b3.config(bg=back,image=blank)
    elif e == 24:
        b3.config(bg=back,image=squid)
    elif e == 25:
        b3.config(bg=back,image=red_fish)
    elif e == 26:
        b3.config(bg=back,image=green_fish)
    elif e == 27:
        b3.config(bg=back,image=spiny)
    elif e == 28:
        b3.config(bg=back,image=cannon)
    elif e == 29:
        b3.config(bg=back,image=bullet)
    elif e == 30:
        b3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b3.config(bg=back,image=blank)
    elif e == 32:
        b3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b3.config(bg=back,image=mario_left)
            else:
                b3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b3.config(bg=back,image=super_mario_left)
            else:
                b3.config(bg=back,image=super_mario_right)
        else:
            b3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b3.config(bg=back,image=bro)
    elif e == 35:
        b3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][2]
    if e == 0:
        c3.config(bg=back,image=blank)
    elif e == 1:
        c3.config(bg=back,image=water)
    elif e == 2:
        c3.config(bg=back,image=brick)
    elif e == 3:
        c3.config(bg=back,image=ground)
    elif e == 4:
        c3.config(bg=back,image=blue_brick)
    elif e == 5:
        c3.config(bg=back,image=water_block)
    elif e == 6:
        c3.config(bg=back,image=coral)
    elif e == 7:
        c3.config(bg=back,image=pipe)
    elif e == 8:
        c3.config(bg=back,image=shroom)
    elif e == 9:
        c3.config(bg=back,image=stem)
    elif e == 10:
        c3.config(bg=back,image=flagpole)
    elif e == 11:
        c3.config(bg=back,image=platform)
    elif e == 12:
        c3.config(bg=back,image=coin)
    elif e == 13:
        c3.config(bg=back,image=lava)
    elif e == 14:
        c3.config(bg=back,image=castle_brick)
    elif e == 15:
        c3.config(bg=back,image=spec_block)
    elif e == 16:
        c3.config(bg=back,image=goomba)
    elif e == 17:
        c3.config(bg=back,image=beetle)
    elif e == 18:
        c3.config(bg=back,image=beetle_shell)
    elif e == 19:
        c3.config(bg=back,image=green_koopa)
    elif e == 20:
        c3.config(bg=back,image=green_shell)
    elif e == 21:
        c3.config(bg=back,image=red_koopa)
    elif e == 22:
        c3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c3.config(bg=back,image=blank)
    elif e == 24:
        c3.config(bg=back,image=squid)
    elif e == 25:
        c3.config(bg=back,image=red_fish)
    elif e == 26:
        c3.config(bg=back,image=green_fish)
    elif e == 27:
        c3.config(bg=back,image=spiny)
    elif e == 28:
        c3.config(bg=back,image=cannon)
    elif e == 29:
        c3.config(bg=back,image=bullet)
    elif e == 30:
        c3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c3.config(bg=back,image=blank)
    elif e == 32:
        c3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c3.config(bg=back,image=mario_left)
            else:
                c3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c3.config(bg=back,image=super_mario_left)
            else:
                c3.config(bg=back,image=super_mario_right)
        else:
            c3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c3.config(bg=back,image=bro)
    elif e == 35:
        c3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][3]
    if e == 0:
        d3.config(bg=back,image=blank)
    elif e == 1:
        d3.config(bg=back,image=water)
    elif e == 2:
        d3.config(bg=back,image=brick)
    elif e == 3:
        d3.config(bg=back,image=ground)
    elif e == 4:
        d3.config(bg=back,image=blue_brick)
    elif e == 5:
        d3.config(bg=back,image=water_block)
    elif e == 6:
        d3.config(bg=back,image=coral)
    elif e == 7:
        d3.config(bg=back,image=pipe)
    elif e == 8:
        d3.config(bg=back,image=shroom)
    elif e == 9:
        d3.config(bg=back,image=stem)
    elif e == 10:
        d3.config(bg=back,image=flagpole)
    elif e == 11:
        d3.config(bg=back,image=platform)
    elif e == 12:
        d3.config(bg=back,image=coin)
    elif e == 13:
        d3.config(bg=back,image=lava)
    elif e == 14:
        d3.config(bg=back,image=castle_brick)
    elif e == 15:
        d3.config(bg=back,image=spec_block)
    elif e == 16:
        d3.config(bg=back,image=goomba)
    elif e == 17:
        d3.config(bg=back,image=beetle)
    elif e == 18:
        d3.config(bg=back,image=beetle_shell)
    elif e == 19:
        d3.config(bg=back,image=green_koopa)
    elif e == 20:
        d3.config(bg=back,image=green_shell)
    elif e == 21:
        d3.config(bg=back,image=red_koopa)
    elif e == 22:
        d3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d3.config(bg=back,image=blank)
    elif e == 24:
        d3.config(bg=back,image=squid)
    elif e == 25:
        d3.config(bg=back,image=red_fish)
    elif e == 26:
        d3.config(bg=back,image=green_fish)
    elif e == 27:
        d3.config(bg=back,image=spiny)
    elif e == 28:
        d3.config(bg=back,image=cannon)
    elif e == 29:
        d3.config(bg=back,image=bullet)
    elif e == 30:
        d3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d3.config(bg=back,image=blank)
    elif e == 32:
        d3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d3.config(bg=back,image=mario_left)
            else:
                d3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d3.config(bg=back,image=super_mario_left)
            else:
                d3.config(bg=back,image=super_mario_right)
        else:
            d3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d3.config(bg=back,image=bro)
    elif e == 35:
        d3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][4]
    if e == 0:
        e3.config(bg=back,image=blank)
    elif e == 1:
        e3.config(bg=back,image=water)
    elif e == 2:
        e3.config(bg=back,image=brick)
    elif e == 3:
        e3.config(bg=back,image=ground)
    elif e == 4:
        e3.config(bg=back,image=blue_brick)
    elif e == 5:
        e3.config(bg=back,image=water_block)
    elif e == 6:
        e3.config(bg=back,image=coral)
    elif e == 7:
        e3.config(bg=back,image=pipe)
    elif e == 8:
        e3.config(bg=back,image=shroom)
    elif e == 9:
        e3.config(bg=back,image=stem)
    elif e == 10:
        e3.config(bg=back,image=flagpole)
    elif e == 11:
        e3.config(bg=back,image=platform)
    elif e == 12:
        e3.config(bg=back,image=coin)
    elif e == 13:
        e3.config(bg=back,image=lava)
    elif e == 14:
        e3.config(bg=back,image=castle_brick)
    elif e == 15:
        e3.config(bg=back,image=spec_block)
    elif e == 16:
        e3.config(bg=back,image=goomba)
    elif e == 17:
        e3.config(bg=back,image=beetle)
    elif e == 18:
        e3.config(bg=back,image=beetle_shell)
    elif e == 19:
        e3.config(bg=back,image=green_koopa)
    elif e == 20:
        e3.config(bg=back,image=green_shell)
    elif e == 21:
        e3.config(bg=back,image=red_koopa)
    elif e == 22:
        e3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e3.config(bg=back,image=blank)
    elif e == 24:
        e3.config(bg=back,image=squid)
    elif e == 25:
        e3.config(bg=back,image=red_fish)
    elif e == 26:
        e3.config(bg=back,image=green_fish)
    elif e == 27:
        e3.config(bg=back,image=spiny)
    elif e == 28:
        e3.config(bg=back,image=cannon)
    elif e == 29:
        e3.config(bg=back,image=bullet)
    elif e == 30:
        e3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e3.config(bg=back,image=blank)
    elif e == 32:
        e3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e3.config(bg=back,image=mario_left)
            else:
                e3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e3.config(bg=back,image=super_mario_left)
            else:
                e3.config(bg=back,image=super_mario_right)
        else:
            e3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e3.config(bg=back,image=bro)
    elif e == 35:
        e3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][5]
    if e == 0:
        f3.config(bg=back,image=blank)
    elif e == 1:
        f3.config(bg=back,image=water)
    elif e == 2:
        f3.config(bg=back,image=brick)
    elif e == 3:
        f3.config(bg=back,image=ground)
    elif e == 4:
        f3.config(bg=back,image=blue_brick)
    elif e == 5:
        f3.config(bg=back,image=water_block)
    elif e == 6:
        f3.config(bg=back,image=coral)
    elif e == 7:
        f3.config(bg=back,image=pipe)
    elif e == 8:
        f3.config(bg=back,image=shroom)
    elif e == 9:
        f3.config(bg=back,image=stem)
    elif e == 10:
        f3.config(bg=back,image=flagpole)
    elif e == 11:
        f3.config(bg=back,image=platform)
    elif e == 12:
        f3.config(bg=back,image=coin)
    elif e == 13:
        f3.config(bg=back,image=lava)
    elif e == 14:
        f3.config(bg=back,image=castle_brick)
    elif e == 15:
        f3.config(bg=back,image=spec_block)
    elif e == 16:
        f3.config(bg=back,image=goomba)
    elif e == 17:
        f3.config(bg=back,image=beetle)
    elif e == 18:
        f3.config(bg=back,image=beetle_shell)
    elif e == 19:
        f3.config(bg=back,image=green_koopa)
    elif e == 20:
        f3.config(bg=back,image=green_shell)
    elif e == 21:
        f3.config(bg=back,image=red_koopa)
    elif e == 22:
        f3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f3.config(bg=back,image=blank)
    elif e == 24:
        f3.config(bg=back,image=squid)
    elif e == 25:
        f3.config(bg=back,image=red_fish)
    elif e == 26:
        f3.config(bg=back,image=green_fish)
    elif e == 27:
        f3.config(bg=back,image=spiny)
    elif e == 28:
        f3.config(bg=back,image=cannon)
    elif e == 29:
        f3.config(bg=back,image=bullet)
    elif e == 30:
        f3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f3.config(bg=back,image=blank)
    elif e == 32:
        f3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f3.config(bg=back,image=mario_left)
            else:
                f3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f3.config(bg=back,image=super_mario_left)
            else:
                f3.config(bg=back,image=super_mario_right)
        else:
            f3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f3.config(bg=back,image=bro)
    elif e == 35:
        f3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[2][6]
    if e == 0:
        g3.config(bg=back,image=blank)
    elif e == 1:
        g3.config(bg=back,image=water)
    elif e == 2:
        g3.config(bg=back,image=brick)
    elif e == 3:
        g3.config(bg=back,image=ground)
    elif e == 4:
        g3.config(bg=back,image=blue_brick)
    elif e == 5:
        g3.config(bg=back,image=water_block)
    elif e == 6:
        g3.config(bg=back,image=coral)
    elif e == 7:
        g3.config(bg=back,image=pipe)
    elif e == 8:
        g3.config(bg=back,image=shroom)
    elif e == 9:
        g3.config(bg=back,image=stem)
    elif e == 10:
        g3.config(bg=back,image=flagpole)
    elif e == 11:
        g3.config(bg=back,image=platform)
    elif e == 12:
        g3.config(bg=back,image=coin)
    elif e == 13:
        g3.config(bg=back,image=lava)
    elif e == 14:
        g3.config(bg=back,image=castle_brick)
    elif e == 15:
        g3.config(bg=back,image=spec_block)
    elif e == 16:
        g3.config(bg=back,image=goomba)
    elif e == 17:
        g3.config(bg=back,image=beetle)
    elif e == 18:
        g3.config(bg=back,image=beetle_shell)
    elif e == 19:
        g3.config(bg=back,image=green_koopa)
    elif e == 20:
        g3.config(bg=back,image=green_shell)
    elif e == 21:
        g3.config(bg=back,image=red_koopa)
    elif e == 22:
        g3.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g3.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g3.config(bg=back,image=blank)
    elif e == 24:
        g3.config(bg=back,image=squid)
    elif e == 25:
        g3.config(bg=back,image=red_fish)
    elif e == 26:
        g3.config(bg=back,image=green_fish)
    elif e == 27:
        g3.config(bg=back,image=spiny)
    elif e == 28:
        g3.config(bg=back,image=cannon)
    elif e == 29:
        g3.config(bg=back,image=bullet)
    elif e == 30:
        g3.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g3.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g3.config(bg=back,image=blank)
    elif e == 32:
        g3.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g3.config(bg=back,image=mario_left)
            else:
                g3.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g3.config(bg=back,image=super_mario_left)
            else:
                g3.config(bg=back,image=super_mario_right)
        else:
            g3.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g3.config(bg=back,image=bro)
    elif e == 35:
        g3.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][0]
    if e == 0:
        a4.config(bg=back,image=blank)
    elif e == 1:
        a4.config(bg=back,image=water)
    elif e == 2:
        a4.config(bg=back,image=brick)
    elif e == 3:
        a4.config(bg=back,image=ground)
    elif e == 4:
        a4.config(bg=back,image=blue_brick)
    elif e == 5:
        a4.config(bg=back,image=water_block)
    elif e == 6:
        a4.config(bg=back,image=coral)
    elif e == 7:
        a4.config(bg=back,image=pipe)
    elif e == 8:
        a4.config(bg=back,image=shroom)
    elif e == 9:
        a4.config(bg=back,image=stem)
    elif e == 10:
        a4.config(bg=back,image=flagpole)
    elif e == 11:
        a4.config(bg=back,image=platform)
    elif e == 12:
        a4.config(bg=back,image=coin)
    elif e == 13:
        a4.config(bg=back,image=lava)
    elif e == 14:
        a4.config(bg=back,image=castle_brick)
    elif e == 15:
        a4.config(bg=back,image=spec_block)
    elif e == 16:
        a4.config(bg=back,image=goomba)
    elif e == 17:
        a4.config(bg=back,image=beetle)
    elif e == 18:
        a4.config(bg=back,image=beetle_shell)
    elif e == 19:
        a4.config(bg=back,image=green_koopa)
    elif e == 20:
        a4.config(bg=back,image=green_shell)
    elif e == 21:
        a4.config(bg=back,image=red_koopa)
    elif e == 22:
        a4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a4.config(bg=back,image=blank)
    elif e == 24:
        a4.config(bg=back,image=squid)
    elif e == 25:
        a4.config(bg=back,image=red_fish)
    elif e == 26:
        a4.config(bg=back,image=green_fish)
    elif e == 27:
        a4.config(bg=back,image=spiny)
    elif e == 28:
        a4.config(bg=back,image=cannon)
    elif e == 29:
        a4.config(bg=back,image=bullet)
    elif e == 30:
        a4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a4.config(bg=back,image=blank)
    elif e == 32:
        a4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a4.config(bg=back,image=mario_left)
            else:
                a4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a4.config(bg=back,image=super_mario_left)
            else:
                a4.config(bg=back,image=super_mario_right)
        else:
            a4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a4.config(bg=back,image=bro)
    elif e == 35:
        a4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][1]
    if e == 0:
        b4.config(bg=back,image=blank)
    elif e == 1:
        b4.config(bg=back,image=water)
    elif e == 2:
        b4.config(bg=back,image=brick)
    elif e == 3:
        b4.config(bg=back,image=ground)
    elif e == 4:
        b4.config(bg=back,image=blue_brick)
    elif e == 5:
        b4.config(bg=back,image=water_block)
    elif e == 6:
        b4.config(bg=back,image=coral)
    elif e == 7:
        b4.config(bg=back,image=pipe)
    elif e == 8:
        b4.config(bg=back,image=shroom)
    elif e == 9:
        b4.config(bg=back,image=stem)
    elif e == 10:
        b4.config(bg=back,image=flagpole)
    elif e == 11:
        b4.config(bg=back,image=platform)
    elif e == 12:
        b4.config(bg=back,image=coin)
    elif e == 13:
        b4.config(bg=back,image=lava)
    elif e == 14:
        b4.config(bg=back,image=castle_brick)
    elif e == 15:
        b4.config(bg=back,image=spec_block)
    elif e == 16:
        b4.config(bg=back,image=goomba)
    elif e == 17:
        b4.config(bg=back,image=beetle)
    elif e == 18:
        b4.config(bg=back,image=beetle_shell)
    elif e == 19:
        b4.config(bg=back,image=green_koopa)
    elif e == 20:
        b4.config(bg=back,image=green_shell)
    elif e == 21:
        b4.config(bg=back,image=red_koopa)
    elif e == 22:
        b4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b4.config(bg=back,image=blank)
    elif e == 24:
        b4.config(bg=back,image=squid)
    elif e == 25:
        b4.config(bg=back,image=red_fish)
    elif e == 26:
        b4.config(bg=back,image=green_fish)
    elif e == 27:
        b4.config(bg=back,image=spiny)
    elif e == 28:
        b4.config(bg=back,image=cannon)
    elif e == 29:
        b4.config(bg=back,image=bullet)
    elif e == 30:
        b4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b4.config(bg=back,image=blank)
    elif e == 32:
        b4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b4.config(bg=back,image=mario_left)
            else:
                b4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b4.config(bg=back,image=super_mario_left)
            else:
                b4.config(bg=back,image=super_mario_right)
        else:
            b4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b4.config(bg=back,image=bro)
    elif e == 35:
        b4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][2]
    if e == 0:
        c4.config(bg=back,image=blank)
    elif e == 1:
        c4.config(bg=back,image=water)
    elif e == 2:
        c4.config(bg=back,image=brick)
    elif e == 3:
        c4.config(bg=back,image=ground)
    elif e == 4:
        c4.config(bg=back,image=blue_brick)
    elif e == 5:
        c4.config(bg=back,image=water_block)
    elif e == 6:
        c4.config(bg=back,image=coral)
    elif e == 7:
        c4.config(bg=back,image=pipe)
    elif e == 8:
        c4.config(bg=back,image=shroom)
    elif e == 9:
        c4.config(bg=back,image=stem)
    elif e == 10:
        c4.config(bg=back,image=flagpole)
    elif e == 11:
        c4.config(bg=back,image=platform)
    elif e == 12:
        c4.config(bg=back,image=coin)
    elif e == 13:
        c4.config(bg=back,image=lava)
    elif e == 14:
        c4.config(bg=back,image=castle_brick)
    elif e == 15:
        c4.config(bg=back,image=spec_block)
    elif e == 16:
        c4.config(bg=back,image=goomba)
    elif e == 17:
        c4.config(bg=back,image=beetle)
    elif e == 18:
        c4.config(bg=back,image=beetle_shell)
    elif e == 19:
        c4.config(bg=back,image=green_koopa)
    elif e == 20:
        c4.config(bg=back,image=green_shell)
    elif e == 21:
        c4.config(bg=back,image=red_koopa)
    elif e == 22:
        c4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c4.config(bg=back,image=blank)
    elif e == 24:
        c4.config(bg=back,image=squid)
    elif e == 25:
        c4.config(bg=back,image=red_fish)
    elif e == 26:
        c4.config(bg=back,image=green_fish)
    elif e == 27:
        c4.config(bg=back,image=spiny)
    elif e == 28:
        c4.config(bg=back,image=cannon)
    elif e == 29:
        c4.config(bg=back,image=bullet)
    elif e == 30:
        c4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c4.config(bg=back,image=blank)
    elif e == 32:
        c4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c4.config(bg=back,image=mario_left)
            else:
                c4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c4.config(bg=back,image=super_mario_left)
            else:
                c4.config(bg=back,image=super_mario_right)
        else:
            c4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c4.config(bg=back,image=bro)
    elif e == 35:
        c4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][3]
    if e == 0:
        d4.config(bg=back,image=blank)
    elif e == 1:
        d4.config(bg=back,image=water)
    elif e == 2:
        d4.config(bg=back,image=brick)
    elif e == 3:
        d4.config(bg=back,image=ground)
    elif e == 4:
        d4.config(bg=back,image=blue_brick)
    elif e == 5:
        d4.config(bg=back,image=water_block)
    elif e == 6:
        d4.config(bg=back,image=coral)
    elif e == 7:
        d4.config(bg=back,image=pipe)
    elif e == 8:
        d4.config(bg=back,image=shroom)
    elif e == 9:
        d4.config(bg=back,image=stem)
    elif e == 10:
        d4.config(bg=back,image=flagpole)
    elif e == 11:
        d4.config(bg=back,image=platform)
    elif e == 12:
        d4.config(bg=back,image=coin)
    elif e == 13:
        d4.config(bg=back,image=lava)
    elif e == 14:
        d4.config(bg=back,image=castle_brick)
    elif e == 15:
        d4.config(bg=back,image=spec_block)
    elif e == 16:
        d4.config(bg=back,image=goomba)
    elif e == 17:
        d4.config(bg=back,image=beetle)
    elif e == 18:
        d4.config(bg=back,image=beetle_shell)
    elif e == 19:
        d4.config(bg=back,image=green_koopa)
    elif e == 20:
        d4.config(bg=back,image=green_shell)
    elif e == 21:
        d4.config(bg=back,image=red_koopa)
    elif e == 22:
        d4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d4.config(bg=back,image=blank)
    elif e == 24:
        d4.config(bg=back,image=squid)
    elif e == 25:
        d4.config(bg=back,image=red_fish)
    elif e == 26:
        d4.config(bg=back,image=green_fish)
    elif e == 27:
        d4.config(bg=back,image=spiny)
    elif e == 28:
        d4.config(bg=back,image=cannon)
    elif e == 29:
        d4.config(bg=back,image=bullet)
    elif e == 30:
        d4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d4.config(bg=back,image=blank)
    elif e == 32:
        d4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d4.config(bg=back,image=mario_left)
            else:
                d4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d4.config(bg=back,image=super_mario_left)
            else:
                d4.config(bg=back,image=super_mario_right)
        else:
            d4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d4.config(bg=back,image=bro)
    elif e == 35:
        d4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][4]
    if e == 0:
        e4.config(bg=back,image=blank)
    elif e == 1:
        e4.config(bg=back,image=water)
    elif e == 2:
        e4.config(bg=back,image=brick)
    elif e == 3:
        e4.config(bg=back,image=ground)
    elif e == 4:
        e4.config(bg=back,image=blue_brick)
    elif e == 5:
        e4.config(bg=back,image=water_block)
    elif e == 6:
        e4.config(bg=back,image=coral)
    elif e == 7:
        e4.config(bg=back,image=pipe)
    elif e == 8:
        e4.config(bg=back,image=shroom)
    elif e == 9:
        e4.config(bg=back,image=stem)
    elif e == 10:
        e4.config(bg=back,image=flagpole)
    elif e == 11:
        e4.config(bg=back,image=platform)
    elif e == 12:
        e4.config(bg=back,image=coin)
    elif e == 13:
        e4.config(bg=back,image=lava)
    elif e == 14:
        e4.config(bg=back,image=castle_brick)
    elif e == 15:
        e4.config(bg=back,image=spec_block)
    elif e == 16:
        e4.config(bg=back,image=goomba)
    elif e == 17:
        e4.config(bg=back,image=beetle)
    elif e == 18:
        e4.config(bg=back,image=beetle_shell)
    elif e == 19:
        e4.config(bg=back,image=green_koopa)
    elif e == 20:
        e4.config(bg=back,image=green_shell)
    elif e == 21:
        e4.config(bg=back,image=red_koopa)
    elif e == 22:
        e4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e4.config(bg=back,image=blank)
    elif e == 24:
        e4.config(bg=back,image=squid)
    elif e == 25:
        e4.config(bg=back,image=red_fish)
    elif e == 26:
        e4.config(bg=back,image=green_fish)
    elif e == 27:
        e4.config(bg=back,image=spiny)
    elif e == 28:
        e4.config(bg=back,image=cannon)
    elif e == 29:
        e4.config(bg=back,image=bullet)
    elif e == 30:
        e4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e4.config(bg=back,image=blank)
    elif e == 32:
        e4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e4.config(bg=back,image=mario_left)
            else:
                e4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e4.config(bg=back,image=super_mario_left)
            else:
                e4.config(bg=back,image=super_mario_right)
        else:
            e4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e4.config(bg=back,image=bro)
    elif e == 35:
        e4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][5]
    if e == 0:
        f4.config(bg=back,image=blank)
    elif e == 1:
        f4.config(bg=back,image=water)
    elif e == 2:
        f4.config(bg=back,image=brick)
    elif e == 3:
        f4.config(bg=back,image=ground)
    elif e == 4:
        f4.config(bg=back,image=blue_brick)
    elif e == 5:
        f4.config(bg=back,image=water_block)
    elif e == 6:
        f4.config(bg=back,image=coral)
    elif e == 7:
        f4.config(bg=back,image=pipe)
    elif e == 8:
        f4.config(bg=back,image=shroom)
    elif e == 9:
        f4.config(bg=back,image=stem)
    elif e == 10:
        f4.config(bg=back,image=flagpole)
    elif e == 11:
        f4.config(bg=back,image=platform)
    elif e == 12:
        f4.config(bg=back,image=coin)
    elif e == 13:
        f4.config(bg=back,image=lava)
    elif e == 14:
        f4.config(bg=back,image=castle_brick)
    elif e == 15:
        f4.config(bg=back,image=spec_block)
    elif e == 16:
        f4.config(bg=back,image=goomba)
    elif e == 17:
        f4.config(bg=back,image=beetle)
    elif e == 18:
        f4.config(bg=back,image=beetle_shell)
    elif e == 19:
        f4.config(bg=back,image=green_koopa)
    elif e == 20:
        f4.config(bg=back,image=green_shell)
    elif e == 21:
        f4.config(bg=back,image=red_koopa)
    elif e == 22:
        f4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f4.config(bg=back,image=blank)
    elif e == 24:
        f4.config(bg=back,image=squid)
    elif e == 25:
        f4.config(bg=back,image=red_fish)
    elif e == 26:
        f4.config(bg=back,image=green_fish)
    elif e == 27:
        f4.config(bg=back,image=spiny)
    elif e == 28:
        f4.config(bg=back,image=cannon)
    elif e == 29:
        f4.config(bg=back,image=bullet)
    elif e == 30:
        f4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f4.config(bg=back,image=blank)
    elif e == 32:
        f4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f4.config(bg=back,image=mario_left)
            else:
                f4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f4.config(bg=back,image=super_mario_left)
            else:
                f4.config(bg=back,image=super_mario_right)
        else:
            f4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f4.config(bg=back,image=bro)
    elif e == 35:
        f4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[3][6]
    if e == 0:
        g4.config(bg=back,image=blank)
    elif e == 1:
        g4.config(bg=back,image=water)
    elif e == 2:
        g4.config(bg=back,image=brick)
    elif e == 3:
        g4.config(bg=back,image=ground)
    elif e == 4:
        g4.config(bg=back,image=blue_brick)
    elif e == 5:
        g4.config(bg=back,image=water_block)
    elif e == 6:
        g4.config(bg=back,image=coral)
    elif e == 7:
        g4.config(bg=back,image=pipe)
    elif e == 8:
        g4.config(bg=back,image=shroom)
    elif e == 9:
        g4.config(bg=back,image=stem)
    elif e == 10:
        g4.config(bg=back,image=flagpole)
    elif e == 11:
        g4.config(bg=back,image=platform)
    elif e == 12:
        g4.config(bg=back,image=coin)
    elif e == 13:
        g4.config(bg=back,image=lava)
    elif e == 14:
        g4.config(bg=back,image=castle_brick)
    elif e == 15:
        g4.config(bg=back,image=spec_block)
    elif e == 16:
        g4.config(bg=back,image=goomba)
    elif e == 17:
        g4.config(bg=back,image=beetle)
    elif e == 18:
        g4.config(bg=back,image=beetle_shell)
    elif e == 19:
        g4.config(bg=back,image=green_koopa)
    elif e == 20:
        g4.config(bg=back,image=green_shell)
    elif e == 21:
        g4.config(bg=back,image=red_koopa)
    elif e == 22:
        g4.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g4.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g4.config(bg=back,image=blank)
    elif e == 24:
        g4.config(bg=back,image=squid)
    elif e == 25:
        g4.config(bg=back,image=red_fish)
    elif e == 26:
        g4.config(bg=back,image=green_fish)
    elif e == 27:
        g4.config(bg=back,image=spiny)
    elif e == 28:
        g4.config(bg=back,image=cannon)
    elif e == 29:
        g4.config(bg=back,image=bullet)
    elif e == 30:
        g4.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g4.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g4.config(bg=back,image=blank)
    elif e == 32:
        g4.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g4.config(bg=back,image=mario_left)
            else:
                g4.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g4.config(bg=back,image=super_mario_left)
            else:
                g4.config(bg=back,image=super_mario_right)
        else:
            g4.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g4.config(bg=back,image=bro)
    elif e == 35:
        g4.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][0]
    if e == 0:
        a5.config(bg=back,image=blank)
    elif e == 1:
        a5.config(bg=back,image=water)
    elif e == 2:
        a5.config(bg=back,image=brick)
    elif e == 3:
        a5.config(bg=back,image=ground)
    elif e == 4:
        a5.config(bg=back,image=blue_brick)
    elif e == 5:
        a5.config(bg=back,image=water_block)
    elif e == 6:
        a5.config(bg=back,image=coral)
    elif e == 7:
        a5.config(bg=back,image=pipe)
    elif e == 8:
        a5.config(bg=back,image=shroom)
    elif e == 9:
        a5.config(bg=back,image=stem)
    elif e == 10:
        a5.config(bg=back,image=flagpole)
    elif e == 11:
        a5.config(bg=back,image=platform)
    elif e == 12:
        a5.config(bg=back,image=coin)
    elif e == 13:
        a5.config(bg=back,image=lava)
    elif e == 14:
        a5.config(bg=back,image=castle_brick)
    elif e == 15:
        a5.config(bg=back,image=spec_block)
    elif e == 16:
        a5.config(bg=back,image=goomba)
    elif e == 17:
        a5.config(bg=back,image=beetle)
    elif e == 18:
        a5.config(bg=back,image=beetle_shell)
    elif e == 19:
        a5.config(bg=back,image=green_koopa)
    elif e == 20:
        a5.config(bg=back,image=green_shell)
    elif e == 21:
        a5.config(bg=back,image=red_koopa)
    elif e == 22:
        a5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a5.config(bg=back,image=blank)
    elif e == 24:
        a5.config(bg=back,image=squid)
    elif e == 25:
        a5.config(bg=back,image=red_fish)
    elif e == 26:
        a5.config(bg=back,image=green_fish)
    elif e == 27:
        a5.config(bg=back,image=spiny)
    elif e == 28:
        a5.config(bg=back,image=cannon)
    elif e == 29:
        a5.config(bg=back,image=bullet)
    elif e == 30:
        a5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a5.config(bg=back,image=blank)
    elif e == 32:
        a5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a5.config(bg=back,image=mario_left)
            else:
                a5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a5.config(bg=back,image=super_mario_left)
            else:
                a5.config(bg=back,image=super_mario_right)
        else:
            a5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a5.config(bg=back,image=bro)
    elif e == 35:
        a5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][1]
    if e == 0:
        b5.config(bg=back,image=blank)
    elif e == 1:
        b5.config(bg=back,image=water)
    elif e == 2:
        b5.config(bg=back,image=brick)
    elif e == 3:
        b5.config(bg=back,image=ground)
    elif e == 4:
        b5.config(bg=back,image=blue_brick)
    elif e == 5:
        b5.config(bg=back,image=water_block)
    elif e == 6:
        b5.config(bg=back,image=coral)
    elif e == 7:
        b5.config(bg=back,image=pipe)
    elif e == 8:
        b5.config(bg=back,image=shroom)
    elif e == 9:
        b5.config(bg=back,image=stem)
    elif e == 10:
        b5.config(bg=back,image=flagpole)
    elif e == 11:
        b5.config(bg=back,image=platform)
    elif e == 12:
        b5.config(bg=back,image=coin)
    elif e == 13:
        b5.config(bg=back,image=lava)
    elif e == 14:
        b5.config(bg=back,image=castle_brick)
    elif e == 15:
        b5.config(bg=back,image=spec_block)
    elif e == 16:
        b5.config(bg=back,image=goomba)
    elif e == 17:
        b5.config(bg=back,image=beetle)
    elif e == 18:
        b5.config(bg=back,image=beetle_shell)
    elif e == 19:
        b5.config(bg=back,image=green_koopa)
    elif e == 20:
        b5.config(bg=back,image=green_shell)
    elif e == 21:
        b5.config(bg=back,image=red_koopa)
    elif e == 22:
        b5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b5.config(bg=back,image=blank)
    elif e == 24:
        b5.config(bg=back,image=squid)
    elif e == 25:
        b5.config(bg=back,image=red_fish)
    elif e == 26:
        b5.config(bg=back,image=green_fish)
    elif e == 27:
        b5.config(bg=back,image=spiny)
    elif e == 28:
        b5.config(bg=back,image=cannon)
    elif e == 29:
        b5.config(bg=back,image=bullet)
    elif e == 30:
        b5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b5.config(bg=back,image=blank)
    elif e == 32:
        b5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b5.config(bg=back,image=mario_left)
            else:
                b5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b5.config(bg=back,image=super_mario_left)
            else:
                b5.config(bg=back,image=super_mario_right)
        else:
            b5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b5.config(bg=back,image=bro)
    elif e == 35:
        b5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][2]
    if e == 0:
        c5.config(bg=back,image=blank)
    elif e == 1:
        c5.config(bg=back,image=water)
    elif e == 2:
        c5.config(bg=back,image=brick)
    elif e == 3:
        c5.config(bg=back,image=ground)
    elif e == 4:
        c5.config(bg=back,image=blue_brick)
    elif e == 5:
        c5.config(bg=back,image=water_block)
    elif e == 6:
        c5.config(bg=back,image=coral)
    elif e == 7:
        c5.config(bg=back,image=pipe)
    elif e == 8:
        c5.config(bg=back,image=shroom)
    elif e == 9:
        c5.config(bg=back,image=stem)
    elif e == 10:
        c5.config(bg=back,image=flagpole)
    elif e == 11:
        c5.config(bg=back,image=platform)
    elif e == 12:
        c5.config(bg=back,image=coin)
    elif e == 13:
        c5.config(bg=back,image=lava)
    elif e == 14:
        c5.config(bg=back,image=castle_brick)
    elif e == 15:
        c5.config(bg=back,image=spec_block)
    elif e == 16:
        c5.config(bg=back,image=goomba)
    elif e == 17:
        c5.config(bg=back,image=beetle)
    elif e == 18:
        c5.config(bg=back,image=beetle_shell)
    elif e == 19:
        c5.config(bg=back,image=green_koopa)
    elif e == 20:
        c5.config(bg=back,image=green_shell)
    elif e == 21:
        c5.config(bg=back,image=red_koopa)
    elif e == 22:
        c5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c5.config(bg=back,image=blank)
    elif e == 24:
        c5.config(bg=back,image=squid)
    elif e == 25:
        c5.config(bg=back,image=red_fish)
    elif e == 26:
        c5.config(bg=back,image=green_fish)
    elif e == 27:
        c5.config(bg=back,image=spiny)
    elif e == 28:
        c5.config(bg=back,image=cannon)
    elif e == 29:
        c5.config(bg=back,image=bullet)
    elif e == 30:
        c5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c5.config(bg=back,image=blank)
    elif e == 32:
        c5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c5.config(bg=back,image=mario_left)
            else:
                c5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c5.config(bg=back,image=super_mario_left)
            else:
                c5.config(bg=back,image=super_mario_right)
        else:
            c5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c5.config(bg=back,image=bro)
    elif e == 35:
        c5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][3]
    if e == 0:
        d5.config(bg=back,image=blank)
    elif e == 1:
        d5.config(bg=back,image=water)
    elif e == 2:
        d5.config(bg=back,image=brick)
    elif e == 3:
        d5.config(bg=back,image=ground)
    elif e == 4:
        d5.config(bg=back,image=blue_brick)
    elif e == 5:
        d5.config(bg=back,image=water_block)
    elif e == 6:
        d5.config(bg=back,image=coral)
    elif e == 7:
        d5.config(bg=back,image=pipe)
    elif e == 8:
        d5.config(bg=back,image=shroom)
    elif e == 9:
        d5.config(bg=back,image=stem)
    elif e == 10:
        d5.config(bg=back,image=flagpole)
    elif e == 11:
        d5.config(bg=back,image=platform)
    elif e == 12:
        d5.config(bg=back,image=coin)
    elif e == 13:
        d5.config(bg=back,image=lava)
    elif e == 14:
        d5.config(bg=back,image=castle_brick)
    elif e == 15:
        d5.config(bg=back,image=spec_block)
    elif e == 16:
        d5.config(bg=back,image=goomba)
    elif e == 17:
        d5.config(bg=back,image=beetle)
    elif e == 18:
        d5.config(bg=back,image=beetle_shell)
    elif e == 19:
        d5.config(bg=back,image=green_koopa)
    elif e == 20:
        d5.config(bg=back,image=green_shell)
    elif e == 21:
        d5.config(bg=back,image=red_koopa)
    elif e == 22:
        d5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d5.config(bg=back,image=blank)
    elif e == 24:
        d5.config(bg=back,image=squid)
    elif e == 25:
        d5.config(bg=back,image=red_fish)
    elif e == 26:
        d5.config(bg=back,image=green_fish)
    elif e == 27:
        d5.config(bg=back,image=spiny)
    elif e == 28:
        d5.config(bg=back,image=cannon)
    elif e == 29:
        d5.config(bg=back,image=bullet)
    elif e == 30:
        d5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d5.config(bg=back,image=blank)
    elif e == 32:
        d5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d5.config(bg=back,image=mario_left)
            else:
                d5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d5.config(bg=back,image=super_mario_left)
            else:
                d5.config(bg=back,image=super_mario_right)
        else:
            d5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d5.config(bg=back,image=bro)
    elif e == 35:
        d5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][4]
    if e == 0:
        e5.config(bg=back,image=blank)
    elif e == 1:
        e5.config(bg=back,image=water)
    elif e == 2:
        e5.config(bg=back,image=brick)
    elif e == 3:
        e5.config(bg=back,image=ground)
    elif e == 4:
        e5.config(bg=back,image=blue_brick)
    elif e == 5:
        e5.config(bg=back,image=water_block)
    elif e == 6:
        e5.config(bg=back,image=coral)
    elif e == 7:
        e5.config(bg=back,image=pipe)
    elif e == 8:
        e5.config(bg=back,image=shroom)
    elif e == 9:
        e5.config(bg=back,image=stem)
    elif e == 10:
        e5.config(bg=back,image=flagpole)
    elif e == 11:
        e5.config(bg=back,image=platform)
    elif e == 12:
        e5.config(bg=back,image=coin)
    elif e == 13:
        e5.config(bg=back,image=lava)
    elif e == 14:
        e5.config(bg=back,image=castle_brick)
    elif e == 15:
        e5.config(bg=back,image=spec_block)
    elif e == 16:
        e5.config(bg=back,image=goomba)
    elif e == 17:
        e5.config(bg=back,image=beetle)
    elif e == 18:
        e5.config(bg=back,image=beetle_shell)
    elif e == 19:
        e5.config(bg=back,image=green_koopa)
    elif e == 20:
        e5.config(bg=back,image=green_shell)
    elif e == 21:
        e5.config(bg=back,image=red_koopa)
    elif e == 22:
        e5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e5.config(bg=back,image=blank)
    elif e == 24:
        e5.config(bg=back,image=squid)
    elif e == 25:
        e5.config(bg=back,image=red_fish)
    elif e == 26:
        e5.config(bg=back,image=green_fish)
    elif e == 27:
        e5.config(bg=back,image=spiny)
    elif e == 28:
        e5.config(bg=back,image=cannon)
    elif e == 29:
        e5.config(bg=back,image=bullet)
    elif e == 30:
        e5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e5.config(bg=back,image=blank)
    elif e == 32:
        e5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e5.config(bg=back,image=mario_left)
            else:
                e5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e5.config(bg=back,image=super_mario_left)
            else:
                e5.config(bg=back,image=super_mario_right)
        else:
            e5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e5.config(bg=back,image=bro)
    elif e == 35:
        e5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][5]
    if e == 0:
        f5.config(bg=back,image=blank)
    elif e == 1:
        f5.config(bg=back,image=water)
    elif e == 2:
        f5.config(bg=back,image=brick)
    elif e == 3:
        f5.config(bg=back,image=ground)
    elif e == 4:
        f5.config(bg=back,image=blue_brick)
    elif e == 5:
        f5.config(bg=back,image=water_block)
    elif e == 6:
        f5.config(bg=back,image=coral)
    elif e == 7:
        f5.config(bg=back,image=pipe)
    elif e == 8:
        f5.config(bg=back,image=shroom)
    elif e == 9:
        f5.config(bg=back,image=stem)
    elif e == 10:
        f5.config(bg=back,image=flagpole)
    elif e == 11:
        f5.config(bg=back,image=platform)
    elif e == 12:
        f5.config(bg=back,image=coin)
    elif e == 13:
        f5.config(bg=back,image=lava)
    elif e == 14:
        f5.config(bg=back,image=castle_brick)
    elif e == 15:
        f5.config(bg=back,image=spec_block)
    elif e == 16:
        f5.config(bg=back,image=goomba)
    elif e == 17:
        f5.config(bg=back,image=beetle)
    elif e == 18:
        f5.config(bg=back,image=beetle_shell)
    elif e == 19:
        f5.config(bg=back,image=green_koopa)
    elif e == 20:
        f5.config(bg=back,image=green_shell)
    elif e == 21:
        f5.config(bg=back,image=red_koopa)
    elif e == 22:
        f5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f5.config(bg=back,image=blank)
    elif e == 24:
        f5.config(bg=back,image=squid)
    elif e == 25:
        f5.config(bg=back,image=red_fish)
    elif e == 26:
        f5.config(bg=back,image=green_fish)
    elif e == 27:
        f5.config(bg=back,image=spiny)
    elif e == 28:
        f5.config(bg=back,image=cannon)
    elif e == 29:
        f5.config(bg=back,image=bullet)
    elif e == 30:
        f5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f5.config(bg=back,image=blank)
    elif e == 32:
        f5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f5.config(bg=back,image=mario_left)
            else:
                f5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f5.config(bg=back,image=super_mario_left)
            else:
                f5.config(bg=back,image=super_mario_right)
        else:
            f5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f5.config(bg=back,image=bro)
    elif e == 35:
        f5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[4][6]
    if e == 0:
        g5.config(bg=back,image=blank)
    elif e == 1:
        g5.config(bg=back,image=water)
    elif e == 2:
        g5.config(bg=back,image=brick)
    elif e == 3:
        g5.config(bg=back,image=ground)
    elif e == 4:
        g5.config(bg=back,image=blue_brick)
    elif e == 5:
        g5.config(bg=back,image=water_block)
    elif e == 6:
        g5.config(bg=back,image=coral)
    elif e == 7:
        g5.config(bg=back,image=pipe)
    elif e == 8:
        g5.config(bg=back,image=shroom)
    elif e == 9:
        g5.config(bg=back,image=stem)
    elif e == 10:
        g5.config(bg=back,image=flagpole)
    elif e == 11:
        g5.config(bg=back,image=platform)
    elif e == 12:
        g5.config(bg=back,image=coin)
    elif e == 13:
        g5.config(bg=back,image=lava)
    elif e == 14:
        g5.config(bg=back,image=castle_brick)
    elif e == 15:
        g5.config(bg=back,image=spec_block)
    elif e == 16:
        g5.config(bg=back,image=goomba)
    elif e == 17:
        g5.config(bg=back,image=beetle)
    elif e == 18:
        g5.config(bg=back,image=beetle_shell)
    elif e == 19:
        g5.config(bg=back,image=green_koopa)
    elif e == 20:
        g5.config(bg=back,image=green_shell)
    elif e == 21:
        g5.config(bg=back,image=red_koopa)
    elif e == 22:
        g5.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g5.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g5.config(bg=back,image=blank)
    elif e == 24:
        g5.config(bg=back,image=squid)
    elif e == 25:
        g5.config(bg=back,image=red_fish)
    elif e == 26:
        g5.config(bg=back,image=green_fish)
    elif e == 27:
        g5.config(bg=back,image=spiny)
    elif e == 28:
        g5.config(bg=back,image=cannon)
    elif e == 29:
        g5.config(bg=back,image=bullet)
    elif e == 30:
        g5.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g5.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g5.config(bg=back,image=blank)
    elif e == 32:
        g5.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g5.config(bg=back,image=mario_left)
            else:
                g5.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g5.config(bg=back,image=super_mario_left)
            else:
                g5.config(bg=back,image=super_mario_right)
        else:
            g5.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g5.config(bg=back,image=bro)
    elif e == 35:
        g5.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][0]
    if e == 0:
        a6.config(bg=back,image=blank)
    elif e == 1:
        a6.config(bg=back,image=water)
    elif e == 2:
        a6.config(bg=back,image=brick)
    elif e == 3:
        a6.config(bg=back,image=ground)
    elif e == 4:
        a6.config(bg=back,image=blue_brick)
    elif e == 5:
        a6.config(bg=back,image=water_block)
    elif e == 6:
        a6.config(bg=back,image=coral)
    elif e == 7:
        a6.config(bg=back,image=pipe)
    elif e == 8:
        a6.config(bg=back,image=shroom)
    elif e == 9:
        a6.config(bg=back,image=stem)
    elif e == 10:
        a6.config(bg=back,image=flagpole)
    elif e == 11:
        a6.config(bg=back,image=platform)
    elif e == 12:
        a6.config(bg=back,image=coin)
    elif e == 13:
        a6.config(bg=back,image=lava)
    elif e == 14:
        a6.config(bg=back,image=castle_brick)
    elif e == 15:
        a6.config(bg=back,image=spec_block)
    elif e == 16:
        a6.config(bg=back,image=goomba)
    elif e == 17:
        a6.config(bg=back,image=beetle)
    elif e == 18:
        a6.config(bg=back,image=beetle_shell)
    elif e == 19:
        a6.config(bg=back,image=green_koopa)
    elif e == 20:
        a6.config(bg=back,image=green_shell)
    elif e == 21:
        a6.config(bg=back,image=red_koopa)
    elif e == 22:
        a6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a6.config(bg=back,image=blank)
    elif e == 24:
        a6.config(bg=back,image=squid)
    elif e == 25:
        a6.config(bg=back,image=red_fish)
    elif e == 26:
        a6.config(bg=back,image=green_fish)
    elif e == 27:
        a6.config(bg=back,image=spiny)
    elif e == 28:
        a6.config(bg=back,image=cannon)
    elif e == 29:
        a6.config(bg=back,image=bullet)
    elif e == 30:
        a6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a6.config(bg=back,image=blank)
    elif e == 32:
        a6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a6.config(bg=back,image=mario_left)
            else:
                a6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a6.config(bg=back,image=super_mario_left)
            else:
                a6.config(bg=back,image=super_mario_right)
        else:
            a6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a6.config(bg=back,image=bro)
    elif e == 35:
        a6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][1]
    if e == 0:
        b6.config(bg=back,image=blank)
    elif e == 1:
        b6.config(bg=back,image=water)
    elif e == 2:
        b6.config(bg=back,image=brick)
    elif e == 3:
        b6.config(bg=back,image=ground)
    elif e == 4:
        b6.config(bg=back,image=blue_brick)
    elif e == 5:
        b6.config(bg=back,image=water_block)
    elif e == 6:
        b6.config(bg=back,image=coral)
    elif e == 7:
        b6.config(bg=back,image=pipe)
    elif e == 8:
        b6.config(bg=back,image=shroom)
    elif e == 9:
        b6.config(bg=back,image=stem)
    elif e == 10:
        b6.config(bg=back,image=flagpole)
    elif e == 11:
        b6.config(bg=back,image=platform)
    elif e == 12:
        b6.config(bg=back,image=coin)
    elif e == 13:
        b6.config(bg=back,image=lava)
    elif e == 14:
        b6.config(bg=back,image=castle_brick)
    elif e == 15:
        b6.config(bg=back,image=spec_block)
    elif e == 16:
        b6.config(bg=back,image=goomba)
    elif e == 17:
        b6.config(bg=back,image=beetle)
    elif e == 18:
        b6.config(bg=back,image=beetle_shell)
    elif e == 19:
        b6.config(bg=back,image=green_koopa)
    elif e == 20:
        b6.config(bg=back,image=green_shell)
    elif e == 21:
        b6.config(bg=back,image=red_koopa)
    elif e == 22:
        b6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b6.config(bg=back,image=blank)
    elif e == 24:
        b6.config(bg=back,image=squid)
    elif e == 25:
        b6.config(bg=back,image=red_fish)
    elif e == 26:
        b6.config(bg=back,image=green_fish)
    elif e == 27:
        b6.config(bg=back,image=spiny)
    elif e == 28:
        b6.config(bg=back,image=cannon)
    elif e == 29:
        b6.config(bg=back,image=bullet)
    elif e == 30:
        b6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b6.config(bg=back,image=blank)
    elif e == 32:
        b6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b6.config(bg=back,image=mario_left)
            else:
                b6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b6.config(bg=back,image=super_mario_left)
            else:
                b6.config(bg=back,image=super_mario_right)
        else:
            b6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b6.config(bg=back,image=bro)
    elif e == 35:
        b6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][2]
    if e == 0:
        c6.config(bg=back,image=blank)
    elif e == 1:
        c6.config(bg=back,image=water)
    elif e == 2:
        c6.config(bg=back,image=brick)
    elif e == 3:
        c6.config(bg=back,image=ground)
    elif e == 4:
        c6.config(bg=back,image=blue_brick)
    elif e == 5:
        c6.config(bg=back,image=water_block)
    elif e == 6:
        c6.config(bg=back,image=coral)
    elif e == 7:
        c6.config(bg=back,image=pipe)
    elif e == 8:
        c6.config(bg=back,image=shroom)
    elif e == 9:
        c6.config(bg=back,image=stem)
    elif e == 10:
        c6.config(bg=back,image=flagpole)
    elif e == 11:
        c6.config(bg=back,image=platform)
    elif e == 12:
        c6.config(bg=back,image=coin)
    elif e == 13:
        c6.config(bg=back,image=lava)
    elif e == 14:
        c6.config(bg=back,image=castle_brick)
    elif e == 15:
        c6.config(bg=back,image=spec_block)
    elif e == 16:
        c6.config(bg=back,image=goomba)
    elif e == 17:
        c6.config(bg=back,image=beetle)
    elif e == 18:
        c6.config(bg=back,image=beetle_shell)
    elif e == 19:
        c6.config(bg=back,image=green_koopa)
    elif e == 20:
        c6.config(bg=back,image=green_shell)
    elif e == 21:
        c6.config(bg=back,image=red_koopa)
    elif e == 22:
        c6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c6.config(bg=back,image=blank)
    elif e == 24:
        c6.config(bg=back,image=squid)
    elif e == 25:
        c6.config(bg=back,image=red_fish)
    elif e == 26:
        c6.config(bg=back,image=green_fish)
    elif e == 27:
        c6.config(bg=back,image=spiny)
    elif e == 28:
        c6.config(bg=back,image=cannon)
    elif e == 29:
        c6.config(bg=back,image=bullet)
    elif e == 30:
        c6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c6.config(bg=back,image=blank)
    elif e == 32:
        c6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c6.config(bg=back,image=mario_left)
            else:
                c6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c6.config(bg=back,image=super_mario_left)
            else:
                c6.config(bg=back,image=super_mario_right)
        else:
            c6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c6.config(bg=back,image=bro)
    elif e == 35:
        c6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][3]
    if e == 0:
        d6.config(bg=back,image=blank)
    elif e == 1:
        d6.config(bg=back,image=water)
    elif e == 2:
        d6.config(bg=back,image=brick)
    elif e == 3:
        d6.config(bg=back,image=ground)
    elif e == 4:
        d6.config(bg=back,image=blue_brick)
    elif e == 5:
        d6.config(bg=back,image=water_block)
    elif e == 6:
        d6.config(bg=back,image=coral)
    elif e == 7:
        d6.config(bg=back,image=pipe)
    elif e == 8:
        d6.config(bg=back,image=shroom)
    elif e == 9:
        d6.config(bg=back,image=stem)
    elif e == 10:
        d6.config(bg=back,image=flagpole)
    elif e == 11:
        d6.config(bg=back,image=platform)
    elif e == 12:
        d6.config(bg=back,image=coin)
    elif e == 13:
        d6.config(bg=back,image=lava)
    elif e == 14:
        d6.config(bg=back,image=castle_brick)
    elif e == 15:
        d6.config(bg=back,image=spec_block)
    elif e == 16:
        d6.config(bg=back,image=goomba)
    elif e == 17:
        d6.config(bg=back,image=beetle)
    elif e == 18:
        d6.config(bg=back,image=beetle_shell)
    elif e == 19:
        d6.config(bg=back,image=green_koopa)
    elif e == 20:
        d6.config(bg=back,image=green_shell)
    elif e == 21:
        d6.config(bg=back,image=red_koopa)
    elif e == 22:
        d6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d6.config(bg=back,image=blank)
    elif e == 24:
        d6.config(bg=back,image=squid)
    elif e == 25:
        d6.config(bg=back,image=red_fish)
    elif e == 26:
        d6.config(bg=back,image=green_fish)
    elif e == 27:
        d6.config(bg=back,image=spiny)
    elif e == 28:
        d6.config(bg=back,image=cannon)
    elif e == 29:
        d6.config(bg=back,image=bullet)
    elif e == 30:
        d6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d6.config(bg=back,image=blank)
    elif e == 32:
        d6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d6.config(bg=back,image=mario_left)
            else:
                d6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d6.config(bg=back,image=super_mario_left)
            else:
                d6.config(bg=back,image=super_mario_right)
        else:
            d6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d6.config(bg=back,image=bro)
    elif e == 35:
        d6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][4]
    if e == 0:
        e6.config(bg=back,image=blank)
    elif e == 1:
        e6.config(bg=back,image=water)
    elif e == 2:
        e6.config(bg=back,image=brick)
    elif e == 3:
        e6.config(bg=back,image=ground)
    elif e == 4:
        e6.config(bg=back,image=blue_brick)
    elif e == 5:
        e6.config(bg=back,image=water_block)
    elif e == 6:
        e6.config(bg=back,image=coral)
    elif e == 7:
        e6.config(bg=back,image=pipe)
    elif e == 8:
        e6.config(bg=back,image=shroom)
    elif e == 9:
        e6.config(bg=back,image=stem)
    elif e == 10:
        e6.config(bg=back,image=flagpole)
    elif e == 11:
        e6.config(bg=back,image=platform)
    elif e == 12:
        e6.config(bg=back,image=coin)
    elif e == 13:
        e6.config(bg=back,image=lava)
    elif e == 14:
        e6.config(bg=back,image=castle_brick)
    elif e == 15:
        e6.config(bg=back,image=spec_block)
    elif e == 16:
        e6.config(bg=back,image=goomba)
    elif e == 17:
        e6.config(bg=back,image=beetle)
    elif e == 18:
        e6.config(bg=back,image=beetle_shell)
    elif e == 19:
        e6.config(bg=back,image=green_koopa)
    elif e == 20:
        e6.config(bg=back,image=green_shell)
    elif e == 21:
        e6.config(bg=back,image=red_koopa)
    elif e == 22:
        e6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e6.config(bg=back,image=blank)
    elif e == 24:
        e6.config(bg=back,image=squid)
    elif e == 25:
        e6.config(bg=back,image=red_fish)
    elif e == 26:
        e6.config(bg=back,image=green_fish)
    elif e == 27:
        e6.config(bg=back,image=spiny)
    elif e == 28:
        e6.config(bg=back,image=cannon)
    elif e == 29:
        e6.config(bg=back,image=bullet)
    elif e == 30:
        e6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e6.config(bg=back,image=blank)
    elif e == 32:
        e6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e6.config(bg=back,image=mario_left)
            else:
                e6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e6.config(bg=back,image=super_mario_left)
            else:
                e6.config(bg=back,image=super_mario_right)
        else:
            e6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e6.config(bg=back,image=bro)
    elif e == 35:
        e6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][5]
    if e == 0:
        f6.config(bg=back,image=blank)
    elif e == 1:
        f6.config(bg=back,image=water)
    elif e == 2:
        f6.config(bg=back,image=brick)
    elif e == 3:
        f6.config(bg=back,image=ground)
    elif e == 4:
        f6.config(bg=back,image=blue_brick)
    elif e == 5:
        f6.config(bg=back,image=water_block)
    elif e == 6:
        f6.config(bg=back,image=coral)
    elif e == 7:
        f6.config(bg=back,image=pipe)
    elif e == 8:
        f6.config(bg=back,image=shroom)
    elif e == 9:
        f6.config(bg=back,image=stem)
    elif e == 10:
        f6.config(bg=back,image=flagpole)
    elif e == 11:
        f6.config(bg=back,image=platform)
    elif e == 12:
        f6.config(bg=back,image=coin)
    elif e == 13:
        f6.config(bg=back,image=lava)
    elif e == 14:
        f6.config(bg=back,image=castle_brick)
    elif e == 15:
        f6.config(bg=back,image=spec_block)
    elif e == 16:
        f6.config(bg=back,image=goomba)
    elif e == 17:
        f6.config(bg=back,image=beetle)
    elif e == 18:
        f6.config(bg=back,image=beetle_shell)
    elif e == 19:
        f6.config(bg=back,image=green_koopa)
    elif e == 20:
        f6.config(bg=back,image=green_shell)
    elif e == 21:
        f6.config(bg=back,image=red_koopa)
    elif e == 22:
        f6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f6.config(bg=back,image=blank)
    elif e == 24:
        f6.config(bg=back,image=squid)
    elif e == 25:
        f6.config(bg=back,image=red_fish)
    elif e == 26:
        f6.config(bg=back,image=green_fish)
    elif e == 27:
        f6.config(bg=back,image=spiny)
    elif e == 28:
        f6.config(bg=back,image=cannon)
    elif e == 29:
        f6.config(bg=back,image=bullet)
    elif e == 30:
        f6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f6.config(bg=back,image=blank)
    elif e == 32:
        f6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f6.config(bg=back,image=mario_left)
            else:
                f6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f6.config(bg=back,image=super_mario_left)
            else:
                f6.config(bg=back,image=super_mario_right)
        else:
            f6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f6.config(bg=back,image=bro)
    elif e == 35:
        f6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[5][6]
    if e == 0:
        g6.config(bg=back,image=blank)
    elif e == 1:
        g6.config(bg=back,image=water)
    elif e == 2:
        g6.config(bg=back,image=brick)
    elif e == 3:
        g6.config(bg=back,image=ground)
    elif e == 4:
        g6.config(bg=back,image=blue_brick)
    elif e == 5:
        g6.config(bg=back,image=water_block)
    elif e == 6:
        g6.config(bg=back,image=coral)
    elif e == 7:
        g6.config(bg=back,image=pipe)
    elif e == 8:
        g6.config(bg=back,image=shroom)
    elif e == 9:
        g6.config(bg=back,image=stem)
    elif e == 10:
        g6.config(bg=back,image=flagpole)
    elif e == 11:
        g6.config(bg=back,image=platform)
    elif e == 12:
        g6.config(bg=back,image=coin)
    elif e == 13:
        g6.config(bg=back,image=lava)
    elif e == 14:
        g6.config(bg=back,image=castle_brick)
    elif e == 15:
        g6.config(bg=back,image=spec_block)
    elif e == 16:
        g6.config(bg=back,image=goomba)
    elif e == 17:
        g6.config(bg=back,image=beetle)
    elif e == 18:
        g6.config(bg=back,image=beetle_shell)
    elif e == 19:
        g6.config(bg=back,image=green_koopa)
    elif e == 20:
        g6.config(bg=back,image=green_shell)
    elif e == 21:
        g6.config(bg=back,image=red_koopa)
    elif e == 22:
        g6.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g6.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g6.config(bg=back,image=blank)
    elif e == 24:
        g6.config(bg=back,image=squid)
    elif e == 25:
        g6.config(bg=back,image=red_fish)
    elif e == 26:
        g6.config(bg=back,image=green_fish)
    elif e == 27:
        g6.config(bg=back,image=spiny)
    elif e == 28:
        g6.config(bg=back,image=cannon)
    elif e == 29:
        g6.config(bg=back,image=bullet)
    elif e == 30:
        g6.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g6.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g6.config(bg=back,image=blank)
    elif e == 32:
        g6.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g6.config(bg=back,image=mario_left)
            else:
                g6.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g6.config(bg=back,image=super_mario_left)
            else:
                g6.config(bg=back,image=super_mario_right)
        else:
            g6.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g6.config(bg=back,image=bro)
    elif e == 35:
        g6.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][0]
    if e == 0:
        a7.config(bg=back,image=blank)
    elif e == 1:
        a7.config(bg=back,image=water)
    elif e == 2:
        a7.config(bg=back,image=brick)
    elif e == 3:
        a7.config(bg=back,image=ground)
    elif e == 4:
        a7.config(bg=back,image=blue_brick)
    elif e == 5:
        a7.config(bg=back,image=water_block)
    elif e == 6:
        a7.config(bg=back,image=coral)
    elif e == 7:
        a7.config(bg=back,image=pipe)
    elif e == 8:
        a7.config(bg=back,image=shroom)
    elif e == 9:
        a7.config(bg=back,image=stem)
    elif e == 10:
        a7.config(bg=back,image=flagpole)
    elif e == 11:
        a7.config(bg=back,image=platform)
    elif e == 12:
        a7.config(bg=back,image=coin)
    elif e == 13:
        a7.config(bg=back,image=lava)
    elif e == 14:
        a7.config(bg=back,image=castle_brick)
    elif e == 15:
        a7.config(bg=back,image=spec_block)
    elif e == 16:
        a7.config(bg=back,image=goomba)
    elif e == 17:
        a7.config(bg=back,image=beetle)
    elif e == 18:
        a7.config(bg=back,image=beetle_shell)
    elif e == 19:
        a7.config(bg=back,image=green_koopa)
    elif e == 20:
        a7.config(bg=back,image=green_shell)
    elif e == 21:
        a7.config(bg=back,image=red_koopa)
    elif e == 22:
        a7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        a7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        a7.config(bg=back,image=blank)
    elif e == 24:
        a7.config(bg=back,image=squid)
    elif e == 25:
        a7.config(bg=back,image=red_fish)
    elif e == 26:
        a7.config(bg=back,image=green_fish)
    elif e == 27:
        a7.config(bg=back,image=spiny)
    elif e == 28:
        a7.config(bg=back,image=cannon)
    elif e == 29:
        a7.config(bg=back,image=bullet)
    elif e == 30:
        a7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        a7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        a7.config(bg=back,image=blank)
    elif e == 32:
        a7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                a7.config(bg=back,image=mario_left)
            else:
                a7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                a7.config(bg=back,image=super_mario_left)
            else:
                a7.config(bg=back,image=super_mario_right)
        else:
            a7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        a7.config(bg=back,image=bro)
    elif e == 35:
        a7.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][1]
    if e == 0:
        b7.config(bg=back,image=blank)
    elif e == 1:
        b7.config(bg=back,image=water)
    elif e == 2:
        b7.config(bg=back,image=brick)
    elif e == 3:
        b7.config(bg=back,image=ground)
    elif e == 4:
        b7.config(bg=back,image=blue_brick)
    elif e == 5:
        b7.config(bg=back,image=water_block)
    elif e == 6:
        b7.config(bg=back,image=coral)
    elif e == 7:
        b7.config(bg=back,image=pipe)
    elif e == 8:
        b7.config(bg=back,image=shroom)
    elif e == 9:
        b7.config(bg=back,image=stem)
    elif e == 10:
        b7.config(bg=back,image=flagpole)
    elif e == 11:
        b7.config(bg=back,image=platform)
    elif e == 12:
        b7.config(bg=back,image=coin)
    elif e == 13:
        b7.config(bg=back,image=lava)
    elif e == 14:
        b7.config(bg=back,image=castle_brick)
    elif e == 15:
        b7.config(bg=back,image=spec_block)
    elif e == 16:
        b7.config(bg=back,image=goomba)
    elif e == 17:
        b7.config(bg=back,image=beetle)
    elif e == 18:
        b7.config(bg=back,image=beetle_shell)
    elif e == 19:
        b7.config(bg=back,image=green_koopa)
    elif e == 20:
        b7.config(bg=back,image=green_shell)
    elif e == 21:
        b7.config(bg=back,image=red_koopa)
    elif e == 22:
        b7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        b7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        b7.config(bg=back,image=blank)
    elif e == 24:
        b7.config(bg=back,image=squid)
    elif e == 25:
        b7.config(bg=back,image=red_fish)
    elif e == 26:
        b7.config(bg=back,image=green_fish)
    elif e == 27:
        b7.config(bg=back,image=spiny)
    elif e == 28:
        b7.config(bg=back,image=cannon)
    elif e == 29:
        b7.config(bg=back,image=bullet)
    elif e == 30:
        b7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        b7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        b7.config(bg=back,image=blank)
    elif e == 32:
        b7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                b7.config(bg=back,image=mario_left)
            else:
                b7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                b7.config(bg=back,image=super_mario_left)
            else:
                b7.config(bg=back,image=super_mario_right)
        else:
            b7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        b7.config(bg=back,image=bro)
    elif e == 35:
        b7.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][2]
    if e == 0:
        c7.config(bg=back,image=blank)
    elif e == 1:
        c7.config(bg=back,image=water)
    elif e == 2:
        c7.config(bg=back,image=brick)
    elif e == 3:
        c7.config(bg=back,image=ground)
    elif e == 4:
        c7.config(bg=back,image=blue_brick)
    elif e == 5:
        c7.config(bg=back,image=water_block)
    elif e == 6:
        c7.config(bg=back,image=coral)
    elif e == 7:
        c7.config(bg=back,image=pipe)
    elif e == 8:
        c7.config(bg=back,image=shroom)
    elif e == 9:
        c7.config(bg=back,image=stem)
    elif e == 10:
        c7.config(bg=back,image=flagpole)
    elif e == 11:
        c7.config(bg=back,image=platform)
    elif e == 12:
        c7.config(bg=back,image=coin)
    elif e == 13:
        c7.config(bg=back,image=lava)
    elif e == 14:
        c7.config(bg=back,image=castle_brick)
    elif e == 15:
        c7.config(bg=back,image=spec_block)
    elif e == 16:
        c7.config(bg=back,image=goomba)
    elif e == 17:
        c7.config(bg=back,image=beetle)
    elif e == 18:
        c7.config(bg=back,image=beetle_shell)
    elif e == 19:
        c7.config(bg=back,image=green_koopa)
    elif e == 20:
        c7.config(bg=back,image=green_shell)
    elif e == 21:
        c7.config(bg=back,image=red_koopa)
    elif e == 22:
        c7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        c7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        c7.config(bg=back,image=blank)
    elif e == 24:
        c7.config(bg=back,image=squid)
    elif e == 25:
        c7.config(bg=back,image=red_fish)
    elif e == 26:
        c7.config(bg=back,image=green_fish)
    elif e == 27:
        c7.config(bg=back,image=spiny)
    elif e == 28:
        c7.config(bg=back,image=cannon)
    elif e == 29:
        c7.config(bg=back,image=bullet)
    elif e == 30:
        c7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        c7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        c7.config(bg=back,image=blank)
    elif e == 32:
        c7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                c7.config(bg=back,image=mario_left)
            else:
                c7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                c7.config(bg=back,image=super_mario_left)
            else:
                c7.config(bg=back,image=super_mario_right)
        else:
            c7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        c7.config(bg=back,image=bro)
    elif e == 35:
        c7.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][3]
    if e == 0:
        d7.config(bg=back,image=blank)
    elif e == 1:
        d7.config(bg=back,image=water)
    elif e == 2:
        d7.config(bg=back,image=brick)
    elif e == 3:
        d7.config(bg=back,image=ground)
    elif e == 4:
        d7.config(bg=back,image=blue_brick)
    elif e == 5:
        d7.config(bg=back,image=water_block)
    elif e == 6:
        d7.config(bg=back,image=coral)
    elif e == 7:
        d7.config(bg=back,image=pipe)
    elif e == 8:
        d7.config(bg=back,image=shroom)
    elif e == 9:
        d7.config(bg=back,image=stem)
    elif e == 10:
        d7.config(bg=back,image=flagpole)
    elif e == 11:
        d7.config(bg=back,image=platform)
    elif e == 12:
        d7.config(bg=back,image=coin)
    elif e == 13:
        d7.config(bg=back,image=lava)
    elif e == 14:
        d7.config(bg=back,image=castle_brick)
    elif e == 15:
        d7.config(bg=back,image=spec_block)
    elif e == 16:
        d7.config(bg=back,image=goomba)
    elif e == 17:
        d7.config(bg=back,image=beetle)
    elif e == 18:
        d7.config(bg=back,image=beetle_shell)
    elif e == 19:
        d7.config(bg=back,image=green_koopa)
    elif e == 20:
        d7.config(bg=back,image=green_shell)
    elif e == 21:
        d7.config(bg=back,image=red_koopa)
    elif e == 22:
        d7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        d7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        d7.config(bg=back,image=blank)
    elif e == 24:
        d7.config(bg=back,image=squid)
    elif e == 25:
        d7.config(bg=back,image=red_fish)
    elif e == 26:
        d7.config(bg=back,image=green_fish)
    elif e == 27:
        d7.config(bg=back,image=spiny)
    elif e == 28:
        d7.config(bg=back,image=cannon)
    elif e == 29:
        d7.config(bg=back,image=bullet)
    elif e == 30:
        d7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        d7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        d7.config(bg=back,image=blank)
    elif e == 32:
        d7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                d7.config(bg=back,image=mario_left)
            else:
                d7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                d7.config(bg=back,image=super_mario_left)
            else:
                d7.config(bg=back,image=super_mario_right)
        else:
            d7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        d7.config(bg=back,image=bro)
    elif e == 35:
        d7.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][4]
    if e == 0:
        e7.config(bg=back,image=blank)
    elif e == 1:
        e7.config(bg=back,image=water)
    elif e == 2:
        e7.config(bg=back,image=brick)
    elif e == 3:
        e7.config(bg=back,image=ground)
    elif e == 4:
        e7.config(bg=back,image=blue_brick)
    elif e == 5:
        e7.config(bg=back,image=water_block)
    elif e == 6:
        e7.config(bg=back,image=coral)
    elif e == 7:
        e7.config(bg=back,image=pipe)
    elif e == 8:
        e7.config(bg=back,image=shroom)
    elif e == 9:
        e7.config(bg=back,image=stem)
    elif e == 10:
        e7.config(bg=back,image=flagpole)
    elif e == 11:
        e7.config(bg=back,image=platform)
    elif e == 12:
        e7.config(bg=back,image=coin)
    elif e == 13:
        e7.config(bg=back,image=lava)
    elif e == 14:
        e7.config(bg=back,image=castle_brick)
    elif e == 15:
        e7.config(bg=back,image=spec_block)
    elif e == 16:
        e7.config(bg=back,image=goomba)
    elif e == 17:
        e7.config(bg=back,image=beetle)
    elif e == 18:
        e7.config(bg=back,image=beetle_shell)
    elif e == 19:
        e7.config(bg=back,image=green_koopa)
    elif e == 20:
        e7.config(bg=back,image=green_shell)
    elif e == 21:
        e7.config(bg=back,image=red_koopa)
    elif e == 22:
        e7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        e7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        e7.config(bg=back,image=blank)
    elif e == 24:
        e7.config(bg=back,image=squid)
    elif e == 25:
        e7.config(bg=back,image=red_fish)
    elif e == 26:
        e7.config(bg=back,image=green_fish)
    elif e == 27:
        e7.config(bg=back,image=spiny)
    elif e == 28:
        e7.config(bg=back,image=cannon)
    elif e == 29:
        e7.config(bg=back,image=bullet)
    elif e == 30:
        e7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        e7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        e7.config(bg=back,image=blank)
    elif e == 32:
        e7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                e7.config(bg=back,image=mario_left)
            else:
                e7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                e7.config(bg=back,image=super_mario_left)
            else:
                e7.config(bg=back,image=super_mario_right)
        else:
            e7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        e7.config(bg=back,image=bro)
    elif e == 35:
        e7.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][5]
    if e == 0:
        f7.config(bg=back,image=blank)
    elif e == 1:
        f7.config(bg=back,image=water)
    elif e == 2:
        f7.config(bg=back,image=brick)
    elif e == 3:
        f7.config(bg=back,image=ground)
    elif e == 4:
        f7.config(bg=back,image=blue_brick)
    elif e == 5:
        f7.config(bg=back,image=water_block)
    elif e == 6:
        f7.config(bg=back,image=coral)
    elif e == 7:
        f7.config(bg=back,image=pipe)
    elif e == 8:
        f7.config(bg=back,image=shroom)
    elif e == 9:
        f7.config(bg=back,image=stem)
    elif e == 10:
        f7.config(bg=back,image=flagpole)
    elif e == 11:
        f7.config(bg=back,image=platform)
    elif e == 12:
        f7.config(bg=back,image=coin)
    elif e == 13:
        f7.config(bg=back,image=lava)
    elif e == 14:
        f7.config(bg=back,image=castle_brick)
    elif e == 15:
        f7.config(bg=back,image=spec_block)
    elif e == 16:
        f7.config(bg=back,image=goomba)
    elif e == 17:
        f7.config(bg=back,image=beetle)
    elif e == 18:
        f7.config(bg=back,image=beetle_shell)
    elif e == 19:
        f7.config(bg=back,image=green_koopa)
    elif e == 20:
        f7.config(bg=back,image=green_shell)
    elif e == 21:
        f7.config(bg=back,image=red_koopa)
    elif e == 22:
        f7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        f7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        f7.config(bg=back,image=blank)
    elif e == 24:
        f7.config(bg=back,image=squid)
    elif e == 25:
        f7.config(bg=back,image=red_fish)
    elif e == 26:
        f7.config(bg=back,image=green_fish)
    elif e == 27:
        f7.config(bg=back,image=spiny)
    elif e == 28:
        f7.config(bg=back,image=cannon)
    elif e == 29:
        f7.config(bg=back,image=bullet)
    elif e == 30:
        f7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        f7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        f7.config(bg=back,image=blank)
    elif e == 32:
        f7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                f7.config(bg=back,image=mario_left)
            else:
                f7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                f7.config(bg=back,image=super_mario_left)
            else:
                f7.config(bg=back,image=super_mario_right)
        else:
            f7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        f7.config(bg=back,image=bro)
    elif e == 35:
        f7.config(bg=back,image=lakitu)
    else:
        pass
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    e = seen_world[6][6]
    if e == 0:
        g7.config(bg=back,image=blank)
    elif e == 1:
        g7.config(bg=back,image=water)
    elif e == 2:
        g7.config(bg=back,image=brick)
    elif e == 3:
        g7.config(bg=back,image=ground)
    elif e == 4:
        g7.config(bg=back,image=blue_brick)
    elif e == 5:
        g7.config(bg=back,image=water_block)
    elif e == 6:
        g7.config(bg=back,image=coral)
    elif e == 7:
        g7.config(bg=back,image=pipe)
    elif e == 8:
        g7.config(bg=back,image=shroom)
    elif e == 9:
        g7.config(bg=back,image=stem)
    elif e == 10:
        g7.config(bg=back,image=flagpole)
    elif e == 11:
        g7.config(bg=back,image=platform)
    elif e == 12:
        g7.config(bg=back,image=coin)
    elif e == 13:
        g7.config(bg=back,image=lava)
    elif e == 14:
        g7.config(bg=back,image=castle_brick)
    elif e == 15:
        g7.config(bg=back,image=spec_block)
    elif e == 16:
        g7.config(bg=back,image=goomba)
    elif e == 17:
        g7.config(bg=back,image=beetle)
    elif e == 18:
        g7.config(bg=back,image=beetle_shell)
    elif e == 19:
        g7.config(bg=back,image=green_koopa)
    elif e == 20:
        g7.config(bg=back,image=green_shell)
    elif e == 21:
        g7.config(bg=back,image=red_koopa)
    elif e == 22:
        g7.config(bg=back,image=red_shell)
    elif e == 23 and peen == True:
        g7.config(bg=back,image=p_plant)
    elif e == 23 and peen == False:
        g7.config(bg=back,image=blank)
    elif e == 24:
        g7.config(bg=back,image=squid)
    elif e == 25:
        g7.config(bg=back,image=red_fish)
    elif e == 26:
        g7.config(bg=back,image=green_fish)
    elif e == 27:
        g7.config(bg=back,image=spiny)
    elif e == 28:
        g7.config(bg=back,image=cannon)
    elif e == 29:
        g7.config(bg=back,image=bullet)
    elif e == 30:
        g7.config(bg=back,image=firewall)
    elif e == 31 and peen == True:
        g7.config(bg=back,image=peen_snatcher)
    elif e == 31 and peen == False:
        g7.config(bg=back,image=blank)
    elif e == 32:
        g7.config(bg=back,image=power_up)
    elif e == 33:
        if hp == 1:
            if mario_dir == False:
                g7.config(bg=back,image=mario_left)
            else:
                g7.config(bg=back,image=mario_right)
        elif hp == 2:
            if mario_dir == False:
                g7.config(bg=back,image=super_mario_left)
            else:
                g7.config(bg=back,image=super_mario_right)
        else:
            g7.config(bg=back,image=blank)
            raise OSError
    elif e == 34:
        g7.config(bg=back,image=bro)
    elif e == 35:
        g7.config(bg=back,image=lakitu)
    else:
        pass
    #print("e")
    global jump
    if not(world[y+1][x] == 0):
        jump = False
    interactions()
    interactions()
    interactions()
    interactions()
    #print(level.l1())
    #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  except SyntaxError:
    running = False
    #tk.destroy()
    print("LEVEL WIN")
    stage += 1
    select_world()
    #raise SyntaxError
  except:
    #tk.destroy()
    print("GAME OVER")
    running = False
    select_world()
def move_enemy(enemy):
    global world
    if obj_in_seen_world(enemy) == True:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(enemy)
        x = find_x_of(enemy,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y][x-1] == 0:
            world[y][x-1] = enemy
            world[y][x] = 0
    update_world()
def down_enemy(enemy):
    global world
    if obj_in_seen_world(enemy) == True:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(enemy)
        x = find_x_of(enemy,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y+1][x] == 0:
            world[y+1][x] = enemy
            world[y][x] = 0
    update_world()
time = 0
def move_fish(enemy):
    global world
    if obj_in_seen_world(enemy) == True:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(enemy)
        x = find_x_of(enemy,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y][x-1] == 1:
            world[y][x-1] = enemy
            world[y][x] = 1
    update_world()
def move_bullet():
    global world
    if obj_in_seen_world(29) == True:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(29)
        x = find_x_of(29,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y][x-1] == 0:
            world[y][x-1] = 29
            world[y][x] = 0
        else:
            world[y][x] = 0
    update_world()
def move_squid():
    global world
    if obj_in_seen_world(24) == True:
        y = find_y_of(24)
        x = find_x_of(24,y)
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if y > y2 and world[y-1][x] == 1:
            world[y-1][x] = 24
            world[y][x] = 1
        elif y < y2 and world[y+1][x] == 1:
            world[y+1][x] = 24
            world[y][x] = 1
        else:
            if world[y][x-1] == 1:
                world[y][x-1] = 24
                world[y][x] = 1
            else:
                pass
    update_world()
def spawn_bullet():
    global world
    if obj_in_seen_world(28) == True:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(28)
        x = find_x_of(28,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y][x-1] == 0:
            world[y][x-1] = 29
            update_world()
    update_world()
def spawn_spiny():
    global world
    if obj_in_seen_world(35) == True and find_amount_of(27) < 2:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(35)
        x = find_x_of(35,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y][x-1] == 0:
            world[y][x-1] = 27
    update_world()
def move_bro():
    global world
    if obj_in_seen_world(34) == True:
        y2 = find_player_y()
        x2 = find_player_x(y2)
        y = find_y_of(34)
        x = find_x_of(34,y)
        y = y-3
        x = x-3
        y = y+y2
        x = x+x2
        if world[y+1][x] == 0:
            world[y][x] = 0
            world[y+1][x] = 34
        elif world[y+1][x] == 33:
            damage()
        elif world[y-1][x] == 0:
            world[y][x] = 0
            world[y-1][x] = 34
        elif world[y-1][x] == 33:
            damage()
def time_():
    global time
    global running
    if running == True:
        time += 1
        move_world()
        ree.after(500,time_)
score = 0
sco = tkinter.Label(ree)
sco.place(x=70,y=10)
def interactions():
    global world
    global hp
    global prev_block
    global stage
    global score
    global peen
    global invincible
    sco.config(text=f"Score:\n{score}")
    y = find_player_y()
    x = find_player_x(y)
    if prev_block == 12:
        if stage == 3 or stage == 6 or stage == 12 or stage == 15:
            prev_block = 1
        else:
            prev_block = 0
        score += 1
    if obj_near_player(13) == True:
        damage()
    if world[y-1][x] == 15:
        score += 1
        world[y-1][x] = 2
    if world[y+1][x] == 16:
        world[y+1][x] = 0
        score += 2
    #damage script
    if world[y][x+1] == 16 or world[y][x+1] == 17 or world[y][x+1] == 19 or world[y][x+1] == 21 or world[y][x+1] == 27 or world[y][x+1] == 25 or world[y][x+1] == 26 or world[y][x+1] == 29:
        damage()
    if world[y+1][x] == 17:
        world[y+1][x] = 18
        score += 2
    if world[y+1][x] == 19:
        world[y+1][x] = 20
        score += 2
    if world[y+1][x] == 21:
        world[y+1][x] = 22
        score += 2
    if world[y+1][x] == 29:
        world[y+1][x] = 0
        score += 2
    if world[y+1][x] == 27:
        damage()
    if (prev_block == 23 or prev_block == 31) and peen == True:
        damage()
    if obj_near_player(24) == True:
        damage()
    if prev_block == 30:
        damage()
    if prev_block == 32:
        hp = 2
        if stage == 3 or stage == 6 or stage == 12 or stage == 15:
            prev_block = 1
        else:
            prev_block = 0
    if score > 32:
        score = 0
        hp = 2
    if prev_block == 29 or prev_block == 26 or prev_block == 25 or prev_block == 16 or prev_block == 17 or prev_block == 19 or prev_block == 21 or prev_block == 27:
        damage()
def move_world():
    global world
    global time
    global peen
    if time % 6 == 0:
        if peen == True:
            peen = False
        else:
            peen = True
        spawn_bullet()
        move_squid()
        spawn_spiny()
    move_bro()
    if not time % 6 == 0:
        move_bullet()
        move_enemy(27)
    down_enemy(27)
    move_fish(25)
    move_fish(26)
    down_enemy(16)
    down_enemy(17)
    down_enemy(19)
    down_enemy(21)
    move_enemy(16)
    move_enemy(17)
    move_enemy(19)
    move_enemy(21)
    interactions()
    update_world()
go_through = [0,1,11,12,13,30,32,31,23,29,25,26,16,17,19,21,18,20,22,27]
go_through2 = [0,1,11,12,13,30,32,31,23,29,25,26,16,17,19,21,18,20,22,27]
fly = [1,11]
moves = 1
def move_timer():
    global moves
    moves = 1
    ree.after(200,move_timer)
move_timer()
###################################
def up(event): #up is world [y-1][x]
  try:
    global jump
    global world
    global prev_block
    global moves
    global fly
    global go_through
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y-1][x] in go_through) and (moves == 1) and (jump == False or prev_block in fly):    
        world[y][x] = prev_block
        prev_block = world[y-1][x]
        world[y-1][x] = 33
    else:
        pass
    moves = 0
    gravity()
    jump = True
    update_world()
  except:
    pass
def d_up(event):
  try:
    global jump
    global world
    global prev_block
    global moves
    global fly
    global go_through
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y-1][x] in go_through and world[y-2][x] in go_through) and (moves == 1) and (jump == False or prev_block in fly):    
        world[y][x] = prev_block
        prev_block = world[y-2][x]
        world[y-2][x] = 33
    else:
        pass
    moves = 0
    gravity()
    jump = True
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
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y+1][x] in go_through) and (moves == 1):    
        world[y][x] = prev_block
        prev_block = world[y+1][x]
        world[y+1][x] = 33
    else:
        pass
    moves = 0
    jump = True
    gravity()
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
    global mario_dir
    mario_dir = False
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x-1] in go_through) and (moves == 1):
        world[y][x] = prev_block
        prev_block = world[y][x-1]
        world[y][x-1] = 33
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
    global mario_dir
    mario_dir = False
    global go_through2
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x-1] in go_through2) and (moves == 1) and (world[y][x-2] in go_through):
        world[y][x] = prev_block
        prev_block = world[y][x-2]
        world[y][x-2] = 33
    else:
        pass
    moves = 0
    jump = True
    gravity()
    update_world()
  except:
    pass
def d_right(event):
  try:
    global world
    global mario_dir
    mario_dir = True
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
        world[y][x+2] = 33
    else:
        pass
    moves = 0
    jump = True
    gravity()
    update_world()
  except:
    pass
def right(event): #right is world [y][x+1]
  try:
    global world
    global mario_dir
    mario_dir = True
    global prev_block
    global moves
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x+1] in go_through) and (moves == 1):
        world[y][x] = prev_block
        prev_block = world[y][x+1]
        world[y][x+1] = 33
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
    y = find_player_y()  
    x = find_player_x(y)
    if world[y+1][x] == 0 and jump == True and (not prev_block in fly):
        world[y][x] = prev_block
        prev_block = world[y+1][x]
        world[y+1][x] = 33
        down(0)
    else:
        pass
    jump = False
    update_world()
###################################
def vincible():
    global invincible
    invincible = False
def damage():
    global invincible
    global hp
    if invincible == False:
        hp += -1
        invincible = True
        ree.after(3000,vincible)
print("Please dont destroy any of the windows")
print("Get a score of 33 to get a power up")
e = input("Press enter to begin")
n1 = tkinter.Button(ree,command=lambda:d_left(0),text="q")
n2 = tkinter.Button(ree,command=lambda:d_right(0),text="e")
n3 = tkinter.Button(ree,command=lambda:d_up(0),text="w")
n4 = tkinter.Button(ree,command=lambda:left(0),text="a")
n5 = tkinter.Button(ree,command=lambda:right(0),text="d")
n6 = tkinter.Button(ree,command=lambda:up(0),text="s")
n7 = tkinter.Button(ree,command=lambda:down(0),text="x")
n1.place(x=0,y=0,width=20,height=20)
n2.place(x=40,y=0,width=20,height=20)
n3.place(x=20,y=0,width=20,height=20)
n4.place(x=0,y=20,width=20,height=20)
n5.place(x=40,y=20,width=20,height=20)
n6.place(x=20,y=20,width=20,height=20)
n7.place(x=20,y=40,width=20,height=20)
create_world()

