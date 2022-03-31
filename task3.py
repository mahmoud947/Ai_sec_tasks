_grade_dec = {
    (90, 100): "A",
    (80, 89): "B",
    (70, 79): "C",
    (60, 69): "D",
    (0, 59): "F",
}


def get_grade(grade: int):
    for (min, max) in _grade_dec:
        if(min < grade and max > grade):
            return _grade_dec[(min, max)]


def fizz_buzz():
    for i in range(100):
        if (i % 3 == 0):
            print("FIZZ")
            continue
        elif (i % 5 == 0):
            print("BUZZ")
            continue
        elif (i % 3 == 0) and (i % 5 == 0):
            continue
            print(" FIZZ BUZZ")
        print(i)


sub = int(input("Enter marks obtained in subject : "))
print(get_grade(sub))
fizz_buzz()
