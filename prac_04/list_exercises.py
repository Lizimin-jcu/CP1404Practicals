number_list=[]
for i in range(5):
    number= int(input("Number:"))
    number_list.append(number)

print("The first number is", number_list[0])
print("The last number is", number_list[4])
print("The smallest number is",min(number_list))
print("The largest number is",max(number_list))
print("The average of the numbers is:",sum(number_list)/len(number_list))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user=input("Enter your name:")
if user in usernames:
    print("Access granted")
else:
    print("Access denied")