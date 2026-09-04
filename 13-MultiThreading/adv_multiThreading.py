## Multithreading with Thread Pool executor

from concurrent.futures import ThreadPoolExecutor

import time

def print_number(number):
  time.sleep(1)
  return f"Number: {number}"

numbers= [1,2,3,4,5,6,6,7,8,9,12,1,1,11]

with ThreadPoolExecutor(max_workers=3) as excutor:
  results = excutor.map(print_number, numbers)

for result in results:
  print(result)