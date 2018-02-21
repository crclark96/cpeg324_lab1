#!/usr/local/bin/python3
"""
Collin Clark
Zach Irons

CPEG 324- Lab 1

ASI ISA
"""
reg = [0,0,0,0]

def main():
    global reg

    instruction = input("")

    bit0 = instruction[:1]

    bit1 = instruction[1:2]

    #Arithmetic Instructions
    if bit0 == 0:

        #Subtract
        if bit1 == 0:

            reg[int(instruction[2:4], 2)] = instruction[4:6] - instruction[6:]

        #Addition
        else:

            reg[int(instruction[2:4], 2)] = instruction[4:6] + instruction[6:]

    #Logical/Display/Compare Instructions
    else:

        #Load
        if bit1 == 0:

            reg[int(instruction[2:4], 2)] = int(instruction[4:], 2)
            
        #Display/Compare
        else:

            bit2 = instruction[2:3]

            #Compare
            if bit2 == 0:

                if instruction[3:5] == instruction[5:7]:

                    offset = int(instruction[7:],2)

            #Display
            else:

                print(int(instruction[3:5],2))
    



if __name__ == "__main__":
    main()
