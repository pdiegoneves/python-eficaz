# Use zip para processar iteradores em paralelo

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)

print("---")

longest_name2 = None
max_letters2 = 0

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name2 = name
        max_letters2 = count

print(longest_name)

# precisa garantir que os iteradores tenham o mesmo tamanho