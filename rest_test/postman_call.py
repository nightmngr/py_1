import requests

url = ""

payload = "{}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic qweqw'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.headers)
print(response.headers.get('json_out'))
print(response.text.encode('utf8'))
