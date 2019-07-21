################# if elif else ##############

language = 'SQL'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('language not found')

#and
#or
#not

language = 'SQL'
in_use = True
if language == 'Python' and in_use:
    print('Language is Python and its in use :)')
else:
    print('language not found or not in use')


logged_in = False
if not logged_in:
    print('Please log in')
else:
    print('Welcome Broh!')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

print(id(a))
print(id(b))

b = a
print(a == b)
print(a is b)
print(id(a))
print(id(b))


#False, None, 0, empty List, Tuple, Set, Dictionary  ex: [], (), {}