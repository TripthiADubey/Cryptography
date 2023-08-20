print("Encryption of Text using ceaser Cipher algorithm: ")
def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

plaintext = input("Enter the Text to be encrypted: ")
n = int(input("Enter the number of shift: "))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext,n))


print("Decrypting the Cipher text: ")
alphabets= 'abcdefghijklmnopqrstuvwxyz'
def decrypt_caesar(num, text):
 results = ''
 for k in text.lower():
  try:
    i = (alphabets.index(k) - num) % 26
    results +=alphabets[i]
  except ValueError:
   results += k
 return results.lower()
num =int(input("please input the shift:\t"))
text=input("please input the text: \t")
ciphertext = decrypt_caesar(num, text)
print("Decoded text:",ciphertext)