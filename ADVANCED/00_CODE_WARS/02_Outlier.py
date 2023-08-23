# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python


def find_outlier(integers):
    odds = []
    evens = []
    for number in integers:
        if number % 2:
            odds.append(number)
        else:
            evens.append(number)
    if len(odds) == 1:
        return odds[0]
    elif len(evens) == 1:
        return evens[0]