# كود يحول من الدولار إلى الدينار (مثال بسعر صرف ثابت)
amount_usd = float(input("Enter amount in USD: "))
exchange_rate = 200  # مثال لسعر الصرف
amount_dzd = amount_usd * exchange_rate

print(f"${amount_usd} is equal to {amount_dzd} DZD")
