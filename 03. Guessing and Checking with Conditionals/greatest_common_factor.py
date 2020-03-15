def greater(num1,num2):
	if num1 >= num2:
		return num1
	else:
		return num2

def gcf(num1,num2):
	'''find the gcf of two numbers'''
	greater_num = greater(num1,num2)
	gcf_num = 0

	for i in range(1,greater_num+1):
		if num1 % i == 0 and num2 % i == 0:
			gcf_num = i

	return gcf_num

print(gcf(150,138))