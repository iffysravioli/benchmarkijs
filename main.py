#32-bit integer operation 
#import time
#timer
#start_time = time.time()
#result = 0
#for i in range(1010):
    #result += i
#for i in range(5*10**9):
    #result *= i
#for i in range(2*10**9):
    #result /= i 
#stop timer
#end_time = time.time()
#calculating & printing the execution time 
#execution_time = end_time - start_time
#print("Integer operation benchmark execution time:", execution_time)

#64-bit Floating Point Operation Benchmark
import time 
start_time = time.time()

result = 1.0 
for i in range(1010):
    result += i
for i in range(5*10**9):
    result *= i 
for i in range(2*10**9):
    result /= i 

#to stop the timer 
end_time = time.time()

#calculate & print its exection time 
execution_time = end_time - start_time
print("64-floating point operation benchmark execution time:", execution_time)