#######  Tuples #######

tuple_1 = ('A', 'AB', 'ABCD', 'EUIHVEAO')
print(tuple_1)

tuple_2 = tuple_1
print(tuple_2)

####### Empty Tuple #########
empty_tuple = tuple()
empty_tuple = ()

#tuple_1[0] = 'WUI'
#print(tuple_1)
#tuple_2[0] = 'WUI'
#print(tuple_2)

######### Set ######

subject_set = {'Maths', 'Physics', 'Chemistry', 'Biology', 'Sanskrit', 'Telugu', 'Maths'}
course_set = {'IT', 'Data Science', 'Big Data', 'Maths'}
print(subject_set)
print(course_set)

print(subject_set.intersection(course_set))
print(subject_set.union(course_set))
print(subject_set.difference(course_set))
print(course_set.difference(subject_set))


###### Empty Set #####
empty_Set={}
empty_Set=set()
