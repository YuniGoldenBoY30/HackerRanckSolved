def burbleSort(a):
    cont = 0
    for numPasada in range(len(a)-1,0,-1):
        for i in range(numPasada):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                cont +=1

    print 'Array is sorted in '+ str(cont)+ ' swaps'
    print 'FirstElement: '+ str(a[0])
    print 'LastElement: '+ str(a[-1])


n = int(raw_input('Cantidad de numeros').strip())
a = map(int, raw_input(' arreglo').strip().split(' '))
burbleSort(a)
