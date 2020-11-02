#Cyclic Sum Sets, Actually looking for real CSS now not "Combinatorial Sum Sets"
#Sam Nelson, 2/20/2020. Thanks Bruce and Dr. Haile.
import timeit
start = timeit.default_timer()
size = int(input("What order of a tuple do you want to test? ")) + 1 #Order is one less than the number of terms, thus a one is added so the size variable is based on number of terms.
N = (size - 1) ** 2 + size  # the last term technically should be (size - 1) but after that there is a +1 added so they cancel out.
terms = [] #List to hold the input values for the tuple.
for i in range(size):
    terms.append(int(input("Enter the tuple value #" + str(i + 1) + ": "))) #Manual input of tuple values.
start = timeit.default_timer()
termTuple = tuple(terms)
if sum(terms) != N: #Test to see if the sum of the entered terms is equal to N.
    print("The tuple:", termTuple, "does not generate a CSS.")
else:
    CSS = terms[:] #Adds the original tuple values to the final list.
    lastValue = sum(terms) #Sums all values to add as the last value.
    terms *= 2 #Doubles the list so the list can iterate past the last tuple value.

    slyce = 2 #Variable to save how large the slices are for summing terms; starts as 2 because sums of indivs already added.
    while slyce < size: #While the slices are smaller than the length of the list.
        for ph in range(0, size):
            CSS.append(sum(terms[ph : ph + slyce])) #Adds the sums of the slices of terms.
        slyce += 1
    CSS.append(lastValue) #Adds the last term

    NSet = list(range(1, N + 1)) #What the CSS is compared to.
    if set(CSS) == set(NSet): #If the CSS terms are equal to the NSet than it is a CSS.
        print("The tuple:", termTuple, "generates a CSS.")
    else:
        print("The tuple:", termTuple, "does not generate a CSS.")

stop = timeit.default_timer()
print('Time: ', stop - start)






