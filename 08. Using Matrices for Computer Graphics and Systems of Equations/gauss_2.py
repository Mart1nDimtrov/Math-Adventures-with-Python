def gauss(A):
	'''Converts a matrix into the identity
	matrix by Gaussian elimination, with
	the last column containing the solutions
	for the variables'''
	m = len(A)
	n = len(A[0])
	for i,row in enumerate(A):
		# divide each row to get the identity value for the row
		div = row[i]
		for c in range(n):
			row[c] = row[c] / div
			print(row[c])

		for r in range(m):
			if r != i:
				add_inv = -A[r][i] # i always goes a little bit further
				for prev in range(n):
					A[r][prev] += add_inv * A[i][prev] 

	return A

#test:
B = [[2,1,-1,8],
[-3,-1,2,-1],
[-2,1,2,-3]]
print(gauss(B))