# Ship Name Maker

Make ship names for you and your dependency(or dependencies if youre a player ;) )

# Examples

Stacy & Lester

['Stales', 'Stater', 'Cyles', 'Cyter', 'Lessta', 'Lescy', 'Tersta', 'Tercy']

Felipe & Orlando

['Feor', 'Felan', 'Fedo', 'Lior', 'Lilan', 'Lido', 'Peor', 'Pelan', 'Pedo', 'Orfe', 'Orli', 'Orpe', 'Lanfe', 'Lanli', 'Lanpe', 'Dofe', 'Doli', 'Dope']

# How to run

1. Clone this repository
2. Cd into src
3. Pip3 install the dependencies listed below
4. python3 shipname.py
5. Have fun!

*Note: shipname.py uses lovecalculator.py, so if you want both shipnames and love calculations, you only need to run shipname.py*

**The api may not be 100% percent accurate, but then again, love can't be calculated in numbers...**

# Dependencies

- Beautiful Soup 4 (Webscrape)
- Requests (for bs4)
- Re (for regular expression)
- [This Website](http://www.syllablecount.com/syllables/) (for syllable splitting)
- [Lovecalculator.com](Lovecalculator.com) (for the love calculator scraping part)

# How it works

The algorithem is quite simple.

1. You take the names
2. Split them into syllables using an online "api" (this program used web-scraping to get the data off the site)
3. Do all combinations with both
4. Return the data in a nicely formatted array :)
