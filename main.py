#32-bit integer operation 
import time
#timer
start_time = time.time()
result = 0
for i in range(1010):
    result += i
for i in range(5*10**9):
    result *= i
    