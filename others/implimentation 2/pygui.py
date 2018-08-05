from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
import os
import re
import win32api
import shutil
import time
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from PIL import ImageFile

tk=Tk()                                  #shortcut to creating a window

def qt():
                              #funtion to quit 
    top.destroy()

def scan():         
    dstroot='img/nsfw' 
                   #on click scan funtion 
    os.makedirs(dstroot)    
    os.makedirs('img/sfw')
    i=1
    flg=0;
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        progress['value']=i*30
        tk.update_idletasks()
        i=i+1
        if(find_file(drive)>0):                                       #returns flag value if file exists or not
                    flg=1;
                    progress['value']=100
                    for i in range(1000):
                        continue
                    fl=tkinter.Label(text="DONE,PLEASE WAIT WHILE WE PROCESS THE DATA",fg="red",bg="black",font="Verdana 15 bold")
                    fl.place(x=150,y=450)

                    

    try:
        if os.path.exists('img/nsfw/truncated.jpg'):
            os.remove('img/nsfw/truncated.jpg')

    except:
        pass
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    test_datagen = ImageDataGenerator(rescale = 1./255)
    classifier = load_model('save_data.h5')
    result_set = test_datagen.flow_from_directory('img',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary',shuffle=False)
    
 
    #Manually delete truncated.jpg

    result = classifier.predict_generator(result_set)
    names = result_set.filenames

    for i in range(len(result)) :

        if result[i] < 0.5 :
            path=str(os.path.abspath("UNSAFE.txt"))   
            unf = open(path,'a')
            unf.write(names[i][5:])
            unf.write('\n')

                
    unf.close()
    fl=tkinter.Label(text="CHECK TEXT FILE NAMED \'UNSAFE.txt\' ",fg="green",bg="black",font="Verdana 15 bold")
    fl.place(x=230,y=90)
    os.startfile('UNSAFE.txt')

    #Fails with read-only files
    # shutil.rmtree('img/nsfw')
 	
			
    if(flg==0):
        print('not found')
        progress['value']=100
        fl=tkinter.Label(text="no images found",fg="red",bg="black",font="Verdana 15 bold")
        fl.place(x=200,y=350)
        				

def find_file(root_folder):
    fla=0											#read per drive	
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            try:
                if f.endswith('.jpg'):
                    fla=fla+1    
                    srcfile =str(os.path.join(root,f))
                    dstroot = 'img/nsfw'
    
                    
                    #assert not os.path.isabs(srcfile)
                    #dstdir =  os.path.join(dstroot)
                    
                    # create all directories, raise an error if it already exists
                    shutil.copy(srcfile, dstroot)
            
                    #pt=tkinter.Label(text=str(os.path.join(root,f)),fg="red",bg="black",font="Verdana 10 bold")
                    #pt.place(x=300,y=315)
            except:
                pass    				
    return fla
				
				
                
top = tk 																	#GUI code
top.resizable(width=False,height=False)
top.geometry("900x600")
top.title("CHILD PC SAFE")
progress=Progressbar(orient=HORIZONTAL,length=400,mode='determinate')
frame =tkinter.Frame(top, bg="black", colormap="new")
top.configure(background="black")
B = tkinter.Button(text ="START SCAN",height=5,width=20,command = scan)
cl = tkinter.Button(text ="CLOSE", command = qt,height=5,width=20)
l=tkinter.Label(text="LETS KEEP OUR CHILDREN SAFE",fg="red",bg="black",font="Verdana 30 bold")
lb=tkinter.Label(text="SCAN YOUR PC TO MAKE IT CHILD FRIENDLY",fg="yellow",bg="black",font="Verdana 20 bold")
l.pack()
lb.place(x=100,y=550)
progress.place(x=250,y=350)
B.place(x=290,y=200)
cl.place(x=460,y=200)
frame.pack()
top.mainloop()