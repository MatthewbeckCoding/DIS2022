words = {}

sentence = input("enter snetence")
words_list = sentence.split()
for word in words:
    word = word.lower()
    if len(word) > 0:
        if word in words_list:
            words_list[word] += 1
        else:
            words_list[word] = 1

for k,v in words_list.items():
    print(k, v)