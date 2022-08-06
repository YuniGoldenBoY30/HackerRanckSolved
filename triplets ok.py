def triplets(a0,a1,a2,b0,b1,b2):
    c_alice = 0
    c_bob= 0
    if a0 > b0:
        c_alice+=1
    elif a0==b0:
        c_alice+=0
        c_bob+=0
    else:
        c_bob+=1
    if a1 > b1:
        c_alice+=1
    elif a1==b1:
        c_alice+=0
        c_bob+=0
    else:
        c_bob+=1
    if a2 > b2:
        c_alice+=1
    elif a2==b2:
        c_alice+=0
        c_bob+=0
    else:
        c_bob+=1
    print str(c_alice) + ' ' + str(c_bob)

a0A1A2 =raw_input('alice').split()
a0= int(a0A1A2[0])
a1= int(a0A1A2[1])
a2= int(a0A1A2[2])

b0B1B2 =raw_input('bob').split()
b0= int(b0B1B2[0])
b1= int(b0B1B2[1])
b2= int(b0B1B2[2])

triplets(a0,a1,a2,b0,b1,b2)
