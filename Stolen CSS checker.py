
import itertools
import timeit
N = int(input("enter order of CSS: "))
start = timeit.default_timer()
n = N* N + N + 1
numTerm = N + 1

#######################################################

def accelAsc(n):  ## For the sake of efficiency the integer partition algorithm, accelAsc was borrowed from Jerome Kelleher http://jeromekelleher.net/partitions.php.
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


####################################################

def filterPart(partSet, k):
    potentCSS = set()
    for part in partSet:
        if (len(part) == k) and (1 in part) and (2 in part):
            potentCSS.add(tuple(sorted(part)))
    return list(potentCSS)


def filterDuplicates(potentCSS):
    filtered = potentCSS[:]
    for part in potentCSS:
        seen = []
        for i in part:
            if i in seen:
                if part in filtered:
                    filtered.remove(part)
            seen.append(i)
    return filtered


def Permutate(filtered):
    permList = []
    for i in filtered:
        permList.append(list(itertools.permutations(i, len(i))))
    return permList


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


def isCSS(L):
    seen = []
    n = len(L)
    for i in range(1, n):
        for start in range(0, n):
            Sum = 0
            for j in range(0, i):
                Sum = Sum + L[(start + j) % n]
            if Sum in seen:
                return False
            seen.append(Sum)
    return True


def CSS(perms):
    cssList = []
    for listPerms in perms:
        for j in listPerms:
            if isCSS(j) == True:
                css = []
                css.append(j)
                css.append(isCSS(j))
                cssList.append(css)
    return cssList

part = accelAsc(n)
potCSS = filterPart(part, numTerm)
filtPotCSS = filterDuplicates(potCSS)
perms = Permutate(filtPotCSS)
css = CSS(perms)

for i in css:
    print(i)
stop = timeit.default_timer()
print('Time: ', stop - start)