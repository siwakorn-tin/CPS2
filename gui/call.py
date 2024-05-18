from client import Client
from server import Server
from tkinter import Tk, Label, Button


Client = Client()
Server=Server()
Client.keyExchange(Server)

Client.payloadSend("IN",Server)
Client.payloadSend("IN",Server)


root = Tk()
root.mainloop()