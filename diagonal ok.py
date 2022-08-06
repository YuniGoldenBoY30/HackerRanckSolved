def diagonal(a):
    i,sum_diagonal1,sum_diagonal2 = 0,0,0
    while i <=len(a)-1:
        sum_diagonal1 += a[i][i]
        sum_diagonal2 += (a[i][(len(a)-1)-i])
        i+=1
    dif = abs(sum_diagonal1 - sum_diagonal2)
    return dif



n= int(raw_input('Filas y columnas'))
a=[]
for _ in xrange(n):
    a.append(map(int,raw_input('Elementos').rstrip().split()))
print diagonal(a)
