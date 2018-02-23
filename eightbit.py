#!/usr/local/bin/python3

def eightbit(i):
    n = bin(i)
    if len(n) < 10:
        return n[:2] + '0'*(10-len(n)) + n[2:]
    else:
        return n[:2] + n[-8:]

if __name__ == '__main__':
    
    print(3,eightbit(3))
    print(45,eightbit(45))
    print(255,eightbit(255))
    print(256,eightbit(256))
    print(-1, eightbit(-1))
    print(-3, eightbit(-3))
    print(-256, eightbit(-256))
    print(-257, eightbit(-257))
    print(0, eightbit(0))

