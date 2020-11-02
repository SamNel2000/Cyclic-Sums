#Order 3 Search
#2/18/20
from itertools import combinations
import timeit
start = timeit.default_timer()
size = 4 #testing for an order of 3
terms = [1, 2]  #Set to hold the input values for the tuple.
C = 0
D = 0
N = ((size - 1) * (size - 1)) + size

stop = timeit.default_timer()
print('Time: ', stop - start)