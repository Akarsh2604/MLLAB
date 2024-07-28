

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")


for i in range(R):		 
	for j in range(C):	
		a.append(int(input()))
	matrix.append(a)


for i in range(R):
	for j in range(C):
		print(matrix[i][j], end = " ")
	print()

x=transpose_matrix(matrix[])
print("The transposed matrix is",x)

def transpose_matrix(matrix[i][j]):
    result=[
            [0,0,0]
            [0,0,0]
            [0,0,0]]
    for i in range(len(matrix)):
        for j in range(len x[0]):
            result[j][i]= matrix[i][j]

   
