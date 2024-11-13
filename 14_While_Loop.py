          #1.simple program of while loop#
count=0
while(count<3):
    count=count+1
    print("simple : ",count)
    
       #2.infinite program of while loop#
age=28
while(age>19):
    print("infinite",age)
    break
    
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

    #6. while loop with else statement#
i=0
while(i<4):
    i=i+1
    print("else statement : ",i)
else:
    print("no break")

i=0
while(i<4):
    i=i+1
    print(i)
    break
else:
    print("break")
    
     #7.while loop with boolean #
print("boolean stetements are: ")
count=0
while True:
    count=count+1
    print(f"count is {count}")
    
    if(count==10):
        break
    
    #8.while loop with list#
    a=[1,2,3,4]
    
    while a:
        print("a given list elements are: ",a.pop())