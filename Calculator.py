operations = {"+": [], "-": [], "*": [], "/": []}
while(1):
    a = float(input())
    b = float(input())
    c = 1
    oper = input()
    if(oper == "+"):
        c = a + b
    elif(oper == "-"):
        c = a - b
    elif(oper == "*"):
        c = a * b
    elif(oper == "/"):
        if(b == 0):
            c = None
        else:
            c = a / b
    else:
        print("Неправильный оператор")
        continue
    operations[oper] = operations[oper] + [f"{a} {oper} {b} = {c}"]
    print(f"{a} {oper} {b} = {c}")
    print(operations)
    for i in operations.keys():
        print(i, operations[i])