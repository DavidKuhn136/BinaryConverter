# convert to and from binary

def convert_to(txt_convert):
    converted_binary = ' '.join(format(ord(c), 'b') for c in txt_convert)
    return converted_binary

def convert_from(bin_convert):
    binary_values = bin_convert.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

print(convert_to("hello"))
print(convert_from("1101000 1100101 1101100 1101100 1101111"))
