def decimal_to_binary(number):
    """Converting The Give Decimal to Binary Without In-Built Function"""
    a = []
    b = []
    while number > 0:
        digit = number % 2
        a.append(digit)
        number = number // 2

    for i in range(len(a)):
        i -= 1
        b.append(a[i])
    print("binary of given number:", number, "is", b)
    return number, b


if __name__ == '__main__':
    decimal_to_binary(11)
