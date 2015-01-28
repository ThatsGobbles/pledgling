#!/usr/bin/python3

'''This module processes PayPal Instant Payment Notification messages (IPNs).
'''

import sys
import urllib.parse
import requests

#VERIFY_URL = 'https://www.paypal.com/cgi-bin/webscr'
VERIFY_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'

# CGI preamble
print("content-type: text/plain")
print()

# Read and parse query string
param_str = sys.stdin.readline().strip()
params = urllib.parse.parse_qsl(param_str)

# Add '_notify-validate' parameter
params.append(('cmd', '_notify-validate'))

# Post back to PayPal for validation
headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
r.raise_for_status()

if r.text == 'VERIFIED':
	pass
elif r.text == 'INVALID':
	pass
else:
	pass

