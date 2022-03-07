english = input("enter a sentence")
words = english.split()
piglatin = ""
for word in words:
    if len(word) == 1:
        latin_word = word + "ay"
    else:
        latin_word = word[1:] + word[0] + "ay"
    piglatin = piglatin + latin_word + " "
print(piglatin.upper())