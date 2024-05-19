import sys
sys.path.append('../')
from tkinter import *
from CPS2.utils.RSA import RSAEncryption 
from CPS2.utils.AES import *
import secrets
import hashlib
import streamlit as st

class Server:
    RSA=RSAEncryption()
    def __init__(self):
        self.PU , self.__PR= self.RSA.generate_keys()
        self.PUOuther=""
        self.count= 0
        self.available=120
        self.root = Tk()
        self.root.title("Server")
        self.root.geometry('350x200')
        self.root.resizable(False, False)
        self.v= StringVar(self.root)
        self.statusLbl=Label(self.root, textvariable=self.v,bg="red",padx=13)
        self.statusLbl.pack(side=TOP,expand=True)
        self.statusLbl1=Label(self.root, text=self.available,bg="green",padx=13)
        self.statusLbl1.pack(side=TOP,expand=True)
        
    def __generateSSSK(self):
        return secrets.token_hex(256)
    def keyExchange(self,other):
        self.PUOuther=other.PU
        other.PUOuther=self.PU
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
        if verify:
            if message_encode == "IN":
                if (self.count<= self.available):
                    self.count+=1
                    print(self.count) 
                    self.v.set(str(self.count))  # Update with current count
                    self.statusLbl.update()

            elif message_encode == "OUT":
                if (self.count>0):
                    self.count-=1
                    print(self.count)
                    self.v.set(str(self.count))  # Update with current count
                    self.statusLbl.update()
        else:
            print("Your permission is denied.")





        

