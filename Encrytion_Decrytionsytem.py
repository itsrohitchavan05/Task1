def encrypt(text):
    key = 3 
    encrypted = ""
    for ch in text:
        encrypted += chr(ord(ch) + key)
    return encrypted

def decrypt(text):
    key = 3  
    decrypted = ""
    for ch in text:
        decrypted += chr(ord(ch) - key)
    return decrypted

message = input("Enter a message: ")

encrypted_msg = encrypt(message)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg)
print("Decrypted message:", decrypted_msg)
