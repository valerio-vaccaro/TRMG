---
layout: default
title: Metodo della moneta
description: Genera indici di parole BIP-39 con lanci di moneta.
lang: it
permalink: /it/methods/coin/
---

## Genera una frase mnemonica con una moneta

Questo è il metodo più semplice: richiede soltanto una moneta equa. Ogni lancio fornisce un bit, quindi genera ogni parola BIP-39 provvisoria con 11 lanci. Ripeti per 12 o 24 parole, quindi segui la [procedura per l’ultima parola](../../#correggi-lultima-parola).

Lancia la moneta 11 volte per ogni parola e usa questa tabella di conversione:

|Risultato|Bit|
|------|---|
|Testa|0|
|Croce|1|

Leggi gli 11 risultati da sinistra a destra e usa la [tabella binaria delle parole](../../tables/binary-table/) per associare il valore ottenuto a una parola BIP-39.
