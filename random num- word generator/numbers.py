import random

#This code is used to pick a number in a range we pick and at random in the range of number we pick
number = random.random()
randomlist = []
for i in range (1):
    number = random.randrange(1, 30) #if you add a number after it takes the first number plus that number
    randomlist.append(number)
print(number)


#This code is used to pick multiple numbers in a range we pick and at random in the range of number we pick
randomlist2 = []
for i in range (0,5):
    numbers = random.randrange(1, 30)
    randomlist2.append(numbers)
print(randomlist2)


#This code is the same as the one above but more compact
randomlist3 = random.sample(range(1, 30), 5)
print(randomlist3)


#This line of code uses the sort() funtion and takes the number and sort them from smallest to biggest
randomlist2.sort()

print(randomlist2)


#This line of code uses the sort() funtion and takes the number and sort them from biggest to smallest
randomlist2.reverse()

print(randomlist2)


