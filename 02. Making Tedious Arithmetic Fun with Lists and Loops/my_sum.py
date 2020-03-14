def my_sum(value):
    running_sum = 0
    for i in range(1,value + 1):
        running_sum += i

    return running_sum

print(my_sum(10))
print(my_sum(100))
print(my_sum(1000))
