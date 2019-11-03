# Goal : Find the odd
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

test_list = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

import collections

print(collections.Counter(test_list)) # collections.Counter() will count the number of times

def find_it(seq):
    if len(seq) == 0:
        return None
    times = collections.Counter(seq)
    for odd in times:
        if times[odd] % 2 == 1:
            return odd

def find_it_1(seq):
    for i in seq: # put every number(in the list) into the count() to caculate the appear times
        if seq.count(i)%2!=0: # appear times % 2, so we can know it is an odd or even, in this case: !=0 means odd
            return i

print(find_it(test_list))
print(find_it_1(test_list))