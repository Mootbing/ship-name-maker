from bs4 import BeautifulSoup
import requests
import re

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
        
        if "a" in Name.lower():
            return Name.lower().split("a")[0] + "a"
        elif "e" in Name.lower():
            return Name.lower().split("e")[0] + "e"
        elif "i" in Name.lower():
            return Name.lower().split("i")[0] + "i"
        elif "o" in Name.lower():
            return Name.lower().split("o")[0] + "o"
        elif "u" in Name.lower():
            return Name.lower().split("u")[0]+ "u"

def StartsWithAEIOU(AString):

    L = AString[0].lower()

    if (L == "a" or L == "e" or L == "i" or L == "o" or L == "u"):
        return True

    return False

def ReturnArrayOfShips(ShipString1, ShipString2):

    Ships = []

    Syllabul1 = ShipString1.split("-")

    Syllabul2 = ShipString2.split("-")

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
        

P1Name = input("Someone: ")

P2Name = input(f"Person you\'d like to ship with {P1Name}: ")

print(ReturnArrayOfShips(GetShipName(P1Name), GetShipName(P2Name)))

print("The api may not be perfect")
