import random
from collections import Counter
obj_list = ['a', 'b', 'c', 'd']

counter = Counter()
for _ in range(100):
        mum_list = random.choice(obj_list)
        counter[mum_list] += 1
        print(counter)