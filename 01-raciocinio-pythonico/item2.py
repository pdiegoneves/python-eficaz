# Siga o Guia de Estilo PEP 8
# https://peps.python.org/pep-0008/

def long_function_name():
    pass

long_variable_name = "value"

class LongClassName:
    def __init__(self):
        _protected_atribute = 1
        __private_atribute = 2

    def long_instance_method_name(self):
        pass

    def long_class_method_name(cls):
        pass

CONSTANT_NAME = "value"

a = 1
b = 2

if a is not b:
    pass

list = []

if list:
    # em vez de
    if len(list) == 0:
        pass


# Os módulos importados devem estar em seções na seguinte ordem:
# módulos da biblioteca nativa, módulos de terceiros, seus próprios módulos.
# Os módulos em cada subseção devem ser importados em ordem alfabética.