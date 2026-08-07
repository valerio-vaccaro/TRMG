---
layout: default
title: Metodo con D8
description: Genera indici di parole BIP-39 con un dado a otto facce.
lang: it
permalink: /it/methods/d8/
---

## Genera una frase mnemonica con un dado D8

Questo metodo usa un solo dado a otto facce. Ogni lancio fornisce tre bit, quindi quattro lanci forniscono 12 bit; conserva i primi 11 bit per ogni parola provvisoria. Ripeti per 12 o 24 parole, quindi segui la [procedura per l’ultima parola](../../#correggi-lultima-parola).

Lancia il dado quattro volte, usando questa tabella di conversione:

|Risultato|Bit|
|------|----|
|1|000|
|2|001|
|3|010|
|4|011|
|5|100|
|6|101|
|7|110|
|8|111|

Dopo quattro lanci, conserva soltanto gli 11 bit più a sinistra e scarta il bit finale.

Usa la [tabella binaria delle parole](../../../tables/binary-table/) per associare il valore ottenuto di 11 bit a una parola BIP-39.
