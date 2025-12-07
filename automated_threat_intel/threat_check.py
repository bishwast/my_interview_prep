# Enriching an IP address with Threat Intelligence.
import requests         # This tool allows us to send Data over the Internet
import json             # This tool helps us read the data we get back
import config           # Local File Connection

# --- CONFIGURATION ---
# The specific IP we want to investigate. This is the malicious IP we use for testing
target_ip = '118.25.6.39'

# The URL where the AbuseIPDB API lives
url = 'https://api.abuseipdb.com/api/v2/check'


# --- THE VIP PASS (HEADERS) ---
# We must send our keys or the server will block us (401 Unauthorized)
headers = {
    'Accept': 'application/json',
    'Key': config.ABUSE_IPDB_KEY
}

# --- THE PARAMETERS ---
# We filter the request, where we ask data from last 90 days
querystring = {
    'ipAddress': target_ip,
    'maxAgeInDays': '90'
}

# --- THE ACTION (SENDING THE REQUEST) ---
print(f"Connecting to AbuseIPDB to check Target IP Address: {target_ip}")

# GOAL: GET Information. We use 'requests.get' for this
response = requests.get(url=url, headers=headers, params=querystring)

# --- THE OUTPUT ---
# The server sends us raw text. We need to decode it in Python Dictionary format (JSON)
decoded_data = json.loads(response.text)

# Check if the request was successful
if response.status_code == 200:
    print("\n--- SUCCESS! THREAT REPORT IS BELOW ---")

    print(json.dumps(decoded_data, sort_keys=True, indent=4))       # The print(json.dumps(...)) makes the text output looks pretty with indentation

    score = decoded_data['data']['abuseConfidenceScore']            # Extract just the specific "Abuse Confidence Score"
    print(f"\nAbuse Confidence Score: {score}")

else:
    print("\n--- ERROR ---")
    print(f"Status Code: {response.status_code}")
    print(f"Verify if your API Key is correct!")


