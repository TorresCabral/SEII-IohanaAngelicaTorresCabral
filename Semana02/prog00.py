print('Hello World')
#---------------------------
message1 = "Iohana's World"
print(message1)
#---------------------------
message2 = """Antes tarde 
do que nunca"""
print(message2)
#---------------------------
print(len(message2))
#---------------------------
print(message1[:6])
#---------------------------
print(message1.lower())
#---------------------------
print(message2.upper())
#---------------------------
print(message2.count('a'))
#---------------------------
print(message1.find('Iohana'))
#---------------------------
message3 = message1.replace('World', 'Program')
print(message3)
#---------------------------
greeting = 'Hello'
name = 'Éder'
message4 = greeting + ', ' + name + '. Welcome!'
print(message4)
#---------------------------
message5 = '{}, {}. Welcome!'.format(greeting, name)
print(message5)
#---------------------------
message6 = f'{greeting}, {name.upper()}. Welcome!'
print(message6)
#---------------------------
print(dir(name))
#---------------------------
print(help(str.lower))