# Write a program that takes n words from a user and outputs a string that contains all the words separated by a space. n here is the number of words the user would like to input.

num_words = int(input("Enter number of words: "))
sentence = ""

for i in range(num_words):
    sentence += input("")
    if (i + 1 < num_words):
        sentence += " "

print(sentence)
