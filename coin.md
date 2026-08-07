## Generate a mnemonic with a coin

Use a coin to generate 12 or 24 words. Each word requires 11 bits of entropy.

Flip the coin 11 times for each word and use this conversion table:

|Result|Bit|
|------|---|
|Heads|0|
|Tails|1|

Use the [binary words table](binary-table.md) to match the resulting 11-bit value to a BIP-39 word.
