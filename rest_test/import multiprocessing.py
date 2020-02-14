import multiprocessing
import time
import requests
from requests.auth import HTTPDigestAuth
import json


# url
url = 'https://handhelds.api.qa.lto.direct/ords/dl_a_letas/hhd/v1/getIRMVChecklist?limit=2000'


def make_call():
    test_response = requests.get(url, auth=('869092030733866', 'RGVTF000054869092030733866869092030733874'))

    if(test_response.ok):
        #print('%d:' % x)        
        print(test_response.elapsed)
        #print(test_response.headers)
        #print(test_response.json())

    else:
        print("test not ok")


if __name__ == '__main__':

    t1 = time.perf_counter()

    numbers = range(100)
    processes = []

    for number in numbers:
        p = multiprocessing.Process(target=make_call)#, args=(number,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    t2 = time.perf_counter()

    print(f"total time {t2-t1}")