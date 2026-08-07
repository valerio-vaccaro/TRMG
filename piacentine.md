## Generate mnemonic
Use a complete deck of cards to generate 12 or 24 words. Each word requires 11 bits of entropy.

Use a table like the following to record the results of card draws, using the conversion table below. You can use any regional Italian deck; the example below uses Piacentine cards.

|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |

The index is calculated by adding the values in every column containing `1`. For example:

|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1   |0  |1  |1  |0 |0 |0 |1|0|1|0|     |    |

The index is `1024 + 256 + 128 + 8 + 2 = 1418`. You do not need to calculate it yourself; use the table to find the index and word.


## Generate mnemonic with the Piacentine cards
With a 40-card Italian regional deck, such as Piacentine cards, draw one card at a time until you have enough entropy. Return each card to the deck and shuffle it before the next draw.

Like other regional Italian decks, Piacentine cards have four suits with ten cards each.
Cards 1 through 7 show one to seven suit symbols.
The remaining cards are:

- 8: Fante (Jack), a man holding the suit symbol
- 9: Donna (Queen), a woman holding the suit symbol
- 10: Re (King), a king holding the suit symbol

These court cards are called Fante, Donna, and Re. Depending on the game, they have values of 8, 9, and 10 respectively. Card 1 of each suit is called Asso (Ace).

For each card, find its value in the following table by matching:

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
