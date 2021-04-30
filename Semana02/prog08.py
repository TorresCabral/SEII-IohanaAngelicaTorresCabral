import os
from datetime import datetime

print(dir(os))
print(os.getcwd())
os.chdir('/Users/Torres Cabral/Documents/GitHub/')
print(os.getcwd())
os.chdir('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral')
print(os.getcwd())
print(os.listdir())
#------------------------
os.makedirs('Semana02/prog08')
os.removedirs('Semana02/prog08')
#os.rename('Semana02', 'Semana2')
print(os.stat('Semana02/prog00.py'))
#------------------------
mod_time = os.stat('Semana02').st_mtime
print(datetime.fromtimestamp(mod_time))
#------------------------
for dirPath, dirNames, fileNames in os.walk('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'):
    print('Pasta atual:', dirPath)
    print('Diretórios:', dirNames)
    print('Arquivos:', fileNames)
    print()
#------------------------
print(os.environ)
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'teste.txt')
print(file_path)
#------------------------
print(os.path.basename('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'))
print(os.path.dirname('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'))
print(os.path.split('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'))
print(os.path.exists('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'))
print(os.path.isdir('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'))
print(os.path.isfile('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral'))
print(os.path.splitext('/Users/Torres Cabral/Documents/GitHub/SEII-IohanaAngelicaTorresCabral/Semana02/prog00.py'))
print(dir(os.path))
