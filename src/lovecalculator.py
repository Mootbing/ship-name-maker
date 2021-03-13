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

    while (len(FinalArray) > 2):
        for i in range((len(FinalArray) - 1) // 2):
            FinalArray[i] = FinalArray[i] + FinalArray.pop(len(FinalArray) - 1 - i)

    FinalScore = str(FinalArray[0]) + str(FinalArray[1])

    return FinalScore + "%"


if __name__ == "__main__":
    #print(Tinder("mary","james"))
    print(Tinder(input("Name1:"), input("Name2:")))