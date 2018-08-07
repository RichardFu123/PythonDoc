import random
import collections
counter=collections.Counter()
for i in range(10000):
    step=str(round(random.betavariate(2,5)*10))
    counter.update(step)

print(counter)

for i in range(10):
    print(str(i),end='')
    value=round(counter[str(i)]/100.)
    for j in range(value):
        print('*',end='')
    print('')
    
