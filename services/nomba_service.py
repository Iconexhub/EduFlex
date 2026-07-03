import os
import requests
from dotenv import load_dotenv

load_dotenv()

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

def create_checkout_order(
    amount,
    customer_email,
    callback_url
):

    token_response = get_access_token()

    if token_response.get("code") != "00":
        return token_response

    access_token = token_response["data"]["access_token"]

    credentials = get_nomba_credentials()

    response = requests.post(
        "https://api.nomba.com/v1/checkout/order",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "accountId": credentials["account_id"]
        },
        json={
            "order": {
                "amount": f"{amount}.00",
                "currency": "NGN",
                "customerEmail": customer_email,
                "callbackUrl": callback_url
            }
        }
    )

    return response.json()