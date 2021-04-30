from my_module import find_index, test
import sys
import random
import math
import datetime
import calendar
import os
import antigravity

courses = ['História', 'Geografia', 'Matemática', 'Física']
index = find_index(courses, 'Matemática')

print(index)
print(test)
print(sys.path)
#------------------------
random_course = random.choice(courses)
print(random_course)
#------------------------
rads = math.radians(90)
print(rads)
print(math.sin(rads))
#------------------------
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))
#------------------------
print(os.getcwd())
print(os.__file__)