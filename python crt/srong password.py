password=input("enter your password :")
letter = ''
digit = ''
specialchar = ''
for ch in password:
    if ch.islower():
        letter = True
    elif ch.isdigit():
        digit = True
    elif not ch.isalnum():
        special = True

if letter and digit and special:
    print("It is a valid password.")
else:
    print("It is an invalid password.")
