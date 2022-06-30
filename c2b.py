import requests
import keys
from requests.auth import HTTPBasicAuth


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

json_response = r.json()

my_access_token = json_response['access_token']

access_token = my_access_token


def register_url():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": keys.shortCode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://dad4-102-68-76-193.in.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://dad4-102-68-76-193.in.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


# register_url()


def simulate_c2b_transaction():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {
        "Authorization": "Bearer %s" % access_token}

    request = {
        "ShortCode": keys.shortCode,
        "CommandID": "CustomerPayBillOnline",
        "amount": "1",
        "MSISDN": keys.test_MSISDN,
        "BillRefNumber": "123",
    }

    # response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers=headers, data=)
    # print(response.text.encode('utf8'))

    response = requests.post(api_url, headers=headers, json=request)
    print(response.text.encode('utf8'))


simulate_c2b_transaction()
