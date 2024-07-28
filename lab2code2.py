pip install numpy
import numpy as np
R = int(input("Enter the number of rows for matrix 1:"))
C = int(input("Enter the number of columns for matrix 1:"))

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

x = int(input("Enter the number of rows for matrix 2:"))
y = int(input("Enter the number of columns for matrix 2:"))

matrix2 = []
print("Enter the entries rowwise:")


for i in range(x):		 
	for j in range(y):	
		a.append(int(input()))
	matrix.append(a)


for i in range(x):
	for j in range(y):
		print(matrix[i][j], end = " ")
	print()
if R=x & C=y:
    print("multiplication is possible")
      c=np.multiply(matrix,matrix[])
        print("The product is: ",c)
else:
    print("error the input matrices cannot be multiplied")



