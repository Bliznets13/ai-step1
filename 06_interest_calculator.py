# Формула: final = principal * (1 + rate/12) ** (12 * years)
principal = float(input("Сумма вклада (руб): "))
rate_percent = float(input("Годовая ставка (%): "))
years = float(input("Срок (лет): "))

rate = rate_percent / 100.0
final_amount = principal * (1 + rate / 12) ** (12 * years)

print(f"Итоговая сумма: {final_amount:.2f} руб.")