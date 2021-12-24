import time

import requests

apiService = requests.get("https://www.githubstatus.com/api/v2/status.json") # Success code

indicator = apiService.json()['status']['indicator']

while (indicator == 'none'):
    time.sleep(5)
    indicator = apiService.json()['status']['indicator']

if (indicator != 'none'):
    print("Status API service is not working properly")
    print(indicator)
