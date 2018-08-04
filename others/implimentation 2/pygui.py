from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
tk=Tk()
def bar():
    import time
    for i in range(100):
    	progress['value']=i
    	tk.update_idletasks()
    	time.sleep(.1)
    quit()
def bquit():
	quit()

top = tk
progress=Progressbar(orient=HORIZONTAL,length=400,mode='determinate')
frame =tkinter.Frame(width=768, height=576, bg="black", colormap="new")
B = tkinter.Button(text ="START SCAN", command = bar,height=5,width=20)
cl = tkinter.Button(text ="CLOSE", command = bquit,height=5,width=20)
progress.pack()
B.place(x=250,y=250)
cl.place(x=400,y=250)
frame.pack()
top.mainloop()