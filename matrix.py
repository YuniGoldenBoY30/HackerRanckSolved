def matrixR(matrix):
    matrixTemp = []
    columna = len(matrix)
    fila = len(matrix[0])
    i =0
    j = 0
    while i <=fila:
        for obj in matrix[i+1]:
            matrixTemp.append(obj)
            i+=1
    print matrixTemp



m,n,r = raw_input('m,n,r').strip().split(' ')
m,n,r= [int(m),int(n),int(r)]
matrix = []

for matrix_i in xrange(m):
    matrix_temp = map(int, raw_input().strip().split(' '))
    matrix.append(matrix_temp)


matrixR(matrix)
    
