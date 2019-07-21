my_message="Hello Geek's world"
print(my_message)
#length of the string
print(len(my_message))
#print string from start index to end index
print(my_message[:len(my_message)-1])
# convert string to lowercase
print(my_message.lower())
# returns count od occurence of given letter or word
print(my_message.count('l'))
# returns the index of the given letter
print(my_message.find('l'))

#returns a new string after replacing the given words respectively
my_message_update_1=my_message.replace('Geek','Peek')
print(my_message_update_1)


greeting='Hello'
name='Praveen'
# simple string concatenation
final_greeting=greeting+' '+name
print(final_greeting)
# string formatting with place holder {}
place_holder_greeting='{}, {} Welcome Back:)!'.format(greeting,name)
print(place_holder_greeting)
# string formattings with fStrings in python 3.6
fString_greeting=f'{greeting}, {name} Welcome Back!'
print(fString_greeting)

# returns all the methods and functions for the data types given
print(dir(name))
# returns all method declarations for the string
print(help(str))