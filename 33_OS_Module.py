                        #1.Getting cwd #
import os
cwd=os.getcwd()
print("1.directory: " ,cwd)

                       #2.changing the cwd#
def curr_path():
    print("Before changing : ",os.getcwd())
curr_path()
os.chdir("../")
curr_path()
                      
                      #3.creating a directory#
print("creating using mkdir(): ")
directory="Raj"
parent="D:/users/Desktop"
path=os.path.join(parent,directory)
os.mkdir(path)
print("directory created 1: %s",directory)
                      
print("creating using makedirs(): ")
directory="Nikhil"
parent="c:/users/desktop/nikhil"
path=os.path.join(parent,directory)
os.makedirs(path)
print("Created directory 2: %s",directory)

                   #4.Listing out files#
path="/"
dir_list=os.listdir(path)
print(path)

                  #5.deleting directory or files#
print("deleting : os.remove()")
file="file1.txt"
Location="D:/users/Desktop/"
path=os.path.join(Location,file)
os.remove(path)
            
                #communly use function : rename(),name(),getsize()
                 