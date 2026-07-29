#+++
import tkinter
file = open("eeee.txt","r")
world = file.read()
world = world.split("\n")
for i in range(len(world)):
    world[i] = world[i].split(",")
for i in range(len(world)):
    for j in range(len(world[i])):
        world[i][j] = int(world[i][j])
file.close()
from tkinter.constants import *
tk = tkinter.Tk()
tk.title("Backrooms")
tk.geometry("950x720+50+50")
back = "#b3b3b3"

##
background = tkinter.PhotoImage(file="back.png")
l0 = tkinter.PhotoImage(file="l0.png")
l1 = tkinter.PhotoImage(file="l1.png")
l2 = tkinter.PhotoImage(file="l2.png")
l3 = tkinter.PhotoImage(file="l3.png")
l4 = tkinter.PhotoImage(file="l4.png")
l5 = tkinter.PhotoImage(file="l5.png")
r0 = tkinter.PhotoImage(file="r0.png")
r1 = tkinter.PhotoImage(file="r1.png")
r2 = tkinter.PhotoImage(file="r2.png")
r3 = tkinter.PhotoImage(file="r3.png")
r4 = tkinter.PhotoImage(file="r4.png")
r5 = tkinter.PhotoImage(file="r5.png")
tk.config(bg=back)
a = tkinter.Label(tk,image=background)
a.place(x=0,y=0,width=950,height=720)
f=tkinter.PhotoImage(file="f.png")
xl0=tkinter.PhotoImage(file="xl0.png")
xr0=tkinter.PhotoImage(file="xr0.png")
##
oxr5=tkinter.Label(bg=back)
oxr5.place(x=571,y=285,width=91,height=150)
oxl5=tkinter.Label(bg=back)
oxl5.place(x=287,y=285,width=91,height=150)
or5=tkinter.Label(bg=back)
or5.place(x=496,y=285,width=91,height=150)
ol5=tkinter.Label(bg=back)
ol5.place(x=362,y=285,width=91,height=150)
of5=tkinter.Label(bg=back)
of5.place(x=437,y=285,width=75,height=150)
##
oxr4=tkinter.Label(bg=back)
oxr4.place(x=581,y=269,width=111,height=182)
oxl4=tkinter.Label(bg=back)
oxl4.place(x=257,y=269,width=111,height=182)
or4=tkinter.Label(bg=back)
or4.place(x=494,y=269,width=111,height=182)
ol4=tkinter.Label(bg=back)
ol4.place(x=344,y=269,width=111,height=182)
of4=tkinter.Label(bg=back)
of4.place(x=431,y=269,width=87,height=182)
##
oxr3=tkinter.Label(bg=back)
oxr3.place(x=625,y=245,width=142,height=230)
oxl3=tkinter.Label(bg=back)
oxl3.place(x=182,y=245,width=142,height=230)
or3=tkinter.Label(bg=back)
or3.place(x=508,y=245,width=142,height=230)
ol3=tkinter.Label(bg=back)
ol3.place(x=299,y=245,width=142,height=230)
of3=tkinter.Label(bg=back)
of3.place(x=416,y=245,width=117,height=230)
##
oxr2=tkinter.Label(bg=back)
oxr2.place(x=644,y=211,width=181,height=297)
oxl2=tkinter.Label(bg=back)
oxl2.place(x=125,y=211,width=181,height=297)
or2=tkinter.Label(bg=back)
or2.place(x=504,y=211,width=181,height=297)
ol2=tkinter.Label(bg=back)
ol2.place(x=265,y=211,width=181,height=297)
of2=tkinter.Label(bg=back)
of2.place(x=405,y=211,width=140,height=297)
##
oxr1=tkinter.Label(bg=back)
oxr1.place(x=714,y=166,width=236,height=388)
oxl1=tkinter.Label(bg=back)
oxl1.place(x=0,y=166,width=236,height=388)
or1=tkinter.Label(bg=back)
or1.place(x=524,y=166,width=236,height=388)
ol1=tkinter.Label(bg=back)
ol1.place(x=190,y=166,width=236,height=388)
of1=tkinter.Label(bg=back)
of1.place(x=380,y=166,width=190,height=388)
##
or0=tkinter.Label(bg=back)
or0.place(x=86,y=101,width=314,height=517)
ol0=tkinter.Label(bg=back)
ol0.place(x=549,y=101,width=314,height=517)
of0=tkinter.Label(bg=back)
of0.place(x=345,y=101,width=259,height=517)
oxr0=tkinter.Label(bg=back)
oxr0.place(x=0,y=0,width=86,height=720)
oxl0=tkinter.Label(bg=back)
oxl0.place(x=864,y=0,width=86,height=720)
##
seen_world = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
dir_ = 1
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
def obj_in_world(obj):
    global world
    e = False
    for i in range(len(world)):
        if obj in world[i]:
            e = True
            break
    return e
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
############################
ree = tkinter.Toplevel()
ree.title("scan")
ree.geometry("150x150")
#
a1=tkinter.Label(ree,bg="#0000ff")
a1.place(x=0,y=0,width=30,height=30)
a2=tkinter.Label(ree,bg="#0000ff")
a2.place(x=30,y=0,width=30,height=30)
a3=tkinter.Label(ree,bg="#0000ff")
a3.place(x=60,y=0,width=30,height=30)
a4=tkinter.Label(ree,bg="#0000ff")
a4.place(x=90,y=0,width=30,height=30)
a5=tkinter.Label(ree,bg="#0000ff")
a5.place(x=120,y=0,width=30,height=30)
#
b1=tkinter.Label(ree,bg="#0000ff")
b1.place(x=0,y=30,width=30,height=30)
b2=tkinter.Label(ree,bg="#0000ff")
b2.place(x=30,y=30,width=30,height=30)
b3=tkinter.Label(ree,bg="#0000ff")
b3.place(x=60,y=30,width=30,height=30)
b4=tkinter.Label(ree,bg="#0000ff")
b4.place(x=90,y=30,width=30,height=30)
b5=tkinter.Label(ree,bg="#0000ff")
b5.place(x=120,y=30,width=30,height=30)
#
c1=tkinter.Label(ree,bg="#0000ff")
c1.place(x=0,y=60,width=30,height=30)
c2=tkinter.Label(ree,bg="#0000ff")
c2.place(x=30,y=60,width=30,height=30)
c3=tkinter.Label(ree,bg="#0000ff")
c3.place(x=60,y=60,width=30,height=30)
c4=tkinter.Label(ree,bg="#0000ff")
c4.place(x=90,y=60,width=30,height=30)
c5=tkinter.Label(ree,bg="#0000ff")
c5.place(x=120,y=60,width=30,height=30)
#
d1=tkinter.Label(ree,bg="#0000ff")
d1.place(x=0,y=90,width=30,height=30)
d2=tkinter.Label(ree,bg="#0000ff")
d2.place(x=30,y=90,width=30,height=30)
d3=tkinter.Label(ree,bg="#0000ff")
d3.place(x=60,y=90,width=30,height=30)
d4=tkinter.Label(ree,bg="#0000ff")
d4.place(x=90,y=90,width=30,height=30)
d5=tkinter.Label(ree,bg="#0000ff")
d5.place(x=120,y=90,width=30,height=30)
#
e1=tkinter.Label(ree,bg="#0000ff")
e1.place(x=0,y=120,width=30,height=30)
e2=tkinter.Label(ree,bg="#0000ff")
e2.place(x=30,y=120,width=30,height=30)
e3=tkinter.Label(ree,bg="#0000ff")
e3.place(x=60,y=120,width=30,height=30)
e4=tkinter.Label(ree,bg="#0000ff")
e4.place(x=90,y=120,width=30,height=30)
e5=tkinter.Label(ree,bg="#0000ff")
e5.place(x=120,y=120,width=30,height=30)
############################
def update_world():
    global world
    global dir_
    global seen_world
    y = find_y_of(2)
    x = find_x_of(2,y)
    #############################################
    eee = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]
    if dir_ == 1:
        eee[0][0] = world[y-4][x-2]
        eee[0][1] = world[y-4][x-1]
        eee[0][2] = world[y-4][x]
        eee[0][3] = world[y-4][x+1]
        eee[0][4] = world[y-4][x+2]
        eee[1][0] = world[y-3][x-2]
        eee[1][1] = world[y-3][x-1]
        eee[1][2] = world[y-3][x]
        eee[1][3] = world[y-3][x+1]
        eee[1][4] = world[y-3][x+2]
        eee[2][0] = world[y-2][x-2]
        eee[2][1] = world[y-2][x-1]
        eee[2][2] = world[y-2][x]
        eee[2][3] = world[y-2][x+1]
        eee[2][4] = world[y-2][x+2]
        eee[3][0] = world[y-1][x-2]
        eee[3][1] = world[y-1][x-1]
        eee[3][2] = world[y-1][x]
        eee[3][3] = world[y-1][x+1]
        eee[3][4] = world[y-1][x+2]
        eee[4][0] = world[y][x-2]
        eee[4][1] = world[y][x-1]
        eee[4][2] = world[y][x]
        eee[4][3] = world[y][x+1]
        eee[4][4] = world[y][x+2]
    elif dir_ == 3:
        eee[0][0] = world[y+4][x+2]
        eee[0][1] = world[y+4][x+1]
        eee[0][2] = world[y+4][x]
        eee[0][3] = world[y+4][x-1]
        eee[0][4] = world[y+4][x-2]
        eee[1][0] = world[y+3][x+2]
        eee[1][1] = world[y+3][x+1]
        eee[1][2] = world[y+3][x]
        eee[1][3] = world[y+3][x-1]
        eee[1][4] = world[y+3][x-2]
        eee[2][0] = world[y+2][x+2]
        eee[2][1] = world[y+2][x+1]
        eee[2][2] = world[y+2][x]
        eee[2][3] = world[y+2][x-1]
        eee[2][4] = world[y+2][x-2]
        eee[3][0] = world[y+1][x+2]
        eee[3][1] = world[y+1][x+1]
        eee[3][2] = world[y+1][x]
        eee[3][3] = world[y+1][x-1]
        eee[3][4] = world[y+1][x-2]
        eee[4][0] = world[y][x+2]
        eee[4][1] = world[y][x+1]
        eee[4][2] = world[y][x]
        eee[4][3] = world[y][x-1]
        eee[4][4] = world[y][x-2]
    elif dir_ == 4:
        eee[0][0] = world[y+2][x-4]
        eee[0][1] = world[y+1][x-4]
        eee[0][2] = world[y][x-4]
        eee[0][3] = world[y-1][x-4]
        eee[0][4] = world[y-2][x-4]
        eee[1][0] = world[y+2][x-3]
        eee[1][1] = world[y+1][x-3]
        eee[1][2] = world[y][x-3]
        eee[1][3] = world[y-1][x-3]
        eee[1][4] = world[y-2][x-3]
        eee[2][0] = world[y+2][x-2]
        eee[2][1] = world[y+1][x-2]
        eee[2][2] = world[y][x-2]
        eee[2][3] = world[y-1][x-2]
        eee[2][4] = world[y-2][x-2]
        eee[3][0] = world[y+2][x-1]
        eee[3][1] = world[y+1][x-1]
        eee[3][2] = world[y][x-1]
        eee[3][3] = world[y-1][x-1]
        eee[3][4] = world[y-2][x-1]
        eee[4][0] = world[y+2][x]
        eee[4][1] = world[y+1][x]
        eee[4][2] = world[y][x]
        eee[4][3] = world[y-1][x]
        eee[4][4] = world[y-2][x]
    elif dir_ == 2:
        eee[0][0] = world[y-2][x+4]
        eee[0][1] = world[y-1][x+4]
        eee[0][2] = world[y][x+4]
        eee[0][3] = world[y+1][x+4]
        eee[0][4] = world[y+2][x+4]
        eee[1][0] = world[y-2][x+3]
        eee[1][1] = world[y-1][x+3]
        eee[1][2] = world[y][x+3]
        eee[1][3] = world[y+1][x+3]
        eee[1][4] = world[y+2][x+3]
        eee[2][0] = world[y-2][x+2]
        eee[2][1] = world[y-1][x+2]
        eee[2][2] = world[y][x+2]
        eee[2][3] = world[y+1][x+2]
        eee[2][4] = world[y+2][x+2]
        eee[3][0] = world[y-2][x+1]
        eee[3][1] = world[y-1][x+1]
        eee[3][2] = world[y][x+1]
        eee[3][3] = world[y+1][x+1]
        eee[3][4] = world[y+2][x+1]
        eee[4][0] = world[y-2][x]
        eee[4][1] = world[y-1][x]
        eee[4][2] = world[y][x]
        eee[4][3] = world[y+1][x]
        eee[4][4] = world[y+2][x]
        #fuuuuuuuuck
    e = eee[0][0]        
    if e == 1:
        a1.config(bg="#00ff00")
    elif e == 0:
        a1.config(bg="#0000ff")
    else:
        a1.config(bg="#ff0000")
    e = eee[0][1]        
    if e == 1:
        a2.config(bg="#00ff00")
    elif e == 0:
        a2.config(bg="#0000ff")
    else:
        a2.config(bg="#ff0000")
    e = eee[0][2]        
    if e == 1:
        a3.config(bg="#00ff00")
    elif e == 0:
        a3.config(bg="#0000ff")
    else:
        a3.config(bg="#ff0000")
    e = eee[0][3]        
    if e == 1:
        a4.config(bg="#00ff00")
    elif e == 0:
        a4.config(bg="#0000ff")
    else:
        a4.config(bg="#ff0000")
    e = eee[0][4]        
    if e == 1:
        a5.config(bg="#00ff00")
    elif e == 0:
        a5.config(bg="#0000ff")
    else:
        a5.config(bg="#ff0000")
    #eeeee
    e = eee[1][0]        
    if e == 1:
        b1.config(bg="#00ff00")
    elif e == 0:
        b1.config(bg="#0000ff")
    else:
        b1.config(bg="#ff0000")
    e = eee[1][1]        
    if e == 1:
        b2.config(bg="#00ff00")
    elif e == 0:
        b2.config(bg="#0000ff")
    else:
        b2.config(bg="#ff0000")
    e = eee[1][2]        
    if e == 1:
        b3.config(bg="#00ff00")
    elif e == 0:
        b3.config(bg="#0000ff")
    else:
        b3.config(bg="#ff0000")
    e = eee[1][3]        
    if e == 1:
        b4.config(bg="#00ff00")
    elif e == 0:
        b4.config(bg="#0000ff")
    else:
        b4.config(bg="#ff0000")
    e = eee[1][4]        
    if e == 1:
        b5.config(bg="#00ff00")
    elif e == 0:
        b5.config(bg="#0000ff")
    else:
        b5.config(bg="#ff0000")
    #eeeee
    e = eee[2][0]        
    if e == 1:
        c1.config(bg="#00ff00")
    elif e == 0:
        c1.config(bg="#0000ff")
    else:
        c1.config(bg="#ff0000")
    e = eee[2][1]        
    if e == 1:
        c2.config(bg="#00ff00")
    elif e == 0:
        c2.config(bg="#0000ff")
    else:
        c2.config(bg="#ff0000")
    e = eee[2][2]        
    if e == 1:
        c3.config(bg="#00ff00")
    elif e == 0:
        c3.config(bg="#0000ff")
    else:
        c3.config(bg="#ff0000")
    e = eee[2][3]        
    if e == 1:
        c4.config(bg="#00ff00")
    elif e == 0:
        c4.config(bg="#0000ff")
    else:
        c4.config(bg="#ff0000")
    e = eee[2][4]        
    if e == 1:
        c5.config(bg="#00ff00")
    elif e == 0:
        c5.config(bg="#0000ff")
    else:
        c5.config(bg="#ff0000")
    #eeeee
    e = eee[3][0]        
    if e == 1:
        d1.config(bg="#00ff00")
    elif e == 0:
        d1.config(bg="#0000ff")
    else:
        d1.config(bg="#ff0000")
    e = eee[3][1]        
    if e == 1:
        d2.config(bg="#00ff00")
    elif e == 0:
        d2.config(bg="#0000ff")
    else:
        d2.config(bg="#ff0000")
    e = eee[3][2]        
    if e == 1:
        d3.config(bg="#00ff00")
    elif e == 0:
        d3.config(bg="#0000ff")
    else:
        d3.config(bg="#ff0000")
    e = eee[3][3]        
    if e == 1:
        d4.config(bg="#00ff00")
    elif e == 0:
        d4.config(bg="#0000ff")
    else:
        d4.config(bg="#ff0000")
    e = eee[3][4]        
    if e == 1:
        d5.config(bg="#00ff00")
    elif e == 0:
        d5.config(bg="#0000ff")
    else:
        d5.config(bg="#ff0000")
    #eeeee
    e = eee[4][0]        
    if e == 1:
        e1.config(bg="#00ff00")
    elif e == 0:
        e1.config(bg="#0000ff")
    else:
        e1.config(bg="#ff0000")
    e = eee[4][1]        
    if e == 1:
        e2.config(bg="#00ff00")
    elif e == 0:
        e2.config(bg="#0000ff")
    else:
        e2.config(bg="#ff0000")
    e = eee[4][2]        
    if e == 1:
        e3.config(bg="#00ff00")
    elif e == 0:
        e3.config(bg="#0000ff")
    else:
        e3.config(bg="#ff0000")
    e = eee[4][3]        
    if e == 1:
        e4.config(bg="#00ff00")
    elif e == 0:
        e4.config(bg="#0000ff")
    else:
        e4.config(bg="#ff0000")
    e = eee[4][4]        
    if e == 1:
        e5.config(bg="#00ff00")
    elif e == 0:
        e5.config(bg="#0000ff")
    else:
        e5.config(bg="#ff0000")
    #############################################
    if dir_ == 1:
        seen_world[0][0] = world[y-6][x-2]
        seen_world[0][1] = world[y-6][x-1]
        seen_world[0][2] = world[y-6][x]
        seen_world[0][3] = world[y-6][x+1]
        seen_world[0][4] = world[y-6][x+2]
        seen_world[1][0] = world[y-5][x-2]
        seen_world[1][1] = world[y-5][x-1]
        seen_world[1][2] = world[y-5][x]
        seen_world[1][3] = world[y-5][x+1]
        seen_world[1][4] = world[y-5][x+2]
        seen_world[2][0] = world[y-4][x-2]
        seen_world[2][1] = world[y-4][x-1]
        seen_world[2][2] = world[y-4][x]
        seen_world[2][3] = world[y-4][x+1]
        seen_world[2][4] = world[y-4][x+2]
        seen_world[3][0] = world[y-3][x-2]
        seen_world[3][1] = world[y-3][x-1]
        seen_world[3][2] = world[y-3][x]
        seen_world[3][3] = world[y-3][x+1]
        seen_world[3][4] = world[y-3][x+2]
        seen_world[4][0] = world[y-2][x-2]
        seen_world[4][1] = world[y-2][x-1]
        seen_world[4][2] = world[y-2][x]
        seen_world[4][3] = world[y-2][x+1]
        seen_world[4][4] = world[y-2][x+2]
        seen_world[5][0] = world[y-1][x-2]##
        seen_world[5][1] = world[y-1][x-1]
        seen_world[5][2] = world[y-1][x]
        seen_world[5][3] = world[y-1][x+1]
        seen_world[5][4] = world[y-1][x+2]##
        seen_world[6][0] = world[y][x-2]##
        seen_world[6][1] = world[y][x-1]
        seen_world[6][2] = world[y][x]
        seen_world[6][3] = world[y][x+1]
        seen_world[6][4] = world[y][x+2]##
    elif dir_ == 3:
        seen_world[0][0] = world[y+6][x-2]
        seen_world[0][1] = world[y+6][x-1]
        seen_world[0][2] = world[y+6][x]
        seen_world[0][3] = world[y+6][x+1]
        seen_world[0][4] = world[y+6][x+2]
        seen_world[1][0] = world[y+5][x-2]
        seen_world[1][1] = world[y+5][x-1]
        seen_world[1][2] = world[y+5][x]
        seen_world[1][3] = world[y+5][x+1]
        seen_world[1][4] = world[y+5][x+2]
        seen_world[2][0] = world[y+4][x-2]
        seen_world[2][1] = world[y+4][x-1]
        seen_world[2][2] = world[y+4][x]
        seen_world[2][3] = world[y+4][x+1]
        seen_world[2][4] = world[y+4][x+2]
        seen_world[3][0] = world[y+3][x-2]
        seen_world[3][1] = world[y+3][x-1]
        seen_world[3][2] = world[y+3][x]
        seen_world[3][3] = world[y+3][x+1]
        seen_world[3][4] = world[y+3][x+2]
        seen_world[4][0] = world[y+2][x-2]
        seen_world[4][1] = world[y+2][x-1]
        seen_world[4][2] = world[y+2][x]
        seen_world[4][3] = world[y+2][x+1]
        seen_world[4][4] = world[y+2][x+2]
        seen_world[5][0] = world[y+1][x-2]##
        seen_world[5][1] = world[y+1][x-1]
        seen_world[5][2] = world[y+1][x]
        seen_world[5][3] = world[y+1][x+1]
        seen_world[5][4] = world[y+1][x+2]##
        seen_world[6][0] = world[y][x-2]##
        seen_world[6][1] = world[y][x-1]
        seen_world[6][2] = world[y][x]
        seen_world[6][3] = world[y][x+1]
        seen_world[6][4] = world[y][x+2]##
    elif dir_ == 4:
        seen_world[0][0] = world[y+2][x-6]
        seen_world[0][1] = world[y+1][x-6]
        seen_world[0][2] = world[y][x-6]
        seen_world[0][3] = world[y-1][x-6]
        seen_world[0][4] = world[y-2][x-6]
        seen_world[1][0] = world[y+2][x-5]
        seen_world[1][1] = world[y+1][x-5]
        seen_world[1][2] = world[y][x-5]
        seen_world[1][3] = world[y-1][x-5]
        seen_world[1][4] = world[y-2][x-5]
        seen_world[2][0] = world[y+2][x-4]
        seen_world[2][1] = world[y+1][x-4]
        seen_world[2][2] = world[y][x-4]
        seen_world[2][3] = world[y-1][x-4]
        seen_world[2][4] = world[y-2][x-4]
        seen_world[3][0] = world[y+2][x-3]
        seen_world[3][1] = world[y+1][x-3]
        seen_world[3][2] = world[y][x-3]
        seen_world[3][3] = world[y-1][x-3]
        seen_world[3][4] = world[y-2][x-3]
        seen_world[4][0] = world[y+2][x-2]
        seen_world[4][1] = world[y+1][x-2]
        seen_world[4][2] = world[y][x-2]
        seen_world[4][3] = world[y-1][x-2]
        seen_world[4][4] = world[y-2][x-2]
        seen_world[5][0] = world[y+2][x-1]
        seen_world[5][1] = world[y+1][x-1]
        seen_world[5][2] = world[y][x-1]
        seen_world[5][3] = world[y-1][x-1]
        seen_world[5][4] = world[y-2][x-1]
        seen_world[6][0] = world[y+2][x]
        seen_world[6][1] = world[y+1][x]
        seen_world[6][2] = world[y][x]
        seen_world[6][3] = world[y-1][x]
        seen_world[6][4] = world[y-2][x]
    elif dir_ == 2:
        seen_world[0][0] = world[y-2][x+6]
        seen_world[0][1] = world[y-1][x+6]
        seen_world[0][2] = world[y][x+6]
        seen_world[0][3] = world[y+1][x+6]
        seen_world[0][4] = world[y+2][x+6]
        seen_world[1][0] = world[y-2][x+5]
        seen_world[1][1] = world[y-1][x+5]
        seen_world[1][2] = world[y][x+5]
        seen_world[1][3] = world[y+1][x+5]
        seen_world[1][4] = world[y+2][x+5]
        seen_world[2][0] = world[y-2][x+4]
        seen_world[2][1] = world[y-1][x+4]
        seen_world[2][2] = world[y][x+4]
        seen_world[2][3] = world[y+1][x+4]
        seen_world[2][4] = world[y+2][x+4]
        seen_world[3][0] = world[y-2][x+3]
        seen_world[3][1] = world[y-1][x+3]
        seen_world[3][2] = world[y][x+3]
        seen_world[3][3] = world[y+1][x+3]
        seen_world[3][4] = world[y+2][x+3]
        seen_world[4][0] = world[y-2][x+2]
        seen_world[4][1] = world[y-1][x+2]
        seen_world[4][2] = world[y][x+2]
        seen_world[4][3] = world[y+1][x+2]
        seen_world[4][4] = world[y+2][x+2]
        seen_world[5][0] = world[y-2][x+1]
        seen_world[5][1] = world[y-1][x+1]
        seen_world[5][2] = world[y][x+1]
        seen_world[5][3] = world[y+1][x+1]
        seen_world[5][4] = world[y+2][x+1]
        seen_world[6][0] = world[y-2][x]
        seen_world[6][1] = world[y-1][x]
        seen_world[6][2] = world[y][x]
        seen_world[6][3] = world[y+1][x]
        seen_world[6][4] = world[y+2][x]
    else:
        pass
    ##
    e = seen_world[0][0]
    if e == 0:
        oxl5.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxl5.config(image=l5)
        oxl5.place(x=287,y=285,width=95,height=150)
    else:
        pass
    e = seen_world[0][1]
    if e == 0:
        ol5.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        ol5.config(image=l5)
        ol5.place(x=362,y=285,width=95,height=150)
    else:
        pass
    e = seen_world[0][2]
    if e == 0:
        of5.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        of5.config(image=l5)
        of5.place(x=437,y=285,width=75,height=150)
    else:
        pass
    e = seen_world[0][3]
    if e == 0:
        or5.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        or5.config(image=r5)
        or5.place(x=496,y=285,width=95,height=150)
    else:
        pass
    e = seen_world[0][4]
    if e == 0:
        oxr5.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxr5.config(image=r5)
        oxr5.place(x=571,y=285,width=95,height=150)
    else:
        pass
    ##
    e = seen_world[1][0]
    if e == 0:
        oxl4.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxl4.config(image=l4)
        oxl4.place(x=257,y=269,width=115,height=182)
    else:
        pass
    e = seen_world[1][1]
    if e == 0:
        ol4.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        ol4.config(image=l4)
        ol4.place(x=344,y=269,width=115,height=182)
    else:
        pass
    e = seen_world[1][2]
    if e == 0:
        of4.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        of4.config(image=l4)
        of4.place(x=431,y=269,width=87,height=182)
    else:
        pass
    e = seen_world[1][3]
    if e == 0:
        or4.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        or4.config(image=r4)
        or4.place(x=494,y=269,width=115,height=182)
    else:
        pass
    e = seen_world[1][4]
    if e == 0:
        oxr4.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxr4.config(image=r4)
        oxr4.place(x=581,y=269,width=115,height=182)
    else:
        pass
    ##
    e = seen_world[2][0]
    if e == 0:
        oxl3.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxl3.config(image=l3)
        oxl3.place(x=182,y=245,width=145,height=230)
    else:
        pass
    e = seen_world[2][1]
    if e == 0:
        ol3.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        ol3.config(image=l3)
        ol3.place(x=299,y=245,width=145,height=230)
    else:
        pass
    e = seen_world[2][2]
    if e == 0:
        of3.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        of3.config(image=l3)
        of3.place(x=416,y=245,width=117,height=230)
    else:
        pass
    e = seen_world[2][3]
    if e == 0:
        or3.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        or3.config(image=r3)
        or3.place(x=508,y=245,width=145,height=230)
    else:
        pass
    e = seen_world[2][4]
    if e == 0:
        oxr3.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxr3.config(image=r3)
        oxr3.place(x=625,y=245,width=145,height=230)
    else:
        pass
    ##
    e = seen_world[3][0]
    if e == 0:
        oxl2.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxl2.config(image=l2)
        oxl2.place(x=125,y=211,width=185,height=297)
    else:
        pass
    e = seen_world[3][1]
    if e == 0:
        ol2.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        ol2.config(image=l2)
        ol2.place(x=265,y=211,width=185,height=297)
    else:
        pass
    e = seen_world[3][2]
    if e == 0:
        of2.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        of2.config(image=l2)
        of2.place(x=405,y=211,width=140,height=297)
    else:
        pass
    e = seen_world[3][3]
    if e == 0:
        or2.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        or2.config(image=r2)
        or2.place(x=504,y=211,width=185,height=297)
    else:
        pass
    e = seen_world[3][4]
    if e == 0:
        oxr2.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxr2.config(image=r2)
        oxr2.place(x=644,y=211,width=185,height=297)
    else:
        pass
    ##
    e = seen_world[4][0]
    if e == 0:
        oxl1.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxl1.config(image=l1)
        oxl1.place(x=0,y=166,width=240,height=388)
    else:
        pass
    e = seen_world[4][1]
    if e == 0:
        ol1.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        ol1.config(image=l1)
        ol1.place(x=190,y=166,width=240,height=388)
    else:
        pass
    e = seen_world[4][2]
    if e == 0:
        of1.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        of1.config(image=l1)
        of1.place(x=380,y=166,width=190,height=388)
    else:
        pass
    e = seen_world[4][3]
    if e == 0:
        or1.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        or1.config(image=r1)
        or1.place(x=524,y=166,width=240,height=388)
    else:
        pass
    e = seen_world[4][4]
    if e == 0:
        oxr1.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxr1.config(image=r1)
        oxr1.place(x=714,y=166,width=240,height=388)
    else:
        pass
    ##
    e = seen_world[5][1]
    if e == 0:
        ol0.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        ol0.config(image=xl0)
        ol0.place(x=0,y=101,width=345,height=517)
    else:
        pass
    e = seen_world[5][2]
    if e == 0:
        of0.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        of0.config(image=f)
        of0.place(x=86,y=101,width=778,height=517)

    else:
        pass
    e = seen_world[5][3]
    if e == 0:
        or0.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        or0.config(image=xr0)
        or0.place(x=600,y=101,width=345,height=517)
    else:
        pass
    ##
    e = seen_world[6][1]
    if e == 0:
        oxl0.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxl0.config(image=l0)
        oxl0.place(x=0,y=0,width=86,height=720)
    else:
        pass
    e = seen_world[6][3]
    if e == 0:
        oxr0.place(x=0,y=0,width=0,height=0)
    elif e == 1:
        oxr0.config(image=r0)
        oxr0.place(x=864,y=0,width=86,height=720)
    else:
        pass
    ##
