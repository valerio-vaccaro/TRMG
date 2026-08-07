---
layout: default
title: Guía de métodos
description: Crear palabras BIP-39 con monedas, dados y cartas.
lang: es
permalink: /es/methods/
---

## Guía de métodos

Cada método crea un índice de 11 bits para una palabra BIP-39 provisional. Genera 12 o 24 palabras provisionales y después corrige la última como se explica en la página principal en español.

<a id="coin"></a>
### Moneda

Lanza la moneda 11 veces por palabra: cara es `0` y cruz es `1`. Lee los bits de izquierda a derecha y busca la palabra en la [tabla binaria](../../tables/binary-table/).

<a id="d6"></a>
### D6

Convierte `1–4` en `00`, `01`, `10`, `11`; `5` es `0` y `6` es `1`. Tira hasta reunir 11 bits; si la última tirada aporta demasiados, conserva solo los bits izquierdos necesarios.

<a id="d8"></a>
### D8

Convierte `1–8` en `000–111`. Cuatro tiradas producen 12 bits: conserva los primeros 11 y búscalos en la tabla binaria.

<a id="d8d16d16"></a>
### D8/D16/D16

Lanza un D8 y dos D16. El índice es `(D8 - 1) × 256 + (primer D16 - 1) × 16 + (segundo D16 - 1)`. Cada serie selecciona directamente un índice; consulta la [tabla completa](d8d16d16/).

<a id="888cc"></a>
### D8/D8/D8/moneda/moneda

Lanza tres D8 y dos monedas. Cara es `0` y cruz es `1`. El índice es `(primer D8 - 1) × 256 + (segundo D8 - 1) × 32 + (tercer D8 - 1) × 4 + primera moneda × 2 + segunda moneda`; consulta la [tabla completa](888cc/).

<a id="poker"></a>
### Cartas de póquer

Usa una baraja estándar de 52 cartas sin comodines. Convierte cada carta con la [tabla de póquer](poker/), devuélvela al mazo y baraja hasta reunir 11 bits.

<a id="piacentine"></a>
### Cartas piacentinas

Usa una baraja piacentina de 40 cartas. Reúne 11 bits con la [tabla de cartas](piacentine/); devuelve y baraja después de cada extracción.

<a id="tarot"></a>
### Tarot

Usa las 78 cartas. Su nivel aporta entre uno y seis bits; roba, registra, devuelve y baraja hasta reunir 11 bits. Consulta la [tabla de Tarot](tarot/).
