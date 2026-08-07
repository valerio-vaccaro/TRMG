---
layout: default
title: 塔罗牌
lang: zh
permalink: /zh/methods/tarot/
---

## 塔罗牌

使用完整的 78 张塔罗牌。牌所属层级提供 1 至 6 位；抽牌、记录、放回并洗牌，直到获得 11 位。映射见[塔罗牌表](../../../methods/tarot/)。

## 完整流程
1. 按本页规则取得11位。
2. 按顺序记录比特。
3. 在链接表中查找英文BIP-39词。
4. 重复至12或24个临时词。
5. 校正最后一个词。

[返回完整方法指南](../)


## 完整查找表

## The Sacred Instrument

A standard Tarot deck holds **78 cards**. All 78 participate in this ritual — none are set aside, none are exiled. The cards are divided into four Arcane Tiers by their cosmic weight:

| Tier | Cards | Count | Bits per Draw | Arcane Meaning |
|------|-------|-------|---------------|----------------|
| I — The Mundane Veil | All Minor Arcana + The Fool through The Chariot (0–VII) | **64** | **6 bits** | The rich chaos of earthly experience |
| II — The Hidden Path | Strength through The Devil (VIII–XV) | **8** | **3 bits** | The trials of transformation |
| III — The Celestial Fire | The Tower through The Sun (XVI–XIX) | **4** | **2 bits** | The great upheavals of fate |
| IV — The Absolute | Judgement and The World (XX–XXI) | **2** | **1 bit** | The indivisible forces of ending and completion |

**Total: 64 + 8 + 4 + 2 = 78 cards.**

Each tier contributes bits equal to log₂ of its size: 2⁶=64, 2³=8, 2²=4, 2¹=2. Every card in a tier maps to a unique bit pattern within that tier.

## The Ritual of Drawing

1. Gather all 78 cards into a single unified deck.
2. Perform the **Opening Shuffle** seven times while reciting the Opening Invocation (see below).
3. For each bit sequence needed:
   - Draw the topmost card.
   - Read its Tier and record the bits from the corresponding table.
   - Return the card to the deck.
   - **Reshuffle** the deck while reciting the appropriate Reshuffle Incantation (see below).
   - Repeat until 11 bits are accumulated for the current word.
   - If the last draw yields more bits than needed, take only the leftmost bits required and discard the rest — they were not destined for this word.
4. Look up the 11-bit index in the [shared binary words table](../../tables/binary-table/) and record the word on paper.
5. Repeat until all 12 or 24 words are recorded.
6. Close the ritual (see: *Closing the Chamber*).

## The Sacred Incantations

*These formulas bind the will of the caster to the chaos of the universe. Speak them clearly, at a measured pace, without hesitation. A stumbled word requires the current shuffle to begin again.*

### Opening Invocation — spoken during the first seven shuffles

> *"Per ignem duodecim et tenebras sine fine,*
> *aperio ostium entropiae.*
> *Voci magistrorum obedio — Turing, Shannon, Diffie.*
> *Chaos ordinetur in verbo secreto."*
>
> *(By the twelve fires and the endless dark,*
> *I open the gate of entropy.*
> *I heed the voice of the masters — Turing, Shannon, Diffie.*
> *Let chaos be ordered into the secret word.)*

### Reshuffle Incantation — spoken during every reshuffle between draws

> *"Misceo fata, misceo sortes.*
> *Nulla memoria, nullus ordo.*
> *Arcanum redit in chaos.*
> *Fiat voluntas entropiae."*
>
> *(I mix the fates, I mix the lots.*
> *No memory, no order.*
> *The secret returns to chaos.*
> *Let the will of entropy be done.)*

### Invocation of the Absolute — spoken only when a Tier IV card (Judgement or The World) is drawn

> *"Vox ultima locuta est.*
> *Unus morsus de infinito.*
> *Gratum ago, O Finis."*
>
> *(The final voice has spoken.*
> *One bite of the infinite.*
> *I give thanks, O End.)*

## Tier I — The Mundane Veil (64 cards → 6 bits each)

