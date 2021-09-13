
#!/usr/bin/env python3

# This scripts validates the signature present in the Rapyd webhooks

__author__ = "Isaac Benitez"
__date__ = "07/21/2021"
__version__ = "0.0.1"

import hashlib
import base64
import json
import string
from random import *
import hmac

path = 'https://webhook.site/bb2fab13-ac12-4d6a-9843' # webhook listener url configured in Rapyd portal
timestamp = 1626830114 # present in the webhook header
salt = 'salt-present-in-the-webhook-header'
access_key = ''
secret_key = ''

# body of the webhook with no spaces
body_obj = '{"id":"wh_500d5534e75219af0c1a26113bb07d0e","type":"CUSTOMER_DELETED","data":{"id":"cus_9d170fd802ead04e5dbda8b48125cf74","deleted":true},"trigger_operation_id":"f675b964-9bac-4f36-9cbf-f768413d947c","status":"NEW","created_at":1626830113}'
body = json.dumps (json.loads(body_obj), separators=(',', ':'))

to_sign = path + salt + str(timestamp) + access_key + secret_key + body

h = hmac.new(bytes(secret_key, 'utf-8'), bytes(to_sign, 'utf-8'), hashlib.sha256)
signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

wh_signature = 'the-signature-to-validate-present-in-the-webhook-header'

print(signature.decode('utf-8'))
print(wh_signature)

print("True") if signature.decode('utf-8') == wh_signature else print("False")
