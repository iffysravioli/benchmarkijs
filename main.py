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
#def float_point():
    #start_time = time.time()
    #value = 1.0 
    #for i in range(10**10):
        #value +- i 
    #for i in range((5*10)**9):
        #value *= i 
    #for i in range((2*10)**9):
        #value /= i 
    #stop_timer2 = time.time()
    #execution_time2 = stop_timer2 - start_time
    #print("The 64-bit Floating Point Opreation benchmark execution time is ", execution_time2)
#float_point()

#Memory 
#def memory():
    #start_time = time()
    #for i in range(10**5):
        #array[i] = i 
        #value = array[i]
        #stop_timer3 = time.time()
        #runtime3 = stop_timer3 - timer3 
        #print("The Memory Benchmark execution time is ", execution_time3)
        
    
#Hard Drive 1 
#def hard_drive():
    #timer4 - time.time()
    #with open("BenchmarkProject.txt", "wb") as f: 
        #for i in range(10**9):
            #f.write(100)
        #with open("BenchmarkProject.txt","rb") as f: 
            #for i in range(10**9):
                #f.read(100)
            #stop_timer4 = time.time()
            #runtime4 = stop_timer4 - timer4 
            #print("The Hard drive #1 benchmark exe")


#Hard Drive 2 
#def hand_drive2():
#   timer
    