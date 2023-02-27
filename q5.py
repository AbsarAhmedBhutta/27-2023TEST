# You are a advance cryptographers and you have to write a code for it.
# In the code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a],
# while every other character (including uppercase letters and punctuation) is left untouched.
# That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc. For instance,
# the word ""vmxibkgrlm"", when decoded, would become ""encryption"".
#
# # Write a function called solution which takes in a string and returns the deciphered string.


def solution(s):
    result = ""
    for c in s:
        if c.islower():
            result += chr(ord('z') - ord(c) + ord('a'))
        else:
            result += c
    return result


s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
print(solution(s))
