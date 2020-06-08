import os
import sys
import hashlib
import re

os.system("clear")
os.system("figlet Hac1dd")

pass_found = 0

hashtxt = input("[+]Enter the hash: ")

md5reg = re.fullmatch(r'[0-9a-f]{32}',hashtxt)

sha224reg = re.fullmatch(r'[0-9a-f]{56}',hashtxt)

sha256reg = re.fullmatch(r'[0-9a-f]{64}',hashtxt)


if md5reg != None:
    print("[+]{} is md5".format(hashtxt))
    hashtype = "md5"

elif sha224reg != None:
    print("[+]{} is sha224".format(hashtxt))
    hashtype = "sha224"

elif sha256reg != None:
    print("[+]{} is sha256".format(hashtxt))
    hashtype = "sha256"

os.system("clear")
os.system("figlet Crack")

print("[+]{0} is {1}".format(hashtxt,hashtype))

def line():
    print("-"*60)
    print("-"*60)


line()

print("[+]Type: {}".format(hashtype))
line()

pass_doc  = input("[*]Enter passwords list dic(root/home/):")

try:
    pass_file = open(pass_doc, 'r')
except:
    print("[+]Error:")
    print(pass_doc,"is not found.\n please give the path of file correctly.")
    quit()
    
for word in pass_file:
    enc_word = word.encode('utf-8')
    if hashtype == "md5":
        hash_word = hashlib.md5(enc_word.strip())
    elif hashtype == "sha224":
        hash_word = hashlib.sha224(enc_word.strip())
    elif hashtype == "sha256":
        hash_word = hashlib.sha256(enc_word.strip())
    
    print("try_at/:{}".format(hash_word))
    print("try_at/:{}".format(enc_word))
    digest = hash_word.hexdigest()
    
    if digest == hashtxt:
        line()
        os.system("figlet Found!!!!!!!!")
        line()
        line()
        print("password found. \nThe  password is :",word)
        line()
        pass_found = 1
        break
if not pass_found:
    #os.system("clear")
    print("password is not found in the ", pass_doc, "file")


