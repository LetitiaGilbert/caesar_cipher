def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' for encrypt or 'D' for decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'E':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
