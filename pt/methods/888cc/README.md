---
layout: default
title: D8/D8/D8/moeda/moeda
lang: pt
permalink: /pt/methods/888cc/
---

## D8/D8/D8/moeda/moeda

Lance três D8 e duas moedas. Cara é `0` e coroa é `1`. O índice é `(primeiro D8 - 1) × 256 + (segundo D8 - 1) × 32 + (terceiro D8 - 1) × 4 + primeira moeda × 2 + segunda moeda`; consulte a [tabela completa](../../../methods/888cc/).

## Procedimento completo
1. Aplique a regra ate reunir 11 bits.
2. Registe os bits na ordem obtida.
3. Procure a palavra BIP-39 inglesa na tabela ligada.
4. Repita para 12 ou 24 palavras provisórias.
5. Corrija a palavra final.

[Voltar ao guia completo](../)
