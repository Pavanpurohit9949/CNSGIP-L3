import requests

def currency_converter(amount, from_currency, to_currency):
    # Your API key from Open Exchange Rates
    api_key = 'YOUR_API_KEY'
    
    # Base URL for the Open Exchange Rates API
    base_url = 'https://open.er-api.com/v6/latest/{}'.format(from_currency)
    
    # Make a GET request to fetch latest exchange rates
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        if to_currency in rates:
            exchange_rate = rates[to_currency]
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            return 'Currency code not found.'
    else:
        return 'Failed to fetch exchange rates.'

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("From Currency (3-letter code): ").upper()
    to_currency = input("To Currency (3-letter code): ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print(converted_amount)

if __name__ == "__main__":
    main()
