import random

# This code is used to pick a number at random in the range from 1 to 30
number = random.randrange(1, 30)
print(number)

# This code is used to pick multiple numbers at random in the range from 1 to 30
randomlist2 = [random.randrange(1, 30) for _ in range(3)]
print(randomlist2)

# Sort the numbers from smallest to biggest
randomlist2.sort()
print(randomlist2)

# Sort the numbers from biggest to smallest
randomlist2.sort(reverse=True)
print(randomlist2)

# This code uses the random.sample function to pick 5 unique random numbers in the range from 1 to 30
randomlist3 = random.sample(range(1, 30), 5)
print(randomlist3)