def is_matched(expression):
    print expression
    if len(expression) % 2 != 0:
        print False
    else:
        abierto = ("(", "[", "{")
        cerrado = (")", "]", "}")
        mapa = {abierto[0]:cerrado[0],
                abierto[1]:cerrado[1],
                abierto[2]:cerrado[2]}
        array = []

        for obj in expression:
            if obj in abierto:
                array.append(mapa[obj])
                bandera = 'YES'

            elif obj in cerrado:
                if not array:
                    return False
                elif array[-1] == obj:
                    array.pop()
                else:
                    return False    
        return True
    

t = int(raw_input().strip())
for a0 in xrange(t):
    expression=raw_input().strip()
    if is_matched(expression) == True:
        print 'Yes'
    else:
        print 'No'

