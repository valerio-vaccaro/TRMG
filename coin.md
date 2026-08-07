## Generate a mnemonic with a coin

This is the simplest method: it needs only a fair coin. Each flip supplies one bit, so generate each provisional BIP-39 word from 11 flips. Repeat for 12 or 24 words, then follow the [final-word procedure](README.md#correct-the-final-word).

Flip the coin 11 times for each word and use this conversion table:

|Result|Bit|
|------|---|
|Heads|0|
|Tails|1|

Read the 11 results from left to right and use the [binary words table](binary-table.md) to match the resulting value to a BIP-39 word.
