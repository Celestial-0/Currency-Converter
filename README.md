# Currency Converter

This Python script allows you to convert an amount from one currency to another using exchange rates. The script includes a `convert_currency` function that takes the amount, source currency code, and target currency code as input parameters and returns the converted amount.

## Usage

To use the currency converter, run the script and follow the prompts to enter the amount, source currency code, and target currency code.

```bash
python currency_converter.py
```

## Function: `convert_currency`

```python
def convert_currency(amount, source_currency, target_currency):
    """
    Convert an amount from the source currency to the target currency.

    Parameters:
    - amount (float): The amount to convert.
    - source_currency (str): The source currency code.
    - target_currency (str): The target currency code.

    Returns:
    - str: A formatted string representing the converted amount.
    """
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
```

## Running the Script

To run the script, execute the `main` function. The script will prompt you to enter the amount, source currency code, and target currency code.

```python
if __name__ == "__main__":
    main()
```

## Note

- The exchange rates used in the script are as of a specific date and may not reflect the current rates.
- Ensure that you enter valid currency codes when prompted.
- If an invalid input is provided, the script will display an appropriate error message.