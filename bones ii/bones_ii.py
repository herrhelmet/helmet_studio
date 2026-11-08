import tkinter
root = tkinter.Tk() ##
tk = tkinter.Toplevel() #
tk.title("bones ii") #
tk.geometry("462x462+10+10")
green = "#67a336"
root.wm_attributes("-transparentcolor","#67a336")
tk.wm_attributes("-transparentcolor","#67a336")
root.geometry("462x462+10+10")
tk.geometry("462x462+10+10")
root.title("bones ii") #
root.config(bg=green) #
#
name = "world_.txt"
file = open(name,"r")
world = file.read()
world = world.split("\n")
for i in range(len(world)):
    world[i] = world[i].split(",")
for i in range(len(world)):
    for j in range(len(world[i])):
        world[i][j] = int(world[i][j])
file.close()
#i sometimes use random strings to name widgets that are never used twice
norm = tkinter.PhotoImage(file="background_.png")
wat = tkinter.PhotoImage(file="background.png")
qwe = tkinter.Label(tk)
qwe.place(x=0,y=0,width=462,height=462)
qwe.config(image=norm)
##
a1=tkinter.Label(root,bg=green)
a1.place(x=0,y=0,width=42,height=42)
a2=tkinter.Label(root,bg=green)
a2.place(x=42,y=0,width=42,height=42)
a3=tkinter.Label(root,bg=green)
a3.place(x=84,y=0,width=42,height=42)
a4=tkinter.Label(root,bg=green)
a4.place(x=126,y=0,width=42,height=42)
a5=tkinter.Label(root,bg=green)
a5.place(x=168,y=0,width=42,height=42)
a6=tkinter.Label(root,bg=green)
a6.place(x=210,y=0,width=42,height=42)
a7=tkinter.Label(root,bg=green)
a7.place(x=252,y=0,width=42,height=42)
a8=tkinter.Label(root,bg=green)
a8.place(x=294,y=0,width=42,height=42)
a9=tkinter.Label(root,bg=green)
a9.place(x=336,y=0,width=42,height=42)
a10=tkinter.Label(root,bg=green)
a10.place(x=378,y=0,width=42,height=42)
a11=tkinter.Label(root,bg=green)
a11.place(x=420,y=0,width=42,height=42)
##
b1=tkinter.Label(root,bg=green)
b1.place(x=0,y=42,width=42,height=42)
b2=tkinter.Label(root,bg=green)
b2.place(x=42,y=42,width=42,height=42)
b3=tkinter.Label(root,bg=green)
b3.place(x=84,y=42,width=42,height=42)
b4=tkinter.Label(root,bg=green)
b4.place(x=126,y=42,width=42,height=42)
b5=tkinter.Label(root,bg=green)
b5.place(x=168,y=42,width=42,height=42)
b6=tkinter.Label(root,bg=green)
b6.place(x=210,y=42,width=42,height=42)
b7=tkinter.Label(root,bg=green)
b7.place(x=252,y=42,width=42,height=42)
b8=tkinter.Label(root,bg=green)
b8.place(x=294,y=42,width=42,height=42)
b9=tkinter.Label(root,bg=green)
b9.place(x=336,y=42,width=42,height=42)
b10=tkinter.Label(root,bg=green)
b10.place(x=378,y=42,width=42,height=42)
b11=tkinter.Label(root,bg=green)
b11.place(x=420,y=42,width=42,height=42)
##
c1=tkinter.Label(root,bg=green)
c1.place(x=0,y=84,width=42,height=42)
c2=tkinter.Label(root,bg=green)
c2.place(x=42,y=84,width=42,height=42)
c3=tkinter.Label(root,bg=green)
c3.place(x=84,y=84,width=42,height=42)
c4=tkinter.Label(root,bg=green)
c4.place(x=126,y=84,width=42,height=42)
c5=tkinter.Label(root,bg=green)
c5.place(x=168,y=84,width=42,height=42)
c6=tkinter.Label(root,bg=green)
c6.place(x=210,y=84,width=42,height=42)
c7=tkinter.Label(root,bg=green)
c7.place(x=252,y=84,width=42,height=42)
c8=tkinter.Label(root,bg=green)
c8.place(x=294,y=84,width=42,height=42)
c9=tkinter.Label(root,bg=green)
c9.place(x=336,y=84,width=42,height=42)
c10=tkinter.Label(root,bg=green)
c10.place(x=378,y=84,width=42,height=42)
c11=tkinter.Label(root,bg=green)
c11.place(x=420,y=84,width=42,height=42)
##
d1=tkinter.Label(root,bg=green)
d1.place(x=0,y=126,width=42,height=42)
d2=tkinter.Label(root,bg=green)
d2.place(x=42,y=126,width=42,height=42)
d3=tkinter.Label(root,bg=green)
d3.place(x=84,y=126,width=42,height=42)
d4=tkinter.Label(root,bg=green)
d4.place(x=126,y=126,width=42,height=42)
d5=tkinter.Label(root,bg=green)
d5.place(x=168,y=126,width=42,height=42)
d6=tkinter.Label(root,bg=green)
d6.place(x=210,y=126,width=42,height=42)
d7=tkinter.Label(root,bg=green)
d7.place(x=252,y=126,width=42,height=42)
d8=tkinter.Label(root,bg=green)
d8.place(x=294,y=126,width=42,height=42)
d9=tkinter.Label(root,bg=green)
d9.place(x=336,y=126,width=42,height=42)
d10=tkinter.Label(root,bg=green)
d10.place(x=378,y=126,width=42,height=42)
d11=tkinter.Label(root,bg=green)
d11.place(x=420,y=126,width=42,height=42)
##
e1=tkinter.Label(root,bg=green)
e1.place(x=0,y=168,width=42,height=42)
e2=tkinter.Label(root,bg=green)
e2.place(x=42,y=168,width=42,height=42)
e3=tkinter.Label(root,bg=green)
e3.place(x=84,y=168,width=42,height=42)
e4=tkinter.Label(root,bg=green)
e4.place(x=126,y=168,width=42,height=42)
e5=tkinter.Label(root,bg=green)
e5.place(x=168,y=168,width=42,height=42)
e6=tkinter.Label(root,bg=green)
e6.place(x=210,y=168,width=42,height=42)
e7=tkinter.Label(root,bg=green)
e7.place(x=252,y=168,width=42,height=42)
e8=tkinter.Label(root,bg=green)
e8.place(x=294,y=168,width=42,height=42)
e9=tkinter.Label(root,bg=green)
e9.place(x=336,y=168,width=42,height=42)
e10=tkinter.Label(root,bg=green)
e10.place(x=378,y=168,width=42,height=42)
e11=tkinter.Label(root,bg=green)
e11.place(x=420,y=168,width=42,height=42)
##
f1=tkinter.Label(root,bg=green)
f1.place(x=0,y=210,width=42,height=42)
f2=tkinter.Label(root,bg=green)
f2.place(x=42,y=210,width=42,height=42)
f3=tkinter.Label(root,bg=green)
f3.place(x=84,y=210,width=42,height=42)
f4=tkinter.Label(root,bg=green)
f4.place(x=126,y=210,width=42,height=42)
f5=tkinter.Label(root,bg=green)
f5.place(x=168,y=210,width=42,height=42)
f6=tkinter.Label(root,bg=green)
f6.place(x=210,y=210,width=42,height=42)
f7=tkinter.Label(root,bg=green)
f7.place(x=252,y=210,width=42,height=42)
f8=tkinter.Label(root,bg=green)
f8.place(x=294,y=210,width=42,height=42)
f9=tkinter.Label(root,bg=green)
f9.place(x=336,y=210,width=42,height=42)
f10=tkinter.Label(root,bg=green)
f10.place(x=378,y=210,width=42,height=42)
f11=tkinter.Label(root,bg=green)
f11.place(x=420,y=210,width=42,height=42)
##
g1=tkinter.Label(root,bg=green)
g1.place(x=0,y=252,width=42,height=42)
g2=tkinter.Label(root,bg=green)
g2.place(x=42,y=252,width=42,height=42)
g3=tkinter.Label(root,bg=green)
g3.place(x=84,y=252,width=42,height=42)
g4=tkinter.Label(root,bg=green)
g4.place(x=126,y=252,width=42,height=42)
g5=tkinter.Label(root,bg=green)
g5.place(x=168,y=252,width=42,height=42)
g6=tkinter.Label(root,bg=green)
g6.place(x=210,y=252,width=42,height=42)
g7=tkinter.Label(root,bg=green)
g7.place(x=252,y=252,width=42,height=42)
g8=tkinter.Label(root,bg=green)
g8.place(x=294,y=252,width=42,height=42)
g9=tkinter.Label(root,bg=green)
g9.place(x=336,y=252,width=42,height=42)
g10=tkinter.Label(root,bg=green)
g10.place(x=378,y=252,width=42,height=42)
g11=tkinter.Label(root,bg=green)
g11.place(x=420,y=252,width=42,height=42)
##
h1=tkinter.Label(root,bg=green)
h1.place(x=0,y=294,width=42,height=42)
h2=tkinter.Label(root,bg=green)
h2.place(x=42,y=294,width=42,height=42)
h3=tkinter.Label(root,bg=green)
h3.place(x=84,y=294,width=42,height=42)
h4=tkinter.Label(root,bg=green)
h4.place(x=126,y=294,width=42,height=42)
h5=tkinter.Label(root,bg=green)
h5.place(x=168,y=294,width=42,height=42)
h6=tkinter.Label(root,bg=green)
h6.place(x=210,y=294,width=42,height=42)
h7=tkinter.Label(root,bg=green)
h7.place(x=252,y=294,width=42,height=42)
h8=tkinter.Label(root,bg=green)
h8.place(x=294,y=294,width=42,height=42)
h9=tkinter.Label(root,bg=green)
h9.place(x=336,y=294,width=42,height=42)
h10=tkinter.Label(root,bg=green)
h10.place(x=378,y=294,width=42,height=42)
h11=tkinter.Label(root,bg=green)
h11.place(x=420,y=294,width=42,height=42)
##
i1=tkinter.Label(root,bg=green)
i1.place(x=0,y=336,width=42,height=42)
i2=tkinter.Label(root,bg=green)
i2.place(x=42,y=336,width=42,height=42)
i3=tkinter.Label(root,bg=green)
i3.place(x=84,y=336,width=42,height=42)
i4=tkinter.Label(root,bg=green)
i4.place(x=126,y=336,width=42,height=42)
i5=tkinter.Label(root,bg=green)
i5.place(x=168,y=336,width=42,height=42)
i6=tkinter.Label(root,bg=green)
i6.place(x=210,y=336,width=42,height=42)
i7=tkinter.Label(root,bg=green)
i7.place(x=252,y=336,width=42,height=42)
i8=tkinter.Label(root,bg=green)
i8.place(x=294,y=336,width=42,height=42)
i9=tkinter.Label(root,bg=green)
i9.place(x=336,y=336,width=42,height=42)
i10=tkinter.Label(root,bg=green)
i10.place(x=378,y=336,width=42,height=42)
i11=tkinter.Label(root,bg=green)
i11.place(x=420,y=336,width=42,height=42)
##
j1=tkinter.Label(root,bg=green)
j1.place(x=0,y=378,width=42,height=42)
j2=tkinter.Label(root,bg=green)
j2.place(x=42,y=378,width=42,height=42)
j3=tkinter.Label(root,bg=green)
j3.place(x=84,y=378,width=42,height=42)
j4=tkinter.Label(root,bg=green)
j4.place(x=126,y=378,width=42,height=42)
j5=tkinter.Label(root,bg=green)
j5.place(x=168,y=378,width=42,height=42)
j6=tkinter.Label(root,bg=green)
j6.place(x=210,y=378,width=42,height=42)
j7=tkinter.Label(root,bg=green)
j7.place(x=252,y=378,width=42,height=42)
j8=tkinter.Label(root,bg=green)
j8.place(x=294,y=378,width=42,height=42)
j9=tkinter.Label(root,bg=green)
j9.place(x=336,y=378,width=42,height=42)
j10=tkinter.Label(root,bg=green)
j10.place(x=378,y=378,width=42,height=42)
j11=tkinter.Label(root,bg=green)
j11.place(x=420,y=378,width=42,height=42)
##
k1=tkinter.Label(root,bg=green)
k1.place(x=0,y=420,width=42,height=42)
k2=tkinter.Label(root,bg=green)
k2.place(x=42,y=420,width=42,height=42)
k3=tkinter.Label(root,bg=green)
k3.place(x=84,y=420,width=42,height=42)
k4=tkinter.Label(root,bg=green)
k4.place(x=126,y=420,width=42,height=42)
k5=tkinter.Label(root,bg=green)
k5.place(x=168,y=420,width=42,height=42)
k6=tkinter.Label(root,bg=green)
k6.place(x=210,y=420,width=42,height=42)
k7=tkinter.Label(root,bg=green)
k7.place(x=252,y=420,width=42,height=42)
k8=tkinter.Label(root,bg=green)
k8.place(x=294,y=420,width=42,height=42)
k9=tkinter.Label(root,bg=green)
k9.place(x=336,y=420,width=42,height=42)
k10=tkinter.Label(root,bg=green)
k10.place(x=378,y=420,width=42,height=42)
k11=tkinter.Label(root,bg=green)
k11.place(x=420,y=420,width=42,height=42)
print("Click the window to begin")
print("This game makes use of the IDE.\nMake sure the window is separate to the IDE by moving the IDE away from the window.")
##
blank = tkinter.PhotoImage(file="blank.png")
#abcde = tkinter.PhotoImage(file="blank.png")
block = tkinter.PhotoImage(file="block.png")
bulb = tkinter.PhotoImage(file="bulb.png")
dreed = tkinter.PhotoImage(file="dreed.png")
frame = tkinter.PhotoImage(file="frame.png")
ladder = tkinter.PhotoImage(file="ladder.png")
panel = tkinter.PhotoImage(file="panel.png")
red_rock = tkinter.PhotoImage(file="red_rock.png")
signal = tkinter.PhotoImage(file="signal.png")
water = tkinter.PhotoImage(file="water.png")
################################
prev_block = 0
jump = False
seen_world = [[0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0]]
def find_player_y():
  try:
    global world
    notfound = True
    i = 0
    while notfound:
        if 10 in world[i]:
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
        if world[y][i] == 10:
            notfound = False
        else:
            i += 1
    return i
  except:
    return 4
