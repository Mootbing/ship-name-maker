# Ship Name Maker

Make ship names for you and your dependency :). (sadly I don't have a gf to test this program on, so it may be bugged)

# Examples

Stacy & Lester

['Stales', 'Stater', 'Cyles', 'Cyter', 'Lessta', 'Lescy', 'Tersta', 'Tercy']

Felipe & Orlando

['Feor', 'Felan', 'Fedo', 'Lior', 'Lilan', 'Lido', 'Peor', 'Pelan', 'Pedo', 'Orfe', 'Orli', 'Orpe', 'Lanfe', 'Lanli', 'Lanpe', 'Dofe', 'Doli', 'Dope']

## Terminal format

For brief viewing and gossiping at school, but you should save if you would like to revisit the ship

![terminal format image](https://user-images.githubusercontent.com/50122069/111045005-c50dd900-8419-11eb-880d-a6840613ecb8.png)

## Saved format

It is the same as terminal format, but now you can print it out and hang it on the wall!

![saved format image](https://user-images.githubusercontent.com/50122069/111045030-e53d9800-8419-11eb-9f59-bcd3a36a31b0.png)

## API format

Returns a dictionairy with the keys "Full Names" and "Mixture Names"

![API format image](https://user-images.githubusercontent.com/50122069/111050903-5f235080-841d-11eb-9773-af5c00fb2165.png)

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
- [Lovecalculator.com](https://www.lovecalculator.com/) (for the love calculator scraping part)

# How it works

The algorithem is quite simple.

1. You take the names
2. Split them into syllables using an online "api" (this program used web-scraping to get the data off the site)
3. Do all combinations with both
4. Return the data in a nicely formatted array :)

Extra thanks to [@wiisportsresort](https://github.com/wiisportsresort) for helping run some testcases
