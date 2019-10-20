from Tkinter import *

dy = 1
t=200

f= Tk()
f.title("ROBOT")

plansa = Canvas(f,height = 590,width = 845)
plansa.grid()

#picioarele robotului
plansa.create_line(325,400,275,500,fill="Blue")
plansa.create_line(375,400,325,500,fill="Blue")
plansa.create_line(275,500,325,591,fill="Blue")
plansa.create_line(325,500,375,591,fill="Blue")
plansa.create_line(425,400,475,591,fill="Blue")
plansa.create_line(475,400,525,591,fill="Blue")
plansa.create_line(325,400,475,400,fill="Blue")

#trunchiul robotului
plansa.create_line(325,400,325,225,fill="Blue")
plansa.create_line(475,400,475,225,fill="Blue")
plansa.create_line(325,175,375,175,fill="Blue")
plansa.create_line(425,175,475,175,fill="Blue")

#mainile robotului
plansa.create_line(325,175,225,300,fill="Blue")
plansa.create_line(325,225,225,350,fill="Blue")
plansa.create_line(225,300,200,250,fill="Blue")
plansa.create_line(225,350,170,265,fill="Blue")
plansa.create_line(170,265,200,250,fill="Blue")
plansa.create_line(170,265,165,225,fill="Blue")
plansa.create_line(200,250,165,225,fill="Blue")
plansa.create_line(475,175,575,300,fill="Blue")
plansa.create_line(475,225,575,350,fill="Blue")
plansa.create_line(200,250,165,225,fill="Blue")
plansa.create_line(200,250,165,225,fill="Blue")
plansa.create_line(575,300,600,250,fill="Blue")
plansa.create_line(575,350,630,260,fill="Blue")
plansa.create_line(600,250,630,260,fill="Blue")
plansa.create_line(600,250,630,225,fill="Blue")
plansa.create_line(630,260,630,225,fill="Blue")

#gatul robotului
plansa.create_line(375,175,375,125,fill="Blue")
plansa.create_line(425,175,425,125,fill="Blue")

#capul robotului
plansa.create_line(365,125,435,125,fill="Blue")
plansa.create_line(365,125,350,50,fill="Blue")
plansa.create_line(435,125,450,50,fill="Blue")
plansa.create_line(350,50,365,0,fill="Blue")
plansa.create_line(365,0,375,35,fill="Blue")
plansa.create_line(375,35,400,25,fill="Blue")
plansa.create_line(400,25,425,35,fill="Blue")
plansa.create_line(425,35,435,0,fill="Blue")
plansa.create_line(435,0,450,50,fill="Blue")
plansa.create_line(370,60,375,80,fill="Blue")
plansa.create_line(375,80,395,70,fill="Blue")
plansa.create_line(395,70,395,65,fill="Blue")
plansa.create_line(370,60,395,65,fill="Blue")
plansa.create_line(365,125,350,50,fill="Blue")
plansa.create_line(405,65,405,70,fill="Blue")
plansa.create_line(405,65,430,60,fill="Blue")
plansa.create_line(430,60,425,80,fill="Blue")
plansa.create_line(425,80,405,70,fill="Blue")
plansa.create_line(355,80,400,85,fill="Blue")
plansa.create_line(400,85,445,80,fill="Blue")
plansa.create_line(400,85,400,125,fill="Blue")
plansa.create_line(395,70,395,85,fill="Blue")
plansa.create_line(405,65,405,85,fill="Blue")



def desen():
    plansa.create_oval(150,205,170,230,fill="black",tag = "cerc")
    plansa.create_oval(625,205,645,230,fill="black",tag = "cerc")

def sus():
    plansa.move("cerc",0,-dy)
    plansa.after(t,sus)
def jos():
    plansa.move("cerc",0,dy)
    plansa.after(t,jos)

def apas(tasta):
    if tasta.keysym == "Up" :
        sus()
    elif tasta.keysym == "Down" :
        jos()

f.bind('<Key>',apas)


desen()
f.mainloop()

