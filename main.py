import time 

#32-bit integer operation 
def integer_operation():
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
integer_operation()

#64-bit Floating Point Operation Benchmark
def float_point():
    start_time2 = time.time()
    value = 1.0 
    for i in range(10**10):
        value +- i 
    for i in range((5*10)**9):
        value *= i 
    for i in range((2*10)**9):
        value /= i 
    end_timer2 = time.time()
    execution_time2 = end_timer2 - start_time2
    print("The 64-bit Floating Point Opreation benchmark execution time is ", execution_time2)
float_point()

#Memory 
arrary = ((5*10)**4)
def memory():
    start_time3 = time.time()
    for i in range(10**5):
        arrary[i] = i 
        value = arrary[i]
        end_timer3 = time.time()
        execution_time3 = end_timer3 - start_time3 
        print("The Memory Benchmark execution time is ", execution_time3)
memory()
    
#Hard Drive 1 
def harddrive1():
    start_timer4 = time.time()
    with open("BenchmarkProject.txt", "wb") as f: 
        for i in range(10**9):
            f.write(100)
        with open("BenchmarkProject.txt","rb") as f: 
            for i in range(10**9):
                f.read(100)
            end_timer4 = time.time()
            execution_time4 = end_timer4 - start_timer4 
            print("The Hard drive 1 benchmark runtime is ", execution_time4)
harddrive1()

#Hard Drive 2 
def harddrive2():
    start_timer5 = time.time()
    with open("BenchmarkProject.txt", "wb") as f: 
        for i in range(10**9):
            f.write(100)
        with open("BenchmarkProject.txt","rb") as f: 
            for i in range(10**9):
                f.read(100)
            end_timer5 = time.time()
            execution_time5 = end_timer5 - start_timer5 
            print("The Hard drive 1 benchmark runtime is ", execution_time5)
harddrive2()
