# Considere usar expressões geradoras em abrangências muito grandes

value = [len(x) for x in open('./my_file.txt')]
print(value)

it = (len(x) for x in open('./my_file.txt'))
print(next(it))
print(next(it))

print(list(it))