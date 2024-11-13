          #1.concatention method #
Tuple1=(1,2,3,4)
Tuple2=(10,20,30,40)
print(Tuple1+Tuple2)

         #2.Nesting method #
Tuple3=(1,2,3,4)
Tuple4=(10,20,30,40)
tuple5=(Tuple3+Tuple4)
print(tuple5)

        #3.Repeatation method #
tuple6=("Python")*3
print(tuple6)

       #4.Slicing method in tuple#
tuple7=(0,1,2,3)
print(tuple7[1:])
print(tuple7[:: -1])
print(tuple7[2:7])

        #5.delete method in tuple#
tuple8=(0,1,2,3)
#del tuple8
print(tuple8)

         #6.Length in tuple#
tuple9=("raj","Singh")
print(tuple9)

        #7.multiple datatype in tuple#
Tuple3=("immutable",True,"Gekks")
print(Tuple3)

       #8.convert List to tuple#
List=[1,2,3,4]
print(tuple(List))

       #9.Tuple in Loop#
tup=("Geeks")
n=5
for i in range(int(n)):
    tup=(tup,)
    print(tup)
