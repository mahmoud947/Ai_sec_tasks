from tokenize import String


def convert_temp(value: int, unit: str):
    converted_temp = 0
    if unit == "F":
        converted_temp = ((value * 9) / 5) + 32
        return converted_temp
    elif unit == "C":
        converted_temp = (value-32) * (5/9)
        return converted_temp


def check_event(num):
    if num % 2 == 0:
        return True
    elif num == 0:
        return True
    else:
        return False


def reverse_string(str_value: str):
    return str_value[::-1]


print(convert_temp(40, "F"))
print(check_event(6))
print(reverse_string("mahmoud"))
