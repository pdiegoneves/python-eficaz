# Prefira enumerate em vez de range

cars = ['bmw', 'audi', 'toyota', 'subaru']

for i in range(len(cars)):
    print(i + 1, cars[i])

print("---")

for i, car in enumerate(cars, 1):
    print(i, car)