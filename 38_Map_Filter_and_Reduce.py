       #1.Map() function in python #
from functools import reduce
def cube(x):
    return x*x*x

List=[1,2,3,5]
result=list(map(cube,List))

print("map: ",result)

    #2.Filter function in python#

def filt(a):
    return a>2

List1=[3,1,4,0,5]
newl=list(filter(filt,List1))
print("filter : ",newl)

  #3.reduce function in python #
def mysum(x,y):
    return x+y

List2=[2,3,4,5]
newl2=reduce(mysum,List2)

print("reduce:",newl2)