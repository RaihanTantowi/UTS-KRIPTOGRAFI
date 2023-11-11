def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key = key.upper()

    for i in range(len(plain_text)):
        char = plain_text[i]

        if char.isalpha():
            # Tentukan pergeseran berdasarkan huruf kunci
            key_char = key[i % len(key)]
            shift = ord(key_char) - ord('A')

            # Enkripsi huruf
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key = key.upper()

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]

        if char.isalpha():
            # Tentukan pergeseran berdasarkan huruf kunci
            key_char = key[i % len(key)]
            shift = ord(key_char) - ord('A')

            # Dekripsi huruf
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text

# Input dari pengguna
plain_text = input("Masukkan Plain Text: ")
key = input("Masukkan Key: ")

# Enkripsi dan dekripsi
encrypted_text = encrypt_vigenere(plain_text, key)
decrypted_text = decrypt_vigenere(encrypted_text, key)

# Output hasil
print("\nPlain Text   : ", plain_text)
print("Key          : ", key)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)
