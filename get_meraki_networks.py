import requests
import json

# Define the Meraki Sandbox connection details
BASE_URL = "https://meraki.com"
API_KEY = "0468a240744e9c13b29c97b5e4075f9227efbc86"  # Public shared Cisco sandbox key

# Construct the required HTTPS headers (DevNet Exam Topic: API Authentication)
headers = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Accept": "application/json"
}

# Target endpoint: Fetch all networks for the Cisco Demo Organization (ID: 549236)
url = f"{BASE_URL}/organizations/549236/networks"

try:
    print("Connecting to Cisco Meraki API Sandbox...")
    # Execute the live REST API GET request
    response = requests.get(url, headers=headers)
    
    # Check for HTTP errors (DevNet Exam Topic: HTTP Status Codes)
    response.raise_for_status()
    
    # Parse the raw JSON payload into a clean Python list
    networks = response.json()
    print(f"Successfully retrieved {len(networks)} networks!\n")
    
    # Print a clean, formatted overview of the first 5 networks
    print(f"{'Network Name':<30} | {'Product Types'}")
    print("-" * 60)
    for network in networks[:5]:
        products = ", ".join(network.get("productTypes", []))
        print(f"{network.get('name'):<30} | {products}")

except requests.exceptions.RequestException as e:
    print(f"API Connection Failed: {e}")
