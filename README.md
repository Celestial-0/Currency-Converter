# Currency Converter 💱

This Python script is a simple yet efficient currency converter that allows you to convert an amount from one currency to another using exchange rates. It includes interactive prompts and uses emojis to enhance the user experience.

## How to Use 🚀

1. Run the script by executing the following command in your terminal or command prompt:

    ```bash
    python currency_converter.py
    ```

2. Enter the required information as prompted:

    - Enter the amount to convert.
    - Enter the source currency code.
    - Enter the target currency code.

3. The script will then display the converted amount along with the source and target currency codes.

## Functionality 🛠️

The script comprises two main functions:

### `convert_currency(amount, source_currency, target_currency, rates)`

This function takes in the amount to be converted, the source and target currency codes, and a dictionary of exchange rates. It then calculates and returns the converted amount, rounded to two decimal places.

### `get_user_input()`

This function prompts the user to input the amount, source currency code, and target currency code. It handles exceptions to ensure that the input is valid (numeric amount).

## Example 📝

```python
# Exchange rates as of a specific date
currency_rates = {"USD": 1.00, "INR": 83.22, "EUR": 0.92, "JPY": 147, "GBP": 0.79, "AUD": 1.5}

try:
    amount, source_currency, target_currency = get_user_input()

    # Call the conversion function and print the result
    result = convert_currency(amount, source_currency, target_currency, currency_rates)
    print(result)

except ValueError as e:
    print(f"⚠️ Error: {str(e)}")
```

In this example, the script prompts the user for input, validates the input, performs the currency conversion, and prints the result. If there are any errors (e.g., invalid input or currency codes), it catches the `ValueError` and prints an error message with an attention-grabbing emoji. Happy currency converting! 💸✨
