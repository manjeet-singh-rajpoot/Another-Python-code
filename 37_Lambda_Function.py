def double(x):
    return x*x

def five(fx,value):
    return 6+fx(value)

triple=lambda x: x*x*x
fourth=lambda x,y:x*y
avg=lambda x,y,z :(x+y+z)/3

print(double(5))
print(triple(3))
print(fourth(2,3))
print(avg(2,2,2))
print(five(lambda x:x*x,2))
