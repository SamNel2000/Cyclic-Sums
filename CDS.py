#Cyclic Difference Set #this was way easier to make than the CSS lol
#Sam Nelson 3/10/20
import timeit
start = timeit.default_timer()
size = int(input("What size of a tuple do you want to test? "))
S = size ** 2 - size + 1
terms = []
for i in range(size):
    terms.append(int(input("Enter the tuple value #" + str(i + 1) + ": ")))
start = timeit.default_timer()
diffList = []

for x in terms:
    for y in terms:
        if x == y:
            continue
        else:
            if x - y > 0:
                diffList.append(x - y)
            else:
                diffList.append(x - y + S)

NumList = list(range(1, S))
if set(diffList) == set(NumList):
    if sorted(terms)[0] == 1:
        print("This is a Cyclic Difference Set in Normal Form", sorted(terms))
    else:
        print("This is a Cyclic Difference Set not in Normal Form", sorted(terms))
else:
    print("This is not a Cyclic Difference Set")

stop = timeit.default_timer()
print('Time: ', stop - start)