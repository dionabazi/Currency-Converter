import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Error fetching data from API.")

    rates = response.json().get("rates")

    if to_currency not in rates:
        raise ValueError(f"Currency '{to_currency}' not found.")
    
    return amount * rates[to_currency]

def get_supported_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Get base currency in USD for a list of supported currencies
    response = requests.get(url)
    return response.json().get("rates").keys()

if __name__ == "__main__":
    print("Supported currencies:", ", ".join(get_supported_currencies()))
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., EUR): ").upper()
    
    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}.")
    except ValueError as e:
        print(e)
