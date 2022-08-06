from collections import Counter

def ransom_note(magazine, ransom):
    ran = Counter(ransom)
    if not ran:
        return True  # handle edge case
    for m in magazine:
        if m in ran:
            # we need this word
            if ran[m] > 1:
                ran[m] -= 1
                # still need more of that one
            else:
                # the last usage of this word
                ran.pop(m)
                if len(ran) == 0:
                    # we found the last word of our ransom
                    return True
    return False

m, n = map(int, raw_input('Longitud cadena UNO Y DOS').strip().split(' '))
magazine = raw_input('MAGAZINE ').strip().split(' ')
ransom = raw_input('RANSOM ').strip().split(' ')
answer = ransom_note(magazine,ransom)
if answer:
    print 'YES'
else:
    print 'NO'







