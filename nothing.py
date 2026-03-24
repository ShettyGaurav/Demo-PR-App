import requests

def get_exchange_rate(base_currency, target_currency):
    """Fetches real-time exchange rates using a free API."""
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["result"] == "success":
            rates = data["rates"]
            return rates.get(target_currency.upper())
        else:
            print("Error: Could not fetch data.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("--- 🌍 Minimalist Currency Converter ---")
    
    base = input("Enter source currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., EUR): ").upper()
    
    try:
        amount = float(input(f"Enter amount in {base}: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    rate = get_exchange_rate(base, target)

    if rate:
        converted_amount = amount * rate
        print(f"\n✅ {amount} {base} is equal to {converted_amount:.2f} {target}")
        print(f"Current rate: 1 {base} = {rate} {target}")
    else:
        print("Sorry, that currency pair is not available.")

if __name__ == "__main__":
    main()