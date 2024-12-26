E = int(input("Enter a number to chck divisble"))
print(E)

if E %3== 0 :
    print("Fizz")
    if E %5 == 0:
        print("Buzz")
    elif E %5 ==0  and E %3 ==0:
        print ("Fizz Buzz")
elif E %5 == 0:
        print("Buzz")
else:
    print("it is not divisble",E)
