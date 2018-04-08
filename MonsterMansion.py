from Tkinter import *


gui = Tk()
gui.title("Monster Mansion")
gui.geometry("800x600")



#CREATING FRAMES
leftFrame = Frame(gui)
leftFrame.pack(side=LEFT)
textFrame = Frame(gui, bg="lightgray")
textFrame.pack(side=RIGHT, fill=Y)
entryFrame= Frame(gui)
entryFrame.pack(side=BOTTOM, fill=X)

#BUTTONS FOR PLAYING
buttonI = Button(textFrame, text="  Interact(Q)  ", fg="black")
buttonN = Button(textFrame, text="    North(W)   ", fg="black")
buttonT = Button(textFrame, text="    Take(E)    ", fg="black")
buttonW = Button(textFrame, text="    West (A)    ", fg="black")
buttonS = Button(textFrame, text="    South (S)   ", fg="black")
buttonE = Button(textFrame, text="    East (D)    ", fg="black")

buttonI.grid(row=0,column=0)
buttonN.grid(row=0,column=1)
buttonT.grid(row=0,column=2)
buttonW.grid(row=1,column=0)
buttonS.grid(row=1,column=1)
buttonE.grid(row=1,column=2)

#Sets image to left
img=None
image=Label(leftFrame,image = img)
image.pack(side=LEFT, fill=Y)
image.pack_propagate(False)

#Players Input
playerinput=Entry(entryFrame,bg="white")
playerinput.pack(side=BOTTOM,fill=X)

#################################################################################
gui.mainloop()


