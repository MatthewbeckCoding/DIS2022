user = "Matthew"
user_attempt = input("enter user")
pw = "Matthew"
pw_attempt = input("enter password")
attempts_remaining = 3

while pw != pw_attempt or user != user_attempt:
    attempts_remaining -= 1
    if attempts_remaining > 0:
        print("incorrect, try again, you have", attempts_remaining,"remaining")
        user_attempt = input("enter user")
        pw_attempt = input("enter password")
    if attempts_remaining == 0:
        print("you have been logged out for 60 miins lol")
print("your in")


 

