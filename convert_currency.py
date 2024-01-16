def convert_currency(amount, source_currency, target_currency):
    # Exchange rates as of a specific date
    currency_rates = {"USD": 1.00, "INR": 83.22, "EUR": 0.92, "JPY": 147, "GBP": 0.79, "AUD": 1.5}

    # Check if source currency is valid
    if source_currency not in currency_rates:
        return f"Invalid source currency code: {source_currency}. Please use valid currency codes."

    # Check if target currency is valid
    if target_currency not in currency_rates:
        return f"Invalid target currency code: {target_currency}. Please use valid currency codes."

    # Calculate the converted amount
    converted_amount = amount * (currency_rates[target_currency] / currency_rates[source_currency])
    rounded_amount = round(converted_amount, 2)

    # Format the result string
    result = "{:.2f} {} = {:.2f} {}".format(amount, source_currency, rounded_amount, target_currency)
    return result

def main():
    try:
        # Get user input for amount, source currency, and target currency
        amount = float(input("Enter the amount to convert: "))
        source_currency = input("Enter the source currency code: ").upper()
        target_currency = input("Enter the target currency code: ").upper()

        # Call the conversion function and print the result
        result = convert_currency(amount, source_currency, target_currency)
        print(result)

    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")

if __name__ == "__main__":
    main()
