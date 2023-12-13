import time
import math

def cpu_benchmark():
    start_time = time.time()
    
    result = 0
    for i in range(10**9):
        result += math.sqrt(i)

    
    end_time = time.time()
    elapsed_time = ( 1 / (end_time - start_time)) * 10000
    print("CPU completed")
    
    return elapsed_time

if __name__ == "__main__":
    elapsed_time = cpu_benchmark()
    print(f"Benchmark time: {elapsed_time} second elapsed")



