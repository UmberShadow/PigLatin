#CJ Malson
#March 6th, 2021
#Intro to Python Programming
#Professor Wright

#I don't understand pig latin at all. What is this??

#Program requests a word (in lowercase letters) as input and translates the word into Pig Latin.
#If the word begins with a group of consonants, move them to the end of the word and add "ay". For instance, "chip" becomes "ipchay".
#If the word begins with a vowel, add "way" to the end of the word. For instance, "else" becomes "elseway".


#Ask the user to kindly insert a word to translate to Pig.
word = input("Enter word to translate: ")

#vowel and consonant letters
vowel = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


#when the first letter of a word is a vowel, add "way" to the end.
if word[0] in vowel:
    print(word + "way")
elif word[0] and word[1] in consonant:
    print(word[2:] + word[0:2] + "ay")
else:
    print(word[1:] + word[0] + 'ay')
