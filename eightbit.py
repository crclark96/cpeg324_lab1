#!/usr/local/bin/python3

def eightbit(i):

    ans = ''

    if i > 0:

        n = 1

        while n < i:
          
            n *= 2

        while n != 0:

            if (i - n < 0):

                ans += '0'
                
                n = int(n/2)
                
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
                
                n = int(n/2)
                
            else:

                i -= n
                
                ans += '0'
                
                n = int(n/2)

        if ans[-1:] == '0':

            ans = ans[:-1] + '1'

        else:

            ans = ans[:-1] + '0'

        ans = '1'*(8- len(ans)) + ans

        ans = '0b' + ans[-8:]

        return(ans)

    else:

        return('0b00000000')
    

print(3,eightbit(3))
print(45,eightbit(45))
print(127,eightbit(127))
print(128,eightbit(128))
print(-1, eightbit(-1))
print(-3, eightbit(-3))
print(-127, eightbit(-127))
print(-129, eightbit(-129))
print(0, eightbit(0))
