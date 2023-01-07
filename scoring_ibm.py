# -*- coding: utf-8 -*-

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Z4p0bvDJ0SlOGLSiWSbNiEJwrBbIM4tI-zuvBaVW3MIs"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [["year","month"]], "values": [[2015,2]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/0999f23f-f7b3-4eaa-a9b2-7ec8e2af1de2/predictions?version=2021-12-04', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
pred= response_scoring.json()
print(pred)
output= pred['predictions'][0]['values'][0][0]
print(output)