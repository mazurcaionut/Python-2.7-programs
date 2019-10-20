from Tkinter import *

fereastra = Tk()
fereastra.title("Logare")
fereastra.geometry("175x175")

cadru = Frame(fereastra)
cadru.grid()

userLbl = Label(cadru,text = "User:")
userLbl.grid()

userTxt = Entry(cadru)
userTxt.grid()

parolaLbl = Label(cadru,text ="Parola:")
parolaLbl.grid()

parolaTxt= Entry(cadru,show = '*')
parolaTxt.grid()

def logare():
    if userTxt.get() == "elev" and parolaTxt.get() == "destept":
        cadru["bg"] = "blue"
    else:
        cadru["bg"] = "red"

logareBtn = Button(cadru,text = "Login", command = logare)
logareBtn.grid()

fereastra.mainloop()
