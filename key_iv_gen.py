import os

f_key = open("key.txt","w")

f_key.write(str(int(os.urandom(4).hex(),16)) + "\n")
f_key.write(str(int(os.urandom(4).hex(),16)) + "\n")
f_key.write(str(int(os.urandom(4).hex(),16)) + "\n")

f_key.close()

f_iv = open("iv.txt","w")

f_iv.write(str(int(os.urandom(4).hex(),16)) + "\n")
f_iv.write(str(int(os.urandom(4).hex(),16)) + "\n")
f_iv.write(str(int(os.urandom(4).hex(),16)) + "\n")

f_iv.close()
