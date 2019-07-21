########## Functions ##########

def my_func():
    print('Inside my_func ...')
    return 'got it, Thanks!'

def greeting_func(greeting = 'nerds'):
    print(f'Hello {greeting}, Welcome Back :)!')
    return

print(my_func)
print(my_func())
print(greeting_func('geeks'))
print(greeting_func())

#  *args -- value passing
#   **kwargs -- information passing
def employee_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'physics', 'chemistry']
info = {'name' : 'praveen', 'Age': 22}

employee_info(*courses, **info);
