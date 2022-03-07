contents = open('textfiles/pangram.txt').readlines()
contents.pop(0)
alphabet = set(list('abcdefghijklmnopqrstuvwxyz'))

for line in contents:
    line = line.strip('\n')
    letters = {}
    for c in line:
        if c.isalpha():
            letters.add(c.lower())
    missing = ''.join(sorted(alphabet.difference(letters)))
    print(line)
    if len(missing) == 0:
        print("    ", "Pangram")
    else:
        print("    ", "not pangram",missing)