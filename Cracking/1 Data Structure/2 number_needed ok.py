def number_needed(a,b):
    list_a = list(a)
    list_b = list(b)
    i = 0
    number = 0
    while i < len(list_a):
        if list_b.count(list_a[i]) >= 2 or list_b.count(list_a[i]) == 1:
            list_b[list_b.index(list_a[i])]= None
            list_a[i]=None
        i+=1
    j=0
    while j < len(list_b):
        if list_a.count(list_b[j]) >= 2 or list_a.count(list_b[j]) == 1:
            list_a[list_a.index(list_b[j])]= None
            list_b[j]=None
        j+=1
    lista = list_a + list_b
    for obj in lista:
        if obj != None:
            number+=1



    print list_a
    print list_b
    return number
                
        

    ### hacer lo mismo para la segunda cadena!!!
a = raw_input('A ').strip()
b = raw_input('B ').strip()

print number_needed(a,b)
