#!/usr/local/bin/python3
"""
Collin Clark
Zach Irons

CPEG 324- Lab 1

ASI ISA
"""

import sys

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


def eightbit(i):

    ans = ''

    if i > 0:
        n = 1

        while n < i:          
            n *= 2

        while n != 0:
            if (i - n < 0):
                ans += '0'
                
            else:
                i -= n                
                ans += '1'                
            n = int(n/2)

        ans = '0'*(8- len(ans)) + ans
        ans = '0b' + ans[-8:]
                
        return(ans)
            
    elif i < 0:
        i *= -1
        n = 1

        while n < i:          
            n *= 2

        while n != 0:
            if (i - n < 0):
                ans += '1'
                
            else:
                i -= n                
                ans += '0'                
            n = int(n/2)

        if ans[-1:] == '0':
            ans = ans[:-1] + '1'

        else:
            x = -1

            while ans[x] == '1' and x < 8:
                x -= 1
            ans = ans[:len(ans) - abs(x)] + '1' + '0'*(abs(x) - 1)

        ans = '1'*(8- len(ans)) + ans
        ans = '0b' + ans[-8:]

        return(ans)

    else:
        return('0b00000000')


def operate(registers, instruction):

    offset = 0
    
    bit0 = int(instruction[0])

    bit1 = int(instruction[1])

    #Arithmetic Instructions
    if bit0 == 0:

        #Subtract
        if bit1 == 0:
            
            registers[int(instruction[2:4], 2)] = registers[int(instruction[4:6],2)] \
                                                  - registers[int(instruction[6:],2)]

        #Addition
        else:

            registers[int(instruction[2:4], 2)] = registers[int(instruction[4:6],2)] \
                                                  + registers[int(instruction[6:],2)]

    #Logical/Display/Compare Instructions
    else:

        #Load
        if bit1 == 0:

            registers[int(instruction[2:4], 2)] = dec_convert(instruction[4:])
            
        #Display/Compare
        else:

            bit2 = int(instruction[2])

            #Compare
            if bit2 == 0:

                if eightbit(registers[int(instruction[3:5],2)]) \
                   == eightbit(registers[int(instruction[5:7],2)]):

                    offset = int(instruction[7],2) + 1

            #Display
            else:

                print(eightbit(registers[int(instruction[3:5],2)]))
    
    return registers,offset


if __name__ == "__main__":
    
    registers = [0]*4
    
    instructions = []
    comments = []
    
    pc = 0
    
    if len(sys.argv) != 2:
        
        print('usage: ./asi.py <filename>')
        sys.exit()

    try:
        
        f = open(sys.argv[1],'r')
        
    except IOError:
        
        print('no such file')
        sys.exit(1)

    for instruction in f:
        instructions.append(instruction.rstrip())


    # check input validity
    for i in range(len(instructions)):
        if instructions[i][0] == '#':
            comments.append(instructions[i])
            continue
        if len(instructions[i]) != 8:
            print("Invalid input format on line {}".format(i+1))
            sys.exit(1)
        for char in instructions[i]:
            if char != '1' and char != '0':
                print("Invalid input format on line {}".format(i+1))
                sys.exit(1)

    # parse out comments
    for comment in comments:
        instructions.remove(comment)
                
    while pc < len(instructions):
        
        registers,offset = operate(registers,instructions[pc])

        pc += offset + 1

        
