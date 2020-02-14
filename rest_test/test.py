import time
import concurrent.futures
from multiprocessing import Process
from multiprocessing import Pool
import os

_MAX_ITERATIONS = 10

def print_test(number):
    time.sleep(10)
    return number

def mp(numbers):
    iteration = 0
    while True:
        if iteration > _MAX_ITERATIONS:
            break

        t1 = time.perf_counter()
        p = Pool(2)
        result = p.map(print_test, numbers)

        p.close()
        p.join()

        t2 = time.perf_counter()
        print(f"Time it took is: {t2-t1} second(s).")
        iteration += 1

if __name__ == '__main__':
    numbers = range(10)
    mp(numbers)


"""
for i in range(os.cpu_count()):
    print("registring process %d" % i)
    processes.append(Process(target=print_test))

for process in processes:
    process.start
    print(process.result)

for process in processes:
    process.join

"""
"""
with concurrent.futures.ProcessPoolExecutor() as executor:
    users = [1, 2]
    res = executor.map(print_test, users)

    for result in res:
        print(result)
"""
"""
def process_print():
    print("err")

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_print, users) 
"""

t2 = time.perf_counter()

print(f"Finished in {round(t2-t1, 2)}")