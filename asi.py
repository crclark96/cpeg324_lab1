#!/usr/local/bin/python3
"""
Collin Clark
Zach Irons

CPEG 324- Lab 1

ASI ISA
"""

import sys
from eightbit import eightbit
from dec_convert import dec_convert

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

                if registers[int(instruction[3:5],2)] == registers[int(instruction[5:7],2)]:

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

        
