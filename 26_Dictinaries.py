          #1.simple program #
dict={
       1:"raj",
       2:"singh",
       3:"rajpoot"
     }
print(dict)

         #2.different way to create dictionary#
dict={}
print(dict)

        #3.Nested dictionary#
Dict={
      1:"Geeks",
      2:"For",
      3:{"a":"Welcome",
         "b":"To",
         "c":"Raj"}
     }
print(Dict)

     #4.Adding the element into the dictionary #
Dict[0]="manjeet"
Dict[1]="singh"
Dict[2]="Rajpoot"
print("After adding 3 element into dictionary: ",Dict)

     #5.Accessing Element from Dictionary#
dict={
       1:"raj",
       2:"singh",
       3:"rajpoot"
     }
print("Accessing elemtn:",dict[2])
print(dict.get(2))
       
    #6.Nested dictionary#
dict={
    "dict1":{1:"geeks"},
    "dict2":{"name":"Shivam"}
}
print("Nested dictionary : ",dict["dict1"])
print("Nested dictionary : ",dict["dict1"][1])
print("Nested dictionary : ",dict["dict2"]["name"])

     #7.delete dictionary #
Dict={
        "name":"raj",
        "sirname":"singh"
     }
del(Dict)

print("delete")

    #8.clear method #
Dict={
        "name":"raj",
        "sirname":"singh"
     }
Dict.clear()
print("After clear() : ",Dict)

         #9.clear method #
Dict={
        "name":"raj",
        "sirname":"singh"
     }
Dict.copy()
print("After copy() : ",Dict)

       #10.clear method #
Dict={
        "name":"raj",
        "sirname":"singh"
     }
Dict.pop()
print("After pop() : ",Dict)
   

       