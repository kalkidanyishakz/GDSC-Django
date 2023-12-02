word=input('Please enter the word to check: ')
word_len=len(word)
reverse=''
for i in range(word_len-1, -1, -1 ):
    reverse+=word[i]
        
if word==reverse:
    print(f'The word {word} is a palindrom.')
else:
    print(f'The word {word} is not a palindrom,\nbecause {reverse} is not equal to {word}')
