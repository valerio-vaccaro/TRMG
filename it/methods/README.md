---
layout: default
title: Guida ai metodi
description: Creare parole BIP-39 con monete, dadi e carte.
lang: it
permalink: /it/methods/
---

## Guida ai metodi

Ogni metodo produce un indice di 11 bit per una parola BIP-39 provvisoria. Genera 12 o 24 parole provvisorie e poi correggi l'ultima come descritto nella pagina iniziale italiana.

<a id="coin"></a>
### Moneta

Lancia la moneta 11 volte per ogni parola: testa è `0` e croce è `1`. Leggi i bit da sinistra a destra e cerca la parola nella [tabella binaria](../../tables/binary-table/).

<a id="d6"></a>
### D6

Converti `1–4` in `00`, `01`, `10`, `11`; `5` è `0` e `6` è `1`. Lancia finché non raccogli 11 bit; se l'ultimo risultato è troppo lungo, conserva solo i bit necessari a sinistra.

<a id="d8"></a>
### D8

Converti `1–8` in `000–111`. Quattro lanci producono 12 bit: conserva i primi 11 e cercali nella tabella binaria.

<a id="d8d16d16"></a>
### D8/D16/D16

Lancia un D8 e due D16. L'indice è `(D8 - 1) × 256 + (primo D16 - 1) × 16 + (secondo D16 - 1)`. Ogni serie seleziona un indice; consulta la [tabella completa](../../methods/d8ff/).

<a id="888cc"></a>
### D8/D8/D8/moneta/moneta

Lancia tre D8 e due monete. Testa è `0` e croce è `1`. L'indice è `(primo D8 - 1) × 256 + (secondo D8 - 1) × 32 + (terzo D8 - 1) × 4 + prima moneta × 2 + seconda moneta`; consulta la [tabella completa](../../methods/888cc/).

<a id="poker"></a>
### Carte da poker

Usa un mazzo standard di 52 carte senza Joker. Converti ogni carta con la [tabella del poker](../../methods/poker/), rimettila nel mazzo e mescola fino a raccogliere 11 bit.

<a id="piacentine"></a>
### Carte piacentine

Usa un mazzo piacentino da 40 carte. Raccogli 11 bit con la [tabella delle carte](../../methods/piacentine/); rimetti e mescola dopo ogni estrazione.

<a id="tarot"></a>
### Tarocchi

Usa tutte le 78 carte. Il livello di ogni carta fornisce da uno a sei bit; estrai, annota, rimetti e mescola fino a raccogliere 11 bit. Consulta la [tabella dei Tarocchi](../../methods/tarot/).
