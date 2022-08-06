def ransom_note(magazine,ransom):
    mag = {word:0 for word in set(magazine)}
    for word in magazine:
        mag[word]+=1
    for word in ransom:
        if word not in mag.keys():
            return False
        mag[word]-=1
        if mag[word] < 0:
            return False
    return True


m, n = map(int, raw_input('Int Mag, Int Ran').strip().split(' '))
magazine = raw_input('magazine').strip().split(' ')
ransom = raw_input('ransom').strip().split(' ')

answer = ransom_note(magazine,ransom)
if answer:
    print 'Yes'
else:
    print 'No'

