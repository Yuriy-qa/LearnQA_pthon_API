import requests
response = requests.get("https://stage.podpis.by")
# print(dir(response))
print(response)
print(response.status_code)
