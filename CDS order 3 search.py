#Cyclic Difference Set #this was way easier to make than the CSS lol
#Sam Nelson 3/10/20
import timeit
start = timeit.default_timer()
size = 4
S = size ** 2 - size + 1
terms = []
diffList = []
CDSList = []
permCheck = []
NumList = list(range(1, S))
start = timeit.default_timer()
for a in range(1, S):
    for b in range(1, S):
        if b == a:
            continue
        for c in range(1, S):
            if c == b or c == a:
                continue
            for d in range(1, S):
                if d == c or d == b or d == a:
                    continue
                del terms[:]
                del diffList[:]
                terms.extend((a, b, c, d))
                if sorted(terms) in permCheck:
                    continue
                for x in terms:
                    for y in terms:
                        if x == y:
                            continue
                        else:
                            if x - y > 0:
                                diffList.append(x - y)
                            else:
                                diffList.append(x - y + S)
                if set(diffList) == set(NumList):
                    if sorted(terms)[0] == 1:
                        CDSList.append(terms)
                        permCheck.append(sorted(terms))
                        #print("The tuple:", sorted(tuple(terms)), "generates a CDS.")
                        print(sorted(tuple(terms)))

stop = timeit.default_timer()
print('Time: ', stop - start)