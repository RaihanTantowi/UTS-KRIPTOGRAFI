def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Mengabaikan karakter non-alphabetic
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    # Input teks dan pergeseran dari pengguna
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    shift = int(input("Masukkan jumlah pergeseran: "))

    # Enkripsi
    ciphertext = encrypt(plaintext, shift)
    print(f"Hasil enkripsi: {ciphertext}")

    # Dekripsi
    decrypted_text = decrypt(ciphertext, shift)
    print(f"Hasil dekripsi: {decrypted_text}")

if __name__ == "__main__":
    main()
