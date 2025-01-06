# Escreva funções auxiliares em vez de expressões complexas

full_string = "ABCDEF0"
# full_string = "1ABCDEF0"

print(full_string[:6])
# print(full_string[:6])
# print(full_string[:6])
# print(full_string[:6])
# print(full_string[:6])


full_string2 = "GHIJKL0"
# full_string2 = "1GHIJKL0"
def _get_partial_String(string:str) -> str:
    return string[:6]

print(_get_partial_String(full_string2))
# print(_get_partial_String(full_string2))
# print(_get_partial_String(full_string2))
# print(_get_partial_String(full_string2))
# print(_get_partial_String(full_string2))
