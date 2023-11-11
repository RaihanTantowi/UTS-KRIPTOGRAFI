def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encrypt(message, key):
    encrypted_text = ""
    for i in range(len(message)):
        if message[i].isalpha():
            # Mengonversi karakter pesan dan kunci ke dalam ASCII
            char = chr((ord(message[i]) + ord(key[i])) % 26 + 65)
            encrypted_text += char
        else:
            encrypted_text += message[i]
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Mengonversi karakter ciphertext dan kunci ke dalam ASCII
            char = chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + 65)
            decrypted_text += char
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

def main():
    message = input("Masukkan pesan: ").upper()
    key = input("Masukkan kunci: ").upper()

    key = generate_key(message, key)

    encrypted_text = encrypt(message, key)
    decrypted_text = decrypt(encrypted_text, key)

    print("\nPesan Asli: {}".format(message))
    print("Pesan Terenkripsi: {}".format(encrypted_text))
    print("Pesan Terdekripsi: {}".format(decrypted_text))

if __name__ == "__main__":
    main()
