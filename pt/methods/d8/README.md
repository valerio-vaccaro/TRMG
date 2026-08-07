---
layout: default
title: Método com D8
description: Gera índices de palavras BIP-39 com um dado de oito faces.
lang: pt
permalink: /pt/methods/d8/
---

## Gere uma frase de recuperação com um D8

Cada lançamento fornece três bits; quatro lançamentos fornecem 12. Guarde os primeiros 11 bits por palavra, repita para 12 ou 24 palavras e siga o [procedimento da última palavra](../../#corrigir-a-ultima-palavra).

|Resultado|Bits|
|------|----|
|1|000|
|2|001|
|3|010|
|4|011|
|5|100|
|6|101|
|7|110|
|8|111|

Descarte o último bit e use a [tabela binária de palavras](../../../tables/binary-table/).
