import random
import string
import codecs

def generate_key_with_length(length):
    return ''.join(random.choices(string.printable, k=length))

def cipher(text,key):
    text = bytearray(bytes(text,'ascii'))
    key = bytearray(bytes(key,'ascii'))
    ciphered_text = bytearray(b'')
    for char, keychar in zip(text,key):
        ciphered_text.append(char ^ keychar)
    return ciphered_text.decode('ascii')

def unescaped_input(string):
    return string.encode('ascii').decode('unicode-escape')

option = 1

while 1 <= option <= 2:
    print("Vernam Cipher:\n1) Cipher\n2) Decipher\nOther) Exit")
    option = int(input())

    if option == 1:
        text = input("Text to cipher: ").strip()
        key = generate_key_with_length(len(text))
        ciphered_text = cipher(text,key).encode('ascii')
        key = key.encode('ascii')
        print("Ciphered text:\n{}".format(ciphered_text))
        print("Key:\n{}".format(key))
        input("Press Enter to continue:")
    elif option == 2:
        text = input("Text to decipher:\n"); text = unescaped_input(text)
        key = input("Key: "); key = unescaped_input(key)
        deciphered_text = cipher(text,key)
        print(deciphered_text)
        input("Press Enter to continue:")