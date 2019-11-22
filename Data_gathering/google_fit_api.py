import requests

url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/" \
      "derived:com.google.step_count.delta:1234567890:Example%20" \
      "Manufacturer:ExampleTablet:1000001/datasets/1397513334728708316-1397515179728708316"
k = requests.get(url)
k = k.json()
print(k)
