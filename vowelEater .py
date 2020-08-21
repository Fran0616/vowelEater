#program eat vowels. it utilize the continue statment to skip over letters that are vowels
# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = input("Enter a word: ")
#capitilize the whole word
userWord = userWord.upper()


#for loop with if-elif, and continue statment to eat the vowels
for letter in userWord:
     if letter == 'A':
         continue
     elif letter == 'E':
         continue
     elif letter == 'I':
         continue
     elif letter == 'O':
         continue
     elif letter == 'U':
         continue
     print (letter)
    
