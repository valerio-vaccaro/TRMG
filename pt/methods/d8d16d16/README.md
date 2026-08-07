---
layout: default
title: D8/D16/D16
lang: pt
permalink: /pt/methods/d8d16d16/
---

## D8/D16/D16

Lance um D8 e dois D16. O índice é `(D8 - 1) × 256 + (primeiro D16 - 1) × 16 + (segundo D16 - 1)`. Cada série seleciona um índice; consulte a [tabela completa](../../../methods/d8ff/).

## Procedimento completo
1. Aplique a regra ate reunir 11 bits.
2. Registe os bits na ordem obtida.
3. Procure a palavra BIP-39 inglesa na tabela ligada.
4. Repita para 12 ou 24 palavras provisórias.
5. Corrija a palavra final.

[Voltar ao guia completo](../)
