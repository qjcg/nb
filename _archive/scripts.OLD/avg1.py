#!/usr/bin/env python3

def median(intlist):
    intlist.sort()
    # odd list length
    if len(intlist) % 2:
        med = intlist[len(intlist) // 2]
    # even list length
    else:
        low_mid = intlist[len(intlist) // 2 - 1]
        high_mid = intlist[len(intlist) // 2]
        med = (low_mid + high_mid) / 2
    return med

numbers = []
while True:
    num = input('enter a number or Enter to finish: ')
    if not num:
        break
    numbers.append(int(num))

print('numbers: {}'.format(numbers))
print('count = {:d} sum = {:d} lowest = {:d} highest = {:d} mean = {:f} '
      'median = {:f}'.format(
      len(numbers), sum(numbers), min(numbers),
      max(numbers),sum(numbers)/len(numbers), median(numbers) )
)
