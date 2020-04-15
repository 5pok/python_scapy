#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Ingresa la IP a escanear: ")
puerto = int(input("Ingresa el PUERTO a escanear: "))


def pScanner(puerto):
    if s.connect_ex((host, puerto)):
        print("El puerto esta cerrado")
    else:
        print("El puerto esta abierto")

pScanner(puerto)  
        