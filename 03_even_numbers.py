print("Чётные числа 1..20 (for):")
for n in range(1, 21):
    if n % 2 == 0:
        print(n, end=" ")
print()

print("Чётные числа 1..20 (while):")
n = 1
while n <= 20:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()