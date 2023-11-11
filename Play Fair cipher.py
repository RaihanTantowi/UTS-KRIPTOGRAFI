def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []

    for char in key + alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    key_matrix = [key_matrix[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def find_char(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = [char for char in plaintext if char.isalpha()]
    ciphertext = []

    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        if len(pair) == 1:
            pair += "X"

        row1, col1 = find_char(key_matrix, pair[0])
        row2, col2 = find_char(key_matrix, pair[1])

        if row1 == row2:
            ciphertext.append(key_matrix[row1][(col1 + 1) % 5])
            ciphertext.append(key_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(key_matrix[(row1 + 1) % 5][col1])
            ciphertext.append(key_matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(key_matrix[row1][col2])
            ciphertext.append(key_matrix[row2][col1])

    return "".join(ciphertext)

def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = [char for char in ciphertext if char.isalpha()]
    plaintext = []

    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        row1, col1 = find_char(key_matrix, pair[0])
        row2, col2 = find_char(key_matrix, pair[1])

        if row1 == row2:
            plaintext.append(key_matrix[row1][(col1 - 1) % 5])
            plaintext.append(key_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(key_matrix[(row1 - 1) % 5][col1])
            plaintext.append(key_matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(key_matrix[row1][col2])
            plaintext.append(key_matrix[row2][col1])

    return "".join(plaintext)

def main():
    key = input("Masukkan kunci: ")
    plaintext = input("Masukkan plaintext: ")

    ciphertext = encrypt(plaintext, key)
    print(f"Encrypted Text: {ciphertext}")

    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
