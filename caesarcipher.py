alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def cipher(text,key):
    new_text = ""
    for index,letter in enumerate(text):
        offset = key[index%len(key)]
        try:
            position = alphabet.index(letter.upper())
            new_position = (position+offset)%len(alphabet)
            new_text+=alphabet[new_position]
        except:
            new_text+=letter
    return new_text

def invert_key(key):
    return [0-x for x in key]

def decipher(text,key):
    key = invert_key(key)
    return cipher(text,key)

def key_word_to_list(key):
    return [alphabet.index(x.upper()) for x in key]

option = 1

while 1 <= option <= 2:
    print("Caesar Cipher:\n1) Cipher\n2) Decipher\nOther) Exit")
    option = int(input())

    if option == 1:
        text = input("Text to cipher:\n").strip()
        key = input("Key: ").strip(); key = key_word_to_list(key)
        ciphered_text = cipher(text,key)
        print(ciphered_text)
        input("Press Enter to continue:")
    elif option == 2:
        text = input("Text to decipher:\n").strip()
        key = input("Key: ").strip(); key = key_word_to_list(key);
        deciphered_text = decipher(text,key)
        print(deciphered_text)
        input("Press Enter to continue:")

