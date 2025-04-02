setuso = []

string = 'aabcaacaacaaaab'

for r in range (len(string)):
    while string[r] in setuso:
        setuso.remove(string[r])
    setuso.append(string[r])

print(setuso)