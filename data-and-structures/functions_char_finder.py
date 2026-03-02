str = input('Enter the string: ')
c = input('Enter the character you would like to locate: ')

def findall(str, c):
    locate = []
    for i in range(len(str)):
        if str[i] == c:
            locate.append(i + 1)
    print(locate)

findall(str, c)


