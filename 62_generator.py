                     #1.generator without object#
def gen():
   yield 1
   yield 2
   yield 3

for i in gen():
    print(i)
                   
                     #2.generator using object#
def gen2():
    yield 1
    yield 2
    yield 3

x=gen2()
print(next(x))
print(next(x))
print(next(x))