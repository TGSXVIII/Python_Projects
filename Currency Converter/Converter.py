from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return result

if __name__ == '__main__':
    amount = float(input("Enter the amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")