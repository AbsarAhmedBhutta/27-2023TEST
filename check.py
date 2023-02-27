def solution(x):
    count = 0
    for number in x:
        if number % 2 == 0:
            count += 1
    return count


x = [1, 4, 2, 3, 13, 4, 1]
solution(x)