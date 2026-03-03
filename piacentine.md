## Generate mnemonic
You need the complete deck of cards, generate 12 or 24 words and for each one you will need to use a 11 bits of entropy using cards.

You can fill a table like the following to track filling using the result of the drawn of cards (using the translation tables following). You can use any of the regional cards from the Italian traditional ones. The example below is an homage to Piacenza and their regional cards.

|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |

Index is calculate as the sum of all walues in columns containing values 1, for example:

|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1   |0  |1  |1  |0 |0 |0 |1|0|1|0|     |    |

index is 1024+256+128+8+2=1418, you don't need to calculate but you can use the table to find out index and word.


## Generate mnemonic with the Piacentine cards
If you have a 40 cards from Italian traditional card games, like the Piacentine, you can get one card per time multiple times until you have enought entropy, every time you have to reinsert card and mix the deck.

The Piacentine, like also all the other regional cards, have 4 suits and 10 cards for each suit.
Cards from 1 to 7, are represented with one to seven symbols of each suit.
Cards from 9 to 10, are represented with:
8 = Fante (like Jack) a man holding the suit symbol.
9 = Donna (like Queen) a woman holding the suit symbol.
10 = Re (like King) a king holding the suit symbol.
These lasts are called Fante-Donna-Re, but they can play a value of 8-9-10 respectively, depending on which game you are playing to.
Card 1 of each suit is called Asso (Ace).

For each card you can read the value in the following table comparing:

- the suit (Coppe, Denari, Bastoni, Spade)
- the rank (A for Ace, 2-7, 8/J for Fante, 9/Q for Donna, 10/K for Re).


Suit     |Rank|Value|
|--------|----|-----|
|Coppe   | A  |00000|
|Coppe   | 2  |00001|
|Coppe   | 3  |00010|
|Coppe   | 4  |00011|
|Coppe   | 5  |00100|
|Coppe   | 6  |00101|
|Coppe   | 7  |00110|
|Coppe   | 8/J|00111|
|Coppe   | 9/Q|01000|
|Coppe   |10/K|01001|
|Denari  | A  |01010|
|Denari  | 2  |01011|
|Denari  | 3  |01100|
|Denari  | 4  |01101|
|Denari  | 5  |01110|
|Denari  | 6  |01111|
|Denari  | 7  |10000|
|Denari  | 8/J|10001|
|Denari  | 9/Q|10010|
|Denari  |10/K|10011|
|Bastoni | A  |10100|
|Bastoni | 2  |10101|
|Bastoni | 3  |10110|
|Bastoni | 4  |10111|
|Bastoni | 5  |11000|
|Bastoni | 6  |11001|
|Bastoni | 7  |11010|
|Bastoni | 8/J|11011|
|Bastoni | 9/Q|11100|
|Bastoni |10/K|11101|
|Spade   | A  |11110|
|Spade   | 2  |11111|
|Spade   | 3  | 000 |
|Spade   | 4  | 001 |
|Spade   | 5  | 010 |
|Spade   | 6  | 011 |
|Spade   | 7  | 100 |
|Spade   | 8/J| 101 |
|Spade   | 9/Q| 110 |
|Spade   |10/K| 111 |
