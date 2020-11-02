#Cyclic Sum Sets Order 5 Search
#Sam Nelson 2/17/20
from itertools import combinations
import timeit
start = timeit.default_timer()
terms = [1, 2]  #Set to hold the input values for the tuple.
TermCount = 0 #for debugging
CombSSList = [] #Set of all found CombSS
RepCombSSList = []
NoRepCombSSList = []  # Set of all found CombSS with no duplicate values
tracking_counter = 0  # For comparing total number of CombSS to number checked, all combinations that fit criteria and add up to N

size = 6 #testing for an order of 5
num = 0
N = ((size - 1) * (size - 1)) + size  # the last term technically should be (size - 1) but after that there is a +1 added so they cancel out.
max = N // 2 + 2 #The highest possible tuple value is no greater than N/2 + 1.5
for t in range(1, max):  #Will look into effective ranges later
    C = t
    for u in range(1, max):
        D = u
        for v in range(1, max):
            E = v
            for w in range(1, max):
                if ((t + u + v + w) != (N - 3)): #If all the terms besides 1 & 2 does not equal N minus 3 it cannot be a CombSS.
                    continue
                # print(tracking_counter) #To check if it is running.
                CombSet = [] #resetting set
                CombLengthList = []
                del terms[2:]
                F = w
                terms.extend((C, D, E, F))
                tracking_counter += 1
                #print(terms)
                for i in range(size):
                    #TermCount += 1
                    comb = tuple(combinations(terms, i + 1))
                    # print(TermCount, len(list(comb)), list(comb))  #TermCount = the number of values in the individual comb tuples.
                    CombSet.append(comb)  # len(list(comb)) = the number of tuples of the specified TermCount.
                    CombLengthList.append(len(list(comb)))  # list(comb) = the list of the tuples in comb
                    # CombLengthList stores the lengths of each list of tuples for future use.

                CombSet2 = []
                for x in range(size):  # Selects a tuple from the CombSet.
                    # print(CombSet[x])
                    for y in range(CombLengthList[x]):  # Selects a tuple from that tuple.
                        # print(CombSet[x][y])
                        for z in range(x + 1):  # Selects the integer from that tuple.
                            CombSet2.append(CombSet[x][y][z])
                            # print(CombSet[x][y][z])

                ph = 0  # place-holder
                count = 1
                AddSet = []
                for n in CombLengthList:
                    # print(CombSet2[ph:ph + count * n])
                    AddSet.append(CombSet2[
                                  ph:ph + count * n])  # Creates a list of lists of strings of values, each value being the terms indiviudally in order.
                    ph = ph + count * n
                    count += 1

                DoneSet = AddSet[0]  # Adds the original tuple values to the final set.
                for g in range(size - 1):
                    for h in range(len(AddSet[g + 1])):
                        if (h % (
                                g + 2)) == 0:  # When g=1 two consecutive values need to be added, this checks to make sure numbers are not repeat added to create different terms.
                            DoneSet.append(sum(AddSet[g + 1][
                                               h:h + g + 2]))  # Sums slices of lists together to produce the finished values.
                            # print(DoneSet)

                #for w in range(len(DoneSet)): #Shows all final values in their original order, not nuerical order.
                    #print(DoneSet[w])

                # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                NSet = list(range(1, N + 1))
                if set(DoneSet) == set(NSet):
                    dup = set()
                    # print("The tuple:", terms, "generates a CombSS.")  # DoneSet does include all the values of NSet.
                    SortedTerms = sorted(terms)  # Sorts the terms before adding them to a list.
                    if SortedTerms not in CombSSList:  # Checks if the tuple is already within the list, this is because multiple permuations of the same values.
                        CombSSList.append(
                            SortedTerms)  # Adds CombSS to a list if there are no repeat values within the tuple.
                        for num in terms:
                            if num in dup:
                                RepCombSSList.append(
                                    SortedTerms)  # Adds CombSS to a list with other Repeating value CombSS.
                            dup.add(num)
                        # print(SortedTerms) #shows the CombSS
                        if (SortedTerms in CombSSList) & (SortedTerms not in RepCombSSList):
                            NoRepCombSSList.append(SortedTerms)
                            print(SortedTerms)

print("There are", len(CombSSList), "CombSS of order 5.\nThere are", len(NoRepCombSSList), "NoRepCombSS of order 5.")
stop = timeit.default_timer()
print('Time: ', stop - start)