import time
import os
import tempfile

def disk_benchmark():
    start_time = time.time()

    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)

    # Write data to the temporary file
    with open(temp_file.name, "wb") as f:
        f.seek(0)
        while f.tell() < 100**100:
            f.write(b'a')
            # Check if the elapsed time is more than 60 seconds
            if time.time() - start_time > 60:
                break

    # Close the temporary file
    temp_file.close()

    # Calculate the score based on the amount of data written
    score_raw = os.path.getsize(temp_file.name) / (1024 * 1024) * 100
    score = score_raw / 100
    print("Disk completed")

    # Remove the temporary file
    os.unlink(temp_file.name)
    return score

if __name__ == "__main__":
    score = disk_benchmark()

    print(f"Disk Benchmark score: {round(score)}")