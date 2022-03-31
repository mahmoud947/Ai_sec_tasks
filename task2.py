from datetime import datetime
import string

phrase = "Pony stash token"

print(phrase[5:10])
print(phrase[-16:-11])
print(phrase[::-1])
print(phrase[0::3])


def get_full_name_formated(full_name_Input: str):
    arr_full_name = full_name_Input.split()
    full_name = ""
    try:
        first_name = arr_full_name[0].lower()
        last_name = arr_full_name[1].lower()
        full_name = first_name.capitalize()+" "+last_name.capitalize()
        return full_name
    except:
        raise ValueError


def dateFormated(time_str: str):
    time = datetime.strptime(time_str, "%d%m%Y").strftime("%d/%m/%Y")
    return str(time)


def get_birth_day_formated(birth_day_input: str):
    birth_day_len = len(str(birth_day_input))
    if birth_day_len != 8:
        raise ValueError
    else:
        return dateFormated(str(birth_day_input))


def form():
    try:
        full_name_Input = input("enter your full name \n")
        full_name = get_full_name_formated(full_name_Input)

        birth_day_input = input(
            "enter your Birthday by an 8-digit like `10031999`\n")
        birth_day = get_birth_day_formated(birth_day_input)

        print(full_name+" was born on "+birth_day)
    except:
        print("error \n please enter your full name like `mahmoud kamal` and enter your Birthday by an 8-digit like `10031999")
        form()


form()
