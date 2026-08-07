---
layout: default
title: Piacentine-Kartenmethode
description: Erzeuge BIP-39-Wortindizes mit Piacentine-Karten.
lang: de
permalink: /de/methods/piacentine/
---

## Erzeuge eine Wiederherstellungsphrase mit Piacentine-Karten

Diese Methode nutzt ein Piacentine-Deck mit 40 Karten oder ein anderes italienisches Regionaldeck mit gleicher Struktur. Jede Karte liefert eine Bitfolge. Sammle 11 Bits pro vorläufigem Wort, wiederhole dies für 12 oder 24 Wörter und folge dem [Verfahren für das letzte Wort](../../#korrigiere-das-letzte-wort).

|1024|512|256|128|64|32|16|8|4|2|1|Index|Wort|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |

Der Index ist die Summe der Spalten mit `1`. Beispiel:

|1024|512|256|128|64|32|16|8|4|2|1|Index|Wort|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1   |0  |1  |1  |0 |0 |0 |1|0|1|0|     |    |

Der Index ist `1024 + 256 + 128 + 8 + 2 = 1418`. Verwende die [gemeinsame binäre Worttabelle](../../../tables/binary-table/).

## Karten-Bit-Zuordnung

Ziehe Karten, lege jede zurück und mische, bis genügend Entropie vorhanden ist. Piacentine-Karten haben vier Farben mit je zehn Karten; 8/J, 9/Q und 10/K sind Fante, Donna und Re.

Farbe    |Rang|Bitfolge|
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
