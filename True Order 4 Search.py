#Cyclic Sum Sets Order 4 Search
#Sam Nelson Feb 22, 2020
import timeit
start = timeit.default_timer()
size = 5 #Testing for an order of 4.
reduc = sum(range(1,size)) - 1
terms = [] #Set to hold the input values for the tuple.
CSSList = []
permCheck = []
N = (size - 1) ** 2 + size

for a in range(1, N - reduc):
    for b in range(1, N - reduc):
        for c in range(1, N - reduc):
            for d in range(1, N - reduc):
                for e in range(1, N - reduc):
                    if ((a + b + c + d + e) != N):  #Checks if the sum of the terms equals N.
                        continue
                    del terms[:]
                    terms.extend((a, b, c, d, e)) #Adds the values to the tuple to test.
                    if len(set(terms)) != size:
                        continue
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
                    CSS.append(lastValue)  # Adds the last term

                    NSet = list(range(1, N + 1))  # What the CSS is compared to.
                    if set(CSS) == set(NSet):  # If the CSS terms are equal to the NSet than it is a CSS.
                        permCheck.append(sorted(termTuple))
                        CSSList.append(termTuple)
                        print("The tuple:", termTuple, "generates a CSS.")

stop = timeit.default_timer()
print('Time: ', stop - start)
