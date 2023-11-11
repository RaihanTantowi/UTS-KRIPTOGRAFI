def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((key[0] * (ord(char) - ord('A')) + key[1]) % 26 + ord('A'))
            else:
                result += chr((key[0] * (ord(char) - ord('a')) + key[1]) % 26 + ord('a'))
        else:
            result += char
    return result

def affine_decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                result += chr((modinv(key[0], 26) * (ord(char) - ord('A') - key[1])) % 26 + ord('A'))
            else:
                result += chr((modinv(key[0], 26) * (ord(char) - ord('a') - key[1])) % 26 + ord('a'))
        else:
            result += char
    return result

def main():
    text = input("Masukkan teks yang ingin dienkripsi: ")
    key_a = int(input("Masukkan kunci a (bilangan bulat yang relatif prima dengan 26): "))
    key_b = int(input("Masukkan kunci b (bilangan bulat): "))

    key = (key_a, key_b)

    encrypted_text = affine_encrypt(text, key)
    decrypted_text = affine_decrypt(encrypted_text, key)

    print("\nTeks Asli: {}".format(text))
    print("Teks Terenkripsi: {}".format(encrypted_text))
    print("Teks Terdekripsi: {}".format(decrypted_text))

if __name__ == "__main__":
    main()
