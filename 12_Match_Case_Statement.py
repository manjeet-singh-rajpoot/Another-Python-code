        # 1. single match condition #
def manmatch():
    num=int(input("Enter num 1 to 3 : "))
    match num:
        case 1:
            print("one")
        case 2:
            print("two")
        case 3:
            print("three")
        case _:
            print("sorry")  
        
        #2.match condition with OR operator #

def manmatch2():
    num2=int(input("Enter num 1 to 6: "))
    match (num2):
        case 1|2:
            print("1 or two ")
        case 3|4:
            print("three or four ")
        case 5|6:
            print("five or six ")
        case _:
            print("sorry")
        
        #3. match with if condition #
def manmatch3():
    num3=int(input("Enter number for pos and neg: "))
    match (num3):
        case num3 if(num3>0):
            print("positive")
        case num3 if(num3<0):
            print("negative")
        case _:
            print("sorry")

        #4.match condition with sequence pattern #
def manmatch4():
    mystr="Hello World"
    match (mystr[6]):
        case "w":
            print("case 1 matches ")
        case "W":
            print("case 2 matches ")
        case _:
            print("sorry")

manmatch()
manmatch2()
manmatch3()
manmatch4()
    