def update_world():
    global world
    global seen_world
    y = find_player_y()
    x = find_player_x(y)
    global prev_block
    ##
    seen_world[0][0] = world[y-5][x-5]
    seen_world[0][1] = world[y-5][x-4]
    seen_world[0][2] = world[y-5][x-3]
    seen_world[0][3] = world[y-5][x-2]
    seen_world[0][4] = world[y-5][x-1]
    seen_world[0][5] = world[y-5][x]
    seen_world[0][6] = world[y-5][x+1]
    seen_world[0][7] = world[y-5][x+2]
    seen_world[0][8] = world[y-5][x+3]
    seen_world[0][9] = world[y-5][x+4]
    seen_world[0][10] = world[y-5][x+5]
    ##
    seen_world[1][0] = world[y-4][x-5]
    seen_world[1][1] = world[y-4][x-4]
    seen_world[1][2] = world[y-4][x-3]
    seen_world[1][3] = world[y-4][x-2]
    seen_world[1][4] = world[y-4][x-1]
    seen_world[1][5] = world[y-4][x]
    seen_world[1][6] = world[y-4][x+1]
    seen_world[1][7] = world[y-4][x+2]
    seen_world[1][8] = world[y-4][x+3]
    seen_world[1][9] = world[y-4][x+4]
    seen_world[1][10] = world[y-4][x+5]
    ##
    seen_world[2][0] = world[y-3][x-5]
    seen_world[2][1] = world[y-3][x-4]
    seen_world[2][2] = world[y-3][x-3]
    seen_world[2][3] = world[y-3][x-2]
    seen_world[2][4] = world[y-3][x-1]
    seen_world[2][5] = world[y-3][x]
    seen_world[2][6] = world[y-3][x+1]
    seen_world[2][7] = world[y-3][x+2]
    seen_world[2][8] = world[y-3][x+3]
    seen_world[2][9] = world[y-3][x+4]
    seen_world[2][10] = world[y-3][x+5]
    ##
    seen_world[3][0] = world[y-2][x-5]
    seen_world[3][1] = world[y-2][x-4]
    seen_world[3][2] = world[y-2][x-3]
    seen_world[3][3] = world[y-2][x-2]
    seen_world[3][4] = world[y-2][x-1]
    seen_world[3][5] = world[y-2][x]
    seen_world[3][6] = world[y-2][x+1]
    seen_world[3][7] = world[y-2][x+2]
    seen_world[3][8] = world[y-2][x+3]
    seen_world[3][9] = world[y-2][x+4]
    seen_world[3][10] = world[y-2][x+5]
    ##
    seen_world[4][0] = world[y-1][x-5]
    seen_world[4][1] = world[y-1][x-4]
    seen_world[4][2] = world[y-1][x-3]
    seen_world[4][3] = world[y-1][x-2]
    seen_world[4][4] = world[y-1][x-1]
    seen_world[4][5] = world[y-1][x]
    seen_world[4][6] = world[y-1][x+1]
    seen_world[4][7] = world[y-1][x+2]
    seen_world[4][8] = world[y-1][x+3]
    seen_world[4][9] = world[y-1][x+4]
    seen_world[4][10] = world[y-1][x+5]
    ##
    seen_world[5][0] = world[y][x-5]
    seen_world[5][1] = world[y][x-4]
    seen_world[5][2] = world[y][x-3]
    seen_world[5][3] = world[y][x-2]
    seen_world[5][4] = world[y][x-1]
    seen_world[5][5] = world[y][x]
    seen_world[5][6] = world[y][x+1]
    seen_world[5][7] = world[y][x+2]
    seen_world[5][8] = world[y][x+3]
    seen_world[5][9] = world[y][x+4]
    seen_world[5][10] = world[y][x+5]
    ##
    seen_world[6][0] = world[y+1][x-5]
    seen_world[6][1] = world[y+1][x-4]
    seen_world[6][2] = world[y+1][x-3]
    seen_world[6][3] = world[y+1][x-2]
    seen_world[6][4] = world[y+1][x-1]
    seen_world[6][5] = world[y+1][x]
    seen_world[6][6] = world[y+1][x+1]
    seen_world[6][7] = world[y+1][x+2]
    seen_world[6][8] = world[y+1][x+3]
    seen_world[6][9] = world[y+1][x+4]
    seen_world[6][10] = world[y+1][x+5]
    ##
    seen_world[7][0] = world[y+2][x-5]
    seen_world[7][1] = world[y+2][x-4]
    seen_world[7][2] = world[y+2][x-3]
    seen_world[7][3] = world[y+2][x-2]
    seen_world[7][4] = world[y+2][x-1]
    seen_world[7][5] = world[y+2][x]
    seen_world[7][6] = world[y+2][x+1]
    seen_world[7][7] = world[y+2][x+2]
    seen_world[7][8] = world[y+2][x+3]
    seen_world[7][9] = world[y+2][x+4]
    seen_world[7][10] = world[y+2][x+5]
    ##
    seen_world[8][0] = world[y+3][x-5]
    seen_world[8][1] = world[y+3][x-4]
    seen_world[8][2] = world[y+3][x-3]
    seen_world[8][3] = world[y+3][x-2]
    seen_world[8][4] = world[y+3][x-1]
    seen_world[8][5] = world[y+3][x]
    seen_world[8][6] = world[y+3][x+1]
    seen_world[8][7] = world[y+3][x+2]
    seen_world[8][8] = world[y+3][x+3]
    seen_world[8][9] = world[y+3][x+4]
    seen_world[8][10] = world[y+3][x+5]
    ##
    seen_world[9][0] = world[y+4][x-5]
    seen_world[9][1] = world[y+4][x-4]
    seen_world[9][2] = world[y+4][x-3]
    seen_world[9][3] = world[y+4][x-2]
    seen_world[9][4] = world[y+4][x-1]
    seen_world[9][5] = world[y+4][x]
    seen_world[9][6] = world[y+4][x+1]
    seen_world[9][7] = world[y+4][x+2]
    seen_world[9][8] = world[y+4][x+3]
    seen_world[9][9] = world[y+4][x+4]
    seen_world[9][10] = world[y+4][x+5]
    ##
    seen_world[10][0] = world[y+5][x-5]
    seen_world[10][1] = world[y+5][x-4]
    seen_world[10][2] = world[y+5][x-3]
    seen_world[10][3] = world[y+5][x-2]
    seen_world[10][4] = world[y+5][x-1]
    seen_world[10][5] = world[y+5][x]
    seen_world[10][6] = world[y+5][x+1]
    seen_world[10][7] = world[y+5][x+2]
    seen_world[10][8] = world[y+5][x+3]
    seen_world[10][9] = world[y+5][x+4]
    seen_world[10][10] = world[y+5][x+5]
    ##
    e = seen_world[0][0]
    if e == 0:
        a1.config(image=blank)
    elif e == 1:
        a1.config(image=block)
    elif e == 2:
        a1.config(image=bulb)
    elif e == 3:
        a1.config(image=dreed)
    elif e == 4:
        a1.config(image=frame)
    elif e == 10:
        a1.config(image=blank)
    elif e == 5:
        a1.config(image=ladder)
    elif e == 6:
        a1.config(image=panel)
    elif e == 7:
        a1.config(image=red_rock)
    elif e == 8:
        a1.config(image=signal)
    elif e == 9:
        a1.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][1]
    if e == 0:
        a2.config(image=blank)
    elif e == 1:
        a2.config(image=block)
    elif e == 2:
        a2.config(image=bulb)
    elif e == 3:
        a2.config(image=dreed)
    elif e == 4:
        a2.config(image=frame)
    elif e == 10:
        a2.config(image=blank)
    elif e == 5:
        a2.config(image=ladder)
    elif e == 6:
        a2.config(image=panel)
    elif e == 7:
        a2.config(image=red_rock)
    elif e == 8:
        a2.config(image=signal)
    elif e == 9:
        a2.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][2]
    if e == 0:
        a3.config(image=blank)
    elif e == 1:
        a3.config(image=block)
    elif e == 2:
        a3.config(image=bulb)
    elif e == 3:
        a3.config(image=dreed)
    elif e == 4:
        a3.config(image=frame)
    elif e == 10:
        a3.config(image=blank)
    elif e == 5:
        a3.config(image=ladder)
    elif e == 6:
        a3.config(image=panel)
    elif e == 7:
        a3.config(image=red_rock)
    elif e == 8:
        a3.config(image=signal)
    elif e == 9:
        a3.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][3]
    if e == 0:
        a4.config(image=blank)
    elif e == 1:
        a4.config(image=block)
    elif e == 2:
        a4.config(image=bulb)
    elif e == 3:
        a4.config(image=dreed)
    elif e == 4:
        a4.config(image=frame)
    elif e == 10:
        a4.config(image=blank)
    elif e == 5:
        a4.config(image=ladder)
    elif e == 6:
        a4.config(image=panel)
    elif e == 7:
        a4.config(image=red_rock)
    elif e == 8:
        a4.config(image=signal)
    elif e == 9:
        a4.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][4]
    if e == 0:
        a5.config(image=blank)
    elif e == 1:
        a5.config(image=block)
    elif e == 2:
        a5.config(image=bulb)
    elif e == 3:
        a5.config(image=dreed)
    elif e == 4:
        a5.config(image=frame)
    elif e == 10:
        a5.config(image=blank)
    elif e == 5:
        a5.config(image=ladder)
    elif e == 6:
        a5.config(image=panel)
    elif e == 7:
        a5.config(image=red_rock)
    elif e == 8:
        a5.config(image=signal)
    elif e == 9:
        a5.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][5]
    if e == 0:
        a6.config(image=blank)
    elif e == 1:
        a6.config(image=block)
    elif e == 2:
        a6.config(image=bulb)
    elif e == 3:
        a6.config(image=dreed)
    elif e == 4:
        a6.config(image=frame)
    elif e == 10:
        a6.config(image=blank)
    elif e == 5:
        a6.config(image=ladder)
    elif e == 6:
        a6.config(image=panel)
    elif e == 7:
        a6.config(image=red_rock)
    elif e == 8:
        a6.config(image=signal)
    elif e == 9:
        a6.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][6]
    if e == 0:
        a7.config(image=blank)
    elif e == 1:
        a7.config(image=block)
    elif e == 2:
        a7.config(image=bulb)
    elif e == 3:
        a7.config(image=dreed)
    elif e == 4:
        a7.config(image=frame)
    elif e == 10:
        a7.config(image=blank)
    elif e == 5:
        a7.config(image=ladder)
    elif e == 6:
        a7.config(image=panel)
    elif e == 7:
        a7.config(image=red_rock)
    elif e == 8:
        a7.config(image=signal)
    elif e == 9:
        a7.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][7]
    if e == 0:
        a8.config(image=blank)
    elif e == 1:
        a8.config(image=block)
    elif e == 2:
        a8.config(image=bulb)
    elif e == 3:
        a8.config(image=dreed)
    elif e == 4:
        a8.config(image=frame)
    elif e == 10:
        a8.config(image=blank)
    elif e == 5:
        a8.config(image=ladder)
    elif e == 6:
        a8.config(image=panel)
    elif e == 7:
        a8.config(image=red_rock)
    elif e == 8:
        a8.config(image=signal)
    elif e == 9:
        a8.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][8]
    if e == 0:
        a9.config(image=blank)
    elif e == 1:
        a9.config(image=block)
    elif e == 2:
        a9.config(image=bulb)
    elif e == 3:
        a9.config(image=dreed)
    elif e == 4:
        a9.config(image=frame)
    elif e == 10:
        a9.config(image=blank)
    elif e == 5:
        a9.config(image=ladder)
    elif e == 6:
        a9.config(image=panel)
    elif e == 7:
        a9.config(image=red_rock)
    elif e == 8:
        a9.config(image=signal)
    elif e == 9:
        a9.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][9]
    if e == 0:
        a10.config(image=blank)
    elif e == 1:
        a10.config(image=block)
    elif e == 2:
        a10.config(image=bulb)
    elif e == 3:
        a10.config(image=dreed)
    elif e == 4:
        a10.config(image=frame)
    elif e == 10:
        a10.config(image=blank)
    elif e == 5:
        a10.config(image=ladder)
    elif e == 6:
        a10.config(image=panel)
    elif e == 7:
        a10.config(image=red_rock)
    elif e == 8:
        a10.config(image=signal)
    elif e == 9:
        a10.config(image=water)
    else:
        pass
    ##
    e = seen_world[0][10]
    if e == 0:
        a11.config(image=blank)
    elif e == 1:
        a11.config(image=block)
    elif e == 2:
        a11.config(image=bulb)
    elif e == 3:
        a11.config(image=dreed)
    elif e == 4:
        a11.config(image=frame)
    elif e == 10:
        a11.config(image=blank)
    elif e == 5:
        a11.config(image=ladder)
    elif e == 6:
        a11.config(image=panel)
    elif e == 7:
        a11.config(image=red_rock)
    elif e == 8:
        a11.config(image=signal)
    elif e == 9:
        a11.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][0]
    if e == 0:
        b1.config(image=blank)
    elif e == 1:
        b1.config(image=block)
    elif e == 2:
        b1.config(image=bulb)
    elif e == 3:
        b1.config(image=dreed)
    elif e == 4:
        b1.config(image=frame)
    elif e == 10:
        b1.config(image=blank)
    elif e == 5:
        b1.config(image=ladder)
    elif e == 6:
        b1.config(image=panel)
    elif e == 7:
        b1.config(image=red_rock)
    elif e == 8:
        b1.config(image=signal)
    elif e == 9:
        b1.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][1]
    if e == 0:
        b2.config(image=blank)
    elif e == 1:
        b2.config(image=block)
    elif e == 2:
        b2.config(image=bulb)
    elif e == 3:
        b2.config(image=dreed)
    elif e == 4:
        b2.config(image=frame)
    elif e == 10:
        b2.config(image=blank)
    elif e == 5:
        b2.config(image=ladder)
    elif e == 6:
        b2.config(image=panel)
    elif e == 7:
        b2.config(image=red_rock)
    elif e == 8:
        b2.config(image=signal)
    elif e == 9:
        b2.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][2]
    if e == 0:
        b3.config(image=blank)
    elif e == 1:
        b3.config(image=block)
    elif e == 2:
        b3.config(image=bulb)
    elif e == 3:
        b3.config(image=dreed)
    elif e == 4:
        b3.config(image=frame)
    elif e == 10:
        b3.config(image=blank)
    elif e == 5:
        b3.config(image=ladder)
    elif e == 6:
        b3.config(image=panel)
    elif e == 7:
        b3.config(image=red_rock)
    elif e == 8:
        b3.config(image=signal)
    elif e == 9:
        b3.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][3]
    if e == 0:
        b4.config(image=blank)
    elif e == 1:
        b4.config(image=block)
    elif e == 2:
        b4.config(image=bulb)
    elif e == 3:
        b4.config(image=dreed)
    elif e == 4:
        b4.config(image=frame)
    elif e == 10:
        b4.config(image=blank)
    elif e == 5:
        b4.config(image=ladder)
    elif e == 6:
        b4.config(image=panel)
    elif e == 7:
        b4.config(image=red_rock)
    elif e == 8:
        b4.config(image=signal)
    elif e == 9:
        b4.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][4]
    if e == 0:
        b5.config(image=blank)
    elif e == 1:
        b5.config(image=block)
    elif e == 2:
        b5.config(image=bulb)
    elif e == 3:
        b5.config(image=dreed)
    elif e == 4:
        b5.config(image=frame)
    elif e == 10:
        b5.config(image=blank)
    elif e == 5:
        b5.config(image=ladder)
    elif e == 6:
        b5.config(image=panel)
    elif e == 7:
        b5.config(image=red_rock)
    elif e == 8:
        b5.config(image=signal)
    elif e == 9:
        b5.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][5]
    if e == 0:
        b6.config(image=blank)
    elif e == 1:
        b6.config(image=block)
    elif e == 2:
        b6.config(image=bulb)
    elif e == 3:
        b6.config(image=dreed)
    elif e == 4:
        b6.config(image=frame)
    elif e == 10:
        b6.config(image=blank)
    elif e == 5:
        b6.config(image=ladder)
    elif e == 6:
        b6.config(image=panel)
    elif e == 7:
        b6.config(image=red_rock)
    elif e == 8:
        b6.config(image=signal)
    elif e == 9:
        b6.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][6]
    if e == 0:
        b7.config(image=blank)
    elif e == 1:
        b7.config(image=block)
    elif e == 2:
        b7.config(image=bulb)
    elif e == 3:
        b7.config(image=dreed)
    elif e == 4:
        b7.config(image=frame)
    elif e == 10:
        b7.config(image=blank)
    elif e == 5:
        b7.config(image=ladder)
    elif e == 6:
        b7.config(image=panel)
    elif e == 7:
        b7.config(image=red_rock)
    elif e == 8:
        b7.config(image=signal)
    elif e == 9:
        b7.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][7]
    if e == 0:
        b8.config(image=blank)
    elif e == 1:
        b8.config(image=block)
    elif e == 2:
        b8.config(image=bulb)
    elif e == 3:
        b8.config(image=dreed)
    elif e == 4:
        b8.config(image=frame)
    elif e == 10:
        b8.config(image=blank)
    elif e == 5:
        b8.config(image=ladder)
    elif e == 6:
        b8.config(image=panel)
    elif e == 7:
        b8.config(image=red_rock)
    elif e == 8:
        b8.config(image=signal)
    elif e == 9:
        b8.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][8]
    if e == 0:
        b9.config(image=blank)
    elif e == 1:
        b9.config(image=block)
    elif e == 2:
        b9.config(image=bulb)
    elif e == 3:
        b9.config(image=dreed)
    elif e == 4:
        b9.config(image=frame)
    elif e == 10:
        b9.config(image=blank)
    elif e == 5:
        b9.config(image=ladder)
    elif e == 6:
        b9.config(image=panel)
    elif e == 7:
        b9.config(image=red_rock)
    elif e == 8:
        b9.config(image=signal)
    elif e == 9:
        b9.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][9]
    if e == 0:
        b10.config(image=blank)
    elif e == 1:
        b10.config(image=block)
    elif e == 2:
        b10.config(image=bulb)
    elif e == 3:
        b10.config(image=dreed)
    elif e == 4:
        b10.config(image=frame)
    elif e == 10:
        b10.config(image=blank)
    elif e == 5:
        b10.config(image=ladder)
    elif e == 6:
        b10.config(image=panel)
    elif e == 7:
        b10.config(image=red_rock)
    elif e == 8:
        b10.config(image=signal)
    elif e == 9:
        b10.config(image=water)
    else:
        pass
    ##
    e = seen_world[1][10]
    if e == 0:
        b11.config(image=blank)
    elif e == 1:
        b11.config(image=block)
    elif e == 2:
        b11.config(image=bulb)
    elif e == 3:
        b11.config(image=dreed)
    elif e == 4:
        b11.config(image=frame)
    elif e == 10:
        b11.config(image=blank)
    elif e == 5:
        b11.config(image=ladder)
    elif e == 6:
        b11.config(image=panel)
    elif e == 7:
        b11.config(image=red_rock)
    elif e == 8:
        b11.config(image=signal)
    elif e == 9:
        b11.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][0]
    if e == 0:
        c1.config(image=blank)
    elif e == 1:
        c1.config(image=block)
    elif e == 2:
        c1.config(image=bulb)
    elif e == 3:
        c1.config(image=dreed)
    elif e == 4:
        c1.config(image=frame)
    elif e == 10:
        c1.config(image=blank)
    elif e == 5:
        c1.config(image=ladder)
    elif e == 6:
        c1.config(image=panel)
    elif e == 7:
        c1.config(image=red_rock)
    elif e == 8:
        c1.config(image=signal)
    elif e == 9:
        c1.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][1]
    if e == 0:
        c2.config(image=blank)
    elif e == 1:
        c2.config(image=block)
    elif e == 2:
        c2.config(image=bulb)
    elif e == 3:
        c2.config(image=dreed)
    elif e == 4:
        c2.config(image=frame)
    elif e == 10:
        c2.config(image=blank)
    elif e == 5:
        c2.config(image=ladder)
    elif e == 6:
        c2.config(image=panel)
    elif e == 7:
        c2.config(image=red_rock)
    elif e == 8:
        c2.config(image=signal)
    elif e == 9:
        c2.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][2]
    if e == 0:
        c3.config(image=blank)
    elif e == 1:
        c3.config(image=block)
    elif e == 2:
        c3.config(image=bulb)
    elif e == 3:
        c3.config(image=dreed)
    elif e == 4:
        c3.config(image=frame)
    elif e == 10:
        c3.config(image=blank)
    elif e == 5:
        c3.config(image=ladder)
    elif e == 6:
        c3.config(image=panel)
    elif e == 7:
        c3.config(image=red_rock)
    elif e == 8:
        c3.config(image=signal)
    elif e == 9:
        c3.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][3]
    if e == 0:
        c4.config(image=blank)
    elif e == 1:
        c4.config(image=block)
    elif e == 2:
        c4.config(image=bulb)
    elif e == 3:
        c4.config(image=dreed)
    elif e == 4:
        c4.config(image=frame)
    elif e == 10:
        c4.config(image=blank)
    elif e == 5:
        c4.config(image=ladder)
    elif e == 6:
        c4.config(image=panel)
    elif e == 7:
        c4.config(image=red_rock)
    elif e == 8:
        c4.config(image=signal)
    elif e == 9:
        c4.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][4]
    if e == 0:
        c5.config(image=blank)
    elif e == 1:
        c5.config(image=block)
    elif e == 2:
        c5.config(image=bulb)
    elif e == 3:
        c5.config(image=dreed)
    elif e == 4:
        c5.config(image=frame)
    elif e == 10:
        c5.config(image=blank)
    elif e == 5:
        c5.config(image=ladder)
    elif e == 6:
        c5.config(image=panel)
    elif e == 7:
        c5.config(image=red_rock)
    elif e == 8:
        c5.config(image=signal)
    elif e == 9:
        c5.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][5]
    if e == 0:
        c6.config(image=blank)
    elif e == 1:
        c6.config(image=block)
    elif e == 2:
        c6.config(image=bulb)
    elif e == 3:
        c6.config(image=dreed)
    elif e == 4:
        c6.config(image=frame)
    elif e == 10:
        c6.config(image=blank)
    elif e == 5:
        c6.config(image=ladder)
    elif e == 6:
        c6.config(image=panel)
    elif e == 7:
        c6.config(image=red_rock)
    elif e == 8:
        c6.config(image=signal)
    elif e == 9:
        c6.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][6]
    if e == 0:
        c7.config(image=blank)
    elif e == 1:
        c7.config(image=block)
    elif e == 2:
        c7.config(image=bulb)
    elif e == 3:
        c7.config(image=dreed)
    elif e == 4:
        c7.config(image=frame)
    elif e == 10:
        c7.config(image=blank)
    elif e == 5:
        c7.config(image=ladder)
    elif e == 6:
        c7.config(image=panel)
    elif e == 7:
        c7.config(image=red_rock)
    elif e == 8:
        c7.config(image=signal)
    elif e == 9:
        c7.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][7]
    if e == 0:
        c8.config(image=blank)
    elif e == 1:
        c8.config(image=block)
    elif e == 2:
        c8.config(image=bulb)
    elif e == 3:
        c8.config(image=dreed)
    elif e == 4:
        c8.config(image=frame)
    elif e == 10:
        c8.config(image=blank)
    elif e == 5:
        c8.config(image=ladder)
    elif e == 6:
        c8.config(image=panel)
    elif e == 7:
        c8.config(image=red_rock)
    elif e == 8:
        c8.config(image=signal)
    elif e == 9:
        c8.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][8]
    if e == 0:
        c9.config(image=blank)
    elif e == 1:
        c9.config(image=block)
    elif e == 2:
        c9.config(image=bulb)
    elif e == 3:
        c9.config(image=dreed)
    elif e == 4:
        c9.config(image=frame)
    elif e == 10:
        c9.config(image=blank)
    elif e == 5:
        c9.config(image=ladder)
    elif e == 6:
        c9.config(image=panel)
    elif e == 7:
        c9.config(image=red_rock)
    elif e == 8:
        c9.config(image=signal)
    elif e == 9:
        c9.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][9]
    if e == 0:
        c10.config(image=blank)
    elif e == 1:
        c10.config(image=block)
    elif e == 2:
        c10.config(image=bulb)
    elif e == 3:
        c10.config(image=dreed)
    elif e == 4:
        c10.config(image=frame)
    elif e == 10:
        c10.config(image=blank)
    elif e == 5:
        c10.config(image=ladder)
    elif e == 6:
        c10.config(image=panel)
    elif e == 7:
        c10.config(image=red_rock)
    elif e == 8:
        c10.config(image=signal)
    elif e == 9:
        c10.config(image=water)
    else:
        pass
    ##
    e = seen_world[2][10]
    if e == 0:
        c11.config(image=blank)
    elif e == 1:
        c11.config(image=block)
    elif e == 2:
        c11.config(image=bulb)
    elif e == 3:
        c11.config(image=dreed)
    elif e == 4:
        c11.config(image=frame)
    elif e == 10:
        c11.config(image=blank)
    elif e == 5:
        c11.config(image=ladder)
    elif e == 6:
        c11.config(image=panel)
    elif e == 7:
        c11.config(image=red_rock)
    elif e == 8:
        c11.config(image=signal)
    elif e == 9:
        c11.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][0]
    if e == 0:
        d1.config(image=blank)
    elif e == 1:
        d1.config(image=block)
    elif e == 2:
        d1.config(image=bulb)
    elif e == 3:
        d1.config(image=dreed)
    elif e == 4:
        d1.config(image=frame)
    elif e == 10:
        d1.config(image=blank)
    elif e == 5:
        d1.config(image=ladder)
    elif e == 6:
        d1.config(image=panel)
    elif e == 7:
        d1.config(image=red_rock)
    elif e == 8:
        d1.config(image=signal)
    elif e == 9:
        d1.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][1]
    if e == 0:
        d2.config(image=blank)
    elif e == 1:
        d2.config(image=block)
    elif e == 2:
        d2.config(image=bulb)
    elif e == 3:
        d2.config(image=dreed)
    elif e == 4:
        d2.config(image=frame)
    elif e == 10:
        d2.config(image=blank)
    elif e == 5:
        d2.config(image=ladder)
    elif e == 6:
        d2.config(image=panel)
    elif e == 7:
        d2.config(image=red_rock)
    elif e == 8:
        d2.config(image=signal)
    elif e == 9:
        d2.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][2]
    if e == 0:
        d3.config(image=blank)
    elif e == 1:
        d3.config(image=block)
    elif e == 2:
        d3.config(image=bulb)
    elif e == 3:
        d3.config(image=dreed)
    elif e == 4:
        d3.config(image=frame)
    elif e == 10:
        d3.config(image=blank)
    elif e == 5:
        d3.config(image=ladder)
    elif e == 6:
        d3.config(image=panel)
    elif e == 7:
        d3.config(image=red_rock)
    elif e == 8:
        d3.config(image=signal)
    elif e == 9:
        d3.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][3]
    if e == 0:
        d4.config(image=blank)
    elif e == 1:
        d4.config(image=block)
    elif e == 2:
        d4.config(image=bulb)
    elif e == 3:
        d4.config(image=dreed)
    elif e == 4:
        d4.config(image=frame)
    elif e == 10:
        d4.config(image=blank)
    elif e == 5:
        d4.config(image=ladder)
    elif e == 6:
        d4.config(image=panel)
    elif e == 7:
        d4.config(image=red_rock)
    elif e == 8:
        d4.config(image=signal)
    elif e == 9:
        d4.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][4]
    if e == 0:
        d5.config(image=blank)
    elif e == 1:
        d5.config(image=block)
    elif e == 2:
        d5.config(image=bulb)
    elif e == 3:
        d5.config(image=dreed)
    elif e == 4:
        d5.config(image=frame)
    elif e == 10:
        d5.config(image=blank)
    elif e == 5:
        d5.config(image=ladder)
    elif e == 6:
        d5.config(image=panel)
    elif e == 7:
        d5.config(image=red_rock)
    elif e == 8:
        d5.config(image=signal)
    elif e == 9:
        d5.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][5]
    if e == 0:
        d6.config(image=blank)
    elif e == 1:
        d6.config(image=block)
    elif e == 2:
        d6.config(image=bulb)
    elif e == 3:
        d6.config(image=dreed)
    elif e == 4:
        d6.config(image=frame)
    elif e == 10:
        d6.config(image=blank)
    elif e == 5:
        d6.config(image=ladder)
    elif e == 6:
        d6.config(image=panel)
    elif e == 7:
        d6.config(image=red_rock)
    elif e == 8:
        d6.config(image=signal)
    elif e == 9:
        d6.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][6]
    if e == 0:
        d7.config(image=blank)
    elif e == 1:
        d7.config(image=block)
    elif e == 2:
        d7.config(image=bulb)
    elif e == 3:
        d7.config(image=dreed)
    elif e == 4:
        d7.config(image=frame)
    elif e == 10:
        d7.config(image=blank)
    elif e == 5:
        d7.config(image=ladder)
    elif e == 6:
        d7.config(image=panel)
    elif e == 7:
        d7.config(image=red_rock)
    elif e == 8:
        d7.config(image=signal)
    elif e == 9:
        d7.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][7]
    if e == 0:
        d8.config(image=blank)
    elif e == 1:
        d8.config(image=block)
    elif e == 2:
        d8.config(image=bulb)
    elif e == 3:
        d8.config(image=dreed)
    elif e == 4:
        d8.config(image=frame)
    elif e == 10:
        d8.config(image=blank)
    elif e == 5:
        d8.config(image=ladder)
    elif e == 6:
        d8.config(image=panel)
    elif e == 7:
        d8.config(image=red_rock)
    elif e == 8:
        d8.config(image=signal)
    elif e == 9:
        d8.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][8]
    if e == 0:
        d9.config(image=blank)
    elif e == 1:
        d9.config(image=block)
    elif e == 2:
        d9.config(image=bulb)
    elif e == 3:
        d9.config(image=dreed)
    elif e == 4:
        d9.config(image=frame)
    elif e == 10:
        d9.config(image=blank)
    elif e == 5:
        d9.config(image=ladder)
    elif e == 6:
        d9.config(image=panel)
    elif e == 7:
        d9.config(image=red_rock)
    elif e == 8:
        d9.config(image=signal)
    elif e == 9:
        d9.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][9]
    if e == 0:
        d10.config(image=blank)
    elif e == 1:
        d10.config(image=block)
    elif e == 2:
        d10.config(image=bulb)
    elif e == 3:
        d10.config(image=dreed)
    elif e == 4:
        d10.config(image=frame)
    elif e == 10:
        d10.config(image=blank)
    elif e == 5:
        d10.config(image=ladder)
    elif e == 6:
        d10.config(image=panel)
    elif e == 7:
        d10.config(image=red_rock)
    elif e == 8:
        d10.config(image=signal)
    elif e == 9:
        d10.config(image=water)
    else:
        pass
    ##
    e = seen_world[3][10]
    if e == 0:
        d11.config(image=blank)
    elif e == 1:
        d11.config(image=block)
    elif e == 2:
        d11.config(image=bulb)
    elif e == 3:
        d11.config(image=dreed)
    elif e == 4:
        d11.config(image=frame)
    elif e == 10:
        d11.config(image=blank)
    elif e == 5:
        d11.config(image=ladder)
    elif e == 6:
        d11.config(image=panel)
    elif e == 7:
        d11.config(image=red_rock)
    elif e == 8:
        d11.config(image=signal)
    elif e == 9:
        d11.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][0]
    if e == 0:
        e1.config(image=blank)
    elif e == 1:
        e1.config(image=block)
    elif e == 2:
        e1.config(image=bulb)
    elif e == 3:
        e1.config(image=dreed)
    elif e == 4:
        e1.config(image=frame)
    elif e == 10:
        e1.config(image=blank)
    elif e == 5:
        e1.config(image=ladder)
    elif e == 6:
        e1.config(image=panel)
    elif e == 7:
        e1.config(image=red_rock)
    elif e == 8:
        e1.config(image=signal)
    elif e == 9:
        e1.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][1]
    if e == 0:
        e2.config(image=blank)
    elif e == 1:
        e2.config(image=block)
    elif e == 2:
        e2.config(image=bulb)
    elif e == 3:
        e2.config(image=dreed)
    elif e == 4:
        e2.config(image=frame)
    elif e == 10:
        e2.config(image=blank)
    elif e == 5:
        e2.config(image=ladder)
    elif e == 6:
        e2.config(image=panel)
    elif e == 7:
        e2.config(image=red_rock)
    elif e == 8:
        e2.config(image=signal)
    elif e == 9:
        e2.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][2]
    if e == 0:
        e3.config(image=blank)
    elif e == 1:
        e3.config(image=block)
    elif e == 2:
        e3.config(image=bulb)
    elif e == 3:
        e3.config(image=dreed)
    elif e == 4:
        e3.config(image=frame)
    elif e == 10:
        e3.config(image=blank)
    elif e == 5:
        e3.config(image=ladder)
    elif e == 6:
        e3.config(image=panel)
    elif e == 7:
        e3.config(image=red_rock)
    elif e == 8:
        e3.config(image=signal)
    elif e == 9:
        e3.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][3]
    if e == 0:
        e4.config(image=blank)
    elif e == 1:
        e4.config(image=block)
    elif e == 2:
        e4.config(image=bulb)
    elif e == 3:
        e4.config(image=dreed)
    elif e == 4:
        e4.config(image=frame)
    elif e == 10:
        e4.config(image=blank)
    elif e == 5:
        e4.config(image=ladder)
    elif e == 6:
        e4.config(image=panel)
    elif e == 7:
        e4.config(image=red_rock)
    elif e == 8:
        e4.config(image=signal)
    elif e == 9:
        e4.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][4]
    if e == 0:
        e5.config(image=blank)
    elif e == 1:
        e5.config(image=block)
    elif e == 2:
        e5.config(image=bulb)
    elif e == 3:
        e5.config(image=dreed)
    elif e == 4:
        e5.config(image=frame)
    elif e == 10:
        e5.config(image=blank)
    elif e == 5:
        e5.config(image=ladder)
    elif e == 6:
        e5.config(image=panel)
    elif e == 7:
        e5.config(image=red_rock)
    elif e == 8:
        e5.config(image=signal)
    elif e == 9:
        e5.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][5]
    if e == 0:
        e6.config(image=blank)
    elif e == 1:
        e6.config(image=block)
    elif e == 2:
        e6.config(image=bulb)
    elif e == 3:
        e6.config(image=dreed)
    elif e == 4:
        e6.config(image=frame)
    elif e == 10:
        e6.config(image=blank)
    elif e == 5:
        e6.config(image=ladder)
    elif e == 6:
        e6.config(image=panel)
    elif e == 7:
        e6.config(image=red_rock)
    elif e == 8:
        e6.config(image=signal)
    elif e == 9:
        e6.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][6]
    if e == 0:
        e7.config(image=blank)
    elif e == 1:
        e7.config(image=block)
    elif e == 2:
        e7.config(image=bulb)
    elif e == 3:
        e7.config(image=dreed)
    elif e == 4:
        e7.config(image=frame)
    elif e == 10:
        e7.config(image=blank)
    elif e == 5:
        e7.config(image=ladder)
    elif e == 6:
        e7.config(image=panel)
    elif e == 7:
        e7.config(image=red_rock)
    elif e == 8:
        e7.config(image=signal)
    elif e == 9:
        e7.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][7]
    if e == 0:
        e8.config(image=blank)
    elif e == 1:
        e8.config(image=block)
    elif e == 2:
        e8.config(image=bulb)
    elif e == 3:
        e8.config(image=dreed)
    elif e == 4:
        e8.config(image=frame)
    elif e == 10:
        e8.config(image=blank)
    elif e == 5:
        e8.config(image=ladder)
    elif e == 6:
        e8.config(image=panel)
    elif e == 7:
        e8.config(image=red_rock)
    elif e == 8:
        e8.config(image=signal)
    elif e == 9:
        e8.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][8]
    if e == 0:
        e9.config(image=blank)
    elif e == 1:
        e9.config(image=block)
    elif e == 2:
        e9.config(image=bulb)
    elif e == 3:
        e9.config(image=dreed)
    elif e == 4:
        e9.config(image=frame)
    elif e == 10:
        e9.config(image=blank)
    elif e == 5:
        e9.config(image=ladder)
    elif e == 6:
        e9.config(image=panel)
    elif e == 7:
        e9.config(image=red_rock)
    elif e == 8:
        e9.config(image=signal)
    elif e == 9:
        e9.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][9]
    if e == 0:
        e10.config(image=blank)
    elif e == 1:
        e10.config(image=block)
    elif e == 2:
        e10.config(image=bulb)
    elif e == 3:
        e10.config(image=dreed)
    elif e == 4:
        e10.config(image=frame)
    elif e == 10:
        e10.config(image=blank)
    elif e == 5:
        e10.config(image=ladder)
    elif e == 6:
        e10.config(image=panel)
    elif e == 7:
        e10.config(image=red_rock)
    elif e == 8:
        e10.config(image=signal)
    elif e == 9:
        e10.config(image=water)
    else:
        pass
    ##
    e = seen_world[4][10]
    if e == 0:
        e11.config(image=blank)
    elif e == 1:
        e11.config(image=block)
    elif e == 2:
        e11.config(image=bulb)
    elif e == 3:
        e11.config(image=dreed)
    elif e == 4:
        e11.config(image=frame)
    elif e == 10:
        e11.config(image=blank)
    elif e == 5:
        e11.config(image=ladder)
    elif e == 6:
        e11.config(image=panel)
    elif e == 7:
        e11.config(image=red_rock)
    elif e == 8:
        e11.config(image=signal)
    elif e == 9:
        e11.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][0]
    if e == 0:
        f1.config(image=blank)
    elif e == 1:
        f1.config(image=block)
    elif e == 2:
        f1.config(image=bulb)
    elif e == 3:
        f1.config(image=dreed)
    elif e == 4:
        f1.config(image=frame)
    elif e == 10:
        f1.config(image=blank)
    elif e == 5:
        f1.config(image=ladder)
    elif e == 6:
        f1.config(image=panel)
    elif e == 7:
        f1.config(image=red_rock)
    elif e == 8:
        f1.config(image=signal)
    elif e == 9:
        f1.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][1]
    if e == 0:
        f2.config(image=blank)
    elif e == 1:
        f2.config(image=block)
    elif e == 2:
        f2.config(image=bulb)
    elif e == 3:
        f2.config(image=dreed)
    elif e == 4:
        f2.config(image=frame)
    elif e == 10:
        f2.config(image=blank)
    elif e == 5:
        f2.config(image=ladder)
    elif e == 6:
        f2.config(image=panel)
    elif e == 7:
        f2.config(image=red_rock)
    elif e == 8:
        f2.config(image=signal)
    elif e == 9:
        f2.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][2]
    if e == 0:
        f3.config(image=blank)
    elif e == 1:
        f3.config(image=block)
    elif e == 2:
        f3.config(image=bulb)
    elif e == 3:
        f3.config(image=dreed)
    elif e == 4:
        f3.config(image=frame)
    elif e == 10:
        f3.config(image=blank)
    elif e == 5:
        f3.config(image=ladder)
    elif e == 6:
        f3.config(image=panel)
    elif e == 7:
        f3.config(image=red_rock)
    elif e == 8:
        f3.config(image=signal)
    elif e == 9:
        f3.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][3]
    if e == 0:
        f4.config(image=blank)
    elif e == 1:
        f4.config(image=block)
    elif e == 2:
        f4.config(image=bulb)
    elif e == 3:
        f4.config(image=dreed)
    elif e == 4:
        f4.config(image=frame)
    elif e == 10:
        f4.config(image=blank)
    elif e == 5:
        f4.config(image=ladder)
    elif e == 6:
        f4.config(image=panel)
    elif e == 7:
        f4.config(image=red_rock)
    elif e == 8:
        f4.config(image=signal)
    elif e == 9:
        f4.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][4]
    if e == 0:
        f5.config(image=blank)
    elif e == 1:
        f5.config(image=block)
    elif e == 2:
        f5.config(image=bulb)
    elif e == 3:
        f5.config(image=dreed)
    elif e == 4:
        f5.config(image=frame)
    elif e == 10:
        f5.config(image=blank)
    elif e == 5:
        f5.config(image=ladder)
    elif e == 6:
        f5.config(image=panel)
    elif e == 7:
        f5.config(image=red_rock)
    elif e == 8:
        f5.config(image=signal)
    elif e == 9:
        f5.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][5]
    if e == 0:
        f6.config(image=blank)
    elif e == 1:
        f6.config(image=block)
    elif e == 2:
        f6.config(image=bulb)
    elif e == 3:
        f6.config(image=dreed)
    elif e == 4:
        f6.config(image=frame)
    elif e == 10:
        f6.config(image=blank)
        global prev_block
        if prev_block == 9:
            qwe.config(image=wat)
        else:
            qwe.config(image=norm)
    elif e == 5:
        f6.config(image=ladder)
    elif e == 6:
        f6.config(image=panel)
    elif e == 7:
        f6.config(image=red_rock)
    elif e == 8:
        f6.config(image=signal)
    elif e == 9:
        f6.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][6]
    if e == 0:
        f7.config(image=blank)
    elif e == 1:
        f7.config(image=block)
    elif e == 2:
        f7.config(image=bulb)
    elif e == 3:
        f7.config(image=dreed)
    elif e == 4:
        f7.config(image=frame)
    elif e == 10:
        f7.config(image=blank)
    elif e == 5:
        f7.config(image=ladder)
    elif e == 6:
        f7.config(image=panel)
    elif e == 7:
        f7.config(image=red_rock)
    elif e == 8:
        f7.config(image=signal)
    elif e == 9:
        f7.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][7]
    if e == 0:
        f8.config(image=blank)
    elif e == 1:
        f8.config(image=block)
    elif e == 2:
        f8.config(image=bulb)
    elif e == 3:
        f8.config(image=dreed)
    elif e == 4:
        f8.config(image=frame)
    elif e == 10:
        f8.config(image=blank)
    elif e == 5:
        f8.config(image=ladder)
    elif e == 6:
        f8.config(image=panel)
    elif e == 7:
        f8.config(image=red_rock)
    elif e == 8:
        f8.config(image=signal)
    elif e == 9:
        f8.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][8]
    if e == 0:
        f9.config(image=blank)
    elif e == 1:
        f9.config(image=block)
    elif e == 2:
        f9.config(image=bulb)
    elif e == 3:
        f9.config(image=dreed)
    elif e == 4:
        f9.config(image=frame)
    elif e == 10:
        f9.config(image=blank)
    elif e == 5:
        f9.config(image=ladder)
    elif e == 6:
        f9.config(image=panel)
    elif e == 7:
        f9.config(image=red_rock)
    elif e == 8:
        f9.config(image=signal)
    elif e == 9:
        f9.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][9]
    if e == 0:
        f10.config(image=blank)
    elif e == 1:
        f10.config(image=block)
    elif e == 2:
        f10.config(image=bulb)
    elif e == 3:
        f10.config(image=dreed)
    elif e == 4:
        f10.config(image=frame)
    elif e == 10:
        f10.config(image=blank)
    elif e == 5:
        f10.config(image=ladder)
    elif e == 6:
        f10.config(image=panel)
    elif e == 7:
        f10.config(image=red_rock)
    elif e == 8:
        f10.config(image=signal)
    elif e == 9:
        f10.config(image=water)
    else:
        pass
    ##
    e = seen_world[5][10]
    if e == 0:
        f11.config(image=blank)
    elif e == 1:
        f11.config(image=block)
    elif e == 2:
        f11.config(image=bulb)
    elif e == 3:
        f11.config(image=dreed)
    elif e == 4:
        f11.config(image=frame)
    elif e == 10:
        f11.config(image=blank)
    elif e == 5:
        f11.config(image=ladder)
    elif e == 6:
        f11.config(image=panel)
    elif e == 7:
        f11.config(image=red_rock)
    elif e == 8:
        f11.config(image=signal)
    elif e == 9:
        f11.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][0]
    if e == 0:
        g1.config(image=blank)
    elif e == 1:
        g1.config(image=block)
    elif e == 2:
        g1.config(image=bulb)
    elif e == 3:
        g1.config(image=dreed)
    elif e == 4:
        g1.config(image=frame)
    elif e == 10:
        g1.config(image=blank)
    elif e == 5:
        g1.config(image=ladder)
    elif e == 6:
        g1.config(image=panel)
    elif e == 7:
        g1.config(image=red_rock)
    elif e == 8:
        g1.config(image=signal)
    elif e == 9:
        g1.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][1]
    if e == 0:
        g2.config(image=blank)
    elif e == 1:
        g2.config(image=block)
    elif e == 2:
        g2.config(image=bulb)
    elif e == 3:
        g2.config(image=dreed)
    elif e == 4:
        g2.config(image=frame)
    elif e == 10:
        g2.config(image=blank)
    elif e == 5:
        g2.config(image=ladder)
    elif e == 6:
        g2.config(image=panel)
    elif e == 7:
        g2.config(image=red_rock)
    elif e == 8:
        g2.config(image=signal)
    elif e == 9:
        g2.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][2]
    if e == 0:
        g3.config(image=blank)
    elif e == 1:
        g3.config(image=block)
    elif e == 2:
        g3.config(image=bulb)
    elif e == 3:
        g3.config(image=dreed)
    elif e == 4:
        g3.config(image=frame)
    elif e == 10:
        g3.config(image=blank)
    elif e == 5:
        g3.config(image=ladder)
    elif e == 6:
        g3.config(image=panel)
    elif e == 7:
        g3.config(image=red_rock)
    elif e == 8:
        g3.config(image=signal)
    elif e == 9:
        g3.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][3]
    if e == 0:
        g4.config(image=blank)
    elif e == 1:
        g4.config(image=block)
    elif e == 2:
        g4.config(image=bulb)
    elif e == 3:
        g4.config(image=dreed)
    elif e == 4:
        g4.config(image=frame)
    elif e == 10:
        g4.config(image=blank)
    elif e == 5:
        g4.config(image=ladder)
    elif e == 6:
        g4.config(image=panel)
    elif e == 7:
        g4.config(image=red_rock)
    elif e == 8:
        g4.config(image=signal)
    elif e == 9:
        g4.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][4]
    if e == 0:
        g5.config(image=blank)
    elif e == 1:
        g5.config(image=block)
    elif e == 2:
        g5.config(image=bulb)
    elif e == 3:
        g5.config(image=dreed)
    elif e == 4:
        g5.config(image=frame)
    elif e == 10:
        g5.config(image=blank)
    elif e == 5:
        g5.config(image=ladder)
    elif e == 6:
        g5.config(image=panel)
    elif e == 7:
        g5.config(image=red_rock)
    elif e == 8:
        g5.config(image=signal)
    elif e == 9:
        g5.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][5]
    if e == 0:
        g6.config(image=blank)
    elif e == 1:
        g6.config(image=block)
    elif e == 2:
        g6.config(image=bulb)
    elif e == 3:
        g6.config(image=dreed)
    elif e == 4:
        g6.config(image=frame)
    elif e == 10:
        g6.config(image=blank)
    elif e == 5:
        g6.config(image=ladder)
    elif e == 6:
        g6.config(image=panel)
    elif e == 7:
        g6.config(image=red_rock)
    elif e == 8:
        g6.config(image=signal)
    elif e == 9:
        g6.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][6]
    if e == 0:
        g7.config(image=blank)
    elif e == 1:
        g7.config(image=block)
    elif e == 2:
        g7.config(image=bulb)
    elif e == 3:
        g7.config(image=dreed)
    elif e == 4:
        g7.config(image=frame)
    elif e == 10:
        g7.config(image=blank)
    elif e == 5:
        g7.config(image=ladder)
    elif e == 6:
        g7.config(image=panel)
    elif e == 7:
        g7.config(image=red_rock)
    elif e == 8:
        g7.config(image=signal)
    elif e == 9:
        g7.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][7]
    if e == 0:
        g8.config(image=blank)
    elif e == 1:
        g8.config(image=block)
    elif e == 2:
        g8.config(image=bulb)
    elif e == 3:
        g8.config(image=dreed)
    elif e == 4:
        g8.config(image=frame)
    elif e == 10:
        g8.config(image=blank)
    elif e == 5:
        g8.config(image=ladder)
    elif e == 6:
        g8.config(image=panel)
    elif e == 7:
        g8.config(image=red_rock)
    elif e == 8:
        g8.config(image=signal)
    elif e == 9:
        g8.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][8]
    if e == 0:
        g9.config(image=blank)
    elif e == 1:
        g9.config(image=block)
    elif e == 2:
        g9.config(image=bulb)
    elif e == 3:
        g9.config(image=dreed)
    elif e == 4:
        g9.config(image=frame)
    elif e == 10:
        g9.config(image=blank)
    elif e == 5:
        g9.config(image=ladder)
    elif e == 6:
        g9.config(image=panel)
    elif e == 7:
        g9.config(image=red_rock)
    elif e == 8:
        g9.config(image=signal)
    elif e == 9:
        g9.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][9]
    if e == 0:
        g10.config(image=blank)
    elif e == 1:
        g10.config(image=block)
    elif e == 2:
        g10.config(image=bulb)
    elif e == 3:
        g10.config(image=dreed)
    elif e == 4:
        g10.config(image=frame)
    elif e == 10:
        g10.config(image=blank)
    elif e == 5:
        g10.config(image=ladder)
    elif e == 6:
        g10.config(image=panel)
    elif e == 7:
        g10.config(image=red_rock)
    elif e == 8:
        g10.config(image=signal)
    elif e == 9:
        g10.config(image=water)
    else:
        pass
    ##
    e = seen_world[6][10]
    if e == 0:
        g11.config(image=blank)
    elif e == 1:
        g11.config(image=block)
    elif e == 2:
        g11.config(image=bulb)
    elif e == 3:
        g11.config(image=dreed)
    elif e == 4:
        g11.config(image=frame)
    elif e == 10:
        g11.config(image=blank)
    elif e == 5:
        g11.config(image=ladder)
    elif e == 6:
        g11.config(image=panel)
    elif e == 7:
        g11.config(image=red_rock)
    elif e == 8:
        g11.config(image=signal)
    elif e == 9:
        g11.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][0]
    if e == 0:
        h1.config(image=blank)
    elif e == 1:
        h1.config(image=block)
    elif e == 2:
        h1.config(image=bulb)
    elif e == 3:
        h1.config(image=dreed)
    elif e == 4:
        h1.config(image=frame)
    elif e == 10:
        h1.config(image=blank)
    elif e == 5:
        h1.config(image=ladder)
    elif e == 6:
        h1.config(image=panel)
    elif e == 7:
        h1.config(image=red_rock)
    elif e == 8:
        h1.config(image=signal)
    elif e == 9:
        h1.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][1]
    if e == 0:
        h2.config(image=blank)
    elif e == 1:
        h2.config(image=block)
    elif e == 2:
        h2.config(image=bulb)
    elif e == 3:
        h2.config(image=dreed)
    elif e == 4:
        h2.config(image=frame)
    elif e == 10:
        h2.config(image=blank)
    elif e == 5:
        h2.config(image=ladder)
    elif e == 6:
        h2.config(image=panel)
    elif e == 7:
        h2.config(image=red_rock)
    elif e == 8:
        h2.config(image=signal)
    elif e == 9:
        h2.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][2]
    if e == 0:
        h3.config(image=blank)
    elif e == 1:
        h3.config(image=block)
    elif e == 2:
        h3.config(image=bulb)
    elif e == 3:
        h3.config(image=dreed)
    elif e == 4:
        h3.config(image=frame)
    elif e == 10:
        h3.config(image=blank)
    elif e == 5:
        h3.config(image=ladder)
    elif e == 6:
        h3.config(image=panel)
    elif e == 7:
        h3.config(image=red_rock)
    elif e == 8:
        h3.config(image=signal)
    elif e == 9:
        h3.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][3]
    if e == 0:
        h4.config(image=blank)
    elif e == 1:
        h4.config(image=block)
    elif e == 2:
        h4.config(image=bulb)
    elif e == 3:
        h4.config(image=dreed)
    elif e == 4:
        h4.config(image=frame)
    elif e == 10:
        h4.config(image=blank)
    elif e == 5:
        h4.config(image=ladder)
    elif e == 6:
        h4.config(image=panel)
    elif e == 7:
        h4.config(image=red_rock)
    elif e == 8:
        h4.config(image=signal)
    elif e == 9:
        h4.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][4]
    if e == 0:
        h5.config(image=blank)
    elif e == 1:
        h5.config(image=block)
    elif e == 2:
        h5.config(image=bulb)
    elif e == 3:
        h5.config(image=dreed)
    elif e == 4:
        h5.config(image=frame)
    elif e == 10:
        h5.config(image=blank)
    elif e == 5:
        h5.config(image=ladder)
    elif e == 6:
        h5.config(image=panel)
    elif e == 7:
        h5.config(image=red_rock)
    elif e == 8:
        h5.config(image=signal)
    elif e == 9:
        h5.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][5]
    if e == 0:
        h6.config(image=blank)
    elif e == 1:
        h6.config(image=block)
    elif e == 2:
        h6.config(image=bulb)
    elif e == 3:
        h6.config(image=dreed)
    elif e == 4:
        h6.config(image=frame)
    elif e == 10:
        h6.config(image=blank)
    elif e == 5:
        h6.config(image=ladder)
    elif e == 6:
        h6.config(image=panel)
    elif e == 7:
        h6.config(image=red_rock)
    elif e == 8:
        h6.config(image=signal)
    elif e == 9:
        h6.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][6]
    if e == 0:
        h7.config(image=blank)
    elif e == 1:
        h7.config(image=block)
    elif e == 2:
        h7.config(image=bulb)
    elif e == 3:
        h7.config(image=dreed)
    elif e == 4:
        h7.config(image=frame)
    elif e == 10:
        h7.config(image=blank)
    elif e == 5:
        h7.config(image=ladder)
    elif e == 6:
        h7.config(image=panel)
    elif e == 7:
        h7.config(image=red_rock)
    elif e == 8:
        h7.config(image=signal)
    elif e == 9:
        h7.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][7]
    if e == 0:
        h8.config(image=blank)
    elif e == 1:
        h8.config(image=block)
    elif e == 2:
        h8.config(image=bulb)
    elif e == 3:
        h8.config(image=dreed)
    elif e == 4:
        h8.config(image=frame)
    elif e == 10:
        h8.config(image=blank)
    elif e == 5:
        h8.config(image=ladder)
    elif e == 6:
        h8.config(image=panel)
    elif e == 7:
        h8.config(image=red_rock)
    elif e == 8:
        h8.config(image=signal)
    elif e == 9:
        h8.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][8]
    if e == 0:
        h9.config(image=blank)
    elif e == 1:
        h9.config(image=block)
    elif e == 2:
        h9.config(image=bulb)
    elif e == 3:
        h9.config(image=dreed)
    elif e == 4:
        h9.config(image=frame)
    elif e == 10:
        h9.config(image=blank)
    elif e == 5:
        h9.config(image=ladder)
    elif e == 6:
        h9.config(image=panel)
    elif e == 7:
        h9.config(image=red_rock)
    elif e == 8:
        h9.config(image=signal)
    elif e == 9:
        h9.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][9]
    if e == 0:
        h10.config(image=blank)
    elif e == 1:
        h10.config(image=block)
    elif e == 2:
        h10.config(image=bulb)
    elif e == 3:
        h10.config(image=dreed)
    elif e == 4:
        h10.config(image=frame)
    elif e == 10:
        h10.config(image=blank)
    elif e == 5:
        h10.config(image=ladder)
    elif e == 6:
        h10.config(image=panel)
    elif e == 7:
        h10.config(image=red_rock)
    elif e == 8:
        h10.config(image=signal)
    elif e == 9:
        h10.config(image=water)
    else:
        pass
    ##
    e = seen_world[7][10]
    if e == 0:
        h11.config(image=blank)
    elif e == 1:
        h11.config(image=block)
    elif e == 2:
        h11.config(image=bulb)
    elif e == 3:
        h11.config(image=dreed)
    elif e == 4:
        h11.config(image=frame)
    elif e == 10:
        h11.config(image=blank)
    elif e == 5:
        h11.config(image=ladder)
    elif e == 6:
        h11.config(image=panel)
    elif e == 7:
        h11.config(image=red_rock)
    elif e == 8:
        h11.config(image=signal)
    elif e == 9:
        h11.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][0]
    if e == 0:
        i1.config(image=blank)
    elif e == 1:
        i1.config(image=block)
    elif e == 2:
        i1.config(image=bulb)
    elif e == 3:
        i1.config(image=dreed)
    elif e == 4:
        i1.config(image=frame)
    elif e == 10:
        i1.config(image=blank)
    elif e == 5:
        i1.config(image=ladder)
    elif e == 6:
        i1.config(image=panel)
    elif e == 7:
        i1.config(image=red_rock)
    elif e == 8:
        i1.config(image=signal)
    elif e == 9:
        i1.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][1]
    if e == 0:
        i2.config(image=blank)
    elif e == 1:
        i2.config(image=block)
    elif e == 2:
        i2.config(image=bulb)
    elif e == 3:
        i2.config(image=dreed)
    elif e == 4:
        i2.config(image=frame)
    elif e == 10:
        i2.config(image=blank)
    elif e == 5:
        i2.config(image=ladder)
    elif e == 6:
        i2.config(image=panel)
    elif e == 7:
        i2.config(image=red_rock)
    elif e == 8:
        i2.config(image=signal)
    elif e == 9:
        i2.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][2]
    if e == 0:
        i3.config(image=blank)
    elif e == 1:
        i3.config(image=block)
    elif e == 2:
        i3.config(image=bulb)
    elif e == 3:
        i3.config(image=dreed)
    elif e == 4:
        i3.config(image=frame)
    elif e == 10:
        i3.config(image=blank)
    elif e == 5:
        i3.config(image=ladder)
    elif e == 6:
        i3.config(image=panel)
    elif e == 7:
        i3.config(image=red_rock)
    elif e == 8:
        i3.config(image=signal)
    elif e == 9:
        i3.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][3]
    if e == 0:
        i4.config(image=blank)
    elif e == 1:
        i4.config(image=block)
    elif e == 2:
        i4.config(image=bulb)
    elif e == 3:
        i4.config(image=dreed)
    elif e == 4:
        i4.config(image=frame)
    elif e == 10:
        i4.config(image=blank)
    elif e == 5:
        i4.config(image=ladder)
    elif e == 6:
        i4.config(image=panel)
    elif e == 7:
        i4.config(image=red_rock)
    elif e == 8:
        i4.config(image=signal)
    elif e == 9:
        i4.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][4]
    if e == 0:
        i5.config(image=blank)
    elif e == 1:
        i5.config(image=block)
    elif e == 2:
        i5.config(image=bulb)
    elif e == 3:
        i5.config(image=dreed)
    elif e == 4:
        i5.config(image=frame)
    elif e == 10:
        i5.config(image=blank)
    elif e == 5:
        i5.config(image=ladder)
    elif e == 6:
        i5.config(image=panel)
    elif e == 7:
        i5.config(image=red_rock)
    elif e == 8:
        i5.config(image=signal)
    elif e == 9:
        i5.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][5]
    if e == 0:
        i6.config(image=blank)
    elif e == 1:
        i6.config(image=block)
    elif e == 2:
        i6.config(image=bulb)
    elif e == 3:
        i6.config(image=dreed)
    elif e == 4:
        i6.config(image=frame)
    elif e == 10:
        i6.config(image=blank)
    elif e == 5:
        i6.config(image=ladder)
    elif e == 6:
        i6.config(image=panel)
    elif e == 7:
        i6.config(image=red_rock)
    elif e == 8:
        i6.config(image=signal)
    elif e == 9:
        i6.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][6]
    if e == 0:
        i7.config(image=blank)
    elif e == 1:
        i7.config(image=block)
    elif e == 2:
        i7.config(image=bulb)
    elif e == 3:
        i7.config(image=dreed)
    elif e == 4:
        i7.config(image=frame)
    elif e == 10:
        i7.config(image=blank)
    elif e == 5:
        i7.config(image=ladder)
    elif e == 6:
        i7.config(image=panel)
    elif e == 7:
        i7.config(image=red_rock)
    elif e == 8:
        i7.config(image=signal)
    elif e == 9:
        i7.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][7]
    if e == 0:
        i8.config(image=blank)
    elif e == 1:
        i8.config(image=block)
    elif e == 2:
        i8.config(image=bulb)
    elif e == 3:
        i8.config(image=dreed)
    elif e == 4:
        i8.config(image=frame)
    elif e == 10:
        i8.config(image=blank)
    elif e == 5:
        i8.config(image=ladder)
    elif e == 6:
        i8.config(image=panel)
    elif e == 7:
        i8.config(image=red_rock)
    elif e == 8:
        i8.config(image=signal)
    elif e == 9:
        i8.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][8]
    if e == 0:
        i9.config(image=blank)
    elif e == 1:
        i9.config(image=block)
    elif e == 2:
        i9.config(image=bulb)
    elif e == 3:
        i9.config(image=dreed)
    elif e == 4:
        i9.config(image=frame)
    elif e == 10:
        i9.config(image=blank)
    elif e == 5:
        i9.config(image=ladder)
    elif e == 6:
        i9.config(image=panel)
    elif e == 7:
        i9.config(image=red_rock)
    elif e == 8:
        i9.config(image=signal)
    elif e == 9:
        i9.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][9]
    if e == 0:
        i10.config(image=blank)
    elif e == 1:
        i10.config(image=block)
    elif e == 2:
        i10.config(image=bulb)
    elif e == 3:
        i10.config(image=dreed)
    elif e == 4:
        i10.config(image=frame)
    elif e == 10:
        i10.config(image=blank)
    elif e == 5:
        i10.config(image=ladder)
    elif e == 6:
        i10.config(image=panel)
    elif e == 7:
        i10.config(image=red_rock)
    elif e == 8:
        i10.config(image=signal)
    elif e == 9:
        i10.config(image=water)
    else:
        pass
    ##
    e = seen_world[8][10]
    if e == 0:
        i11.config(image=blank)
    elif e == 1:
        i11.config(image=block)
    elif e == 2:
        i11.config(image=bulb)
    elif e == 3:
        i11.config(image=dreed)
    elif e == 4:
        i11.config(image=frame)
    elif e == 10:
        i11.config(image=blank)
    elif e == 5:
        i11.config(image=ladder)
    elif e == 6:
        i11.config(image=panel)
    elif e == 7:
        i11.config(image=red_rock)
    elif e == 8:
        i11.config(image=signal)
    elif e == 9:
        i11.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][0]
    if e == 0:
        j1.config(image=blank)
    elif e == 1:
        j1.config(image=block)
    elif e == 2:
        j1.config(image=bulb)
    elif e == 3:
        j1.config(image=dreed)
    elif e == 4:
        j1.config(image=frame)
    elif e == 10:
        j1.config(image=blank)
    elif e == 5:
        j1.config(image=ladder)
    elif e == 6:
        j1.config(image=panel)
    elif e == 7:
        j1.config(image=red_rock)
    elif e == 8:
        j1.config(image=signal)
    elif e == 9:
        j1.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][1]
    if e == 0:
        j2.config(image=blank)
    elif e == 1:
        j2.config(image=block)
    elif e == 2:
        j2.config(image=bulb)
    elif e == 3:
        j2.config(image=dreed)
    elif e == 4:
        j2.config(image=frame)
    elif e == 10:
        j2.config(image=blank)
    elif e == 5:
        j2.config(image=ladder)
    elif e == 6:
        j2.config(image=panel)
    elif e == 7:
        j2.config(image=red_rock)
    elif e == 8:
        j2.config(image=signal)
    elif e == 9:
        j2.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][2]
    if e == 0:
        j3.config(image=blank)
    elif e == 1:
        j3.config(image=block)
    elif e == 2:
        j3.config(image=bulb)
    elif e == 3:
        j3.config(image=dreed)
    elif e == 4:
        j3.config(image=frame)
    elif e == 10:
        j3.config(image=blank)
    elif e == 5:
        j3.config(image=ladder)
    elif e == 6:
        j3.config(image=panel)
    elif e == 7:
        j3.config(image=red_rock)
    elif e == 8:
        j3.config(image=signal)
    elif e == 9:
        j3.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][3]
    if e == 0:
        j4.config(image=blank)
    elif e == 1:
        j4.config(image=block)
    elif e == 2:
        j4.config(image=bulb)
    elif e == 3:
        j4.config(image=dreed)
    elif e == 4:
        j4.config(image=frame)
    elif e == 10:
        j4.config(image=blank)
    elif e == 5:
        j4.config(image=ladder)
    elif e == 6:
        j4.config(image=panel)
    elif e == 7:
        j4.config(image=red_rock)
    elif e == 8:
        j4.config(image=signal)
    elif e == 9:
        j4.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][4]
    if e == 0:
        j5.config(image=blank)
    elif e == 1:
        j5.config(image=block)
    elif e == 2:
        j5.config(image=bulb)
    elif e == 3:
        j5.config(image=dreed)
    elif e == 4:
        j5.config(image=frame)
    elif e == 10:
        j5.config(image=blank)
    elif e == 5:
        j5.config(image=ladder)
    elif e == 6:
        j5.config(image=panel)
    elif e == 7:
        j5.config(image=red_rock)
    elif e == 8:
        j5.config(image=signal)
    elif e == 9:
        j5.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][5]
    if e == 0:
        j6.config(image=blank)
    elif e == 1:
        j6.config(image=block)
    elif e == 2:
        j6.config(image=bulb)
    elif e == 3:
        j6.config(image=dreed)
    elif e == 4:
        j6.config(image=frame)
    elif e == 10:
        j6.config(image=blank)
    elif e == 5:
        j6.config(image=ladder)
    elif e == 6:
        j6.config(image=panel)
    elif e == 7:
        j6.config(image=red_rock)
    elif e == 8:
        j6.config(image=signal)
    elif e == 9:
        j6.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][6]
    if e == 0:
        j7.config(image=blank)
    elif e == 1:
        j7.config(image=block)
    elif e == 2:
        j7.config(image=bulb)
    elif e == 3:
        j7.config(image=dreed)
    elif e == 4:
        j7.config(image=frame)
    elif e == 10:
        j7.config(image=blank)
    elif e == 5:
        j7.config(image=ladder)
    elif e == 6:
        j7.config(image=panel)
    elif e == 7:
        j7.config(image=red_rock)
    elif e == 8:
        j7.config(image=signal)
    elif e == 9:
        j7.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][7]
    if e == 0:
        j8.config(image=blank)
    elif e == 1:
        j8.config(image=block)
    elif e == 2:
        j8.config(image=bulb)
    elif e == 3:
        j8.config(image=dreed)
    elif e == 4:
        j8.config(image=frame)
    elif e == 10:
        j8.config(image=blank)
    elif e == 5:
        j8.config(image=ladder)
    elif e == 6:
        j8.config(image=panel)
    elif e == 7:
        j8.config(image=red_rock)
    elif e == 8:
        j8.config(image=signal)
    elif e == 9:
        j8.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][8]
    if e == 0:
        j9.config(image=blank)
    elif e == 1:
        j9.config(image=block)
    elif e == 2:
        j9.config(image=bulb)
    elif e == 3:
        j9.config(image=dreed)
    elif e == 4:
        j9.config(image=frame)
    elif e == 10:
        j9.config(image=blank)
    elif e == 5:
        j9.config(image=ladder)
    elif e == 6:
        j9.config(image=panel)
    elif e == 7:
        j9.config(image=red_rock)
    elif e == 8:
        j9.config(image=signal)
    elif e == 9:
        j9.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][9]
    if e == 0:
        j10.config(image=blank)
    elif e == 1:
        j10.config(image=block)
    elif e == 2:
        j10.config(image=bulb)
    elif e == 3:
        j10.config(image=dreed)
    elif e == 4:
        j10.config(image=frame)
    elif e == 10:
        j10.config(image=blank)
    elif e == 5:
        j10.config(image=ladder)
    elif e == 6:
        j10.config(image=panel)
    elif e == 7:
        j10.config(image=red_rock)
    elif e == 8:
        j10.config(image=signal)
    elif e == 9:
        j10.config(image=water)
    else:
        pass
    ##
    e = seen_world[9][10]
    if e == 0:
        j11.config(image=blank)
    elif e == 1:
        j11.config(image=block)
    elif e == 2:
        j11.config(image=bulb)
    elif e == 3:
        j11.config(image=dreed)
    elif e == 4:
        j11.config(image=frame)
    elif e == 10:
        j11.config(image=blank)
    elif e == 5:
        j11.config(image=ladder)
    elif e == 6:
        j11.config(image=panel)
    elif e == 7:
        j11.config(image=red_rock)
    elif e == 8:
        j11.config(image=signal)
    elif e == 9:
        j11.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][0]
    if e == 0:
        k1.config(image=blank)
    elif e == 1:
        k1.config(image=block)
    elif e == 2:
        k1.config(image=bulb)
    elif e == 3:
        k1.config(image=dreed)
    elif e == 4:
        k1.config(image=frame)
    elif e == 10:
        k1.config(image=blank)
    elif e == 5:
        k1.config(image=ladder)
    elif e == 6:
        k1.config(image=panel)
    elif e == 7:
        k1.config(image=red_rock)
    elif e == 8:
        k1.config(image=signal)
    elif e == 9:
        k1.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][1]
    if e == 0:
        k2.config(image=blank)
    elif e == 1:
        k2.config(image=block)
    elif e == 2:
        k2.config(image=bulb)
    elif e == 3:
        k2.config(image=dreed)
    elif e == 4:
        k2.config(image=frame)
    elif e == 10:
        k2.config(image=blank)
    elif e == 5:
        k2.config(image=ladder)
    elif e == 6:
        k2.config(image=panel)
    elif e == 7:
        k2.config(image=red_rock)
    elif e == 8:
        k2.config(image=signal)
    elif e == 9:
        k2.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][2]
    if e == 0:
        k3.config(image=blank)
    elif e == 1:
        k3.config(image=block)
    elif e == 2:
        k3.config(image=bulb)
    elif e == 3:
        k3.config(image=dreed)
    elif e == 4:
        k3.config(image=frame)
    elif e == 10:
        k3.config(image=blank)
    elif e == 5:
        k3.config(image=ladder)
    elif e == 6:
        k3.config(image=panel)
    elif e == 7:
        k3.config(image=red_rock)
    elif e == 8:
        k3.config(image=signal)
    elif e == 9:
        k3.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][3]
    if e == 0:
        k4.config(image=blank)
    elif e == 1:
        k4.config(image=block)
    elif e == 2:
        k4.config(image=bulb)
    elif e == 3:
        k4.config(image=dreed)
    elif e == 4:
        k4.config(image=frame)
    elif e == 10:
        k4.config(image=blank)
    elif e == 5:
        k4.config(image=ladder)
    elif e == 6:
        k4.config(image=panel)
    elif e == 7:
        k4.config(image=red_rock)
    elif e == 8:
        k4.config(image=signal)
    elif e == 9:
        k4.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][4]
    if e == 0:
        k5.config(image=blank)
    elif e == 1:
        k5.config(image=block)
    elif e == 2:
        k5.config(image=bulb)
    elif e == 3:
        k5.config(image=dreed)
    elif e == 4:
        k5.config(image=frame)
    elif e == 10:
        k5.config(image=blank)
    elif e == 5:
        k5.config(image=ladder)
    elif e == 6:
        k5.config(image=panel)
    elif e == 7:
        k5.config(image=red_rock)
    elif e == 8:
        k5.config(image=signal)
    elif e == 9:
        k5.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][5]
    if e == 0:
        k6.config(image=blank)
    elif e == 1:
        k6.config(image=block)
    elif e == 2:
        k6.config(image=bulb)
    elif e == 3:
        k6.config(image=dreed)
    elif e == 4:
        k6.config(image=frame)
    elif e == 10:
        k6.config(image=blank)
    elif e == 5:
        k6.config(image=ladder)
    elif e == 6:
        k6.config(image=panel)
    elif e == 7:
        k6.config(image=red_rock)
    elif e == 8:
        k6.config(image=signal)
    elif e == 9:
        k6.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][6]
    if e == 0:
        k7.config(image=blank)
    elif e == 1:
        k7.config(image=block)
    elif e == 2:
        k7.config(image=bulb)
    elif e == 3:
        k7.config(image=dreed)
    elif e == 4:
        k7.config(image=frame)
    elif e == 10:
        k7.config(image=blank)
    elif e == 5:
        k7.config(image=ladder)
    elif e == 6:
        k7.config(image=panel)
    elif e == 7:
        k7.config(image=red_rock)
    elif e == 8:
        k7.config(image=signal)
    elif e == 9:
        k7.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][7]
    if e == 0:
        k8.config(image=blank)
    elif e == 1:
        k8.config(image=block)
    elif e == 2:
        k8.config(image=bulb)
    elif e == 3:
        k8.config(image=dreed)
    elif e == 4:
        k8.config(image=frame)
    elif e == 10:
        k8.config(image=blank)
    elif e == 5:
        k8.config(image=ladder)
    elif e == 6:
        k8.config(image=panel)
    elif e == 7:
        k8.config(image=red_rock)
    elif e == 8:
        k8.config(image=signal)
    elif e == 9:
        k8.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][8]
    if e == 0:
        k9.config(image=blank)
    elif e == 1:
        k9.config(image=block)
    elif e == 2:
        k9.config(image=bulb)
    elif e == 3:
        k9.config(image=dreed)
    elif e == 4:
        k9.config(image=frame)
    elif e == 10:
        k9.config(image=blank)
    elif e == 5:
        k9.config(image=ladder)
    elif e == 6:
        k9.config(image=panel)
    elif e == 7:
        k9.config(image=red_rock)
    elif e == 8:
        k9.config(image=signal)
    elif e == 9:
        k9.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][9]
    if e == 0:
        k10.config(image=blank)
    elif e == 1:
        k10.config(image=block)
    elif e == 2:
        k10.config(image=bulb)
    elif e == 3:
        k10.config(image=dreed)
    elif e == 4:
        k10.config(image=frame)
    elif e == 10:
        k10.config(image=blank)
    elif e == 5:
        k10.config(image=ladder)
    elif e == 6:
        k10.config(image=panel)
    elif e == 7:
        k10.config(image=red_rock)
    elif e == 8:
        k10.config(image=signal)
    elif e == 9:
        k10.config(image=water)
    else:
        pass
    ##
    e = seen_world[10][10]
    if e == 0:
        k11.config(image=blank)
    elif e == 1:
        k11.config(image=block)
    elif e == 2:
        k11.config(image=bulb)
    elif e == 3:
        k11.config(image=dreed)
    elif e == 4:
        k11.config(image=frame)
    elif e == 10:
        k11.config(image=blank)
    elif e == 5:
        k11.config(image=ladder)
    elif e == 6:
        k11.config(image=panel)
    elif e == 7:
        k11.config(image=red_rock)
    elif e == 8:
        k11.config(image=signal)
    elif e == 9:
        k11.config(image=water)
    else:
        pass
    global jump
    if not(world[y+1][x] == 0):
        jump = False
    #print("e")
