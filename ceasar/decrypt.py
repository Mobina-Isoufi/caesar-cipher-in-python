"""در رمزگشایی سزار، برخلاف رمزگذاری،
هر حرف از متن رمز‌شده به اندازهٔ
مقدار کلید به عقب در الفبا جابه‌جا
شده و با حرف اصلی جایگزین می‌شود"""

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
   key = int(input("key(0-25):"))
   
   plain = ceasar_decryption(encrypted_plaintext,key)
   print("plain text :" , plain)
    