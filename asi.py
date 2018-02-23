#!/usr/local/bin/python3
"""
Collin Clark
Zach Irons

CPEG 324- Lab 1

ASI ISA
"""

import sys
from eightbit import eightbit

def operate(registers, instruction):

    offset = 0
    
    bit0 = int(instruction[0])

    bit1 = int(instruction[1])

    #Arithmetic Instructions
    if bit0 == 0:

        #Subtract
        if bit1 == 0:
            
            registers[int(instruction[2:4], 2)] = int(instruction[4:6],2) \
                                                  - int(instruction[6:],2)

        #Addition
        else:

            registers[int(instruction[2:4], 2)] = int(instruction[4:6],2) \
                                                  + int(instruction[6:],2)

    #Logical/Display/Compare Instructions
    else:

        #Load
        if bit1 == 0:

            registers[int(instruction[2:4], 2)] = int(instruction[4:], 2)
            
        #Display/Compare
        else:

            bit2 = int(instruction[2])

            #Compare
            if bit2 == 0:

                if instruction[3:5] == instruction[5:7]:

                    offset = int(instruction[7],2)

            #Display
            else:

                print(eightbit(registers[int(instruction[3:5],2)]))
    
    return registers,offset


if __name__ == "__main__":
    
    registers = [0]*4
    
    instructions = []
    
    pc = 0
    
    if len(sys.argv) != 2:
        
        print('usage: ./asi.py <filename>')
        sys.exit()

    try:
        
        f = open(sys.argv[1],'r')
        
    except IOError:
        
        print('no such file')
        sys.exit()

    for instruction in f:
        if '#' not in instruction:
            instructions.append(instruction.rstrip())

    while pc < len(instructions):
        
        registers,offset = operate(registers,instructions[pc])

        pc += offset + 1

        
