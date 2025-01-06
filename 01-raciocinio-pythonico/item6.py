# Evite usar start, end e stride em uma mesma fatia
# slice = [start:end:stride]

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(a[2::2]) # ['c', 'e', 'g']
print(a[-2::-2]) # ['g', 'e', 'c', 'a']
print(a[-2:2:-2]) # ['g', 'e']
print(a[2:2:-2]) # []

b = a[::2] # ['a', 'c', 'e', 'g']
c = b[1:-1] # ['c', 'e']

print(b)
print(c)

# Se o seu programa por alguma razão não tiver condições de arcar com o uso adicional de memória necessário para esses
# dois passos, experimente o método islice, presente no módulo nativo itertools
# (consulte o Item 46: “Use algoritmos e estruturas de dados nativos”)