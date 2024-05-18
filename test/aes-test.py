import sys
sys.path.append('../')
from CPS2.utils.AES import *

key = key_generation() # Replace with your 16-byte key
data = "HIII".encode()

ciphertext, nonce = aes_encrypt(key, data)
decrypted_data = aes_decrypt(key, ciphertext, nonce)

print("Cipher text:", ciphertext)
print("Plain text:", decrypted_data.decode())
