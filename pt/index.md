---
layout: default
title: Gerar uma frase mnemónica offline
description: Guia para criar palavras BIP-39 com aleatoriedade física.
lang: pt
---

<section class="hero">
  <div class="eyebrow">Aleatoriedade física verificável à mão</div>
  <h1>Gere palavras mnemónicas a partir do mundo real.</h1>
  <p>O TRMG converte resultados de dados, moedas e cartas em índices BIP-39. Registe 11 bits para cada palavra provisória e corrija offline a palavra final de verificação.</p>
  <a class="button" href="#methods">Escolher um método</a>
</section>

## Como funciona

Cada método produz um número de 11 bits entre `0` e `2047`. Procure esse número na tabela de palavras, repita até ter 12 ou 24 palavras provisórias e corrija a palavra final.

## Métodos

|Método|Como produz cada palavra provisória|
|------|-----------------------------------|
|[Moeda](../methods/coin/)|Onze lançamentos: cara é `0` e coroa é `1`.|
|[D6](../methods/d6/)|Converta cada lançamento em um ou dois bits.|
|[D8](../methods/d8/)|Quatro lançamentos produzem 12 bits; conserve os primeiros 11.|
|[D8/D16/D16](../methods/d8ff/)|Três dados selecionam um índice numa única ronda.|
|[D8/D8/D8/moeda/moeda](../methods/888cc/)|Três lançamentos e duas moedas selecionam um índice.|
|[Cartas de póquer](../methods/poker/)|Retire uma carta, converta-a em bits, devolva-a e baralhe.|
|[Cartas piacentinas](../methods/piacentine/)|Use um baralho regional italiano de 40 cartas.|
|[Tarot](../methods/tarot/)|Use as 78 cartas e os valores de bits por nível.|

## Corrigir a palavra final

Numa mnemónica de 12 palavras, gere 12 palavras provisórias e corrija apenas a décima segunda. Numa de 24, gere 24 e corrija apenas a vigésima quarta. A palavra final combina entropia e a soma de verificação BIP-39.

|Comprimento|Parte mantida da palavra final provisória|Candidatas no grupo|
|-----------|------------------------------------------|-------------------|
|12 palavras|Primeiros 7 bits|16|
|24 palavras|Primeiros 3 bits|128|

Encontre o grupo na [tabela binária de palavras](../tables/binary-table/) e use uma carteira ou ferramenta BIP-39 confiável e offline para obter a candidata correta. Nunca introduza a sua mnemónica num site ou dispositivo não confiável.
