import shutil 
 
source = "path/main.py"
destination ="path/main2.py"
 
# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 
 
# Print path of newly 
# created file 
print("Destination path:", dest) 