#################################
go_through = [0,5,9,11,8,3]
go_through2 = [0,5,9,11,8,3]
fly = [5,9,11]
moves = 1
def move_timer():
    global moves
    moves = 1
    root.after(200,move_timer)
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
        world[y-1][x] = 10
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
        world[y+1][x] = 10
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
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x-1] in go_through) and (moves == 1):
        world[y][x] = prev_block
        prev_block = world[y][x-1]
        world[y][x-1] = 10
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
        world[y][x-2] = 10
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
        world[y][x+2] = 10
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
    global prev_block
    global moves
    global go_through
    global jump
    y = find_player_y()  
    x = find_player_x(y)
    if (world[y][x+1] in go_through) and (moves == 1):
        world[y][x] = prev_block
        prev_block = world[y][x+1]
        world[y][x+1] = 10
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
        world[y+1][x] = 10
        down(0)
    else:
        pass
    jump = False
    update_world()
def e(e):
    global seen_world
    for i in range(11):
        print(seen_world[i])
###############################
update_world()
root.bind("<KeyRelease-a>",left)
root.bind("<KeyRelease-d>",right)
root.bind("<KeyRelease-w>",up)
root.bind("<KeyRelease-s>",down)
root.bind("<KeyRelease-q>",d_left)
root.bind("<KeyRelease-e>",d_right)
root.bind("<KeyRelease-m>",e)
move_timer()
tkinter.mainloop()
