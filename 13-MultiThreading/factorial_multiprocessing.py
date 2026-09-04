## Real world example
## Multiprocessing for CPU-bound tasks

import multiprocessing

import math
import sys
import time

#Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#Function to compute factorails of a large numbers

def fact_compute(number):
  print(f" Computing factorial of {number}")

  result = math.factorial(number)
  print(f"Factorail of {number} is {result}")
  return result

if __name__=='__main__':
  numbers=[100,200,300]
  start_time = time.time()

  #create a pool of worker processes
  with multiprocessing.Pool() as pool:
    results= pool.map(fact_compute, numbers)

  end_time = time.time()
  print(f"Result: {results}")
  print(f"time taken: {end_time-start_time} seconds")
