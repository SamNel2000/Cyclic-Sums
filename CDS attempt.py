f=\
truthy=[
[10,12,17,18,21],
[7,5,4],
[57,1,5,7,17,35,38,49],
[1,24,35,38,40,53,86,108,114,118,135,144,185,210,254,266,273],
[16,3,19,4,8,10,15,5,6],
[8,23,11,12,15,2,3,5,7,17,1],
[7,7,7]
]
falsy=[
[1,2,3,4,20],
[57,3,5,7,17,35,38,49],
[3,4,5,9],
]

lambda x:len({*map([(b-a)%max(x)for a in x for b in x].count,range(1,max(x)))})<2

print('truthy',tuple(map(f,truthy)))
print('falsy',tuple(map(f,falsy)))