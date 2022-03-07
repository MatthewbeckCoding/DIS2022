# Task
# Jacob has been passing notes in class without a problem until his teacher intercepted one today.
# In order to prevent future embarrassment, he wants a way to encode his notes so his teacher cannot read them.
# Help him by writing a program that encrypts a string by switching every letter with alphabetical position i
# with the letter with alphabetical position 26-i. For example the letter 'm' is letter 12, so it becomes 26-12 = 14,
# letter 14 which is 'o'. Note counting begins at zero. Can you suggest why?

msg = "My secret message"
encrypted_msg = ""

for letter in msg.lower():
    position = ord(letter)
    if letter.isalpha():
        position = ord(letter) - 97
        # print(position)
        position = 122 - position
    letter = chr(position)
    encrypted_msg = encrypted_msg + letter
print(encrypted_msg)