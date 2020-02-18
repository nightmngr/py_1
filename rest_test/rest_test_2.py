# py 3.8.1
# py rest test v.2.0

# requests
import requests
import sys

# multiprocessing
import multiprocessing
import time

# url
url = ''

username = ''
password = ''

# test connection
def test_connection(url, username, password): #, timeout = 10):
    try:
        _ = requests.get(url, auth=(username, password), verify=False) #, timeout=timeout)
        print(time.perf_counter())
        return True
    except requests.exceptions.RequestException as e:
        print(e)
        return False
        sys.exit(1)


# test call - ok
# test_connection(url, username, password)

# multiprocessing
if __name__ == '__main__':

    t1 = time.perf_counter()

    users = range(200)
    processes = []

# this works ok """
    for user in users:
        p = multiprocessing.Process(target=test_connection, args=(url, username, password))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    t2 = time.perf_counter()

    print(f"total time: {t2-t1}")


"""
# map() function
p = multiprocessing.Process(target=test_connection, args=(url, username, password))
result = map(p, users)
print(result)
results = set(result)
print(results)
"""