

print('Inside Simple Module .....')

num = 1234

def findString(mainarray, searchstring):
    for index, value in enumerate(mainarray):
        if searchstring == value:
            return index

    return -1
