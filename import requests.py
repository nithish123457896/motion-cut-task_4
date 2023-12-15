import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    params = {'apikey': api_key}

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        rate = data['rates'].get(target_currency)
        if rate:
            return rate
        else:
            print(f"Error: Unsupported target currency {target_currency}")
            return None
    else:
        print(f"Error: {data.get('error', 'Unknown error')}")
        return None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your Open Exchange Rates API key
    base_currency = input("Enter the source currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    amount = float(input("Enter the amount to convert: "))

    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
        print(f"Exchange rate used: 1 {base_currency} = {exchange_rate:.4f} {target_currency}")

if __name__ == "__main__":
    main()
