import os , os.path
drive_name=input("Enter your drive_name : ")
Folder_name=input("Enter your Folder_name : ")
# b=os.listdir(drive_name + ":\\"+ Folder_name) 
b=(drive_name + ":\\"+ Folder_name) 
g = input("Enter your file_name : ")  
p=[]
for path, subdirs, files in os.walk(b):
    for name in files:
        p.append (os.path.join(path, name))
# print(p)    
for i in p:
    # print(i.rsplit('\\',1)[-1])
    if(i.rsplit('\\',1)[-1]==g):
        print("matched")
        z=os.path.getsize(i) 
        print(i + "-" + str(z)+ " bytes")
    # else:
    #     print("file name is incorrect")

    