def solution(number):
    a = 0
    if number > 0:
        number -= 1
        while number > 0:
            if number % 3 == 0 or number % 5 == 0:
                a += number
                number -= 1
            else:
                number -= 1
    else:
        return 0
    return a
