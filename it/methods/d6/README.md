---
layout: default
title: Metodo con D6
description: Genera indici di parole BIP-39 con un dado a sei facce.
lang: it
permalink: /it/methods/d6/
---

## Genera una frase mnemonica con un dado D6

Questo metodo usa un dado standard a sei facce. I risultati da 1 a 4 forniscono due bit ciascuno, mentre i risultati 5 e 6 ne forniscono uno; il numero di lanci necessario per ogni parola provvisoria varia quindi di conseguenza. Continua fino ad avere 11 bit, ripeti per 12 o 24 parole e poi segui la [procedura per l’ultima parola](../../#correggi-lultima-parola).

Lancia il dado finché non hai 11 bit, usando questa tabella di conversione:

|Risultato|Bit|
|------|----|
|1|00|
|2|01|
|3|10|
|4|11|
|5|0|
|6|1|

Se l’ultimo lancio fornisce più bit del necessario, conserva soltanto i bit più a sinistra necessari per arrivare a 11 bit.

Leggi da sinistra a destra il valore di 11 bit accumulato e usa la [tabella binaria delle parole](../../tables/binary-table/) per trovare la parola BIP-39.
