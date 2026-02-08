"تمامی 26 حالت را بررسی میکند تا کلید را پیدا کند"

def ceasar_decryption(ciphertext,key):
    decrypted_plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = (ord(char) - base - key)% 26
            decrypted_plaintext += chr(base + shift)
        else:
            decrypted_plaintext += char
    return decrypted_plaintext            
    
    
if __name__ == "__main__":
   encrypted_plaintext = input("encrypted plain text:")
   print("possible plaintexts: \n")
   for key in range(26):
    plain = ceasar_decryption(encrypted_plaintext,key)
    print("plain text :" , plain)
    