import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 1?
#It prints the number between 5-20

# What was the smallest number you could have seen, what was the largest?
#The smallest one is 5,the largest 20.

# What did you see on line 2?
#3,5,7,9

# What was the smallest number you could have seen, what was the largest?
#The smallest one is 3,the largest 9.

# Could line 2 have produced a 4?
#can not.

# What did you see on line 3?
#the decimal between 2.5-5.5

# What was the smallest number you could have seen, what was the largest?
#The smallest one is 2.5,the largest 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(0, 101))