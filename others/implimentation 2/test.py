from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
class MyFirstGUI:
    #tk=Tk()
   # progress=Progressbar(tk,orient=HORIZONTAL,length=400,mode='determinate')
    def __init__(self, master):
        self.master = master
        master.title("Search Your Child's PC")

        self.label = Label(master, text="CHILD SAFETY AWAITS")
        self.label.pack()

        self.scan_b = Button(master, text="scan", command=self.bar)
        self.scan_b.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def bar(self):
        import time
        for i in range(100):
            progress['value']=i
            tk.update_idletasks()
            time.sleep(.1)
        quit()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()