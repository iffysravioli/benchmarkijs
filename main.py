import time 

#32-bit integer operation 
def integer_op():
    start_time = time.time()
    count = 1 
    for i in range(10**10):
        count += i
    for i in range(5*10**9):
        count *= i
    for i in range(2*10**9):
        count /= 1
    end_time = time.time()
    execution_time = end_time - start_time 
    print("The 32-bit Integer operation benchmark execution time: ", execution_time)
integer_op()

#64-bit Floating Point Operation Benchmark
def float_point():
    start_time = time.time()
    value = 1.0 
    for i in range(10**10):
        value +- i 
    for i in range((5*10)**9):
        value *= i 
    for i in range((2*10)**9):
        value /= i 
    stop_timer2 = time.time()
    execution_time2 = stop_timer2 - start_time
    print("The 64-bit Floating Point Opreation benchmark runtime is ", execution_time2)
float_point()