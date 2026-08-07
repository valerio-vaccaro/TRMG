---
layout: default
title: Método de moneda
description: Genera índices de palabras BIP-39 con lanzamientos de moneda.
lang: es
permalink: /es/methods/coin/
---

## Genera una frase de recuperación con una moneda

Este es el método más sencillo: solo requiere una moneda equilibrada. Cada lanzamiento aporta un bit; genera cada palabra BIP-39 provisional con 11 lanzamientos. Repite para 12 o 24 palabras y sigue el [procedimiento para la última palabra](../../#corrige-la-ultima-palabra).

Lanza la moneda 11 veces por palabra:

|Resultado|Bit|
|------|---|
|Cara|0|
|Cruz|1|

Lee los 11 resultados de izquierda a derecha y usa la [tabla binaria de palabras](../../../tables/binary-table/) para obtener la palabra BIP-39.
