import json
import requests

url = "http://localhost:8000/api/upload"

img_info = {
    "owner": "wikipedia.org",
    "type": "jpeg",
}

files = {
    'imginfo': json.dumps(img_info),
    'imgfile': open('snowflake.jpg', 'rb')
}

response = requests.request("POST", url, files=files)

print(f'response status: {response.status_code}')
print(f'response json: {response.json()}')
