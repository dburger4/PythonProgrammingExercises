################
# Author: Daniel Burger
# Date: 2/24/2019
# This program transposes matrix M and prints it
# in its proper transposed order 
#################

M = [[2, -5, 8, 11],[3, 7, -9, -5], [4, 0, -1, 7]] #starting matrix

Mt = [] #transpose of M

for i in range(len(M[0])): #for every column
    column = [] #create a new column from M that will b a row in Mt
    for j in range(len(M)): #for every row
        x = M[j][i]  #pulls value from M
        column.append(x) #appends value to column string
    Mt.append(column)  #appends column as a row
        
#prints the matrix in an easy to read format
for r in range(len(Mt)):
    for c in range(len(Mt[0])):
        print(str(Mt[r][c]) + '\t',end='')
    print()
