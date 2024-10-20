

def decimal_to_binary(decimal, precision=10):
    integer_part = int(decimal)
    fractional_part = decimal - integer_part
    

    binary_integer_part = bin(integer_part).replace("0b", "")
    

    binary_fractional_part = []
    while fractional_part and len(binary_fractional_part) < precision:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional_part.append(str(bit))
        fractional_part -= bit
    
    binary_fractional_str = "".join(binary_fractional_part)
    
    return f"{binary_integer_part}.{binary_fractional_str}"

decimal_value = 0.02
precision = 32
binary_value = decimal_to_binary(decimal_value, precision)
print(binary_value)