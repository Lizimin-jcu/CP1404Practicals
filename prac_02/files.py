out_file=open("name.txt","w")
name=input("Enter the name:")
print(name,file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

in_file=open("numbers.txt","r")
number=int(in_file.readline())
number_two=int(in_file.readline())
in_file.close()
print(number)
print(number_two)
print(number+number_two)

in_file = open("numbers.txt", "r")
total = 0
for num in in_file:
    number = int(num)
    total += number
in_file.close()
print(total)
