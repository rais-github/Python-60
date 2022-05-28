C,R=[int(x) for x in input("Enter rows and column:").split(" ")]
mat = [[int(input()) for x in range (C)] for y in range(R)]
for i in range(R):
    for j in range(C):
        if(i==j):
            print(mat[i][j],end=" ")
        