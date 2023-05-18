#!/usr/bin/env python3

import hashlib
import base64
import string
import time
import random
import hmac

path = '/v1/data/countries'
timestamp = int(time.time())
salt = ''.join(random.sample(string.ascii_letters + string.digits, 12))
access_key = '' # Rapyd acces key
secret_key = '' # Rapyd secret key


to_sign = 'get' + path + salt + str(timestamp) + access_key + secret_key + ''

h = hmac.new(bytes(secret_key, 'utf-8'), bytes(to_sign, 'utf-8'), hashlib.sha256)
signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

curl = (f'curl -H "Content-Type: application/json" '
      f'-H "access_key: {access_key}" '
      f'-H "salt: {salt}" '
      f'-H "timestamp: {timestamp}" '
      f'-H "signature:{signature.decode("utf-8")}" '
      f'https://sandboxapi.rapyd.net{path}')

print(curl)
