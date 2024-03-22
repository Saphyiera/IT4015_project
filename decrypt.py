import binascii as j

def strxor(t1: str, t2: str) -> str:
    return '{1:0{0}x}'.format(len(t1), int(t1, 16) ^ int(t2, 16))

def decrypt(text: str, key: str) -> str:
    return strxor(text, key)

def split_text_to_list(text: str) -> list:
    result = []
    for i in range(0, len(text) - 1, 2):
        t = text[i] + text[i+1]
        result.append(t)
    return result

def merge_list_to_text(l: list) -> str:
    result = ""
    for i in l:
        result += str(i)
    return result

def possible_encrypted_space(l: list, target: str) -> list:
    if len(l) == 1:
        return l
    result = []
    for item1 in l:
        count = 0
        for item2 in l:
            if int(strxor(item1,item2) , 16) > 63:
                count += 1
                if count == 2:
                    result.append(item1)
                    break
    if len(result) > 1:
        temp = result.copy()
        for item in temp:
            key = strxor(item,"20")
            ch = strxor(key,target)
            num = int(ch,16)
            #flag = 32<=num<=126 
            flag =(65<=num<=90) or (97<=num<=122) or (num==32)
            if flag == False:
                result.remove(item)
    return result

def code_to_text(s: str) -> str:
    l = split_text_to_list(s)
    res = ""
    for item in l:
        res += (j.a2b_hex(item)).decode('utf-8')
    return res

def main():
    file = open("ciphers.txt", "r")

    ciphertext = []
    space = {}
    
    for i in range (0,11,1):
        ciphertext.append(file.readline())
    target = ciphertext[10]

    l = len(target)

    char_cipher = {}
    encrypted_char = {}
    for i in range(0,l//2,1):
        encrypted_char[i] = []

    file2 = open("shorten_ciphers.txt", "w")
    for i in range(0,11,1):
        ciphertext[i] = ciphertext[i][0:l]
        file2.writelines(ciphertext[i] + "\n")
        char_cipher[i] = split_text_to_list(ciphertext[i])

    key = {}

    for i in range(0,l//2,1):
        encrypted_char[i] = []
        for ii in range(0,11,1):
            if char_cipher[ii][i] not in encrypted_char[i]:
                (encrypted_char[i]).append(char_cipher[ii][i])
        space[i] = possible_encrypted_space(encrypted_char[i],char_cipher[10][i])
        l_temp = []
        for item in space[i]:
            l_temp.append(strxor("20",item))
        key[i] = l_temp
        # print(str(i)+ ": " + str(space[i]) + str(key[i]))

    sol = {}
    for i in range(0,l//2,1):
        sol[i] = []
        for item in key[i]:
            cc = strxor(item ,char_cipher[10][i])
            sol[i].append(code_to_text(cc))
        print(str(i) + ": " + str(sol[i]))

    file.close()
    file2.close()
    return 0

main()