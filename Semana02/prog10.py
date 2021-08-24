import os

os.chdir('\Users\Torres Cabral\Documents\Sistemas Embarcados 2\Aulas')

print(os.getcwd())
for f in os.listdir():
    print(f)
    print(os.path.splitext(f))
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))
    f_title, f_course, f_num = file_name.split('-')
    print(f_title)
#------------------------
for f in os.listdir():
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, file_ext))
#------------------------
for f in os.listdir():
    f_title = f_title.stip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    print('{}-{}{}'.format(f_num, f_title, file_ext))
    new_name = '{}-{}{}'.format(f_num, f_title, file_ext)
    os.rename(f, new_name)