This tier contains the eight lowest Major Arcana (0–VII) and all 56 Minor Arcana. Assign values 0–63 sequentially as shown. Record the full 6-bit binary of the drawn card.

### Tier I — Major Arcana section (values 0–7)

| Card | Value | Bits (6) |
|------|-------|----------|
| 0 The Fool | 0 | 000000 |
| I The Magician | 1 | 000001 |
| II The High Priestess | 2 | 000010 |
| III The Empress | 3 | 000011 |
| IV The Emperor | 4 | 000100 |
| V The Hierophant | 5 | 000101 |
| VI The Lovers | 6 | 000110 |
| VII The Chariot | 7 | 000111 |

### Tier I — Minor Arcana section (values 8–63)

| Suit | Rank | Value | Bits (6) |
|------|------|-------|----------|
| Wands | Ace | 8 | 001000 |
| Wands | 2 | 9 | 001001 |
| Wands | 3 | 10 | 001010 |
| Wands | 4 | 11 | 001011 |
| Wands | 5 | 12 | 001100 |
| Wands | 6 | 13 | 001101 |
| Wands | 7 | 14 | 001110 |
| Wands | 8 | 15 | 001111 |
| Wands | 9 | 16 | 010000 |
| Wands | 10 | 17 | 010001 |
| Wands | Page | 18 | 010010 |
| Wands | Knight | 19 | 010011 |
| Wands | Queen | 20 | 010100 |
| Wands | King | 21 | 010101 |
| Cups | Ace | 22 | 010110 |
| Cups | 2 | 23 | 010111 |
| Cups | 3 | 24 | 011000 |
| Cups | 4 | 25 | 011001 |
| Cups | 5 | 26 | 011010 |
| Cups | 6 | 27 | 011011 |
| Cups | 7 | 28 | 011100 |
| Cups | 8 | 29 | 011101 |
| Cups | 9 | 30 | 011110 |
| Cups | 10 | 31 | 011111 |
| Cups | Page | 32 | 100000 |
| Cups | Knight | 33 | 100001 |
| Cups | Queen | 34 | 100010 |
| Cups | King | 35 | 100011 |
| Swords | Ace | 36 | 100100 |
| Swords | 2 | 37 | 100101 |
| Swords | 3 | 38 | 100110 |
| Swords | 4 | 39 | 100111 |
| Swords | 5 | 40 | 101000 |
| Swords | 6 | 41 | 101001 |
| Swords | 7 | 42 | 101010 |
| Swords | 8 | 43 | 101011 |
| Swords | 9 | 44 | 101100 |
| Swords | 10 | 45 | 101101 |
| Swords | Page | 46 | 101110 |
| Swords | Knight | 47 | 101111 |
| Swords | Queen | 48 | 110000 |
| Swords | King | 49 | 110001 |
| Pentacles | Ace | 50 | 110010 |
| Pentacles | 2 | 51 | 110011 |
| Pentacles | 3 | 52 | 110100 |
| Pentacles | 4 | 53 | 110101 |
| Pentacles | 5 | 54 | 110110 |
| Pentacles | 6 | 55 | 110111 |
| Pentacles | 7 | 56 | 111000 |
| Pentacles | 8 | 57 | 111001 |
| Pentacles | 9 | 58 | 111010 |
| Pentacles | 10 | 59 | 111011 |
| Pentacles | Page | 60 | 111100 |
| Pentacles | Knight | 61 | 111101 |
| Pentacles | Queen | 62 | 111110 |
| Pentacles | King | 63 | 111111 |

## Tier II — The Hidden Path (8 cards → 3 bits each)

| Card | Value | Bits (3) |
|------|-------|----------|
| VIII Strength | 0 | 000 |
| IX The Hermit | 1 | 001 |
| X Wheel of Fortune | 2 | 010 |
| XI Justice | 3 | 011 |
| XII The Hanged Man | 4 | 100 |
| XIII Death | 5 | 101 |
| XIV Temperance | 6 | 110 |
| XV The Devil | 7 | 111 |

