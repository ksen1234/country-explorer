import requests

url = "https://countries.dev/countries"

def get_countries(url):

    response = requests.get(url)
    data = response.json()
    return data

# Creating a dictionary with country codes as keys and country names as values
def create_country_codes(data):
    country_codes = {}
    for country in data:
        code = country["alpha3Code"]
        name = country["name"]
        country_codes[code] = name
    return country_codes

# Asking user about the country user wants to explore
def find_country(data):
    country_name = input("What country do you want to explore? ").strip()
    for country in data:
        if country_name.lower() == country["name"].lower():
            return country["name"]

    print(f"Sorry, {country_name} is not a valid country name.")
    return None


# Getting the info about the country user have chosen
def display_country_info(country_name, country_codes):

    url = f"https://countries.dev/name/{country_name}"
    response = requests.request("GET", url)
    new_data = response.json()
    if not new_data:
        print("Country information not found.")
        return
    capital = new_data[0]["capital"]
    population = new_data[0]["population"]
    currencies = new_data[0]["currencies"]
    if currencies:
        currency = currencies[0]["name"]
    else:
        currency = "Not available"
    flag = new_data[0]["flag"]

    # Getting useful info about the country
    print(f"{country_name} capital is: {capital}")
    print(f"{country_name} population is: {population}")
    print(f"{country_name} currency is: {currency}")
    print(f"{country_name} flag is: {flag}")

    # Looping over countries in the list of neighbors and printing their names
    borders = new_data[0].get("borders", [])
    if borders:
        print(f"Here's {country_name} neighbors:")
        for neib in borders:
            print(country_codes[neib])
    else:
        print("This country has no land borders.")

def main():
    
    data = get_countries(url)
    country_codes = create_country_codes(data)
    country_name = find_country(data)
    if country_name:
        display_country_info(country_name, country_codes)

if __name__ == "__main__":
    main()

