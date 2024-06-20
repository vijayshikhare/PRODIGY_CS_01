

def caesar_cipher_encrypt(text, shift):

    encrypted_text = ""
    for char in text:

        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)

        else:
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose 'E' to encrypt or 'D' to decrypt.")
        return

    message = input("Enter the message: ").strip()

    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return


    if choice == 'E':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()

