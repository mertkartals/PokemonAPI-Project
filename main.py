import requgiests

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)
print(response.json())
