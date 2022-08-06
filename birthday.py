def birthday(n,ar):
    i = 0
    c = 0
    ar.sort()
    long=len(ar)
    while i <=n-1:
        if ar[long-1] == ar[i]:
            c+=1
            i+=1
        else:
            i+=1
    print c

    

n=int(raw_input('elemento'))
ar=map(long,raw_input('ar').rstrip().split())
birthday(n,ar)
 
