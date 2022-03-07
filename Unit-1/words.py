word = input('enter a word: ').strip()

if len(word) % 2==0:
    print(word[0:len(word) // 2])
    print(word[len(word) //2 :])
else:
    print(word[len(word) //2])