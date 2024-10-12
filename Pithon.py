import math
import time
enum = int(input("Start generator at what number?"))
runtime = int(input("How many digits to generate?"))
i = 1
while i < runtime:
  print(math.pi*10**(enum-1))
  enum = enum + 1
  i = i + 1
  time.sleep(0.1)
