"""در رمزنگاری سزار، هر حرف از متن اصلی
به اندازهٔ مقدار کلید در الفبا جابه‌جا شده
و با حرف جدید جایگزین می‌شود"""

def ceasar_encrypt(plaintext,key):
    encrypted_plaintext = ""
    
    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = (ord(char) - base + key)% 26
            encrypted_plaintext += chr(base + shift)
        else:
            encrypted_plaintext += char
    return encrypted_plaintext            
    
    
if __name__ == "__main__":
   plain_txt = input("plainText:")
   key = int(input("key(0-25):"))
   
   cipher = ceasar_encrypt(plain_txt,key)
   print("ciphertext :" , cipher)
    