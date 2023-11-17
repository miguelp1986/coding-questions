def get_confusable_numbers(BIDDERS: list) -> list:
    """
    return a list of numbers within bidders that are confusable
    confusable numbers are numbers that can be inverted and still be
    a valid number. i.e. 68 -> 89
    O(n*c) time | O(c) space where c are the digits from a list of numbers n
    TODO: you didn't catch the edge case if we have '111' or '666'.
    do we consider these confusable? I don't think so.
    """
    CONFUSABLE_NUMBERS = []
    for num in BIDDERS:
        confusable_number = get_confusable_number(num)

        if confusable_number is not None:
            CONFUSABLE_NUMBERS.append((str(num), confusable_number))

    return CONFUSABLE_NUMBERS


def get_confusable_number(number: int) -> str:
    """
    return the confusable number of a number
    return None if not a confusable number
    """
    number_str = str(number)
    confusable_number = ""
    for digit in number_str:
        confusable_digit = get_confusable_digit(digit)
        if confusable_digit is not None:
            confusable_number = confusable_digit + confusable_number
        else:
            return None

    return confusable_number


def get_confusable_digit(digit: str) -> str:
    """
    return a confusable digit of a digit
    return None if not a confusable digit
    """
    if digit == '0':
        return '0'
    elif digit == '1':
        return '1'
    elif digit == '6':
        return '9'
    elif digit == '8':
        return '8'
    elif digit == '9':
        return '6'
    else:
        return None


BIDDERS = [num for num in range(1, 801)]
CONFUSABLE_NUMBERS = get_confusable_numbers(BIDDERS)
print(CONFUSABLE_NUMBERS)
