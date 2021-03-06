from bs4 import BeautifulSoup
import requests
import re

import lovecalculator #local package

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

def ShipNamesToo(Name, Syllabuls):

    Name = re.sub("-", "", Name)

    Ships = []

    for c in Syllabuls:
        Ships.append((Name + c).capitalize().replace(" ", ""))
        Ships.append((c + Name).capitalize().replace(" ", ""))

    return Ships

def ReturnArrayOfShips(ShipString1, ShipString2, IsApi = False):

    Syllabul1 = ShipString1.split("-")

    Syllabul2 = ShipString2.split("-")
    
    #also have to add the cases where its the full name for the first one and then parts of the 2nd

    if not IsApi:

        BeforeString = f'''Mixture Names: \n
{str(ShipOneXY(Syllabul1, Syllabul2))}
{str(ShipOneXY(Syllabul2, Syllabul1))}'''

        ToPrint = f'''
{BeforeString}
\nFull Names: \n
{str(ShipNamesToo(ShipString1, Syllabul2))}
{str(ShipNamesToo(ShipString2, Syllabul1))}'''

    else:
        
        ToPrint = {
            "Mixture Names":[ShipOneXY(Syllabul1, Syllabul2), ShipOneXY(Syllabul2, Syllabul1)],
            "Full Names":[ShipNamesToo(ShipString1, Syllabul2), ShipNamesToo(ShipString2, Syllabul1)]
        }

    return ToPrint


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

            Ships.append(str(p1syllabul + p2syllabul).lower().capitalize().replace(" ", ""))
    
    return Ships

def ReturnFinishedNamesInDict(Name1, Name2): #used to call from other files into this api to get lovers
    return ReturnArrayOfShips(GetShipName(Name1), GetShipName(Name2), True)

if __name__ == "__main__":

    print("\n-======Ship Name Generator=====-\n")

    P1Name = input("Someone: ")

    P2Name = input(f"Person you\'d like to ship with {P1Name}: ")

    P1Name = re.sub("[\W_]+", "", P1Name)

    P2Name = re.sub("[\W_]+", "", P2Name)

    if P1Name == "" or P2Name == "":
        raise SystemExit("\nCleb is being a bed boi\n")

    P1Name = P1Name[:100]

    P2Name = P2Name[:100]

    print(f"\n-======Ship Names With {P1Name.capitalize()} & {P2Name.capitalize()}======-")

    print(ReturnArrayOfShips(GetShipName(P1Name), GetShipName(P2Name)))

    print(f"\n-======Love Percentage - {P1Name.capitalize()} & {P2Name.capitalize()}======-")

    print(f"\n>>>{lovecalculator.Tinder(P1Name, P2Name)[0]}<<<\n\n{lovecalculator.Tinder(P1Name, P2Name)[1]}\n-===Provided by lovecalculator.com===-")

    print("\nNotice: The api may not be perfect\nAny bug/feature requests file an issue here https://github.com/Mootbing/ship-name-maker/issues\n")#

    Save = input("Save This Result Locally? (Y/N)\n>>>")

    if(Save.strip().lower() == "y" or Save.strip().lower() == "yes"):
        try:
            with open(f"./saved/Ship{P1Name.capitalize()}With{P2Name.capitalize()}.txt", "w+") as f:
                f.write(f"Shipping {P1Name.capitalize()} With {P2Name.capitalize()}\n")
                f.write(ReturnArrayOfShips(GetShipName(P1Name), GetShipName(P2Name)) + "\n")
                f.write(f"\nLove Percentage of {P1Name.capitalize()} and {P2Name.capitalize()} \n")
                f.write(f"\n>>>{lovecalculator.Tinder(P1Name, P2Name)[0]}<<<\n\n{lovecalculator.Tinder(P1Name, P2Name)[1]}\n-===Provided by lovecalculator.com===-")
                
            print(f"\n-===Sucessfully saved file to ./saved/Ship{P1Name.capitalize()}With{P2Name.capitalize()}.txt!===-\n")

        except:
            raise SystemExit(f"-===Failed saving file to ./saved/Ship{P1Name.capitalize()}With{P2Name.capitalize()}.txt===-\n")

#'''