---
layout: default
title: D8/D8/D8/moneda/moneda
lang: es
permalink: /es/methods/888cc/
---

## D8/D8/D8/moneda/moneda

Lanza tres D8 y dos monedas. Cara es `0` y cruz es `1`. El índice es `(primer D8 - 1) × 256 + (segundo D8 - 1) × 32 + (tercer D8 - 1) × 4 + primera moneda × 2 + segunda moneda`; consulta la [tabla completa](../../../methods/888cc/).

## Procedimiento completo
1. Aplica la regla hasta reunir 11 bits.
2. Anota los bits en orden.
3. Busca la palabra BIP-39 inglesa en la tabla enlazada.
4. Repite para 12 o 24 palabras provisionales.
5. Corrige la última palabra.

[Volver a la guía completa](../)
