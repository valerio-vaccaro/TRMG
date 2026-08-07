---
layout: default
title: Guia de métodos
description: Criar palavras BIP-39 com moedas, dados e cartas.
lang: pt
permalink: /pt/methods/
---

## Guia de métodos

Cada método produz um índice de 11 bits para uma palavra BIP-39 provisória. Gere 12 ou 24 palavras provisórias e corrija a última conforme a página inicial em português.

<a id="coin"></a>
### Moeda

Lance a moeda 11 vezes por palavra: cara é `0` e coroa é `1`. Leia os bits da esquerda para a direita e procure a palavra na [tabela binária](../../tables/binary-table/).

<a id="d6"></a>
### D6

Converta `1–4` em `00`, `01`, `10`, `11`; `5` é `0` e `6` é `1`. Lance até reunir 11 bits; se o último resultado for longo demais, mantenha apenas os bits necessários à esquerda.

<a id="d8"></a>
### D8

Converta `1–8` em `000–111`. Quatro lançamentos produzem 12 bits: mantenha os primeiros 11 e procure-os na tabela binária.

<a id="d8d16d16"></a>
### D8/D16/D16

Lance um D8 e dois D16. O índice é `(D8 - 1) × 256 + (primeiro D16 - 1) × 16 + (segundo D16 - 1)`. Cada série seleciona um índice; consulte a [tabela completa](d8d16d16/).

<a id="888cc"></a>
### D8/D8/D8/moeda/moeda

Lance três D8 e duas moedas. Cara é `0` e coroa é `1`. O índice é `(primeiro D8 - 1) × 256 + (segundo D8 - 1) × 32 + (terceiro D8 - 1) × 4 + primeira moeda × 2 + segunda moeda`; consulte a [tabela completa](888cc/).

<a id="poker"></a>
### Cartas de póquer

Use um baralho de 52 cartas sem Jokers. Converta cada carta com a [tabela de póquer](poker/), devolva-a e baralhe até reunir 11 bits.

<a id="piacentine"></a>
### Cartas piacentinas

Use um baralho piacentino de 40 cartas. Reúna 11 bits com a [tabela de cartas](piacentine/); devolva e baralhe após cada retirada.

<a id="tarot"></a>
### Tarot

Use as 78 cartas. O seu nível fornece entre um e seis bits; retire, registe, devolva e baralhe até reunir 11 bits. Consulte a [tabela de Tarot](tarot/).
