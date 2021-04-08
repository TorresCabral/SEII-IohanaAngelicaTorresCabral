courses = ['História', 'Matemática', 'Física', 'Ciências da Computação']
print(courses)
print(len(courses))
print(courses[3])
print(courses[-1])
print(courses[2:])
#------------------------
courses.append('Artes')
print(courses)
courses.insert(1, 'Português')
print(courses)
#------------------------
courses2 = ['Inglês', 'Educação Física']
courses.insert(0, courses2)
print(courses)
print(courses[0])
#------------------------
courses.extend(courses2)
print(courses)
#------------------------
courses.append(courses2)
print(courses)
#------------------------
courses.remove('Inglês')
popped = courses.pop()
print(popped)
print(courses)
#------------------------
courses.reverse()
print(courses)
#------------------------
courses.pop()
courses.sort()
print(courses)
#------------------------
nums = [1, 2, 3, 9, 8, 5]
nums.sort()
print(nums)
#------------------------
courses.sort(reverse = True)
nums.sort(reverse = True)
print(courses)
print(nums)
#------------------------
sorted_courses = sorted(courses)
sorted_nums = sorted(nums) 
print(sorted_courses)
print(sorted_nums)
#------------------------
print(min(nums))
print(max(nums))
print(sum(nums))
#------------------------
print(courses.index('História'))
print('Sociologia' in courses)
#------------------------
for item in courses:
    print(item)
for index in enumerate(courses):
    print(index)
for index, course in enumerate(courses, start = 2):
    print(index, course)
#------------------------
course_str = ' - '.join(courses)
print(course_str)
#------------------------
new_list = course_str.split(' - ')
print(new_list)
#------------------------
list1 = new_list
list2 = list1
list1[0] = 'Filosofia'
print(list1)
print(list2)
#------------------------
tuple1 = ('Filosofia', 'Matemática', 'História', 'Física', 'Educação Física', 'Ciências da Computação', 'Artes')
tuple2 = tuple1
#tuple[0] = 'Geografia'
print(tuple1)
print(tuple2)
#------------------------
cs_courses = {'Filosofia', 'Física', 'Matemática', 'História', 'Física', 'Educação Física', 'Ciências da Computação', 'Artes'}
ds_courses = {'Filosofia', 'Física', 'Matemática', 'História', 'Engenharia'}
print(cs_courses)
print('Física' in cs_courses)
print(cs_courses.intersection(ds_courses))
print(cs_courses.difference(ds_courses))
print(cs_courses.union(ds_courses))
#------------------------
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
#empty_set = {}
empty_set = set()
#------------------------
#------------------------
#------------------------