contents = open("isomorphic.txt").readlines()
for line in contents:
    line = line.strip('\n')
    words = line.split()
    word1 = words[0]
    word2 = words[1]
    pattern1 = []
    pattern2 = []
    if len(word1) == len(word2):
        for i in range(len(word1)):
            for j in range(i+1):
                if word1[i-1] == word1[j]:
                    pattern1.append(i)
        for i in range(len(word2)):
            for j in range(i+1):
                if word2[i-1] == word2[j]:
                    pattern2.append(i)
        if pattern1 == pattern2:
            print(word1,",",word2, "are isomorphs with repetition pattern",pattern1)
        else:
            print(word1,",",word2, "are not isomorphs")
    else:
        print(word1,",",word2, "have different Lengths")