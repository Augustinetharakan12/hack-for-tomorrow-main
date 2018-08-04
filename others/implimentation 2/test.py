from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
tk=Tk()
progress=Progressbar(tk,orient=HORIZONTAL,length=400,mode='determinate')
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("CHILD SAFETY AWAITS")

       

        self.fr=tkinter.Frame(width=768, height=576, bg="black", colormap="new")
        self.fr.pack()



       

def bar(self):
    import time
    for i in range(100):
        progress['value']=i
        tk.update_idletasks()
        time.sleep(.1)
    quit()
def qt():
    quit()    

root = tk
#my_gui = MyFirstGUI(root)
root.resizable(width=FALSE,height=FALSE)
root.geometry("900x600")
fr=Frame(root)
l = Label(text="Search Your Child's PC")
l.pack()

scan_b = Button( text="scan", command=bar)
scan_b.place(x=200,y=250)

close_button = Button(text="Close", command=quit)
close_button.place(x=420,y=250)
root.mainloop()