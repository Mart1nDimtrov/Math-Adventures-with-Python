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


A = [[2,3],[5,-8]]
B = [[1,-4],[8,-6]]

print(addMatrices(A,B))
