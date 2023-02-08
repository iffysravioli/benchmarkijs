#32-bit integer operation 
import time
#timer
start_time = time.time()
result = 0
for i in range(1010):
    result = 0 
for i in range(5*10**9):
    result *=i 
for i in range(2*10**9):
    result /= i 

