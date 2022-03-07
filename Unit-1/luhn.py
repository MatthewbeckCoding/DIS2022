file = open("textfiles/luhn.txt")
contents = file.readlines()
contents.pop(0)

for line in contents:
    line.strip('\n')
    if line[0] == "V":
        line = line[3:]
        total = 0
        if len(line) % 2 != 0:
            odd = int(line[0])
            even = int(line[1])
            for chr in line:
                if chr == even:
                    chr = int(chr)*2
                    total += int(chr)
                else:
                    total + chr
            if total == 30:
                print("valid")
        else:
            odd = line[1]
            even = line[0]
            for chr in line:
                if chr == even:
                    chr = int(chr) * 2
                    total += int(chr)
                else:
                    total += int(chr)
            if total == 30:
                print("valid")



