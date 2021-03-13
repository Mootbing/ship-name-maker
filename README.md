# Ship Name Maker

Make ship names for you and your dependency ;)

# Examples

Eg:

Stacy & Lester

['Stansta', 'Leysta']

Felipe & Orlando

['Feor', 'Felan', 'Fedo', 'Lior', 'Lilan', 'Lido', 'Peor', 'Pelan', 'Pedo']

# How it works

The algorithem is quite simple, you take the names, split them into syllables using an online "api" (this program used web-scraping to get the data off the site) , and do all combinations with both.

# Dependencies

- Beautiful Soup 4 (Webscrape)
- Requests (for bs4)
- Re (for regular expression)
- [This Website](http://www.syllablecount.com/syllables/) (for syllable splitting)
