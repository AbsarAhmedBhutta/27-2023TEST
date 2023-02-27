# Write the function named as solution for the following sample input and output.
#
# Example 1
# In: solution(["P>E","E>R","R>U"])
# Out: PERU

def solution(l):
    mapping = {}
    for s in l:
        a, b = s.split('>')
        mapping[a] = b
    start = set(mapping.keys()) - set(mapping.values())
    result = ''
    while start:
        current = start.pop()
        result += current
        if current in mapping:
            start.add(mapping[current])

    return result
