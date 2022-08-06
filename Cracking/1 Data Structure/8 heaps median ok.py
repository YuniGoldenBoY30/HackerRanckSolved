def heaps_median(a):
    a.sort()
    if len(a) == 1:
        return float(a[0])
    elif len(a)%2 == 0:
        return (a[(len(a)/2)-1] + a[len(a)/2])/2.0
    else:
        return float(a[len(a)/2])
        

n = int(raw_input('Cantidad de numeros').strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input('Valor arreglo').strip())
    a.append(a_t)
    print heaps_median(a)



