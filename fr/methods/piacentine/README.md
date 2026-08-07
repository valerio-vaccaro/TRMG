---
layout: default
title: Méthode des cartes piacentines
description: Génère des indices de mots BIP-39 avec des cartes piacentines.
lang: fr
permalink: /fr/methods/piacentine/
---

## Générer une phrase de récupération avec des cartes piacentines

Utilisez un jeu piacentin de 40 cartes. Chaque carte fournit des bits ; accumulez-en 11 par mot, répétez pour 12 ou 24 mots, puis suivez la [procédure du dernier mot](../../#corriger-le-dernier-mot).

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Mot|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Mot|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1   |0  |1  |1  |0 |0 |0 |1|0|1|0|     |    |

Utilisez la [table binaire des mots](../../../tables/binary-table/).

## Correspondance cartes-bits

Couleur  |Rang|Bits|
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
