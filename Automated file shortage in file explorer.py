#Automatic file transfer - File Location "D:\resume\python_practice"
import os, shutil
path = r"C:/Users/venka/OneDrive/Desktop/python_practice/"
file_name=os.listdir(path)
# print(file_name)
folder_name=["Image_file","Wrod_doc","PDF_Doc","Vedio_files"]
#folder_creation
for a in folder_name:
    if not os.path.exists(path + a):
        os.mkdir(path + a)
#file_moving
for b in file_name:
    if ".jpg" in b and not os.path.exists(path+"/Image_file/"+b):
        shutil.move(path+b,path+"/Image_file")
        print(f"{b} Moved to Image_file")
    elif ".doc" in b and not os.path.exists(path+"/Wrod_doc/"+b):
        shutil.move(path+b,path+"/Wrod_doc")
        print(f"{b} Moved to Wrod_doc")
    elif ".pdf" in b and not os.path.exists(path+"/PDF_Doc/"+b):
        shutil.move(path+b,path+"/PDF_Doc")
        print(f"{b} Moved to PDF_Doc")
    elif ".mp4" in b and not os.path.exists(path+"/Vedio_files/"+b):
        shutil.move(path+b,path+"/Vedio_files")
        print(f"{b} Moved to Vedio_files")
    else:
        print(f"{b} is an invalid file formate")