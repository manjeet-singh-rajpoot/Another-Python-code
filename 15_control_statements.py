 #3.continue statement in while loop #
i=0
a="raj"
while(i<len(a)):
    if(a[i]=="a" or a[i]=="j"):
        i=i+1
        continue
    print("continue : ",a[i])
    i=i+1
    
    #4.break statement in while loop #
    
a="geeksforgeeks"
i=0
while(i<len(a)):
    if(a[i]=="e" or a[i]=="s"):
        i=i+1
        break
    print("break: ",a[i])
    i=i+1
    
    #5.pass statement in python while loop#
a="geeksforgeeks"
i=0
while(i<len(a)):
    i=i+1
    pass
print("pass value of i is ",i)