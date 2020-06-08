import hashlib
import sys
import os

os.system("clear")
os.system("figlet Ha5hMak6r")

key = input("[+]enter the word for be hash: ")
print("[+]enter the type \n md5: 1, sha224: 2, sha256: 3\n")
mode = input("[+]type:  ")




if mode == "1":

    hashkey = hashlib.md5(key.encode()).hexdigest()
    print(hashkey)

elif mode == "2":
    hashkey = hashlib.sha224(key.encode()).hexdigest()
    print(hashkey)

elif mode == "3":
    hashkey = hashlib.sha256(key.encode()).hexdigest()
    print(hashkey)



