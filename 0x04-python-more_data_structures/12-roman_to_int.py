#!/usr/bin/python3
def roman_to_int(roman_str):
    if roman_str is None or type(roman_str) != str or roman_str == '':
        return 0
    x, y = 0, 2
    twos = []
    for i in range(0, (len(roman_str) // 2) + 1):
        twos.append(roman_str.upper()[x:y])
        x, y = x + 2, y + 2
    res = 0
    for each_two in twos:
        res += evaluate(each_two)
    return res


def evaluate(string):
    value, value1 = 0, check_subtr(string)
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    if value1 is None:
        for numeral in string:
            value += rom_dict[numeral]
        return value
    else:
        return value1


def check_subtr(string):
    rom_subtr = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    for k, v in rom_subtr.items():
        if k == string:
            return v
    return None
