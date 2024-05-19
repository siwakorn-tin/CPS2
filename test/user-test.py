import sys
sys.path.append('../')
from CPS2.gui.user import *

#1 USER    
Tintin=User()
Pin=User()

#2 KEY EXCHANGE
Tintin.keyExchange(Pin)

#3 KEY EXCHANGE
print(f"In Tintin OBJ: {Tintin.PU}")
print(f"In Pin OBJ: {Pin.PUOuther}")

print(f"In Pin OBJ: {Pin.PU}")
print(f"In Tintin OBJ: {Tintin.PUOuther}")


Tintin.payloadSend("Test",Pin)
Pin.payloadSend("LoremIpsum",Tintin)