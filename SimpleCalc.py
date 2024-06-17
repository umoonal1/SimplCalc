print("Welcome to SimpleCalc V1! ")
Operation = input("What Operation Do you want to do? S,D,A,M,E ")
if Operation.upper() == "E":
    print("E is your selected operation! Make sure to have the numbers in the order of x to the power of x.")
else:
    print(Operation.upper() +" Is your selected operation!")
Number1 = input("What is the first number you want in the problem?")
Number2 = input ("What is the second number you want in the problem?")
if Operation.upper() == "D":
    DivisionType = input("(1 or 2) Do you want division with remainders or Division With decimals?")
    if "2" in DivisionType:
        print(int(Number1) / int(Number2))
    if "1" in DivisionType:
        print(int(Number1) // int(Number2))
        print("With a remainder of")
        print(int(Number1) % int(Number2))
if Operation.upper() == "M":
    print (int(Number1) * int(Number2))
if Operation.upper() == "S":
    print(int(Number1) - int(Number2))
if Operation.upper() == "A":
    print(int(Number1) + int(Number2))
if Operation.upper() == "E":
    print(int(Number1) ** int(Number2))