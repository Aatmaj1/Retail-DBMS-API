# Importing necessary libraries for handling JSON, making HTTP requests, and testing.

import json
import requests
import pytest


def reformat_response(response_json):
    # Initialize the output JSON structure with empty dictionaries for each expected key.
    reformatted_json = {
        'EMAIL': {},
        'TELEPHONE': {},
        'CUSTOMER_NAME': {},
        'ORDER_ID': {},
        'PRODUCT_ID': {},
        'BILLING_STREET': {},
        'BILLING_CITY': {},
        'BILLING_STATE': {},
        'BILLING_ZIP_CODE': {},
        'BILLING_ADD_TYPE': {},
        'SHIPPING_STREET': {},
        'SHIPPING_CITY': {},
        'SHIPPING_STATE': {},
        'SHIPPING_ZIP_CODE': {},
        'SHIPPING_ADD_TYPE': {}
    }
    
    # Loop through each item in the original response.
    for idx, details in response_json.items():
        # For each key in the item, add the value to the corresponding key in the reformatted_json.
        reformatted_json['EMAIL'][idx] = details['EMAIL']
        reformatted_json['TELEPHONE'][idx] = details['TELEPHONE']
        reformatted_json['CUSTOMER_NAME'][idx] = details['CUSTOMER_NAME']
        reformatted_json['ORDER_ID'][idx] = details['ORDER_ID']
        reformatted_json['PRODUCT_ID'][idx] = details['PRODUCT_ID']
        reformatted_json['BILLING_STREET'][idx] = details['BILLING_STREET']
        reformatted_json['BILLING_CITY'][idx] = details['BILLING_CITY']
        reformatted_json['BILLING_STATE'][idx] = details['BILLING_STATE']
        reformatted_json['BILLING_ZIP_CODE'][idx] = details['BILLING_ZIP_CODE']
        reformatted_json['BILLING_ADD_TYPE'][idx] = details['BILLING_ADD_TYPE']
        reformatted_json['SHIPPING_STREET'][idx] = details['SHIPPING_STREET']
        reformatted_json['SHIPPING_CITY'][idx] = details['SHIPPING_CITY']
        reformatted_json['SHIPPING_STATE'][idx] = details['SHIPPING_STATE']
        reformatted_json['SHIPPING_ZIP_CODE'][idx] = details['SHIPPING_ZIP_CODE']
        reformatted_json['SHIPPING_ADD_TYPE'][idx] = details['SHIPPING_ADD_TYPE']

    return reformatted_json

# Define a test case to check the API response for invalid input
def test_api_order_history_invalid_response():
    
    url = "http://127.0.0.1:6003/orderHistory"

    # Set up the data payload and headers for the HTTP request.
    payload = {'data': 'john.a@google.com',
    'type': 'telephone'}
    files=[]
    headers = {}

    # Send a POST request and assert the status code.
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 500, "Checking Invalid Status"
    
# Define a test case to check the API response for a valid email-based query.    
def test_api_order_history_email_response():
    
    url = "http://127.0.0.1:6003/orderHistory"

    # Set up the data payload for the request.
    payload = {'data': 'john.doe@google.com',
    'type': 'email'}
    files=[]
    headers = {}

    # Send a POST request and verify the response.
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 200, "API did not return a successful response"

    # Parse the JSON response and reformat it.
    response_json = response.json()['result']
    reformatted_response = reformat_response(response_json)

    # Load the expected JSON data from a file and compare it.
    with open('test_result/email_test.json', 'r') as file:
        expected_json = json.load(file)
    
    # Compare the expected JSON to the response JSON
    assert reformatted_response == expected_json, "API response did not match the expected JSON"


def test_api_order_history_phone_response():
    
    url = "http://127.0.0.1:6003/orderHistory"

    # Set up the data payload for the request.
    payload = payload = {'data': '8378139380',
    'type': 'telephone'}
    files=[
    ]
    headers = {}

    # Send a POST request and verify the response.
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 200, "API did not return a successful response"

    # Parse the JSON response and reformat it.
    response_json = response.json()['result']
    reformatted_response = reformat_response(response_json)

    # Load the expected JSON data from a file and compare it.
    with open("test_result/telephone_test.json", 'r') as file:
        expected_json = json.load(file)
    
    # Compare the expected JSON to the response JSON
    assert reformatted_response == expected_json, "API response did not match the expected JSON"

def test_api_order_billing_response():

    url = "http://127.0.0.1:6003/ordersByBilling"

    # Set up the data payload for the request.
    payload = {'data': 'False'}
    files=[
    ]
    headers = {}

    # Send a POST request and verify the response.
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 200

    # Parse the JSON response and reformat it.
    response_json = response.json()['result']

    # Load the expected JSON data from a file and compare it.
    with open('test_result/list_orders_by_billing_zip_codes_test.json', 'r') as file:
        expected_json = json.load(file)

    # Compare the expected JSON to the response JSON
    assert list(response_json) == list(expected_json.values()), "API response did not match the expected JSON"

def test_api_order_shipping_response():

    url = "http://127.0.0.1:6003/ordersByShipping"

    # Set up the data payload for the request.
    payload = {'data': 'False'}
    files=[
    ]
    headers = {}

    # Send a POST request and verify the response.
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 200

    # Parse the JSON response and reformat it.
    response_json = response.json()['result']

    # Load the expected JSON data from a file and compare it.
    with open('test_result/orders_by_shipping_zip_codes.json', 'r') as file:
        expected_json = json.load(file)

    # Compare the expected JSON to the response JSON
    assert list(response_json) == list(expected_json.values()), "API response did not match the expected JSON"

def test_api_peakHour_response():

    url = "http://127.0.0.1:6003/peakHour"

    # Set up the data payload for the request
    payload = {}
    files=[]
    headers = {}

    # Send a POST request and verify the response.
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    assert response.status_code == 200

    # Parse the JSON response and reformat it.
    response_json = response.json()['result']

    # Load the expected JSON data from a file and compare it.
    with open('test_result/orders_by_shipping_zip_codes.json', 'r') as file:
        expected_json = json.load(file)

    # Compare the expected JSON to the response JSON
    assert int(response_json) == 15, "API response did not match the expected JSON"

# Running the test would typically be done outside this script or in a main block:
if __name__ == "__main__":
    pytest.main()
