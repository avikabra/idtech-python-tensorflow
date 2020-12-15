letters_give = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z"
}

letters_get = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

cipherBroadType = raw_input("Do you want to use the alpha-numeric (type an) code or the caesar's cipher?")

if cipherBroadType != "an":
    cipherType = raw_input("Do you want to encrypt or decrypt a message");

    if cipherType == "encrypt":
        text = raw_input("What would you like to encrypt?")
        key = int(input("What do you want the key to be. The key shifts each of the letters by a certain amount to the right."))
        wordList = []
        newWordList = []
        for i in range(len(text)):
            wordList.append(text[i])
        for i in range(len(text)):
            keyNumber = letters_get[wordList[i]]
            newWordList.append(letters_give[(keyNumber + key) % 26])
        for i in range(len(text)):
            print newWordList[i],
    else:
        text = raw_input("What would you like to decrypt")
        key = raw_input("Do you know the key? If yes, type the key. If no, type no")
        wordList = []
        newWordList = []
        if key != "no":
            key = int(key)
            for i in range(len(text)):
                if text[i] != " ":
                    wordList.append(text[i])
            for i in range(len(wordList)):
                keyNumber = letters_get[wordList[i]]
                newWordList.append(letters_give[(keyNumber - key + 26) % 26])
            for i in range(len(wordList)):
                print newWordList[i],
        else:
            print("Here is a list of all possible codes:")
            for i in range(len(text)):
                if text[i] != " ":
                    wordList.append(text[i])
            for k in range(26):
                for i in range(len(wordList)):
                    keyNumber = letters_get[wordList[i]]
                    give_letter = ((keyNumber - k + 26) % 26)
                    if give_letter == 0:
                        give_letter = 26;
                    newWordList.append(letters_give[give_letter])
                for i in range(len(wordList)):
                    print newWordList[i],
                print()
                newWordList = []
else:
    cipherType = raw_input("Do you want to encrypt or decrypt a message");

    if cipherType == "encrypt":
        text = raw_input("What would you like to encrypt?")
        wordList = []
        newWordList = []
        for i in range(len(text)):
            if text[i] != " ":
                wordList.append(text[i])
        for i in range(len(wordList)):
            keyNumber = letters_get[wordList[i]]
            newWordList.append(keyNumber)
        for i in range(len(wordList)):
            print newWordList[i], "|",
    else:
        text = raw_input("What would you like to decrypt")
        wordList = []
        newWordList = []
        counter = 0
        for i in range(len(text)):
            if text[i] == "|":
                counter == 1
            if text[i] != " ":
                if text[i] != "|":
                    if counter == 1:
                        wordList.append(text[i])
                        counter = 0
        for i in range(len(wordList)):
            keyNumber = letters_give[wordList[i]]
            newWordList.append(keyNumber)
        for i in range(len(wordList)):
            print newWordList[i],
        print("This part of the code doesn't work yet. Try again later.")