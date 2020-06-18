import requests
import os
import json



#os.system("https://login.questrade.com/oauth2/token?grant_type=refresh_token&refresh_token=vjd3HV4_Jl6HxR1KzpAP728BJJarvBIk0")

uri = "https://api07.iq.questrade.com/v1/"

operation = "markets/quotes/"

symbol = "8049"


headers = {'Authorization': 'Bearer xxxxxx'}

final_uri = uri + operation + symbol

print(final_uri)

r = requests.get(final_uri, headers=headers)
response = r.json()


print(response)


########v1


json_data = json.loads(str(response))

#print(json_data[


