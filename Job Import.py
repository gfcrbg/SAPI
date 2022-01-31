import requests
import json
import csv
import pandas as pd
from google.colab import files


url = 'https://www.sassieshop.com/2mysteryshopinc/sapi/api/token'

payload = {
"grant_type": "client_credentials",
"client_id": "Qcf6EeJr6VqqNwZiTeBvSKKCCwjtH7az",
"client_secret": "vfGuKfbfM3AK1k7HlH1e3PfUJ4K4kfIm"   
}

r = requests.post(url, json=payload)
authent = r.json()
accessToken = authent["access_token"]
headers = {'Authorization': f'bearer {accessToken}'}
print(f"{authent} \n\n Header ready for 1-hour usage.")



# MANUAL INPUT TEST

url = 'https://www.sassieshop.com/2mysteryshopinc/sapi/api/job_import'

# SURVEY ID
print("Enter survey ID...")
survey_id = input()

# CLIENT LOCATION ID
print("Enter client location ID...")
location_id = input()

# QUESTIONS
print("Enter question data...")
question_881 = input()

payload = {
'survey_id': f'{survey_id}',
'client_location_id': f'{location_id}',
'question_881': f'{question_881}'
}

r = requests.post(url, headers=headers, json=payload)
r.json()



# READS FROM GOOGLE SHEET ON EXECUTION TEST

from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials



gc = gspread.authorize(GoogleCredentials.get_application_default())
worksheet = gc.open('Sandbox').sheet1


url = 'https://www.sassieshop.com/2mysteryshopinc/sapi/api/job_import'

# SURVEY ID
survey_id = worksheet.acell('A2').value

# CLIENT LOCATION ID
location_id = worksheet.acell('B2').value

# QUESTIONS
question_1 = worksheet.acell('C2').value
question_901 = worksheet.acell('D2').value
question_911 = worksheet.acell('E2').value

payload = {
'survey_id': f'{survey_id}',
'client_location_id': f'{location_id}',
'question_1': f'{question_1}',
'question_901': f'{question_901}' ,
'question_911': f'{question_911}'
}

r = requests.post(url, headers=headers, json=payload)
r.json()
#print(payload)



# READS FROM PANDAS DATAFRAME ON EXECUTION TEST
# Google Sheet converts to pd DataFrame

from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())
worksheet = gc.open('Sandbox').sheet1
worksheet = worksheet.get_all_values()
df = pd.DataFrame(worksheet)

url = 'https://www.sassieshop.com/2mysteryshopinc/sapi/api/job_import'

# SURVEY ID
survey_id = df[0][1]

# CLIENT LOCATION ID
client_location_id = df[1][1]

# QUESTIONS
question_1 = df[2][1]
question_901 = df[3][1]
question_911 = df[4][1]

payload = {
'survey_id': f'{survey_id}',
'client_location_id': f'{location_id}',
'question_1': f'{question_1}',
'question_901': f'{question_901}' ,
'question_911': f'{question_911}'
}

r = requests.post(url, headers=headers, json=payload)
r.json()



# LOOP DATA TEST

gc = gspread.authorize(GoogleCredentials.get_application_default())
worksheet = gc.open('Sandbox').sheet1
worksheet = worksheet.get_all_values()
df = pd.DataFrame(worksheet)

url = 'https://www.sassieshop.com/2mysteryshopinc/sapi/api/job_import'

# SURVEY ID
survey_id = df[0][1]

# CLIENT LOCATION ID
client_location_id = df[1][1]

# QUESTIONS
question_1 = [df[2][1]]
question_901 = df[3][1]
question_911 = df[4][1]

payload = {
'survey_id': f'{survey_id}',
'client_location_id': f'{location_id}',
'question_1': f'{question_1}',
'question_901': f'{question_901}' ,
'question_911': f'{question_911}'
}

#r = requests.post(url, headers=headers, json=payload)
#r.json()

print(question_1)
for i in question_1:
  var = i

print(var)

