Country Explorer is a Python application that allows users to explore information about countries around the world using the countries.dev API.

Users can look up a country by name and view information such as its capital, population, currency, flag, and neighboring countries. 

Features:

1. Search for a country by name.
2. Display country information, including capital, population, currency, and flag.
3. Show neighboring countries.

Technologies:

- Python
- Requests library
- countries.dev API

The application uses the following endpoints:

GET /countries – Retrieves the list of countries.
GET /name/{name} – Retrieves country by name.

Requirements:
Python 3

Installation:

1. Clone the repository:
git clone https://github.com/ksen1234/country-explorer.git
2. Navigate to the project directory:
cd country-explorer
3. Install the required library:
pip install -r requirements.txt
4. Run the application:
python main.py
5. Follow the instructions in the terminal to explore or compare countries.