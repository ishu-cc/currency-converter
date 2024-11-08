# Dictionary holding exchange rates with respect to USD
# Exchange rates are hypothetical; in real applications, you should get live rates
exchange_rates = {
    'USD': 1.0,        # US Dollar
    'EUR': 0.85,       # Euro
    'GBP': 0.75,       # British Pound
    'INR': 83.0,       # Indian Rupee
    'JPY': 148.2,      # Japanese Yen
    'AUD': 1.65,       # Australian Dollar
    'CAD': 1.34        # Canadian Dollar
}

# Function to convert from one currency to another
def currency_converter(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code."

    # Convert the amount to USD first, then convert to the target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return round(converted_amount, 2)

# Main function to interact with the user
def main():
    print("Available currencies:", ', '.join(exchange_rates.keys()))
    
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))
    
    result = currency_converter(amount, from_currency, to_currency)
    
    if isinstance(result, str):
        print(result)
    else:
        print(f"{amount} {from_currency} = {result} {to_currency}")

# Run the currency converter
main()
