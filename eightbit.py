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
    

for a in range(-128,128):
    print(a, eightbit(a))

