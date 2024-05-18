import sys
sys.path.append('../')  # Assuming RSAEncryption is in the parent directory
from CPS2.utils.RSA import RSAEncryption

print("\t\t\t FOR TEST ONLY")
# John (the receiver) generates a key pair
john_public_key, john_private_key = RSAEncryption().generate_keys()
print(f"PUBLIC KEY(e,n):\t {john_public_key}")
print(f"PRIVATE KEY(d,n):\t{john_private_key}")


print("\t\t\t TEST1")

message = "This "
print(f"Original Text: {message}")

encrypted_message = RSAEncryption().encrypt(message, john_private_key)
print("Encrypted message:", encrypted_message)

decrypted_message = RSAEncryption().decrypt(encrypted_message, john_public_key)
print("Decrypted message:", decrypted_message)