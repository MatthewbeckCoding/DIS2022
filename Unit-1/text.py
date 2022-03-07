file = open("textfiles/Murlin1.txt")
contents = file.readlines()

def getCharacter():
    hexValue = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    hv = hv.lower
    total = hexValue(hv[0])*16 + hexValue(hv[1])
    ascii_character = chr(total)
    return ascii_character


for url in contents:
    clean = ""
    i = 0
    while i < len(url):
        character = url[i]
        if character == '%':
            hex = url[i+1:i+3]
            character = getCharacter(hex)
            i += 3
        else:
             i += 1
        print(clean)