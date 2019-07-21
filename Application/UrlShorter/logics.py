import string

# all domain characters [a-zA-Z0-9] will use for creating  total: 62 char
domain_characters = string.ascii_letters + string.digits

# We have to represent base 10 , url id to  ase 62 url_code
# domain_characters = '0123456789ABCDEF'


def base_converter_from_base10(data: int, to_base=len(domain_characters)):
    '''
    Generic function to convert base 10 data to given base
    :param data: integer in base 10
    :param to_base: convert data to given base
    :return: data in new base
    '''

    if len(domain_characters) != to_base:
        raise ValueError('Make sure that domain characters are align with domain characters')

    result = str()
    # division_result = new_base
    # remainder = None
    while True:
        division_result = int(data / to_base)
        remainder = data - (to_base * division_result)
        data = division_result
        result += domain_characters[remainder]

        if data < to_base:
            if data != 0:
                result += domain_characters[data]
            break

    return result[::-1]


def base_converter_to_base10(data: str, from_base=len(domain_characters)):
    '''
    Convert data to base 10
    :param data: string data in in given ase
    :param from_base: base of provided data
    :return: int
    '''
    result = 0
    ini_power = 0
    for i in range(len(data) - 1, -1, -1):
        effective_value = domain_characters.find(data[i])  # for hex effective value of A is 10 and B is 11
        result += effective_value * (from_base ** ini_power)
        ini_power += 1

    return result


