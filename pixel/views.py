import base64
import copy
import json
import time
from datetime import date
from cryptography.fernet import Fernet
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from pixel.models import Email


key = b'OsuSKe1QDZ0kjJv0GLJI6wB2A267xnVpc5-A1bbCbM4='
fernet = Fernet(key)

def decrypt_id(pixel_id):
    result = bytes(pixel_id, encoding='utf-8')
    print(result)
    message = fernet.decrypt(result).decode('utf-8')
    return json.loads(message)


def pixel_view(request, pixel_id):
    pixel_data = base64.b64decode("R0lGODlhAQABAIAAAP8AAP8AACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==")
    event_record = {
        'time': int(time.time()),
        'data': {},
        'headers': {},
    }
    pixel_id = pixel_id.rstrip('.gif')
    event_record['data'] = decrypt_id(pixel_id)
    for header in request.headers:
        event_record['headers'][header[0]] = request.headers.get(header[0])

    print("Saving data to database...")
    
    tracker, created = Email.objects.get_or_create(pixel_id=pixel_id, date=date.today(), subject=event_record['data']['subject'], user_to=event_record['data']['to'], user_cc=event_record['data']['cc'])
    tracker.seen = tracker.seen + 1
    tracker.save()
    print(event_record)
    
    return HttpResponse(pixel_data, content_type='image/gif')
