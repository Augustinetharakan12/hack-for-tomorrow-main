from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
import os
import re
import win32api

tk=Tk()                                  #shortcut to creating a window

def bquit():                             #funtion to to quit 
	quit()

def scan():                              #on click scan funtion 
	print('in scan fn')
	import time
	i=1
	flg=0;
	file_name='myfile'					 #testfile area to add machine learning logic
	rex = re.compile(file_name)
	for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
		progress['value']=i*30
		tk.update_idletasks()
		i=i+1
		if(find_file( drive, rex )):                                       #returns flag value if file exists or not
			flg=1;
			progress['value']=100
			for i in range(1000):
				continue
			fl=tkinter.Label(text="file found",fg="red",bg="black",font="Verdana 15 bold")
			fl.place(x=400,y=290)
			
			
	if(flg==0):	
		print('not found')
		fl=tkinter.Label(text="file not found",fg="red",bg="black",font="Verdana 15 bold")
		fl.place(x=390,y=300)
				

def find_file(root_folder, rex):											#read per drive	
	for root,dirs,files in os.walk(root_folder):
		for f in files:
			if f == 'myfile.txt':
				progress['value']=100
				pt=tkinter.Label(text=str(os.path.join(root,f)),fg="red",bg="black",font="Verdana 10 bold")
				pt.place(x=300,y=315)
				return 1
				
				
                
top = tk 																	#GUI code
top.resizable(width=FALSE,height=FALSE)
top.geometry("900x600")
top.title("CHILD PC SAFE")
progress=Progressbar(orient=HORIZONTAL,length=400,mode='determinate')
frame =tkinter.Frame(top, bg="black", colormap="new")
top.configure(background="black")
B = tkinter.Button(text ="START SCAN",height=5,width=20,command = scan)
cl = tkinter.Button(text ="CLOSE", command = bquit,height=5,width=20)
l=tkinter.Label(text="LETS KEEP OUR CHILDREN SAFE",fg="red",bg="black",font="Verdana 30 bold")
lb=tkinter.Label(text="SCAN YOUR PC TO MAKE IT CHILD FRIENDLY",fg="yellow",bg="black",font="Verdana 20 bold")
l.pack()
lb.place(x=100,y=550)
progress.place(x=250,y=350)
B.place(x=290,y=200)
cl.place(x=460,y=200)
frame.pack()
top.mainloop()