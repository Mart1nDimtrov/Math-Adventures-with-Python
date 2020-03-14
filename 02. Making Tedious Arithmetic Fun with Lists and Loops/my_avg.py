def my_avg(numbers):
    return sum(numbers)/len(numbers)

numbers = [x for x in range(1,11)]
numbers_2 = [8,11,15]
d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]

print(my_avg(numbers))
print(my_avg(numbers_2))
print(my_avg(d))
