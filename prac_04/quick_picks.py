import random
min=1
max=45
numbers_line=6

quick_choice=int(input("How many quick picks?"))
while quick_choice<=0:
    print("Error!!!")
    quick_choice = int(input("How many quick picks?"))

if quick_choice>0:
    for i in range(quick_choice):
        quick_choice=[]
        for choice in range(numbers_line):
            numbers=random.randint(min,max)
            while numbers in quick_choice:
                numbers=random.randint(min,max)
            quick_choice.append(numbers)
        quick_choice.sort()
        print(" ".join("{:2}".format(numbers) for numbers in quick_choice))
