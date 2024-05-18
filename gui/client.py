# Import Module
from tkinter import *
import sys
sys.path.append('../')  # Assuming RSAEncryption is in the parent directory
from CPS2.utils.RSA import RSAEncryption 
import secrets
import hashlib 
import sys
sys.path.append('../')
from CPS2.utils.AES import *

PUs=""
root = Tk()
root.title("Server")
root.geometry('350x200')
root.resizable(False, False)

def sendEncryptedData(message):
    hashM = hashlib.sha256(message.encode()).hexdigest()
    EncyptedData=RSAEncryption().encrypt(hashM, PRs ) #2

    sssk=secrets.token_hex(16)
    message.encode()
    ciphertext, nonce = aes_encrypt(sssk, message)
    x= ciphertext+"!"+nonce #1

    EncyptedSSSK=RSAEncryption().encrypt(hashM, PRs ) #3

    byte_data = pickle.dumps(x+"|"+EncyptedData+"|"+EncyptedSSSK)
    print(byte_data)
    # s.sendall(byte_data)
def clickedKeyExchange():
    PUs, PRs = RSAEncryption().generate_keys()
    s.sendall(f"PK,{public_key[0]},{public_key[1]}".encode())
    sendEncryptedData("Tintin")

def clickedIn():
    # res = "You wrote" + txt.get()
    # lbl.configure(text = res)
    print("IN")

def clickedOut():
    # res = "You wrote" + txt.get()
    # lbl.configure(text = res)
    print("OUT")

# button widget with red color text inside
statusLbl=Label(root, text="Client")
statusLbl.pack(side=TOP,expand=True)
btnConnect = Button(root, text = "Connect" ,
             fg = "black", command=clickedConnect)
# Set Button Grid
btnConnect.pack(side=TOP, expand=True)

# button widget with red color text inside
btnIn = Button(root, text = "IN" ,
             fg = "green", command=clickedIn)
# Set Button Grid
btnIn.pack(side=LEFT, expand=True)

btnIn = Button(root, text = "OUT" ,
             fg = "red", command=clickedOut)
# Set Button Grid
btnIn.pack(side=LEFT, expand=True)


# Execute Tkinter
root.mainloop()