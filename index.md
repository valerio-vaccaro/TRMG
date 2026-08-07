---
layout: default
title: Generate a mnemonic offline
description: Physical randomness methods for creating BIP-39 mnemonic words.
lang: en
---

<section class="hero">
  <div class="eyebrow">Physical entropy, verifiable by hand</div>
  <h1>Generate mnemonic words from the real world.</h1>
  <p>TRMG maps dice, coins, and cards to BIP-39 word indices. Choose a method, record 11 bits for each provisional word, and correct the final word checksum offline.</p>
  <a class="button" href="#methods">Choose a method</a>
</section>

## How it works

Each method produces an 11-bit number from `0` to `2047`. Use that number to find a BIP-39 word, repeat until you have 12 or 24 provisional words, then [correct the final word](#correct-the-final-word).

## Methods

|Method|How it produces each provisional word|
|------|--------------------------------------|
|[Coin](methods/coin/)|Eleven flips make one 11-bit word index.|
|[D6](methods/d6/)|Convert six-sided die rolls into one or two bits.|
|[D8](methods/d8/)|Four rolls create 12 bits; retain the first 11.|
|[D8/D16/D16](methods/d8ff/)|Three dice select one word index in a single set of rolls.|
|[D8/D8/D8/coin/coin](methods/888cc/)|Three D8 rolls and two flips select one word index.|
|[Poker cards](methods/poker/)|Draw, map the card to bits, return it, and reshuffle.|
|[Piacentine cards](methods/piacentine/)|Use a 40-card regional Italian deck to collect bits.|
|[Tarot](methods/tarot/)|Use all 78 cards and their tier-based bit values.|

## Correct the final word

For a 12-word mnemonic, generate 12 provisional words and correct only the 12th. For a 24-word mnemonic, generate 24 provisional words and correct only the 24th. The final word combines entropy with a BIP-39 checksum, so the provisional final word identifies a group rather than a guaranteed valid word.

|Mnemonic length|Keep from provisional final word|Candidates in its group|
|---------------|--------------------------------|-----------------------|
|12 words|First 7 bits|16|
|24 words|First 3 bits|128|

Use the [binary words table](tables/binary-table/) to find the group, then use an offline, trusted BIP-39-compatible wallet or tool to calculate the valid candidate from the preceding words. Only one candidate in that group has the correct checksum.

Never type your mnemonic into a website or an untrusted device.
