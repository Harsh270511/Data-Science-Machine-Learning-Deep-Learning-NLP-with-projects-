import multiprocessing

import time

def square_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"sqaure: {i*i}")

def cube_numbers():
  for i in range(5):
    time.sleep(1.5)
    print(f"Cube: {i*i*i}")


if __name__=='__main__':
  #Creating 2 processes

  p1= multiprocessing.Process(target=square_numbers)
  p2= multiprocessing.Process(target=cube_numbers)

  t= time.time()
  #Start the process
  p1.start()
  p2.start()

  #wait for process to complete
  p1.join()
  p2.join()
  finised_time= time.time()-t
  print(finised_time)
