from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests


class Person:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges


    def print_details(self):
        print("Person Details:")
        print("Age: ", self.age)
        print("Sex: ", self.sex)
        print("BMI: ", self.bmi)
        print("Children: ", self.children)
        print("Smoker: ", self.smoker)
        print("Region: ", self.region)
        print("Charges: ", self.charges)

    def get_costs(self):
        # Settings
        ENDPOINT = "https://europe-west3-aiplatform.googleapis.com/v1/projects/mlops-medical-cost-prediction/locations/europe-west3/endpoints/3147321248183222272:predict"
        SERVICE_ACCOUNT_KEY_FILE = "venv/lib/client_secret_google.json"

        access_token = get_token(ENDPOINT, SERVICE_ACCOUNT_KEY_FILE)

        # JSON data to send in the request

        data = {
            "instances": [
                [self.age, self.sex, self.bmi, self.children, self.smoker, self.region]
            ]
        }

        # Send a request to the endpoint using the access token
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        return requests.post(ENDPOINT, headers=headers, json=data)


def get_token(ENDPOINT, SERVICE_ACCOUNT_KEY_FILE):
    # Load the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_KEY_FILE,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    # Get an access token using the service account credentials
    credentials.refresh(Request())
    return credentials.token


def get_person_list_costs(persons):
    # Settings
    ENDPOINT = "https://europe-west3-aiplatform.googleapis.com/v1/projects/mlops-medical-cost-prediction/locations/europe-west3/endpoints/3147321248183222272:predict"
    SERVICE_ACCOUNT_KEY_FILE = "venv/lib/client_secret_google.json"

    access_token = get_token(ENDPOINT, SERVICE_ACCOUNT_KEY_FILE)

    # JSON data to send in the request
    instances = []

    for person in persons:
        instance = [person.age, person.sex, person.bmi, person.children, person.smoker, person.region]
        instances.append(instance)

    data = {
        "instances": instances
    }

    # Send a request to the endpoint using the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    return requests.post(ENDPOINT, headers=headers, json=data)




