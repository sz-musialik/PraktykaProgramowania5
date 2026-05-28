"""Number converter module"""


def dec_to_bin(number):
    """Convert decimal number to binary"""
    if not isinstance(number, int):
        raise ValueError("Given number must be of type Integer")

    if number < 0 or number > 100:
        raise ValueError("Given number must be in range [0; 100]")

    return bin(number)[2:]
