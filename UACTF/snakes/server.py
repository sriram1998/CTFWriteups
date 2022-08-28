def unreachable():
    from os import getenv
    flag = getenv('FLAG')
    if flag is not None:
        print(flag)
        return
    
    print("An error has occurred. Please contact the moderators")

n = int(input('Please input a number: '))
c = input('Please input a character: ')[0]

if n is ord(c) and n+1 is not ord(c) + 1:
    unreachable()