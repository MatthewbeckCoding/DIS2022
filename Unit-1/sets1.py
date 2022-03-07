a = set('abcdddffaaefg')
print(type(a), a)

sentence = "Hello to the to  my Hello world the"

words = sentence.split()
set_words = set(words)
print(set_words)

#or

set_words = set(sentence.split())

if "Hello" in set_words:
    print("found")
else:
    print("not found")

student_names = {()}
print(type(student_names))