word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
word3 = ""
if len(word1) == len(word2):
    for chr in range(0, len(word1)):
        word3 += word1[chr]
        word3 += word2[chr]
    print(word3)

elif len(word1) > len(word2):
    for chr in range(0, len(word2)):
        word3 += word1[chr]
        word3 += word2[chr]
    word3 += word1[len(word2):]
    print(word3)

elif len(word2) > len(word1):
    for chr in range(0, len(word1)):
        word3 += word1[chr]
        word3 += word2[chr]
    word3 += word2[len(word1):]
    print(word3)


