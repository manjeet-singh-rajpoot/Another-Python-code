          # smple program of sets#
var={10,20,30}
print(var)

          #add methods #
var2={"a","b","c"}
var2.add("d")
print(var2)

        #heterogeneos in sets#
var3={10,20,30,"a",True,False}
print(var3)

       #union method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.union(set2)
print(set3)

    #intersection method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.intersection(set2)
print(set3)

    #intersection update#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.intersection_update(set2)
print(set3)

   #defference methods#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.difference(set2)
print(set3)

   #clear method #
set1={1,2,3,4}
set1.clear()
print(set3)

  #discard method#
set1={1,2,3,4}
#set1.discard()
print(set3)

  # disjoint method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.isdisjoint(set2)
print(set3)

   #issubset method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.issubset(set2)
print(set3)

  #issuperset method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.issuperset(set2)
print(set3) 

  #symmetric defference method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.symmetric_difference(set2)
print(set3)
  
  #update method#
set1={1,2,3,4}
set2={5,6,7,8}
set3=set1.update(set2)
print(set3)



