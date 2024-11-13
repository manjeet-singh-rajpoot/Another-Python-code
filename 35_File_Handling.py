                        #1.read in file handling #       
f=open("myfile.txt","r")
read=f.read()
print(read)
f.close()

                       #2.create or write a file#
f1=open("myfile2.txt","w")
#read2=f.read()
#print(read2)
#f1.close()
                   
                     #3.only write in file #
f=open("myfile2.txt","w")
write=f.write("Hello world")
print(write)
#f.close()

                  #4.append using with keyword a file #
with open("myfile2.txt","a"):
    f.write("hii i am manjeet...")
    
                 #5.append method#
f=open("myfile.txt","a")
f.write("Hi manjeet")
f.close()
                 #6.readlin() and writeline() function #
f=["geeks\n","for\n","geeks\n"]
file1=open("myfile.txt","w")
file1.writelines(f)
file1.close()

file1=open("myfile.txt","r")
line1=file1.readlines()

count=0

for line in line1:
    cont=count+1
    print("Line{}:{}".format(count,line.strip()))