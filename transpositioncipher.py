import random
import itertools

def divisors_of_a_number(n):
    divisors = itertools.filterfalse(lambda x: n%x, range(3,n))
    divisors = list(divisors)
    try:
        rows = random.choice(divisors)
        columns = n//rows
    except ZeroDivisionError:
        pass
    return [rows,columns]

def matrix_from_string(text,rows,columns):
    matrix = []
    for i in range(rows):
        j = i*columns
        matrix.append(text[j:j+columns])
    return matrix

def transpose_matrix(matrix):
    changed_matrix = []
    rows, columns = len(matrix), len(matrix[0])
    for i in range(columns):
        item = []
        for j in range(rows):
            item.append(matrix[j][i])
        changed_matrix.append(item)
    return changed_matrix

def random_order(columns):
    order = list(range(columns))
    random.shuffle(order)
    return order

def apply_order_to_matrix(matrix,order):
    reordered_matrix = list(matrix)
    for i in range(len(matrix)):
        reordered_matrix[i] = matrix[order[i]]
    return reordered_matrix

def matrix_to_string(matrix):
    output = ""
    for i in range(len(matrix)):
        for j in matrix[i]:
            output+=j
        output+=" "
    return output

def cipher(text):
    text = text.strip().replace(" ","").upper()
    text = list(text)
    rows, columns = 0,0
    try:
        rows, columns = divisors_of_a_number(len(text))
    except: # si el numero no tiene divisores -es primo- metele un espacio para que sea par
        text+=" "
        rows, columns = divisors_of_a_number(len(text))

    matrix = []
    matrix = matrix_from_string(text, rows, columns)
    matrix = transpose_matrix(matrix)
    order =  random_order(columns)
    matrix = apply_order_to_matrix(matrix, order)

    order_string = "".join([str(n) for n in order])
    text_cifrado = matrix_to_string(matrix).replace("  ", " ")

    return [text_cifrado,order_string]

def ciphered_string_to_matrix(s):
    words = s.strip().split(' ')
    for i in range(len(words)):
        words[i] = list(words[i])
    return words

def invert_order(order):
    inverted_order = []
    for i in range(len(order)):
        inverted_order.append(order.index(i))
    return inverted_order

def normalize_matrix(matrix): # hay que checkear si todas las 'palabras' tienen el mismo largo
    largos = [len(x) for x in matrix]
    largo_minimo, largo_maximo = min(largos), max(largos)
    if largo_minimo != largo_maximo:
        i = largos.index(largo_minimo)
        matrix[i].append(' ')
    return matrix

def decipher(text,order):
    matrix = ciphered_string_to_matrix(text)
    matrix = normalize_matrix(matrix)
    order = invert_order(order)
    matrix = apply_order_to_matrix(matrix, order)
    matrix = transpose_matrix(matrix)
    text_decifrado = matrix_to_string(matrix).replace(" ","")
    return text_decifrado

option = 1

while 1 <= option <= 2:
    print("Transposition Cipher:\n1) Cipher\n2) Decipher\nOther) Exit")
    option = int(input())

    if option == 1:
        text = input("Text to cipher:\n")
        ciphered_text, order = cipher(text)
        print(ciphered_text)
        print("order: {}".format(order))
        input("Press Enter to continue:")
    elif option == 2:
        text = input("Text to decipher:\n")
        order = list(input("Cipher order (key):\n").strip())
        order = [int(n) for n in order]
        deciphered_text = decipher(text,order)
        print(deciphered_text)
        input("Press Enter to continue:")
