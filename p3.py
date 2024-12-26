h = int(input("enter a number you want to check"))
if h < 0:
    print("its not thre in grade")
elif h <= 39:
    print("your grade",h,"is in F")
elif h <= 49:
    print("your grade",h,"is in D")
elif h <= 59:
    print("your grade",h,"is in C")

elif h <= 69:
    print("your grade",h,"is in B")

elif h <= 79:
    print("your grade",h,"is in A")

elif h <= 100:
    print("your grade",h,"is in A*")
else:
    print("your grade is not there")
