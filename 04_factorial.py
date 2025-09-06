def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определён для n >= 0")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

n = int(input("Введите целое n (>=0): "))
print(f"{n}! =", factorial(n))