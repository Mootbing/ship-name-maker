def Tinder(Name1, Name2): #stupid love calculator thing: sourced from: https://www.youtube.com/watch?v=oFsLVG7EAZ4

    LoveArray = Name1.lower() + "loves" + Name2.lower()
    DictionairyOfLove = {}
    FinalArray = []
    Score = 0

    for character in LoveArray:
        if character not in DictionairyOfLove:
            DictionairyOfLove[character] = LoveArray.count(character)

    for key in DictionairyOfLove:
        FinalArray.append(DictionairyOfLove[key])

    while len(FinalArray) > 1:
        Score += FinalArray.pop(0)

    DigitOne = 0

    for char in str(Score):
        DigitOne += int(char)

    return str(DigitOne) + str(FinalArray[0]) + "%"

if __name__ == "__main__":
    print(Tinder(input("Name1:"), input("Name2:")))