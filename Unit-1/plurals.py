file = open("textfiles/plurals.txt")
contents = file.readlines()
contents.pop(0)
vowels = "aeiouy"
for line in contents:
    values = line.split()

    q = values[0]
    word = values[1]
    if q == "0":
        q = "no"
    elif q == "1":
        q = "one"
    if q != "one":
        if word[-1] in ("s", "x", "z"):
            word += "es"
        elif word[-2] in ("ch", "sh"):
            word += "es"
        elif word[-1] == "o" and word[-2] not in vowels:
            word += "es"
        elif word[-1] == "y" and word[-2] not in vowels:
            word = word[0:-1] + "ies"
        elif word[-2:] == "fe" and word[-3] != "f":
            word = word[0:-2] + "ves"
        elif word[-1] == "f" and word[-2] != "f":
            word = word[0:-1] + "ves"
        else:
            word += "s"
    print(q, word)
