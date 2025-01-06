# Python Eficaz

Acompanhamento do Livro Python Eficaz

1. Raciocínio pythônico
   1. Saiba qual versão de Python está em uso
   2. Siga o Guia de Estilo PEP 8
   3. Saiba as diferenças entre bytes, str e unicode
   4. Escreva funções auxiliares em vez de expressões complexas
   5. Saiba como fatiar sequências
   6. Evite usar start, end e stride em uma mesma fatia
   7. Use abrangências de lista em vez de map e filter
   8. Evite mais de duas expressões em abrangências de lista
   9. Considere usar expressões geradoras em abrangências muito grandes
   10. Prefira enumerate em vez de range
   11. Use zip para processar iteradores em paralelo
   12. Evite usar blocos else depois de laços for e while
   13. Use todo o potencial dos blocos try/except/else/finally
2. Funções
   14. Prefira exceções em vez de devolver None
   15. Saiba como closures interagem com os escopos das variáveis
   16. Prefira geradores em vez de retornar listas
   17. Seja conservador quando iterar sobre argumentos
   18. Reduza a poluição visual com argumentos opcionais
   19. Implemente comportamento opcional usando palavras-chave como argumentos
   20. Use None e docstrings para especificar argumentos default dinâmicos e específicos
   21. Garanta a legibilidade com argumentos por palavras-chave
3. Classes e herança
   Item 22: Prefira classes auxiliares em vez de administrar registros complexos
   com dicionários e tuplas
   Item 23: Aceite funções para interfaces simples em vez de classes
   Item 24: Use o polimorfismo de @classmethod para construir objetos
   genericamente
   Item 25: Inicialize classes ancestrais com super
   Item 26: Use heranças múltiplas apenas para classes utilitárias mix-in
   Item 27: Prefira atributos públicos em vez de privativos
   Item 28: Herde da classe collections.abc para obter tipos de contêiner
   personalizados
   Capítulo 4 ■ Metaclasses e atributos
   Item 29: Use atributos comuns em vez dos métodos get e set
   Item 30: Considere usar @property em vez de refatorar atributos
   Item 31: Use descritores para implementar métodos reutilizáveis de @property
   Item 32: Use __getattr__, __getattribute__ e __setattr__ para atributos
   preguiçosos
   Item 33: Valide subclasses com metaclasses
   Item 34: Registre a existência de uma classe com metaclasses
   Item 35: Crie anotações de atributos de classe com metaclasses
   Capítulo 5 ■ Simultaneidade e paralelismo
   Item 36: Use subprocess para gerenciar processos-filho
   Item 37: Use threads para bloquear I/O e evitar paralelismo
   Item 38: Use Lock para evitar que as threads iniciem condições de corrida nos
   dados
   Item 39: Use Queue para coordenar o trabalho entre as threads
   Item 40: Considere usar corrotinas para rodar muitas funções simultaneamente
   Item 41: Considere usar concurrent.futures para obter paralelismo real

Capítulo 6 ■ Módulos nativos
Item 42: Defina decoradores de função com functools.wraps
Item 43: Considere os comandos contextlib e with para um comportamento
reutilizável de try/finally
Item 44: Aumente a confiabilidade de pickle com copyreg
Item 45: Use datetime em vez de time para relógios locais
Item 46: Use algoritmos e estruturas de dados nativos
Item 47: Use decimal quando a precisão for de importância vital
Item 48: Saiba onde encontrar os módulos desenvolvidos pela comunidade
Capítulo 7 ■ Colaboração
Item 49: Escreva docstrings para toda e qualquer função, classe e módulo
Item 50: Use pacotes para organizar módulos e criar APIs estáveis
Item 51: Defina uma Exception-raiz para isolar chamadores e APIs
Item 52: Saiba como romper dependências circulares
Item 53: Use ambientes virtuais para criar dependências isoladas e reprodutíveis
Capítulo 8 ■ Produção
Item 54: Crie código com escopo no módulo para configurar os ambientes de
implementação
Item 55: Use strings com a função repr para depuração
Item 56: Teste absolutamente tudo com unittest
Item 57: Prefira usar depuradores interativos como o pdb
Item 58: Meça os perfis de desempenho antes de otimizar o código
Item 59: Use tracemalloc para entender o uso e os vazamentos de memória
