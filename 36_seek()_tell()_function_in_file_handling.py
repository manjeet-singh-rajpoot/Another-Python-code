                  #1. seek() function in file handling #
with open("file.txt","r") as f:
    #print(type(f))
    f.seek(10)
    
    data=f.read(5)
    print(data)
    
                  #2.tell() function in file handling#
with open("file.txt","r") as f:
    #print(type(f))
    f.seek(10)
    
    print(f.tell())
    data=f.read(5)
    print(data)
    
                 #3.truncate()  function in python#
with open("sample.txt","w") as f1:
    f1.write("Hello")
    f1.truncate(3)

with open("sample.txt","r") as f:
    data=f.read()
    print(data)