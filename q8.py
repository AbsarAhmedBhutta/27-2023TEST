# In Excel the column is labelled with alphabets A, B, C and so on. After Z the next column
# is assigned AA, AB, AC, …., ZY, ZZ, AAA, AAB and so on.
#
# Write a function named as solution which takes an integer as
# argument and returns its corresponding column label.


def solution(n):
    result = []
    while n > 0:
        # Map the current number to its corresponding letter
        remainder = (n - 1) % 26
        result.append(chr(65 + remainder))
        # Update the number to the next digit
        n = (n - 1) // 26
    # Reverse the list of letters to get the final result
    return ''.join(reversed(result))


n = 26

# Here's how the function works:
#
# We start by dividing the input number by 26 and finding the remainder. This remainder corresponds to the last
# letter in the Excel column label. We then subtract 1 from the input number (since Excel column labels start with A,
# not 0) and divide by 26 again to get the next digit in the column label. We repeat steps 1 and 2 until the input
# number reaches 0. We convert each digit to its corresponding letter (using ASCII code) and append it to a list. We
# reverse the list of letters to get the final result.
