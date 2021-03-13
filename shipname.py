from bs4 import BeautifulSoup
import requests
import re

def IsNotSameBeforeAndAfter(NameArray, Index):

    precondition = tuple(True, True)

    if Index + 1 < len(NameArray):
        precondition[0] = NameArray[Index] != NameArray[Index + 1]
    if Index - 1 > 0:
        precondition[1] = NameArray[Index] != NameArray[Index - 1]
    
    return precondition[0] and precondition[1]

def DealWithOneSyllabulNames(Name):

    for Vowel in ["a", "e", "i", "o", "u", "y"]:
        if Vowel in Name:
            break

        if Vowel == "y":
            return Name #no vowel

    Counter = 0
    NameIntoLists = list(Name)
    FinalList = []

    while True:

        if not (len(NameIntoLists) > Counter):
            FinalList.append("".join(NameIntoLists))
            return FinalList
        
        if NameIntoLists[Counter].lower() in ["a", "e", "i", "o", "u", "y"]:
            
            SacredWord = (str("".join(NameIntoLists)))[:int(Counter + 1)]

            FinalList.append(SacredWord)
            NameIntoLists = list(("".join(NameIntoLists))[Counter + 1:])

            Counter = 0

        Counter += 1

def GetShipName(Name): #webscrape shit

    try:

        Page = requests.get(f"http://www.syllablecount.com/syllables/{Name}") #request the site

        Soup = BeautifulSoup(Page.content, 'html.parser') #let bs4 do the work

        Chunk = str(Soup.find(id="ctl00_ContentPane_paragraphtext2")) #find the id where it is located

        SmolChunk = Chunk.split('''<b style="color: #008000">''')[1] #find the specific color tag right before the text, and rid everything before that

        Final = re.sub("<\/.*>", "", SmolChunk)

        if(len(Final.split("-")) > 1):
            return Final #replace the ending tags
        raise SystemError("Error raised so it can go into the except section! carry on")
    
    except:
        
        return ("-".join(DealWithOneSyllabulNames(Name))).strip("-")


def StartsWithAEIOU(AString):

    L = AString[0].lower()

    if (L == "a" or L == "e" or L == "i" or L == "o" or L == "u"):
        return True

    return False

def ShipOneXY(Syllabul1, Syllabul2):

    Ships = []

    for x in range(len(Syllabul1)):
        for y in range(len(Syllabul2)):

            if (StartsWithAEIOU(Syllabul1[x]) and x != 0):
                p1syllabul = Syllabul1[x - 1][len(Syllabul1[x - 1]) - 1] + Syllabul1[x]
            else:
                p1syllabul = Syllabul1[x]

            if (StartsWithAEIOU(Syllabul2[y]) and y != 0):
                p2syllabul = Syllabul2[y - 1][len(Syllabul2[y - 1]) - 1] + Syllabul2[y]
            else:
                p2syllabul = Syllabul2[y]  

            Ships.append(str(p1syllabul + p2syllabul).lower().capitalize())
    
    return Ships

def ReturnArrayOfShips(ShipString1, ShipString2):

    Syllabul1 = ShipString1.split("-")

    Syllabul2 = ShipString2.split("-")

    Ship1 = ShipOneXY(Syllabul1, Syllabul2)
    Ship2 = ShipOneXY(Syllabul2, Syllabul1)
    
    #also have to add the cases where it's not 2 syllabuls and you're using ther person's name

    return Ship1 + Ship2
        
def Tinder(Name1, Name2): #stupid love calculator thing

    Total1 = 0
    Total2 = 0

    for character in Name1:
        Total1 += ord(character)
    for character in Name2:
        Total2 += ord(character)
    
    LoveRate = str(int(round((Total1/len(Name1))/(Total2/len(Name2)), 2) * 100))

    return str(LoveRate) + "%"


P1Name = input("Someone: ")

P2Name = input(f"Person you\'d like to ship with {P1Name}: ")

print(f"\n-======Ship Names With {P1Name.capitalize()} & {P2Name.capitalize()}======-\n")

print(ReturnArrayOfShips(GetShipName(P1Name), GetShipName(P2Name)))

print(f"\n-======Love Percentage - {P1Name.capitalize()} & {P2Name.capitalize()}======-")

print(f"\n>>>{Tinder(P1Name, P2Name)}<<<\n")

print("The api may not be perfect")#'''
