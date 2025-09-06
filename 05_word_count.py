words = ["яблоко", "банан", "вишня", "яблоко", "апельсин", "банан"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

for w, c in counts.items():
    print(f"{w}: {c}")