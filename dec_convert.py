def dec_convert(b):
    res = 0

    if b[:1] == '1':        
        for i in range(1,4):
            if b[i] == '0':
                res -= 2**(3-i)
        res -= 1

    else:
        for i in range(1,4):
            if b[i] == '1':
                res += 2**(3-i)

    return res

if __name__ == "__main__":

    print(dec_convert('0000'))
    print(dec_convert('0001'))
    print(dec_convert('0010'))
    print(dec_convert('0011'))
    print(dec_convert('0100'))
    print(dec_convert('0101'))
    print(dec_convert('0110'))
    print(dec_convert('0111'))
    print(dec_convert('1000'))
    print(dec_convert('1001'))
    print(dec_convert('1010'))
    print(dec_convert('1011'))
    print(dec_convert('1100'))
    print(dec_convert('1101'))
    print(dec_convert('1110'))
    print(dec_convert('1111'))

