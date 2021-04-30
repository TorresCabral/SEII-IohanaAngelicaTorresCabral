f = open('Semana02/prog09/teste.txt', 'r')

print(f.name)
print(f.mode)
f.close()
#------------------------
with open('Semana02/prog09/teste.txt', 'r') as f:
    #f_contents = f.readlines()
    #f_contents = f.read()
    #f_contents = f.readline()

    '''
    for line in f:
        print(line, end = '')
    '''

    '''
    while len(f_contents) > 0:
        print(f_contents, end = '')
        f_contents = f.read(size_to_read)
    '''
print(f.closed)
#------------------------
with open('Semana02/prog09/teste.txt', 'w') as f:
    f.write('Teste')
    f.seek(0)
    f.write('D')
#------------------------
with open('Semana02/prog09/teste.txt', 'r') as rf:
    with open('Semana02/prog09/teste_copia.txt', 'w') as wf:
        '''
        for line in rf:
            wf.write(line)
        '''
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
