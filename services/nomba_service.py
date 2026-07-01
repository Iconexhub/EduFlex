import os
import requests


BASE_URL = "https://sandbox.nomba.com/v1"

def get_nomba_credentials():

    return {
        "account_id": os.getenv("NOMBA_ACCOUNT_ID"),
        "client_id": os.getenv("NOMBA_CLIENT_ID"),
        "client_secret": os.getenv("NOMBA_CLIENT_SECRET")
    }

def get_access_token():

    credentials = get_nomba_credentials()

    response = requests.post(
        f"{BASE_URL}/auth/token/issue",
        headers={
            "Content-Type": "application/json",
            "accountId": credentials["account_id"]
        },
        json={
            "grant_type": "client_credentials",
            "client_id": credentials["client_id"],
            "client_secret": credentials["client_secret"]
        }
    )

    return response.json()