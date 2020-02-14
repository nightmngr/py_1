# py 3.8.1
# rest_test.py

# requests
import requests
from requests.auth import HTTPDigestAuth
import json

# multiprocessing
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from multiprocessing import pool

# test requests
def test_connection(url, timeout = 1):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print(requests.HTTPError())
        return False
    

# url
url = 'https://handhelds.api.qa.lto.direct1/ords/dl_a_letas/hhd/v1/getIRMVChecklist?limit=2000'


##test_connection(url)


"""
# define user
class User(object):
    
    def __init__(self, id):
        self.id = id
    
    def run_request(self, url):
        test_response = requests.get(url, auth=('869092030733866', 'RGVTF000054869092030733866869092030733874'))    

        if(test_response.ok):
            print()
            print()
            print('%d:' % self.id)        
            print(test_response.elapsed)
            # print(test_response.headers)
            # print(test_response.json())

        else:
            print("test not ok")
"""
# p = pool(5)
#    p.map()
# t_user = User(1)
# t_user.run_request(url)


# test_request
for x in range(10):

    # if host is reachable make the call

    if(test_connection(url)):
        test_response = requests.get(url, auth=('869092030733866', 'RGVTF000054869092030733866869092030733874'))

        print()
        print()
        print('%d:' % x)        
        print(test_response.elapsed)
        print(test_response.status_code)
        # print(test_response.headers)
        # print(test_response.json())

    else:
        print("test not ok")
        print(requests.HTTPError)
        break
