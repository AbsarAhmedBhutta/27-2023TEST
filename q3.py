# Write a function named as solution which a string as argument and
# returns the number of letters and digits (list).
def solution(str_string):
    letter_count = 0
    digit_count = 0
    for char in str_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
    return [letter_count, digit_count]


