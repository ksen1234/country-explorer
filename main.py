import requests

url = "https://countries.dev/countries"

def get_countries(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print("Unable to connect. Please check your internet connection and try again.")
        return None

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
    if not country_name:
        print("Please enter a country name.")
        return None
    for country in data:
        if country_name.lower() == country["name"].lower():
            return country["name"]

    print(f"Sorry, {country_name} is not a valid country name.")
    return None


# Getting the info about the country user have chosen
def display_country_info(country_name, country_codes):

    url = f"https://countries.dev/name/{country_name}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        new_data = response.json()
    except requests.exceptions.RequestException:
        print("Unable to retrieve country information.")
        return
    if not new_data:
        print("Country information not found.")
        return
    capital = new_data[0].get("capital") or "Not available"
    population = new_data[0].get("population") or "Not available"
    currencies = new_data[0].get("currencies", [])
    if currencies:
        currency = currencies[0].get("name", "Not available")
    else:
        currency = "Not available"
    flag = new_data[0].get("flag") or "Not available"

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
            print(country_codes.get(neib, neib))
    else:
        print("This country has no land borders.")

def main():
    
    data = get_countries(url)
    if data is None:
        return
    country_codes = create_country_codes(data)
    country_name = find_country(data)
    if country_name:
        display_country_info(country_name, country_codes)

if __name__ == "__main__":
    main()

