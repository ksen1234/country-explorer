import requests

url = "https://countries.dev/countries"

response = requests.get(url)
data = response.json()
# for country in data:
#   print(country['name'])

# Creating a dictionary with country codes as keys and country names as values
country_codes = {}
for country in data:
    code = country["alpha3Code"]
    name = country["name"]
    country_codes[code] = name

# Asking user about the country user wants to explore
country_name = input("What country do you want to explore? ").capitalize()
if country_name not in [country["name"] for country in data]:
    print(f"Sorry, {country_name} is not a valid country name. Try again.")
    exit()

# Getting the info about the country user have chosen
url = f"https://countries.dev/name/{country_name}"
response = requests.request("GET", url)
new_data = response.json()
capital = new_data[0]["capital"]
population = new_data[0]["population"]
currency = new_data[0]["currencies"][0]["name"]
flag = new_data[0]["flag"]

# Getting useful info about the country
print(f"{country_name} capital is: {capital}")
print(f"{country_name} population is: {population}")
print(f"{country_name} currency is: {currency}")
print(f"{country_name} flag is: {flag}")

# Looping over countries in the list of neighbors and printing their names
borders = new_data[0]["borders"]
print(f"Here's {country_name} neighbors:")
for neib in borders:
    print(country_codes[neib])