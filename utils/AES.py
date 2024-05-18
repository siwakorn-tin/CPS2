from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import secrets

def aes_encrypt(key, data):
  """
  Encrypts data using AES in EAX mode.

  Args:
      key (bytes): The secret key for encryption (must be 16 bytes).
      data (bytes): The data to be encrypted.

  Returns:
      tuple: A tuple containing the encrypted data (ciphertext) and the nonce.
  """
  cipher = AES.new(key, AES.MODE_EAX)
  nonce = cipher.nonce
  ciphertext = cipher.encrypt(data)
  return ciphertext, nonce


def aes_decrypt(key, ciphertext, nonce):
  """
  Decrypts data encrypted with AES in EAX mode.

  Args:
      key (bytes): The secret key for decryption (must be 16 bytes).
      ciphertext (bytes): The encrypted data (ciphertext).
      nonce (bytes): The nonce used for encryption.

  Returns:
      bytes: The decrypted data (plaintext).
  """
  cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
  plaintext = cipher.decrypt(ciphertext)
  return plaintext
def key_generation():
    return secrets.token_hex(16).encode()[:16] 

