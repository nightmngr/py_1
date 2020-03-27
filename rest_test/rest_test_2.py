# py 3.8.1
# py rest test v.2.0

# requests
import requests
import sys

# multiprocessing
import multiprocessing
import time

# url
url = 'https://handhelds.api.qa.lto.direct/ords/dl_a_letas/hhd/v1/getIRMVChecklist?limit=2000'

username = '869092030733866'
password = 'RGVTF000054869092030733866869092030733874'

# test connection
def test_connection(url, username, password): #, timeout = 10):
    try:
        r = requests.get(url, auth=(username, password), verify=False) #, timeout=timeout)
        print(time.perf_counter())
        # print(r.headers)
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

    users = range(600)
    processes = []

# this works ok """
    for i in range(1):
        for user in users:
            p = multiprocessing.Process(target=test_connection, args=(url, username, password))
            p.start()
            processes.append(p)

        for process in processes:
            process.join()

        t2 = time.perf_counter()

        print(f"cycle #{i} total time: {t2-t1}")


"""
# map() function
p = multiprocessing.Process(target=test_connection, args=(url, username, password))
result = map(p, users)
print(result)
results = set(result)
print(results)
"""