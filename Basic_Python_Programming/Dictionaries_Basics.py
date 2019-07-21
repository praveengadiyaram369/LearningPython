################ Dictionaries ####################

# keys can be anything(Map)
employee = {'name': 'praveen', 'age': 22, 'çourses': ['Math', 'Physics', 'Chemistry']}
print(employee)
print(employee['name'])
print(employee.get('çourses'))
print(employee.get('phone','Not found'))

employee['name'] = 'praveen gadiyaram'
employee['age'] = '23'
print(employee)

employee.update({'name': 'sai praveen gadiyaram', 'phone': '7780126057'})
print(employee)

age = employee.pop('age')
print(employee)
print(age)
print(len(employee))

print(employee.items())
for key in employee.items():
    print(key)

for key, value in employee.items():
    print(key, value)