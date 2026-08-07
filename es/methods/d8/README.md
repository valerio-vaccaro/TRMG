---
layout: default
title: Método con D8
description: Genera índices de palabras BIP-39 con un dado de ocho caras.
lang: es
permalink: /es/methods/d8/
---

## Genera una frase de recuperación con un D8

Cada lanzamiento de un D8 aporta tres bits; cuatro lanzamientos dan 12 bits. Conserva los primeros 11 bits por palabra provisional, repite para 12 o 24 palabras y sigue el [procedimiento para la última palabra](../../#corrige-la-ultima-palabra).

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

Tras cuatro lanzamientos, descarta el último bit. Usa la [tabla binaria de palabras](../../../tables/binary-table/) para encontrar la palabra BIP-39.
