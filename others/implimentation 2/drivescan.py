import os
import re
import win32api


def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            if f == 'myfile.txt':
                print("file found")
                print(os.path.join(root,f))
                exit() # if you want to find only one
                
def find_file_in_all_drives(file_name):
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )
        


find_file_in_all_drives('myfile')