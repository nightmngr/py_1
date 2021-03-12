# py 3.8.1
# http_error_test
# vo terminal:
# sudo apt update
# sudo apt install python3-pip
# vo Py3: pip3 install requests

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