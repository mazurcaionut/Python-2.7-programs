from Tkinter import *

fereastra = Tk()
fereastra.title("Calculator")
fereastra.geometry("150x225")

cadru = Frame(fereastra)
cadru.grid()

raspuns= Entry(cadru,bd=8)
raspuns.grid(row=0,column=0)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "1")
buton.grid(row=1,column=1)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "2")
buton.grid(row=1,column=2)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "3")
buton.grid(row=1,column=3)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "4")
buton.grid(row=1,column=4)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "5")
buton.grid(row=2,column=1)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "6")
buton.grid(row=2,column=2)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "7")
buton.grid(row=2,column=3)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "8")
buton.grid(row=2,column=4)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "9")
buton.grid(row=3,column=1)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "+")
buton.grid(row=3,column=2)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "-")
buton.grid(row=3,column=3)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "*")
buton.grid(row=3,column=4)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "/")
buton.grid(row=4,column=1)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = ".")
buton.grid(row=4,column=2)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "C")
buton.grid(row=4,column=3)

buton = Button(cadru,padx = 6,pady = 8,bd = 8,text = "=")
buton.grid(row=4,column=4)

fereastra.mainloop()
