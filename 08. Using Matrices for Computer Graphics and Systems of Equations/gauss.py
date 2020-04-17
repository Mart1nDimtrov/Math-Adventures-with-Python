def gauss(A):
	'''Converts a matrix into the identity
	matrix by Gaussian elimination, with
	the last column containing the solutions
	for the variables'''
	m = len(A)
	n = len(A[0])
	for j,row in enumerate(A):
		#diagonal term to be 1
		#by dividing row by diagonal term
		if row[j] != 0: #diagonal entry can't be zero
			divisor = row[j]
			for i, term in enumerate(row):
				row[i] = term / divisor
			print(row)
		#add the other rows to the additive inverse
		#for every row
		for i in range(m):
			if i != j: #don't do it to row j
				#calculate the additive inverse
				addinv = -1*A[i][j]
				#for every term in the ith row
				for ind in range(n):
					#add the corresponding term in the jth row
					#multiplied by the additive inverse
					#to the term in the ith row
					print(i,ind,j)
					print(A[i])
					A[i][ind] += addinv*A[j][ind]
					print(A[i][ind],addinv,A[j][ind])

	return A

#example:
B = [[2,1,-1,8],
[-3,-1,2,-1],
[-2,1,2,-3]]
print(gauss(B))

D = [[2,-1,5,1,-3],[3,2,2,-6,-32],[1,3,3,-1,-47],[5,-2,-3,3,49]]
print(gauss(D))

#check result
print((2*2)-(-12)+(5*-4)+1)


