def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext


def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext


def brute_force_decrypt(ciphertext):
    for shift in range(26):
        plaintext = caesar_decrypt(ciphertext, shift)
        print(f"Shift: {shift:2} Plaintext: {plaintext}")


# Example usage
ciphertext = input("Enter the encrypted text: ")
brute_force_decrypt(ciphertext)