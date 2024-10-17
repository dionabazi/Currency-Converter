import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    rates = response.json().get("rates")
    return amount * rates[to_currency]

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ")
    to_currency = input("To currency (e.g., EUR): ")
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}.")
