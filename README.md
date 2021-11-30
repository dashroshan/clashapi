# ClashAPI

Using your developer account's login email and password, update the IP address of all your existing Clash of Clans and/or Clash Royale API keys to the current one, and obtain their tokens.

## Getting Started

### Installing

```bash
pip install clashapi
```

### Usage

```python
import clashapi

# Clash of Clans
tokens = clashapi.coc("email", "password")

# Clash Royale
tokens = clashapi.cr("email", "password")

# tokens is a list of api key token strings that you can now use to access the COC/CR APIs
```

### Quick Example

```python
import requests
import clashapi
tokens = clashapi.coc("email", "password")

response = requests.get(url="https://api.clashofclans.com/v1/clans/%23208GJG2J", headers={"Accept": "application/json", "authorization": f"Bearer {tokens[0]}"})
print(response.json())
```
