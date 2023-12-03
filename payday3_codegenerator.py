import os
keys = ["0","1","2","3","4","5","6","7","8","9"]
options = []

for i in range(len(keys)):
    for j in range(len(keys)):
        for k in range(len(keys)):
            for l in range(len(keys)):
                if not (i == j and i == k and i == l and j == k and j == l and k == l):
                    options.append((f"{i}", f"{j}", f"{k}", f"{l}"))

while True:
    count = 0
    numbers = []
    codes = []
    for i in range(4):
        ordinal = ""
        match i:
            case 0:
                ordinal = "st"
            case 1:
                ordinal = "nd"
            case 2:
                ordinal = "rd"
            case _:
                ordinal = "th"
        number = input(f"Enter {i + 1}{ordinal} digit: ")
        if number == "":
            break
        numbers.append(number)


    for option in options:
        valid = True
        for digit in option:
            if not digit in numbers:
                valid = False
                break
        for number in numbers:
            if not number in option:
                valid = False
                break
        if valid:
            codes.append(option)
    print("\nAll possible code variations")
    for code in codes:
        if count % 4 == 0:
            print(f"-----------------")
        count += 1
        print(f"{count}.\t {' '.join(code)}")
    print(f"-----------------")  
        

    print(f"{count} possible different codes")

    if input("\nDo you wish to continue? (Y/N): ").lower() == "n":
        break
    
    os.system("cls")