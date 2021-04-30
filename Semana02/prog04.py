if True:
    print('Condição Verdadeira')

if False:
    print('Condição Falsa')
#------------------------
language = 'Python'

if language == 'Python':
    print('Condição Verdadeira')
#------------------------
'''
É igual a: ==
Não é igual a: !=
É maior que: >
É menor que: <
É maior ou igual a: >=
É menor ou igual a: <=
Identidade de objetos: is
'''
#------------------------
language = 'Java'
if language == 'Python':
    print('A linguagem é Python')
elif language == 'Java':
    print('A linguagem é Java')
else:
    print('A linguagem não reconhecida')
#------------------------
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in == True:
    print('Página do Administrador')
else:
    print('Credenciais não reconhecidas')
#------------------------
'''
and
or
not
'''
#------------------------
logged_in = False
if user == 'Admin' and logged_in == True:
    print('Página do Administrador')
else:
    print('Credenciais não reconhecidas')
#------------------------
if user == 'Admin' or logged_in == True:
    print('Página do Administrador')
else:
    print('Credenciais não reconhecidas')
#------------------------
if not logged_in:
    print('Por favor, faça o login')
else:
    print('Bem vindo')
#------------------------
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))
#------------------------
b = a
print(a == b)
print(a is b)
print(id(a))
print(id(b))
print(id(a) == id(b))
#------------------------
'''
Valores Falsos:
False
None
Zero de qualquer tipo numérico
Qualquer sequência vazia. Por exemplo, '', (), []
Qualquer dicionário vazio. Por exemplo, {}
'''
#------------------------
condition = {}
if condition == False:
    print('Verdadeiro')
else: 
    print('Falso')