import json
import requests

upload_img_url = "http://localhost:8000/api/upload"

img_store_url = "http://localhost:8000/api/imgstore"

img_info = {
    "owner": "wikipedia.org",
    "type": "jpeg",
}

files = {
    'imginfo': json.dumps(img_info),
    'imgfile': open('snowflake.jpg', 'rb')
}

upload_api_response = requests.request("POST", upload_img_url, files=files)

print(f'upload api response status: {upload_api_response.status_code}')
print(f'upload api response json: {upload_api_response.json()}')

imgstore_api_response = requests.request("GET", img_store_url)

print(f'imgstore api response status: {imgstore_api_response.status_code}')
print(f'imgstore api response json: {imgstore_api_response.json()}')
