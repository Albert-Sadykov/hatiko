import requests
import json
from app.config import IMEI_API_TOKEN

def check_imei(imei):
    imei = imei.replace(' ', '')
    if not(imei.isdigit()) or len(imei) != 15:
        return 'Неверный формат IMEI'
    url = "https://api.imeicheck.net/v1/checks"
    payload = json.dumps({
        "deviceId": imei,
        "serviceId": 1
    })
    headers = {
        'Authorization': f'Bearer {IMEI_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        response_json = response.json()
        print(f"IMEI check response: {response_json}")  # Отладочный вывод
        return response_json
    except ValueError:
        print(f"Failed to decode JSON response: {response.text}")  # Отладочный вывод
        return f'Что-то пошло не так {response.text}'
