---
layout: default
title: Metodo con carte piacentine
description: Genera indici di parole BIP-39 con carte piacentine.
lang: it
permalink: /it/methods/piacentine/
---

## Genera una frase mnemonica con carte piacentine

Questo metodo usa un mazzo piacentino di 40 carte, oppure un altro mazzo regionale italiano con la stessa struttura. Ogni estrazione corrisponde a una sequenza di bit nella tabella sottostante; accumula 11 bit per ogni parola provvisoria, ripeti per 12 o 24 parole e poi segui la [procedura per l’ultima parola](../../#correggi-lultima-parola).

Usa una tabella come la seguente per registrare i risultati delle estrazioni nell’ordine in cui sono estratte.

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Parola|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |

L’indice si calcola sommando i valori di ogni colonna che contiene `1`. Per esempio:

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Parola|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1   |0  |1  |1  |0 |0 |0 |1|0|1|0|     |    |

L’indice è `1024 + 256 + 128 + 8 + 2 = 1418`. Non è necessario calcolarlo manualmente; usa la [tabella binaria condivisa delle parole](../../../tables/binary-table/) per trovare indice e parola.


## Corrispondenza carte-bit
Con un mazzo regionale italiano di 40 carte, come le carte piacentine, estrai una carta alla volta finché non hai entropia sufficiente. Rimetti ogni carta nel mazzo e mescola prima dell’estrazione successiva.

Come gli altri mazzi regionali italiani, le carte piacentine hanno quattro semi con dieci carte ciascuno.
Le carte da 1 a 7 mostrano da uno a sette simboli del seme.
Le carte rimanenti sono:

- 8: Fante, un uomo che tiene il simbolo del seme
- 9: Donna, una donna che tiene il simbolo del seme
- 10: Re, un re che tiene il simbolo del seme

Queste figure sono chiamate Fante, Donna e Re. A seconda del gioco, hanno rispettivamente valori 8, 9 e 10. La carta 1 di ogni seme è chiamata Asso.

Per ogni carta, trova il suo valore nella tabella seguente abbinando:

- il seme (Coppe, Denari, Bastoni, Spade)
- il valore (A per Asso, 2-7, 8/J per Fante, 9/Q per Donna, 10/K per Re).


Seme     |Valore|Bit|
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
