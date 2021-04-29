student = {'nome': 'João', 'idade': 25, 'cursos': ['Matemática', 'Computação']}
print(student['nome'])
print(student.get('nome'))
print(student.get('telefone', 'Não encontrado'))
#------------------------
student['telefone'] = '349888888'
student['nome'] = 'Maria'
print(student.get('telefone', 'Não encontrado'))
print(student)
#------------------------
student.update({'nome': 'José', 'idade': 24})
del student['telefone']
print(student)
#------------------------
nome = student.pop('nome')
print(student)
print(nome)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
#------------------------
for key, value in student.items():
    print(key, value)