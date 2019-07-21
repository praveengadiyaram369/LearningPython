########## List  ############
subjects = ['Maths', 'Physics', 'Chemistry']
print(subjects)
print(len(subjects))
print(subjects[-3])
print(subjects[:5])
print(subjects[1:])

subjects.append('Biology')
print(subjects)
subjects.insert(2, 'English')
print(subjects)

optional_subjects = ['Sanskrit', 'Telugu']
subjects_2=subjects
print(optional_subjects)
subjects_2.insert(0, optional_subjects)
print(subjects_2)
print(subjects_2[0])

# Both subjects_3, subjects share same objects, if you change subjects_3, then subjects also gets changed.
subjects_3=subjects
subjects_3.extend(optional_subjects)
print(subjects_3)

subjects = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Sanskrit', 'Telugu']
subjects.remove('Biology')
print(subjects)

popped_subject = subjects.pop()
print(popped_subject)
print(subjects)

subjects.reverse()
print(subjects)

# default sorting order is always Ascending order
subjects.sort()
print(subjects)

#For descending order, we need to make reverse=true
subjects.sort(reverse=True)
print(subjects)


subjects = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Sanskrit', 'Telugu']
sorted_subjects=sorted(subjects)
print(sorted_subjects)


A = [1, 2, 3, 4, 5, 7]
print(A)
print(min(A))
print(max(A))
print(sum(A))

for course in subjects:
    print(course)

for index, course in enumerate(subjects):
    print(index, course)

subjects_joined = ', '.join(subjects)
print(subjects_joined)
subjects_splitted = subjects_joined.split(', ')
print(subjects_splitted)


###### Empty Lists #####
empty_List=[]
empty_List=list()
empty_List.append('first_element')
print(empty_List)

