import requests

url = "https://handhelds.api.lto.direct/ords//dl_a_letas/hhd/v1/verifyDLRecord"

payload = "{\n    \"dls_dl_no\": \"C1014007530\",\n    \"first_name\": \"KAZIM\",\n    \"last_name\": \"SARIKAYA\",\n    \"DATE_OF_BIRTHe\":\"08-01-1990\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ODY5MDkyMDMyMTYzNDE5OlJHVlRGMDAxMjcwODY5MDkyMDMyMTYzNDE5ODY5MDkyMDMyMTYzNDI3'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.headers)
print(response.headers.get('json_out'))
print(response.text.encode('utf8'))
