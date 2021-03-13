import re

def IsNotSameBeforeAndAfter(NameArray, Index):

    precondition = [True, True]

    if Index + 1 < len(NameArray):
        precondition[0] = NameArray[Index] != NameArray[Index + 1]
    if Index - 1 > 0:
        precondition[1] = NameArray[Index] != NameArray[Index - 1]
    
    return precondition[0] and precondition[1]

def DealWithOneSyllabulNames(Name):

    for Vowel in ["a", "e", "i", "o", "u"]:
        if Vowel in Name:
            break

        if Vowel == "u":
            return Name #no vowel

    Counter = 0
    NameIntoLists = list(Name)
    VOWEL_REGEX = re.compile("[aeiou]") # code stolen https://stackoverflow.com/questions/46337907/extract-the-index-of-the-first-vowel-in-a-string/46338545#46338545
    FinalList = []

    while True:

        if not (len(NameIntoLists) > Counter):
            FinalList.append("".join(NameIntoLists))
            return FinalList
        
        if NameIntoLists[Counter].lower() in ["a", "e", "i", "o", "u" ]:
            
            SacredWord = (str("".join(NameIntoLists)))[:int(Counter + 1)]

            FinalList.append(SacredWord)
            NameIntoLists = list(("".join(NameIntoLists))[Counter + 1:])

            Counter = 0

        Counter += 1

print(DealWithOneSyllabulNames("larry"))