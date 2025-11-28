#P1. Currency Conversion Utility
# 1 USD=0.93 EUR and 1 USD=151.78 JPY

USD_TO_EUR = 0.93
USD_TO_JPY = 151.78
usd_amount = float(input('Enter the amount in USD: '))
print(f"{usd_amount} USD is {(usd_amount*USD_TO_EUR):.2f} EUR")
print(f"{usd_amount} USD is {(usd_amount*USD_TO_JPY):.2f} JPY")