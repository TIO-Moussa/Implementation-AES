#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile,isdir, join
import time


def padding(s):
    #print(AES.block_size)
    #print(len(s))
    padd=s +b"\0" * (AES.block_size - (len(s) % AES.block_size))        
    return bytes(padd)
# Chiffrement d'un message
def crypter(message, key, key_size=256):
    message = padding(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)
# Chiffrement d'un fichier 
def crypter_fichier(fichier,key):
    fd=open(fichier,'rb')
    contenue=fd.read()
    fdw=open(fichier + ".cry",'wb')
    fdw.write(crypter(contenue,key))
    fd.close()
    fdw.close()
    os.remove(fichier)

# Chiffrement d'un dossier
def Toutcrypter(chemin,key):
    if isdir(chemin):
        contenue=listdir(path=chemin)
        for element in contenue:
            if isfile(chemin+'\\'+element):
                crypter_fichier(chemin+'\\'+element,key)
            else:
                Toutcrypter(chemin+'\\'+element,key)
    elif isfile(chemin):
        crypter_fichier(chemin+'\\'+element,key)



# Dechiffre un message
def decrypter(textechiffrer, key):
    iv = textechiffrer[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    texte_clair = cipher.decrypt(textechiffrer[AES.block_size:])    
    return texte_clair.rstrip(b"\0")
# Dechiffre un fichier
def decrypterfichier(fichier,key):
    fd=open(fichier,'rb')
    contenue=fd.read()
    dec=decrypter(contenue,key)
    fd=open(fichier[:-4],'wb')
    fd.write(dec)
    os.remove(fichier)
    

cle_AES = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'

# Dechiffrement un dossier 
def Toutdecrypter(chemin,key):
    if isdir(chemin):
        contenue=listdir(path=chemin)
        for element in contenue:
            if isfile(chemin+'\\'+element):
                decrypterfichier(chemin+'\\'+element,key)
            else:
                Toutdecrypter(chemin+'\\'+element,key)
    elif(isfile(chemin)):
        Toutdecrypter(chemin+'\\'+element,key)

Toutdecrypter("teste",cle_AES)
#Toutcrypter("teste",cle_AES)









