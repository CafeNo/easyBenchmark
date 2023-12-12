import cpu_benchmark
import disk_benchmark
import memory_benchmark

def main():

    cpu_score = cpu_benchmark.cpu_benchmark()
    disk_score = disk_benchmark.disk_benchmark()
    memory_score = memory_benchmark.memory_benchmark()

    total_score = cpu_score + disk_score + memory_score
    average_score = total_score / 3

    print("CPU score:", cpu_score)
    print("Disk score:", disk_score)
    print("Memory score:", memory_score)
    print("Total score:", total_score)
    print("Average score:", average_score)

if __name__ == "__main__":
    main()