## Tier III — The Celestial Fire (4 cards → 2 bits each)

| Card | Value | Bits (2) |
|------|-------|----------|
| XVI The Tower | 0 | 00 |
| XVII The Star | 1 | 01 |
| XVIII The Moon | 2 | 10 |
| XIX The Sun | 3 | 11 |

## Tier IV — The Absolute (2 cards → 1 bit each)

*When one of these cards is drawn, speak the Invocation of the Absolute before reshuffling.*

| Card | Value | Bits (1) |
|------|-------|----------|
| XX Judgement | 0 | 0 |
| XXI The World | 1 | 1 |

## The Recording Tablet

Fill the columns from left (most significant bit) to right (least significant bit), one draw at a time. Each draw fills as many columns as its tier allows. When 11 columns are full, sum the column values to get the Index, then look up the BIP39 word.

|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |

Index is the sum of all column headers where the value is 1. Example:

|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1|0|1|0|0|1|1|0|0|1|0| |    |

Index = 1024+256+32+16+2 = **1330** → word: **novel**

### Example draw sequence for a single word

| Draw | Card Drawn | Tier | Bits Given | Bit Sequence So Far |
|------|-----------|------|-----------|---------------------|
| 1st | 5 of Cups (value 26) | I | 011010 | `011010` (6 bits) |
| 2nd | The Tower (value 0) | III | 00 | `01101000` (8 bits) |
| 3rd | The Hermit (value 1) | II | 001 | `01101000001` (11 bits ✓) |

Bits: `01101000001` → Index = 512+256+32+1 = **801** → word: **impose**

After draw 3, the remaining bits of The Hermit (if it had given more) would be discarded. In this case it gave exactly the 3 bits needed to complete 11.

## Entropy Assessment

Each draw samples uniformly from the full 78-card deck (after reshuffling). The expected bits recorded per draw:

| Tier | Cards | Bits | Probability | Expected bits |
|------|-------|------|-------------|---------------|
| I | 64 | 6 | 64/78 ≈ 0.821 | 4.923 |
| II | 8 | 3 | 8/78 ≈ 0.103 | 0.308 |
| III | 4 | 2 | 4/78 ≈ 0.051 | 0.103 |
| IV | 2 | 1 | 2/78 ≈ 0.026 | 0.026 |
| **Total** | **78** | | | **≈ 5.36 bits/draw** |

True entropy of each draw (full 78-card uniform sample): log₂(78) ≈ **6.28 bits**.
Recording efficiency: 5.36 / 6.28 ≈ **85%** — the remaining 15% is surrendered to the cosmic tiers, as offering.

To generate 11 recorded bits per word, expect approximately **2.1 draws per word** on average (11 ÷ 5.36).
For a **12-word** mnemonic (132 bits with checksum): ~25 draws.
For a **24-word** mnemonic (264 bits with checksum): ~50 draws.

*The checksum bits of the final word are not drawn from the Oracle — they are computed from the hash of all preceding entropy. Use a BIP39-compliant tool to derive and verify the complete mnemonic once all words but the last are known, or trust the last word fully to the Oracle and verify the checksum digitally afterward.*

## Closing the Chamber

Once all words are recorded on paper and the pen has been set down:

1. Gather all 78 cards and perform a final **thirteen-shuffle** while reciting:

   > *"Sigillum apponatur. Chaos recreatur.*
   > *Nemo scit, nemo videt, nemo meminit.*
   > *It is sealed."*

2. Wrap the deck in dark cloth. It must not be used for cartomancy or games on the same day it has served as Oracle.
3. Extinguish the twelve candles in **reverse order** — beginning from Satoshi Nakamoto (WSW) and moving counter-clockwise back to Alan Turing (North). Snuff each flame; do not blow. A breath scatters what was bound.
4. The photographs may be stored or destroyed according to the adept's security threat model. They have served their purpose: their entropy has been received.

*The mnemonic is sealed. Guard it as the masters guarded their secrets — with silence, with care, and with the knowledge that what is written can be found.*
