#Cyclic Sum Sets Order 6 Search
#Sam Nelson Feb 22, 2020
import timeit
start = timeit.default_timer()
size = 7 #Testing for an order of 6.
reduc = sum(range(1,size)) - 1
terms = [] #Set to hold the input values for the tuple.
CSSList = []
permCheck = []
N = (size - 1) ** 2 + size

for a in range(1, N - reduc):
    print(a)
    for b in range(1, N - reduc):
        if b in {a}:
            continue
        for c in range(1, N - reduc):
            if c in {a, b}:
                continue
            for d in range(1, N - reduc):
                if d in {a, b, c}:
                    continue
                for e in range(1, N - reduc):
                    if e in {a, b, c, d}:
                        continue
                    for f in range(1, N - reduc):
                        if f in {a, b, c, d, e}:
                            continue
                        for g in range(1, N-reduc):
                            if ((a + b + c + d + e + f + g) != N):  #Checks if the sum of the terms equals N.
                                continue
                            if f in {a, b, c, d, e, f}:
                                continue
                            terms.clear()
                            terms.extend((a, b, c, d, e, f, g)) #Adds the values to the tuple to test.
                            if sorted(terms) in permCheck:
                                continue
                            termTuple = tuple(terms)
                            CSS = terms[:]  #Adds the original tuple values to the final list.
                            lastValue = sum(terms)  # Sums all values to add as the last value.
                            terms *= 2  # Doubles the list so the list can iterate past the last tuple value.

                            slyce = 2  # Variable to save how large the slices are for summing terms; starts as 2 because sums of indivs already added.
                            while slyce < size:  # While the slices are smaller than the length of the list.
                                for ph in range(0, size):
                                    CSS.append(sum(terms[ph: ph + slyce]))  # Adds the sums of the slices of terms.
                                slyce += 1
                            CSS.append(lastValue)  # Adds the last term.

                            NSet = list(range(1, N + 1))  # What the CSS is compared to.
                            if set(CSS) == set(NSet):  # If the CSS terms are equal to the NSet than it is a CSS.
                                permCheck.append(sorted(termTuple))
                                CSSList.append(termTuple)
                                print("The tuple:", termTuple, "generates a CSS.")

stop = timeit.default_timer()
print('Time: ', stop - start)
