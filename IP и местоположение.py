import requests

api_url = "https://api.ipify.org/"
reponse = requests.get(api_url)
ip_adress = reponse.text
api_url2 = "https://geo.ipify.org/api/v1/"
params = {
          "apiKey": "at_YfbUu9j7LjZLxTwrLenlLFs8igqOn",
          "ipAddress": ip_adress
        }
reponse = requests.get(api_url2, params=params)
date = reponse.json()
print(ip_adress)
print(date)
print(date["location"]["country"])
print(date["location"]["city"])
