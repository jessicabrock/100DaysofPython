# def validate_isbn(isbn_num):
#     """
#         ISBN is 13-characters: 978-0262038003
#         The last character is a checksum
#         Take the first twelve characters and apply the agorithm:
#         9 + 3*7 + 8 + 3*0 + 2 + 3*6 + 2 + 3*0 + 3 + 3*8 + 0 + 3*0
#         sum = 87
#         Divide by 10: 87 / 10 = 8 with a remainder of 7
#         10 -7 = 3, will return True. Any other number will be False

#         https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation
#     """
#     last_char = int(isbn_num[-1])
#     # ignore non-digits and the last character
#     isbn_num = re.sub("[^0-9]", "", isbn_num[:-1])
#     running_total = 0
#     # get tuple of next two chars
#     for char1, char2 in zip(isbn_num[0::2], isbn_num[1::2]):
#         running_total += int(char1) + (3 * int(char2))

#     result = 10 - (running_total % 10)

#     if result == last_char:
#         return True
#     else:
#         return False

# print(validate_isbn("9n 78-0262038003"))

def validate_isbn(input_isbn):
    if not input_isbn:
        return False

    check_digit = input_isbn[-1]
    running_total = 0
    is_valid = False
    isbn = [int(x) for x in input_isbn if x.isdigit()]

    if len(isbn) != 13:
        return False
    else:
        for index, digit in enumerate(isbn[:12]):
            if index % 2:               # odd index 3*digit, even index 1*digit
                running_total += 3 * int(digit)
            else:
                running_total += int(digit)

        user_check_digit = 10 - (running_total % 10)
        if user_check_digit == 10:
            user_check_digit = 0

        if user_check_digit == int(check_digit):
            is_valid = True

        return is_valid


def main():
    get_isbn = input("Enter ISBN: ").strip()
    validate_isbn(get_isbn)


if __name__ == '__main__':
    main()
