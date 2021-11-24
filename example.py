import requests

#Updating the ip address of existing keys and getting the list of new tokens
from updatekeys import updatekeys
tokens=updatekeys("email", "password")

#An example get request with an updated token
response=requests.get(url="https://api.clashofclans.com/v1/clans/%23208GJG2J", headers={"Accept": "application/json","authorization":f"Bearer {tokens[0]}"})
print(response.json())