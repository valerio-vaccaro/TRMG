---
layout: default
title: D8/D16/D16
lang: es
permalink: /es/methods/d8d16d16/
---

## D8/D16/D16

Lanza un D8 y dos D16. El índice es `(D8 - 1) × 256 + (primer D16 - 1) × 16 + (segundo D16 - 1)`. Cada serie selecciona directamente un índice; consulta la [tabla completa](../../../methods/d8ff/).

## Procedimiento completo
1. Aplica la regla hasta reunir 11 bits.
2. Anota los bits en orden.
3. Busca la palabra BIP-39 inglesa en la tabla enlazada.
4. Repite para 12 o 24 palabras provisionales.
5. Corrige la última palabra.

[Volver a la guía completa](../)
