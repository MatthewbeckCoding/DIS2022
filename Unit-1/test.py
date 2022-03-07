contents = open("isomorphic.txt").readlines()
def check(x,y):
    for i in range(len(word1)):
        j = i + 1
        found = False
        while j < len(word1) and found == False:
            if word1[j] == word1[i]:
                found = True
                pattern1 += "+" + str(j - i) + " "
            j += 1
        if found == False:
            pattern1 += "0 "

for line in contents:
    line = line.strip('\n')
    words = line.split()
    word1 = words[0]
    word2 = words[1]
    pattern1 = ""
    pattern2 = ""
    if len(word1) == len(word2):
        for i in range(len(word1)):
            j = i+1
            found = False
            while j < len(word1) and found == False:
                if word1[j] == word1[i]:
                    found = True
                    pattern1 += "+" + str(j-i) + " "
                j += 1
            if found == False:
                pattern1 += "0 "
        for i in range(len(word2)):
            j = i+1
            found = False
            while j < len(word2) and found == False:
                if word2[j] == word2[i]:
                    found = True
                    pattern2 += "+" + str(j-i) + " "
                j += 1
            if found == False:
                pattern2 += "0 "
        if pattern1 == pattern2:
            print(word1,",",word2, "are isomorphs with repetition pattern",pattern1)
        else:
            print(word1,",",word2, "are not isomorphs")
    else:
        print(word1,",",word2, "have different Lengths")