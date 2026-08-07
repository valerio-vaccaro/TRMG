---
layout: default
title: Método com D6
description: Gera índices de palavras BIP-39 com um dado de seis faces.
lang: pt
permalink: /pt/methods/d6/
---

## Gere uma frase de recuperação com um D6

Os resultados 1 a 4 fornecem dois bits e 5 e 6 fornecem um. Continue até ter 11 bits, repita para 12 ou 24 palavras e siga o [procedimento da última palavra](../../#corrigir-a-ultima-palavra).

|Resultado|Bits|
|------|----|
|1|00|
|2|01|
|3|10|
|4|11|
|5|0|
|6|1|

Se o último lançamento fornecer bits a mais, mantenha apenas os bits à esquerda necessários. Use a [tabela binária de palavras](../../../tables/binary-table/).
