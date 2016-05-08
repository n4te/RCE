def get_serial_key():
    key         = 'Messing_in_bytes'
    cypher_text = [0x1F, 0x2C, 0x37, 0x36, 0x3B, 0x3D, 0x28, 0x19, 0x3D, 0x26, 0x1A, 0x31, 0x2D, 0x3B, 0x37, 0x3E]
    serial_key = ''.join([chr(cypher_text[i] ^ ord(value)) for i, value in enumerate(key)])
    print('[+] Serial key: {}'.format(serial_key))

if __name__ == '__main__':
    get_serial_key()
