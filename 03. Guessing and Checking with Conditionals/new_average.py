def average(num):
	sum = 0
	for i in range(1,num+1):
		sum += i

	return sum/num

def average_2(num):
	return (num/2)+((num/2)/num)

print(average(7))
print(average_2(7))