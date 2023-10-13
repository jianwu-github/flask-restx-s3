import requests

url = "http://localhost:8000/api/upload"

files = {'file': open('snowflake.jpg', 'rb')}

response = requests.request("POST", url, files=files)

print(f'response: status is {response.status_code}, content is {response.content}')
