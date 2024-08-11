import codecs

# take hexadecimal string
hex_str = '0x68656c6c6f'[2:]

# convert hex string to ASCII string
binary_str = codecs.decode(hex_str, 'hex')
ascii_str = str(binary_str,'utf-8')

# printing ASCII string
print('ASCII String:', ascii_str)