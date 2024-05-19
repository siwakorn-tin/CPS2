import sys
sys.path.append('../')
from CPS2.utils.RSA import RSAEncryption 
from CPS2.utils.AES import *
import secrets
import hashlib
from tkinter import *


class Client:
    RSA=RSAEncryption()
    def __init__(self):
        self.PU , self.__PR= self.RSA.generate_keys()
        self.PUOuther=""
        self.count = 0
        self.available=120
        self.root = Tk()
        self.root.title("Client")
        self.root.geometry('350x200')
        self.root.resizable(False, False)
        
       
    def __generateSSSK(self):
        return secrets.token_hex(256)
    def keyExchange(self,other):
        self.PUOuther=other.PU
        other.PUOuther=self.PU
        def sendIN():
            self.payloadSend("IN",other)
        btnConnect = Button(self.root, text = "IN" ,
             fg = "black", command=sendIN)
        btnConnect.pack(side=TOP, expand=True)
        def sendOUT():
            self.payloadSend("OUT",other)
        btnConnect = Button(self.root, text = "OUT" ,
             fg = "black", command=sendOUT)
        btnConnect.pack(side=TOP, expand=True)
    def __payloadCreated(self,message):
        sssk=key_generation()
        message_encode = message.encode()
        ciphertext, nonce = aes_encrypt(sssk, message_encode) #1
        hash_SHA1_m = hashlib.sha256(message.encode()).hexdigest()
        hash_SHA1_m_PRs=RSAEncryption().encrypt(hash_SHA1_m, self.__PR ) #2
        SSSK_Pu=RSAEncryption().encrypt(str(sssk.decode("utf-8")), self.PUOuther ) #3
        print(f"""     ciphertext: {ciphertext},
            nonce: {nonce},
            hash_SHA1_m_PRs: {hash_SHA1_m_PRs},
            SSSK_Pu": {SSSK_Pu}"""  )
        return {
            "ciphertext": ciphertext,
            "nonce": nonce,
            "hash_SHA1_m_PRs": hash_SHA1_m_PRs,
            "SSSK_Pu": SSSK_Pu
        }    
    def payloadSend(self,message,other):
        payload=self.__payloadCreated(message)
        other.receivePayload(payload)
    
    def receivePayload(self,payload):
        ciphertext=payload["ciphertext"]
        nonce=payload["nonce"]
        hash_SHA1_m_PRs = payload["hash_SHA1_m_PRs"]
        SSSK_Pu=payload["SSSK_Pu"]
        sssk = RSAEncryption().decrypt(SSSK_Pu, self.__PR)
        sssk = sssk.encode("utf-8")  # Encode the string back to bytes
        message_encode = aes_decrypt(sssk, ciphertext, nonce).decode()
        verify= hashlib.sha256(message_encode.encode()).hexdigest()==RSAEncryption().decrypt( hash_SHA1_m_PRs, self.PUOuther)
    

