#Cyclic Sums
#Sam Nelson 2/11/20
from itertools import combinations
import timeit

#Individual tuple checking
choice = int(input("Do you want to input your own tuple (1), or search for a CombSS [of order 3] (2): "))
if choice == 1: #A choice of 1 means inputting your own tuple.
    size = int(input("What order of a tuple do you want to test? ")) + 1 #Order is one less than the number of terms. For a tuple of three, (A,B,C), order would be 2.
    terms = [] #Set to hold the input values for the tuple.
    for a in range(size):
        terms.append(int(input("Enter the tuple value #" + str(a + 1) + ": "))) #inputting tuple values.

    start = timeit.default_timer()
    N = ((size - 1) * (size - 1)) + size  # the last term technically should be (size - 1) but after that there is a +1 added so they cancel out.
    if sum(terms) != N:
        print("The tuple:", terms, "does not generate a CombSS.") #The tuple values need to add up to N for it to be a CombSS
    else:
        #TermCount = 0  #for debugging
        CombSet = []
        CombLengthList = []
        for i in range(size):
            #TermCount += 1  # TermCount = the number of values in the individual comb tuples.
            comb = tuple(combinations(terms, i + 1))
            CombSet.append(comb)                      #len(comb) = the number of tuples of the specified TermCount.
            CombLengthList.append(len(comb))          #CombLengthList stores the lengths of each list of tuples for future use.
            #print(TermCount, len(comb), comb, CombSet[i])

        CombSet2 = []
        for x in range(size): #Selects a tuple from the CombSet.
            #print(CombSet[x])
            for y in range(CombLengthList[x]): #Selects a tuple from that tuple.
                #print(CombSet[x][y])
                for z in range(x + 1): #Selects the integer from that tuple.
                    CombSet2.append(CombSet[x][y][z])
                    #print(CombSet[x][y][z])

        ph = 0 #place-holder
        count = 1
        AddSet = []
        for n in CombLengthList:
            #print(CombSet2[ph:ph + count * n])
            AddSet.append(CombSet2[ph:ph + count * n]) #Creates a list of lists of ints, each value being the terms indiviudally in order.
            ph = ph + count * n
            count += 1

        DoneSet = AddSet[0] #Adds the original tuple values to the final set.
        for g in range(size - 1):
            for h in range(len(AddSet[g + 1])):
                if (h % (g + 2)) == 0: #When g=1 two consecutive values need to be added, this checks to make sure numbers are not repeat added to create different terms.
                    DoneSet.append(sum(AddSet[g + 1][h:h + g + 2])) #Sums slices of lists together to produce the finished values.
                    #print(DoneSet)
        print(set(DoneSet)) #shows all values in DoneSet in order without duplicates.
        for w in range(len(DoneSet)): #Prints all final values in their original order, not nuerical order.
            print(DoneSet[w])

        NSet = list(range(1, N + 1))
        #print(NSet)
        factor = True

        for x in NSet:
            if x not in DoneSet:
                print("The tuple:", terms, "does not generate a CombSS.") #DoneSet does not include all the values of NSet.
                factor = False
                break
        if factor:
            print("The tuple:", terms, "generates a CombSS.") #DoneSet does include all the values of NSet.
#====================================================================================================================================================================================
#Order 3 Search
if choice == 2: #A choice of 2 means searching for CombSS.
    start = timeit.default_timer()
    terms = [1, 2]  #Set to hold the input values for the tuple.
    CombSSList = [] #Set of all found CombSS
    RepCombSSList = []
    NoRepCombSSList = [] #Set of all found CombSS with no duplicate values
    tracking_counter = 0 #For comparing total number of CombSS to number checked, all combinations that fit criteria and add up to N

    size = 4 #testing for an order of 3
    num = 0
    N = ((size - 1) * (size - 1)) + size  # the last term technically should be (size - 1) but after that there is a +1 added so they cancel out.
    max = N // 2 + 2  # The highest possible tuple value is no greater than N/2 + 1.5
    for v in range(1, max): #Will look into effective ranges later
        C = v
        for w in range(1, max):
            if ((v + w) != (N - 3)): #If all the terms besides 1 & 2 does not equal N minus 3 it cannot be a CombSS.
                continue
            # print(tracking_counter) #To check if it is running.
            CombSet = [] #resetting set
            CombLengthList = []
            del terms[2:]
            D = w
            terms.extend((C, D))
            tracking_counter += 1
            for i in range(size):
                comb = tuple(combinations(terms, i + 1))
                #print(TermCount, len(list(comb)), list(comb))  #TermCount = the number of values in the individual comb tuples.
                CombSet.append(comb)  # len(list(comb)) = the number of tuples of the specified TermCount.
                CombLengthList.append(len(comb))  # list(comb) = the list of the tuples in comb
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
                AddSet.append(CombSet2[ph:ph + count * n])  # Creates a list of lists of strings of values, each value being the terms indiviudally in order.
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
            NSet = list(range(1, N + 1)) #The NSet equals the list of all positive integers from 1 to N.
            if set(DoneSet) == set(NSet): #If the DoneSet of all the added terms includes the NSet then it can be added to a final list.
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
                    print(SortedTerms) #shows the CombSS
                    if (SortedTerms in CombSSList) & (SortedTerms not in RepCombSSList):
                        NoRepCombSSList.append(SortedTerms)
                        #print(SortedTerms)

    print("There are", len(CombSSList), "CombSS of order 3.\nThere are", len(NoRepCombSSList), "NoRepCombSS of order 3.")
stop = timeit.default_timer()
print('Time: ', stop - start)