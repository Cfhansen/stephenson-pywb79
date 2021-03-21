###solution to exercise 79 from ben stephenson's "the python workbook".

import random

num = random.randint(1,100)
print(num)
updates = 1

for n in range(1,100):
  new_num = random.randint(1,100)
  if new_num > num:
    updates += 1
    num = new_num
    print(f'{new_num} <-- Update')
  else:
    print(new_num)

print(f'The biggest number was {num}, with {updates} updates.')
