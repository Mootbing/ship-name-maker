from bs4 import BeautifulSoup
import requests
import re

def Tinder(Name1, Name2): 

    try:

        Page = requests.get(f"https://www.lovecalculator.com/love.php?name1={Name1}&name2={Name2}") #request the site

        Soup = BeautifulSoup(Page.content, 'html.parser') #let bs4 do the work

        Chunk = str(Soup.find(class_="result__score")) #find the id where it is located

        Final = re.sub("<.*>", "", Chunk).strip()#find score

        Chunk2 = str(Soup.find(class_="result-text"))

        Description = re.sub("<.*>", "", Chunk2).strip()
    
        return Final, " ".join(Description.split()) #rid wierd spacing

    except:
        raise SystemExit("Error occured while connecting to lovecalculator.com")

if __name__ == "__main__":
    print(Tinder("mary","stephen"))
    #print(Tinder(input("Name1:"), input("Name2:")))