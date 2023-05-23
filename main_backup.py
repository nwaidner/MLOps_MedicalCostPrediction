from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests



# Settings
ENDPOINT = "https://europe-west3-aiplatform.googleapis.com/v1/projects/mlops-medical-cost-prediction/locations/europe-west3/endpoints/2080249611473125376:predict"
SERVICE_ACCOUNT_KEY_FILE = "venv/lib/client_secret_google.json"

# Load the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_KEY_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Get an access token using the service account credentials
credentials.refresh(Request())
access_token = credentials.token

# Send a request to the endpoint using the access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# JSON data to send in the request
data = {
    "instances": [
        [19, 0, 27.9, 0, 1, 3],
        [18, 1, 33.77, 1, 0, 2]
    ]
}

response = requests.post(ENDPOINT, headers=headers, json=data)

print(response)

