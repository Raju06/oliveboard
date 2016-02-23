import itertools

iterables = [ ['A','B','C','D','E','F','G','H'], ['history','chemistry','english','biology','hindi','physics','geography','math'] ]

for t in itertools.product(*iterables)
    print t