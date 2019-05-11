# While Looping: while the statement is True, the code inside the block will be executed.
# So, this code will print the number from 1 to 10
num = 1

while num <= 10:
    print(num)
    num += 1

loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False
