def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in s:
        if i.isdigit():
            if int(i)==0:
                return False
            else:
                break
    if len(s) > 6:
        return False
    elif len(s) < 2:
        return False
    elif str.isdigit(s[0:1]):
        return False
    elif not str.isalnum(s):
        return False
    else:
        return True


main()