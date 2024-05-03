# Create a script that replaces all occurrences of a given word in a sentence with another word provided by the user.

sentence = input("type in your sentence here: ")
oldWord = input("What word do you want to replace? ")
newWord = input("What is the new word? ")
print(sentence.replace(oldWord, newWord))