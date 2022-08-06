def array_left_rotation(a,n,k):
    array=[]
    z = len(a)-k
    i = 0
    while k < len(a):
        array.append(a.pop(k))
    while i < len(a) :
        array.append(a[i])
        i+=1
    return array

n, k = map(int, raw_input('').strip().split(' '))
a = map(int, raw_input('').strip().split(' '))

print array_left_rotation(a,n,k)
