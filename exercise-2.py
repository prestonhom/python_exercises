# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = input('Please enter a word or phrase: ')
length = len(phrase)
sentence = (f'The {phrase} you entered is {length} characters long')
print(sentence)
while phrase != 'quit':
    phrase = input('Please enter a word or phrase: ')
    print(sentence)
    if phrase == 'quit':
        break
