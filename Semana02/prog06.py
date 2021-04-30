def hello_func():
    pass

print(hello_func)
print(hello_func())
#------------------------
def hello_func():
    print('Hello function!!!')

hello_func()
hello_func()
hello_func()
hello_func()
hello_func()
#------------------------
def hello_func(greeting, name = 'Você'):
    return '{}, {} function!!!'.format(greeting, name)

print(hello_func('Calc'))
#------------------------
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Matemática', 'Artes', name = 'João', age = 22)
#------------------------
courses = ('Matemática', 'Artes')
info = {'name': 'João', 'age': 22}

student_info(courses, info)
student_info(*courses, **info)
#------------------------
month_days = [0, 31, 28, 30, 31, 30, 31, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Mês Inválido'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2021))
print(days_in_month(2021, 2))
