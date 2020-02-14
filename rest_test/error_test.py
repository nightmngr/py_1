# py 3.8.1
# http_error_test

# requests
import requests
import sys

# url
url = 'https://google.com'

try:
    response = requests.get(url)
    print(response.elapsed)
    print(response.status_code)
    # print(response.content)
except requests.exceptions.RequestException as e:
    print("err")
    print(e)
    sys.exit(1)