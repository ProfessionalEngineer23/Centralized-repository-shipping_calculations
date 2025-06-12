# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram in USD: "))

## Calculate shipping cost in USD
shipping_cost_usd = weight * rate

## Currency conversion rates (example values — you can update these to real-time rates)
usd_to_eur = 0.93       # Example: 1 USD = 0.93 EUR
usd_to_jpy = 155.35     # Example: 1 USD = 155.35 Yen
usd_to_rub = 89.50      # Example: 1 USD = 89.50 Rubbles

## Calculate shipping cost in other currencies
shipping_cost_eur = shipping_cost_usd * usd_to_eur
shipping_cost_jpy = shipping_cost_usd * usd_to_jpy
shipping_cost_rub = shipping_cost_usd * usd_to_rub

## Display the results
print(f"\nShipping Cost:")
print(f"- USD: ${shipping_cost_usd:.2f}")
print(f"- Euro (EUR): €{shipping_cost_eur:.2f}")
print(f"- Japanese Yen (JPY): ¥{shipping_cost_jpy:.2f}")
print(f"- Russian Rubbles (RUB): ₽{shipping_cost_rub:.2f}")

# Here is a new update by Niki
