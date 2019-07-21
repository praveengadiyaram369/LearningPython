########### Loops ############

nums = [1, 2, 3, 4]
for num in nums:
    if num == 3:
        print('Found it!')
        continue;
    print(num)


for num in nums:
    for letter in 'ABC':
        print(num, letter)


for i in range(1, 11):
    print(i)

i = 15;
while i <= 20:
    print(i)
    i += 1;

## while True:  ==> Infinite loop

