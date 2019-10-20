from Tkinter import *

e = "Enuntul este aici.Scrie raspunsul:"
rc = "raspunsul corect"

fereastra = Tk()
fereastra.title("Intrebare")
fereastra.geometry("300x100")

cadru = Frame(fereastra)
cadru.grid()

enunt = Label(cadru,text=e)
enunt.grid()

raspuns=Entry(cadru)
raspuns.grid()

def handler_buton():
    if raspuns.get() == rc:
        rezultatLbl["text"] = "Bravo!"
    else:
        rezultatLbl["text"] = "Ai gresit."

verificare = Button(cadru,text = "Verifica",command= handler_buton)
verificare.grid()

rezultatLbl= Label(cadru)
rezultatLbl.grid()

fereastra.mainloop()
