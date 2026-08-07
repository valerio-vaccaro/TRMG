---
layout: default
title: Método con D6
description: Genera índices de palabras BIP-39 con un dado de seis caras.
lang: es
permalink: /es/methods/d6/
---

## Genera una frase de recuperación con un D6

Este método usa un dado normal de seis caras. Los resultados del 1 al 4 aportan dos bits y 5 y 6 aportan uno; continúa hasta reunir 11 bits. Repite para 12 o 24 palabras y sigue el [procedimiento para la última palabra](../../#corrige-la-ultima-palabra).

|Resultado|Bits|
|------|----|
|1|00|
|2|01|
|3|10|
|4|11|
|5|0|
|6|1|

Si el último lanzamiento aporta demasiados bits, conserva solo los bits de la izquierda necesarios para llegar a 11. Busca el valor obtenido en la [tabla binaria de palabras](../../../tables/binary-table/).
