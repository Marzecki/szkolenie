import requests
import json

questions = []

URL = 'https://support.oneskyapp.com/hc/en-us/article_attachments/202761727/example_2.json'
response = requests.get(URL).json()
print(response)

result = [[[response[item1][item2][item3]['question'] for item3 in response[item1][item2]] for item2 in response[item1]] for item1 in response]

print(result)

for item in response:
    for item2 in response[item]:
        for item3 in response[item][item2]:
            print(response[item][item2][item3]['question'])
