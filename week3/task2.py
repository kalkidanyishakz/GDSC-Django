letter=input('Please enter a pattern to be printed: ')

if len(letter)>1:
    print('The length of the character should be 1')
elif letter in ['a', 'e', 'i', 'o', 'u']:
    print('Vowels are not allowed in the input')
else:
    for i in range(1, 10, 2):
        print(letter*i)
    
