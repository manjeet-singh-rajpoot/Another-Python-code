         #1.Simple for loop#
str="geeks"
for i in str:
    print(str)
 
       #2.for loops with range #
for  i in range(0,9,2):
    print(i)    
    
     #3.for loops with enumerate#
l1=["eat","sleep","repeat"]
for count,ele in enumerate(l1):
    print(count,ele)

   #4.for loops nested #
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
    
    #5.for loop in one line #
num=[x for x in range(11)]
print(num)

   #6.for loops with tuple #
t=((1,2),(3,4),(5,6))

for a,b in t:
    print(a,b)
    
    #7.for loop with Zip() #
fruits=["apple","banana","mango"]
color=["red","yellow","blue"]
for fruits,color in zip(fruits,color):
    print(fruits,"is",color)
    
     #8.for loops with continues statement#
for letter in "geeksforgeeks":
    if(letter=="e" or letter=="s"):
        continue
    print(letter)
    
    #9.for loops with break statement#
for letter in "geeksforgeeks":
    if(letter=="e" or letter=="s"):
       break
    print(letter)
    
    #10.for loops with else statement #

for i in range(1,4):
    print(i)
else:
    print("no break")
    
    #11.for loop in pass statement #
for letter in "geeksforgeeks":
    pass
print(letter)

    