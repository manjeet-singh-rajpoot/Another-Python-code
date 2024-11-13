#                     #1.shutil.copy()#
# import shutil
# import os
 
# source = "raj.py"
# destination ="main.py"
 
# # Copy the content of 
# # source to destination 
# dest = shutil.copy(source, destination) 
 
# # Print path of newly 
# # created file 
# print("Destination path:", dest) 

#                 #2.shutil.copy2()#
# source = "raj.py"
# destination ="main.py"
 
# # Copy the content of 
# # source to destination 
# dest = shutil.copy2(source, destination) 
 
# # Print path of newly 
# # created file 
# print("Destination path:", dest) 

#              #3.shutil.copytree() #
             
# source = "raj.py"
# destination ="main.py"
 
# # Copy the content of 
# # source to destination 
# dest = shutil.copytree(source, destination) 
 
# # Print path of newly 
# # created file 
# print("Destination path:", dest) 

#           #4.shutil.rmtree()#
              
# source = "raj.py"
# destination ="main.py"
 
# path=os.path.join(source,destination)
# # Copy the content of 
# # source to destination 
# shutil.rmtree(path) 

#           #5.shutil.move()#
            
# source = "raj.py"
# destination ="main.py"
 
# # Copy the content of 
# # source to destination 
# dest = shutil.move(source, destination) 
 
# # Print path of newly 
# # created file 
# print("Destination path:", dest) 
    
#        #6.shutil.which() #
       
# # file search  
# cmd = 'anaconda'
   
# # Using shutil.which() method 
# locate = shutil.which(cmd) 
   
# # Print result 
# print(locate)
