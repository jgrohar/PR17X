import requests

# Define the URL and parameters
url = "https://www.strava.com/api/v3/segments/explore"
params = {
    'bounds': '45.42,13.38,46.88,16.61',
    'activity_type': 'riding'
}

# Define headers including authorization token
headers = {
    'accept': 'application/json',
    'authorization': '****'
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)  # You can print or further process the data
else:
    print(f"Request failed with status code: {response.status_code}")