##
update_world()
##
def right(event):
    global dir_
    dir_ += 1
    if dir_ == 5:
        dir_ = 1
    update_world() 
def left(event):
    global dir_
    dir_ += -1
    if dir_ == 0:
        dir_ = 4
    update_world()
def foreward(event):
    global world
    global dir_
    y = find_y_of(2)
    x = find_x_of(2,y)
    if dir_ == 1:
        if world[y-1][x] == 0:
            world[y-1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif dir_ == 2:
        if world[y][x+1] == 0:
            world[y][x+1] = 2
            world[y][x] = 0
        else:
            pass
    elif dir_ == 3:
        if world[y+1][x] == 0:
            world[y+1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif dir_ == 4:
        if world[y][x-1] == 0:
            world[y][x-1] = 2
            world[y][x] = 0
        else:
            pass
    else:
        pass
    update_world()
def foreward_r(event):
    global world
    global dir_
    y = find_y_of(2)
    x = find_x_of(2,y)
    e = dir_ + 1
    if e == 5:
        e = 1
    if e == 1:
        if world[y-1][x] == 0:
            world[y-1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 2:
        if world[y][x+1] == 0:
            world[y][x+1] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 3:
        if world[y+1][x] == 0:
            world[y+1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 4:
        if world[y][x-1] == 0:
            world[y][x-1] = 2
            world[y][x] = 0
        else:
            pass
    else:
        pass
    update_world()
def foreward_l(event):
    global world
    global dir_
    y = find_y_of(2)
    x = find_x_of(2,y)
    e = dir_ - 1
    if e == 0:
        e = 4
    if e == 1:
        if world[y-1][x] == 0:
            world[y-1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 2:
        if world[y][x+1] == 0:
            world[y][x+1] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 3:
        if world[y+1][x] == 0:
            world[y+1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 4:
        if world[y][x-1] == 0:
            world[y][x-1] = 2
            world[y][x] = 0
        else:
            pass
    else:
        pass
    update_world()
def foreward_b(event):
    global world
    global dir_
    y = find_y_of(2)
    x = find_x_of(2,y)
    e = dir_ + 2
    if e == 6:
        e = 2
    elif e == 5:
        e = 1
    if e == 1:
        if world[y-1][x] == 0:
            world[y-1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 2:
        if world[y][x+1] == 0:
            world[y][x+1] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 3:
        if world[y+1][x] == 0:
            world[y+1][x] = 2
            world[y][x] = 0
        else:
            pass
    elif e == 4:
        if world[y][x-1] == 0:
            world[y][x-1] = 2
            world[y][x] = 0
        else:
            pass
    else:
        pass
    update_world()
##
def see_dir(event):
    global dir_
    if dir_ == 1:
        print("N")
    elif dir_ == 2:
        print("E")
    elif dir_ == 3:
        print("S")
    elif dir_ == 4:
        print("W")
    else:
        pass
##
tk.bind("<KeyRelease-q>",left)
tk.bind("<KeyRelease-e>",right)
tk.bind("<KeyRelease-w>",foreward)
tk.bind("<KeyRelease-a>",foreward_l)
tk.bind("<KeyRelease-d>",foreward_r)
tk.bind("<KeyRelease-s>",foreward_b)
tk.bind("<KeyRelease-x>",see_dir)
print("w foreward\nq turn left\ne turn right\na left\nd right\ns back\nx see direction")
tkinter.mainloop()
