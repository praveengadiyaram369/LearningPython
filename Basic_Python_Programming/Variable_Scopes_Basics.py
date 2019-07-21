''''
          Variable Scopes in Python
LEGB - Local, Enclosing, Global, Built-in
'''
import builtins

## Global Scope
x = 'global x'

def testfunction():
    #global x
    #Local Scope
    x='local x'
    print(x)

#Built-in Scope comes along with python
print(dir(builtins))

testfunction()
print(x)


def Outer():
    x = 'Outer x'
    def Inner():
        nonlocal x
        x = 'Inner x'
        print(x)
    Inner()
    print(x)

Outer()