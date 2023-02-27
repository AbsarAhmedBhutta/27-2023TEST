# A website requires a password to register a user. Write a function solution which inputs a password (string) and
# validate it on following rules.
# Password should contain at least one letter from [a-z]
# Password should contain at least one letter from [A-Z]
# Password should contain at least one character from [@,$,#]
# Password should contain at least one digit from [0-9]
# Password should have a minimum length of 6.
#
# The function will return True in case of valid password and False in case of in-valid password.

def solution(password):
    # Check if the password satisfies all the rules
    if len(password) >= 6 and any(char.islower() for char in password) \
            and any(char.isupper() for char in password) \
            and any(char in '@$#' for char in password) \
            and any(char.isdigit() for char in password):
        # If it satisfies all the rules, return True
        return True
    else:
        # Otherwise, return False
        return False
