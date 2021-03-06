cypher_text = [
    0xAF, 0xAA, 0xAD, 0xEB, 0xAE, 0xAA, 0xEC, 0xA4, 0xBA, 0xAF, 0xAE, 0xAA, 0x8A, 0xC0, 0xA7, 0xB0,
    0xBC, 0x9A, 0xBA, 0xA5, 0xA5, 0xBA, 0xAF, 0xB8, 0x9D, 0xB8, 0xF9, 0xAE, 0x9D, 0xAB, 0xB4, 0xBC,
    0xB6, 0xB3, 0x90, 0x9A, 0xA8
    ]

ROL = lambda val, r_bits, max_bits:\
        (val << r_bits%max_bits) & (2**max_bits-1) |\
        ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
                 
def get_mail():
    _sum = 0
    result = []
    for value in cypher_text[::-1]:
        addvalue = ROL(1, _sum & 3, 32) + 1
        newvalue = value
        _sum += newvalue
        newvalue -= addvalue
        newvalue &= 0xFF
        newvalue ^= 0xC7
        result.append(chr(newvalue))
    return ''.join(result)

mail = get_mail()
print mail
