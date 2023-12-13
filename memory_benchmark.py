import time
import random

NUMBER = 200000000

def memory_benchmark():

    startTime = time.time()

    for i in range(NUMBER):
        list_letter = []
        letter = str(chr(random.randint(65,90)))
        list_letter.append(letter)
        

    stopTime = time.time()
    scoresTime = (1 / (stopTime - startTime)) * 10000
    print("Memory completed")
    
    return scoresTime

if __name__ == "__main__":

    scores_memory = memory_benchmark()
    print(f'Memory Benchmark scores: {scores_memory}s.')

