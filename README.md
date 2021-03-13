# Ship Name Maker

Make ship names for you and your dependency(or dependencies if youre a player ;) )

# Examples

Eg:

Stacy & Lester

['Stansta', 'Leysta']

Felipe & Orlando

['Feor', 'Felan', 'Fedo', 'Lior', 'Lilan', 'Lido', 'Peor', 'Pelan', 'Pedo']

# How it works

The algorithem is quite simple.

1. You take the names
2. Split them into syllables using an online "api" (this program used web-scraping to get the data off the site)
3. Do all combinations with both
4. Return the data in a nicely formatted array :)

Pro tip: Additional scripts are (or will be) included that can turn this innocent shipper into an iMessage spammer

# Dependencies

- Beautiful Soup 4 (Webscrape)
- Requests (for bs4)
- Re (for regular expression)
- [This Website](http://www.syllablecount.com/syllables/) (for syllable splitting)
