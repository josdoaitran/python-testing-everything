# if
# Write a program to input 2 number and the operation. Then check with the result from user with corect result


first_no = input("Please input first number: ")
oper = input("Please input the operation: ")
second_no = input("Please input second number: ")

first_no = int(first_no)
second_no = int(second_no)

if (oper == "+"):
    result_no = first_no + second_no
else:
    if (oper == "-"):
        result_no = first_no - second_no
    else:
        if (oper == "*"):
            result_no = first_no * second_no
        else:
            if (oper == "/"):
                result_no = first_no / second_no

print(result_no)