def namerev():
    Fname = input("Enter user first name:")
    Lname = input("Enter user last name:")
    RFname = Fname[::-1]
    print("my name is :", Fname,"",Lname)
    print(" Reversed string is :",RFname,"",Lname[::-1])


def reverse():
    Fstr = ""
    Lstr = ""
    Fname = input("Enter user first name:")
    for i in Fname:
        Fstr = i + Fstr

    Lname = input("Enter user last name:")
    for i in Lname:
        Lstr = i + Lstr
        
    print(" Reversed string is :",Fstr,"",Lstr)


namerev()

reverse()
