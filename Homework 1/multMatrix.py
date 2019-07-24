################
# Author: Daniel Burger
# Date: 2/24/2019
# This program multiplies two matrices and prints
# results in matrix format
# THIS PROGRAM IS INCORRECT, I DO NOT KNOW HOW TO MULTIPLY MATRICES
#################

M = [[2, -5, 8, 11],[3, 7, -9, -5], [4, 0, -1, 7]] #matrix
Mt = [[2, 3, 4], [-5, 7, 0], [8, -9, -1], [11, -5, 7]] #transposed matrix

product = []  #where the answer will be stored, in matrix format

for i in range(len(M)): #for every number of rows in M
    for j in range(len(Mt[0])): #for every number of cols in Mt
        temp_row = []  #temporary row array to fill values and eventually append
        for k in range(len(Mt)):
            x = M[i][k]*Mt[k][j]  #calculation done for matrix multiplication
            temp_row.append(x)
    product.append(temp_row)  #adding the product row to matrix 'product'

#prints the matrix in an easy to read format
for r in range(len(product)):
    for c in range(len(product[0])):
        print(str(product[r][c]) + '\t',end='')
    print()

