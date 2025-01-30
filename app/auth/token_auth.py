import requests
import json
from app.config import IMEI_API_TOKEN

def is_authorized():
    url = "https://api.imeicheck.net/"
    payload = {}
    headers = {
        'Authorization': f'Bearer {IMEI_API_TOKEN}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return True
    else:
        print(f"Authorization failed: {response.text}")
        return False

def token_required(f):
    def decorated(*args, **kwargs):
        if not is_authorized():
            return {'error': 'Invalid API token'}, 401
        return f(*args, **kwargs)
    return decorated
