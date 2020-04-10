def addMatrices(a,b):
	'''adds two 2x2 matrices together'''
	mat = []
	for row in range(len(a)):
		r = []
		for col in range(len(a)):
			r.append(a[row][col] + b[row][col])	
		mat.append(r)

	return mat

def multmatrix(a,b):
	#Returns the product of matrix a and matrix b
	m = len(a) #number of rows in first matrix
	n = len(b[0]) #number of columns in second matrix
	newmatrix = []
	for i in range(m):
		row = []
		#for every column in b
		for j in range(n):
			sum1 = 0
			#for every element in the column
			for k in range(len(b)):
				sum1 += a[i][k]*b[k][j]
			row.append(sum1)
		newmatrix.append(row)
	return newmatrix


def multmatrix_2(a,b):
	#Returns the product of matrix a and matrix b
	m = len(a) #number of rows in first matrix
	n = len(b[0]) #number of columns in second matrix
	newmatrix = []
	for r in range(m):
		new_row = []
		for c in range(n):
			sum = 0
			for j in range(len(b)):
				sum += a[r][j] * b[j][c]
			new_row.append(sum)
		newmatrix.append(new_row)

	return newmatrix


def transmute(a):
	for r in range(len(a)):
		for c in range(len(a[r])):
			el = a[r][c] 
			if c != r and  c % 2 == 1:
				a[r][c] = a[c][r]
				a[c][r] = el
				

	return a

def transpose(a):
	rows = len(a)
	columns = len(a[0])
	newmatrix = []
	for c in range(columns):
		row = []
		for r in range(rows):
			row.append(a[r][c])
		newmatrix.append(row)

	return newmatrix

A = [[2,3],[5,-8]]
B = [[1,-4],[8,-6]]

a = [[1,2,-3,-1]]
b = [[4,-1],
[-2,3],
[6,-3],
[1,0]]


print(addMatrices(A,B))
print(transmute(A))
print(multmatrix(a,b))
print(multmatrix_2(a,b))

fmatrix = [[0,0],[1,0],[1,2],[2,2],[2,3],[1,3],[1,4],[3,4],[3,5],[0,5]]
print(transpose(fmatrix))

a = [[1,2,-3,-1]]
print(transpose(a))

b = [[4,-1],
[-2,3],
[6,-3],
[1,0]]
print(transpose(b))