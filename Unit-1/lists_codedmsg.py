coded_msg = input("enter coded message")

clean_msg = ""

words = coded_msg.split()

for word in words:
    if word[0].capitalize():
        clean_msg