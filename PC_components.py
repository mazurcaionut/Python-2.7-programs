from Tkinter import *


f=Tk()
f.title("Monitor")
f.geometry("1500x1000")


plansa = Canvas(f,width=1500,height=1000)
plansa.grid()

def plecare(event):
    print "Punct initial [ " + str(event.x) + " , " +str(event.y) + "]"
    global x,y
    x = event.x
    y = event.y


def final(event):
    print "Punct final [ " + str(event.x) + " , " +str(event.y) + "]"
    global x1,y1
    x1 = event.x
    y1 = event.y
    plansa.create_rectangle(x,y,x1,y1,fill="black",width=1)

plansa.bind('<Button-1>',plecare)
plansa.bind('<ButtonRelease-1>',final)
#MONITOR
plansa.create_rectangle(300,440,600,450,fill="gray")
plansa.create_rectangle(450,440,460,400,fill="black")
plansa.create_rectangle(300,390,600,400,fill="gray")
plansa.create_rectangle(300,400,310,140,fill="gray")
plansa.create_rectangle(600,400,590,140,fill="gray")
plansa.create_rectangle(310,140,590,150,fill="gray")
plansa.create_rectangle(310,150,590,390,fill="black")
plansa.create_rectangle(440,393,471,397,fill="gray",width=1)
plansa.create_rectangle(409,393,440,397,fill="gray",width=1)
plansa.create_rectangle(472,393,502,397,fill="gray",width=1)
plansa.create_rectangle(455,395,455,395,fill="black",width=1)
plansa.create_text(450,250,text="Acesta este un monitor",fill="lightblue")

#UNITATE
plansa.create_rectangle(743,195,1261,583,fill="gray",activefill="white",width=1)
plansa.create_text(1000,185,fill="blue",text="UNITATEA CENTRALA")
plansa.create_rectangle(1128,483,1262,583,fill="gray",activefill="white")
plansa.create_oval(1130,484,1260,580,fill="gray",activefill="white")
plansa.create_line(1194,483,1195,580,fill="black",width=5)
plansa.create_line(1131,536,1260,534,fill="black",width=5)
plansa.create_line(1149,501,1240,569,fill="black",width=5)
plansa.create_line(1152,569,1240,497,fill="black",width=5)
plansa.create_text(1190,475,fill="blue",text="VENTILATOR")
plansa.create_rectangle(744,247,1125,581,fill="gray",activefill="white")
plansa.create_rectangle(1126,246,1260,462,fill="gray",activefill="white")
plansa.create_text(1000,235,fill="blue",text="PLACA DE BAZA")
plansa.create_rectangle(1135,283,1145,386,fill="gray",activefill="white")
plansa.create_rectangle(1150,283,1160,386,fill="gray",activefill="white")
plansa.create_rectangle(1165,283,1175,386,fill="gray",activefill="white")
plansa.create_rectangle(1180,283,1190,386,fill="gray",activefill="white")
plansa.create_text(1140,325,fill="blue",text="1")
plansa.create_text(1155,325,fill="blue",text="2")
plansa.create_text(1170,325,fill="blue",text="3")
plansa.create_text(1185,325,fill="blue",text="4")
plansa.create_text(1220,325,fill="blue",text="RAM")
plansa.create_rectangle(745,249,929,410,fill="gray",activefill="white")
plansa.create_rectangle(929,411,1124,579,fill="gray",activefill="white")
plansa.create_rectangle(745,411,930,580,fill="gray",activefill="white")
plansa.create_text(830,340,fill="blue",text="PLACA VIDEO")
plansa.create_text(1020,340,fill="blue",text="PLACA DE SUNET")
plansa.create_text(835,500,fill="blue",text="PLACA DE RETEA")
plansa.create_text(1020,500,fill="blue",text="CPU")


#CABLUL DINTRE UNITATE SI MONITOR
plansa.create_rectangle(742,243,601,243)



#MOUSE
plansa.create_oval(194,532,248,595,fill="blue")
plansa.create_oval(218,532,226,561,fill="black")
plansa.create_rectangle(194,560,249,562,fill="black")
plansa.create_rectangle(742,527,734,533,fill="black")

f.mainloop()
