x = 18

h = input("enter your name: ")
f = int(input("enter your age: "))
if x > f:
        print ("you are not allowed as you are",f,"you have to be",x)
elif x < f :
    print("you are eligble")
    z = input("enter your country:")
    if z != "United kingdom":
        print("you cannot cause you are from", z)
    else:
        print("hello ",h,"you can vote now in ",z)

else:
    print("you are not in the database")
