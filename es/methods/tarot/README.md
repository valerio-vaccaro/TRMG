---
layout: default
title: Método del Tarot
description: Genera índices de palabras BIP-39 con una baraja completa de Tarot.
lang: es
permalink: /es/methods/tarot/
---

# 🕯️ El ritual arcano para invocar una frase mnemónica 🕯️
Observado el uno de abril, Año del Señor 2026

*Antes de que el velo del reino digital sea desgarrado, el adepto debe preparar la Cámara Sagrada. Dispón doce velas en círculo — una por cada mes del ciclo solar, una por cada pilar del Zodíaco. Coloca entre las velas doce fotografías de los Grandes Criptomantes (véase: *El Consejo de los Doce*), todas mirando hacia el interior. Su entropía espectral, ligada a toda una vida dedicada al arte de los secretos, amplificará el fuego caótico de cada extracción.*

*Solo cuando el espacio ritual respire con su sabiduría conjunta podrán desellarse las Cartas del Oráculo.*

## Resumen del método

Este método usa las 78 cartas de una baraja de Tarot. Cada carta pertenece a un nivel que aporta entre uno y seis bits. Extrae, registra los bits asignados, devuelve la carta a la baraja y vuelve a mezclar hasta reunir 11 bits para una palabra provisional. Repite para 12 o 24 palabras y sigue el [procedimiento para la última palabra](../../#corrige-la-ultima-palabra).

## El Consejo de los Doce — guardianes del campo entrópico

Coloca una fotografía junto a cada vela, dispuestas en sentido horario a partir de la posición norte:

| Posición | Color de la vela | Criptomante | Reino |
|----------|-------------|--------------|-------|
| Norte | Blanco | Alan Turing | Padre de los misterios computables |
| NNE | Plata | Claude Shannon | Arconte de la teoría de la información |
| NE | Oro | Whitfield Diffie | Heraldo de la clave pública |
| ENE | Naranja | Martin Hellman | Guardián del velo exponencial |
| Este | Rojo | Ron Rivest | Primera hoja de RSA |
| ESE | Carmesí | Adi Shamir | Segunda hoja de RSA |
| SE | Azul oscuro | Leonard Adleman | Tercera hoja de RSA |
| SSE | Violeta | Ralph Merkle | Arquitecto del árbol hash |
| Sur | Verde | Bruce Schneier | Centinela de las artes aplicadas |
| SSO | Cian | Phil Zimmermann | Libertador del secreto bastante bueno |
| SO | Amarillo | Moxie Marlinspike | Susurrador del fuego de Signal |
| OSO | Negro | Satoshi Nakamoto | El innombrado, tejedor de cadenas |

*Enciende las doce velas simultáneamente, o tan cerca de ello como lo permitan las manos mortales. Pronuncia en voz alta el nombre de cada Criptomante mientras su vela se enciende. Su entropía acumulada — recogida de toda una vida dedicada a la creación de secretos — entra en el campo ritual e inclina la probabilidad a tu favor.*

## El instrumento sagrado

Una baraja estándar de Tarot contiene **78 cartas**. Las 78 participan en este ritual — ninguna queda aparte, ninguna es desterrada. Las cartas se dividen en cuatro Niveles Arcanos según su peso cósmico:

| Nivel | Cartas | Cantidad | Bits por extracción | Significado arcano |
|------|-------|-------|---------------|----------------|
| I — El velo mundano | Todos los Arcanos Menores + de El Loco a El Carro (0–VII) | **64** | **6 bits** | El rico caos de la experiencia terrenal |
| II — El sendero oculto | De La Fuerza a El Diablo (VIII–XV) | **8** | **3 bits** | Las pruebas de la transformación |
| III — El fuego celestial | De La Torre a El Sol (XVI–XIX) | **4** | **2 bits** | Los grandes trastornos del destino |
| IV — El Absoluto | El Juicio y El Mundo (XX–XXI) | **2** | **1 bit** | Las fuerzas indivisibles del final y la culminación |

**Total: 64 + 8 + 4 + 2 = 78 cartas.**

Cada nivel aporta un número de bits igual al log₂ de su tamaño: 2⁶=64, 2³=8, 2²=4, 2¹=2. Cada carta de un nivel corresponde a un patrón de bits único dentro de ese nivel.

## El ritual de la extracción

1. Reúne las 78 cartas en una única baraja unificada.
2. Realiza la **Mezcla de Apertura** siete veces mientras recitas la Invocación de Apertura (véase más abajo).
3. Para cada secuencia de bits necesaria:
   - Extrae la carta superior.
   - Lee su Nivel y registra los bits de la tabla correspondiente.
   - Devuelve la carta a la baraja.
   - **Vuelve a mezclar** la baraja mientras recitas la Fórmula de Remezcla correspondiente (véase más abajo).
   - Repite hasta acumular 11 bits para la palabra actual.
   - Si la última extracción aporta más bits de los necesarios, toma solo los bits situados más a la izquierda que se requieran y descarta el resto — no estaban destinados a esta palabra.
4. Busca el índice de 11 bits en la [tabla binaria compartida de palabras](../../../tables/binary-table/) y anota la palabra en papel.
5. Repite hasta anotar las 12 o 24 palabras.
6. Cierra el ritual (véase: *Cierre de la Cámara*).

## Las fórmulas sagradas

*Estas fórmulas ligan la voluntad del oficiante al caos del universo. Pronúncialas con claridad, a ritmo pausado, sin titubear. Una palabra tropezada obliga a reiniciar la mezcla en curso.*

### Invocación de Apertura — pronunciada durante las primeras siete mezclas

> *"Per ignem duodecim et tenebras sine fine,*
> *aperio ostium entropiae.*
> *Voci magistrorum obedio — Turing, Shannon, Diffie.*
> *Chaos ordinetur in verbo secreto."*
>
> *(Por los doce fuegos y la oscuridad sin fin,*
> *abro la puerta de la entropía.*
> *Obedezco la voz de los maestros — Turing, Shannon, Diffie.*
> *Que el caos se ordene en la palabra secreta.)*

### Fórmula de Remezcla — pronunciada en cada remezcla entre extracciones

> *"Misceo fata, misceo sortes.*
> *Nulla memoria, nullus ordo.*
> *Arcanum redit in chaos.*
> *Fiat voluntas entropiae."*
>
> *(Mezclo los destinos, mezclo las suertes.*
> *Sin memoria, sin orden.*
> *El secreto vuelve al caos.*
> *Hágase la voluntad de la entropía.)*

### Invocación del Absoluto — pronunciada solo cuando se extrae una carta de Nivel IV (El Juicio o El Mundo)

> *"Vox ultima locuta est.*
> *Unus morsus de infinito.*
> *Gratum ago, O Finis."*
>
> *(La voz final ha hablado.*
> *Un bocado del infinito.*
> *Doy gracias, oh Fin.)*

## Nivel I — El velo mundano (64 cartas → 6 bits cada una)

Este nivel contiene los ocho Arcanos Mayores más bajos (0–VII) y los 56 Arcanos Menores. Asigna los valores 0–63 secuencialmente como se muestra. Registra el binario completo de 6 bits de la carta extraída.

### Nivel I — sección de Arcanos Mayores (valores 0–7)

| Carta | Valor | Bits (6) |
|------|-------|----------|
| 0 El Loco | 0 | 000000 |
| I El Mago | 1 | 000001 |
| II La Sacerdotisa | 2 | 000010 |
| III La Emperatriz | 3 | 000011 |
| IV El Emperador | 4 | 000100 |
| V El Hierofante | 5 | 000101 |
| VI Los Enamorados | 6 | 000110 |
| VII El Carro | 7 | 000111 |

### Nivel I — sección de Arcanos Menores (valores 8–63)

| Palo | Rango | Valor | Bits (6) |
|------|------|-------|----------|
| Bastos | As | 8 | 001000 |
| Bastos | 2 | 9 | 001001 |
| Bastos | 3 | 10 | 001010 |
| Bastos | 4 | 11 | 001011 |
| Bastos | 5 | 12 | 001100 |
| Bastos | 6 | 13 | 001101 |
| Bastos | 7 | 14 | 001110 |
| Bastos | 8 | 15 | 001111 |
| Bastos | 9 | 16 | 010000 |
| Bastos | 10 | 17 | 010001 |
| Bastos | Sota | 18 | 010010 |
| Bastos | Caballo | 19 | 010011 |
| Bastos | Reina | 20 | 010100 |
| Bastos | Rey | 21 | 010101 |
| Copas | As | 22 | 010110 |
| Copas | 2 | 23 | 010111 |
| Copas | 3 | 24 | 011000 |
| Copas | 4 | 25 | 011001 |
| Copas | 5 | 26 | 011010 |
| Copas | 6 | 27 | 011011 |
| Copas | 7 | 28 | 011100 |
| Copas | 8 | 29 | 011101 |
| Copas | 9 | 30 | 011110 |
| Copas | 10 | 31 | 011111 |
| Copas | Sota | 32 | 100000 |
| Copas | Caballo | 33 | 100001 |
| Copas | Reina | 34 | 100010 |
| Copas | Rey | 35 | 100011 |
| Espadas | As | 36 | 100100 |
| Espadas | 2 | 37 | 100101 |
| Espadas | 3 | 38 | 100110 |
| Espadas | 4 | 39 | 100111 |
| Espadas | 5 | 40 | 101000 |
| Espadas | 6 | 41 | 101001 |
| Espadas | 7 | 42 | 101010 |
| Espadas | 8 | 43 | 101011 |
| Espadas | 9 | 44 | 101100 |
| Espadas | 10 | 45 | 101101 |
| Espadas | Sota | 46 | 101110 |
| Espadas | Caballo | 47 | 101111 |
| Espadas | Reina | 48 | 110000 |
| Espadas | Rey | 49 | 110001 |
| Oros | As | 50 | 110010 |
| Oros | 2 | 51 | 110011 |
| Oros | 3 | 52 | 110100 |
| Oros | 4 | 53 | 110101 |
| Oros | 5 | 54 | 110110 |
| Oros | 6 | 55 | 110111 |
| Oros | 7 | 56 | 111000 |
| Oros | 8 | 57 | 111001 |
| Oros | 9 | 58 | 111010 |
| Oros | 10 | 59 | 111011 |
| Oros | Sota | 60 | 111100 |
| Oros | Caballo | 61 | 111101 |
| Oros | Reina | 62 | 111110 |
| Oros | Rey | 63 | 111111 |

## Nivel II — El sendero oculto (8 cartas → 3 bits cada una)

| Carta | Valor | Bits (3) |
|------|-------|----------|
| VIII La Fuerza | 0 | 000 |
| IX El Ermitaño | 1 | 001 |
| X La Rueda de la Fortuna | 2 | 010 |
| XI La Justicia | 3 | 011 |
| XII El Colgado | 4 | 100 |
| XIII La Muerte | 5 | 101 |
| XIV La Templanza | 6 | 110 |
| XV El Diablo | 7 | 111 |

## Nivel III — El fuego celestial (4 cartas → 2 bits cada una)

| Carta | Valor | Bits (2) |
|------|-------|----------|
| XVI La Torre | 0 | 00 |
| XVII La Estrella | 1 | 01 |
| XVIII La Luna | 2 | 10 |
| XIX El Sol | 3 | 11 |

## Nivel IV — El Absoluto (2 cartas → 1 bit cada una)

*Cuando se extraiga una de estas cartas, pronuncia la Invocación del Absoluto antes de volver a mezclar.*

| Carta | Valor | Bits (1) |
|------|-------|----------|
| XX El Juicio | 0 | 0 |
| XXI El Mundo | 1 | 1 |

## La tabla de registro

Rellena las columnas de izquierda (bit más significativo) a derecha (bit menos significativo), una extracción a la vez. Cada extracción llena tantas columnas como permita su nivel. Cuando las 11 columnas estén completas, suma los valores de columna para obtener el Índice y busca la palabra BIP39.

|1024|512|256|128|64|32|16|8|4|2|1|Índice|Palabra|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |
|    |   |   |   |  |  |  | | | | |     |    |

El Índice es la suma de todas las cabeceras de columna cuyo valor es 1. Ejemplo:

|1024|512|256|128|64|32|16|8|4|2|1|Índice|Palabra|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1|0|1|0|0|1|1|0|0|1|0| |    |

Índice = 1024+256+32+16+2 = **1330** → palabra: **novel**

### Ejemplo de secuencia de extracción para una sola palabra

| Extracción | Carta extraída | Nivel | Bits aportados | Secuencia de bits acumulada |
|------|-----------|------|-----------|---------------------|
| 1ª | 5 de Copas (valor 26) | I | 011010 | `011010` (6 bits) |
| 2ª | La Torre (valor 0) | III | 00 | `01101000` (8 bits) |
| 3ª | El Ermitaño (valor 1) | II | 001 | `01101000001` (11 bits ✓) |

Bits: `01101000001` → Índice = 512+256+32+1 = **801** → palabra: **impose**

Tras la 3ª extracción, los bits restantes de El Ermitaño (si hubiera aportado más) se descartarían. En este caso aportó exactamente los 3 bits necesarios para completar 11.

## Evaluación de la entropía

Cada extracción muestrea de forma uniforme la baraja completa de 78 cartas (tras remezclar). Los bits esperados registrados por extracción:

| Nivel | Cartas | Bits | Probabilidad | Bits esperados |
|------|-------|------|-------------|---------------|
| I | 64 | 6 | 64/78 ≈ 0,821 | 4,923 |
| II | 8 | 3 | 8/78 ≈ 0,103 | 0,308 |
| III | 4 | 2 | 4/78 ≈ 0,051 | 0,103 |
| IV | 2 | 1 | 2/78 ≈ 0,026 | 0,026 |
| **Total** | **78** | | | **≈ 5,36 bits/extracción** |

Entropía real de cada extracción (muestra uniforme de la baraja completa de 78 cartas): log₂(78) ≈ **6,28 bits**.
Eficiencia de registro: 5,36 / 6,28 ≈ **85%** — el 15% restante se entrega a los niveles cósmicos, como ofrenda.

Para generar 11 bits registrados por palabra, cabe esperar aproximadamente **2,1 extracciones por palabra** de media (11 ÷ 5,36).
Para una mnemónica de **12 palabras** (132 bits con checksum): ~25 extracciones.
Para una mnemónica de **24 palabras** (264 bits con checksum): ~50 extracciones.

*Los bits de checksum de la última palabra no se extraen del Oráculo — se calculan a partir del hash de toda la entropía precedente. Usa una herramienta compatible con BIP39 para derivar y verificar la mnemónica completa una vez conocidas todas las palabras salvo la última, o confía la última palabra por completo al Oráculo y verifica el checksum digitalmente después.*

## Cierre de la Cámara

Una vez anotadas todas las palabras en papel y depositada la pluma:

1. Reúne las 78 cartas y realiza una última **mezcla de trece veces** mientras recitas:

   > *"Sigillum apponatur. Chaos recreatur.*
   > *Nemo scit, nemo videt, nemo meminit.*
   > *It is sealed."*

2. Envuelve la baraja en un paño oscuro. No debe usarse para cartomancia ni juegos el mismo día en que ha servido de Oráculo.
3. Apaga las doce velas en **orden inverso** — comenzando por Satoshi Nakamoto (OSO) y avanzando en sentido antihorario hasta Alan Turing (Norte). Extingue cada llama; no soples. Un soplo dispersa lo que fue ligado.
4. Las fotografías pueden guardarse o destruirse según el modelo de amenazas del adepto. Han cumplido su propósito: su entropía ha sido recibida.

*La mnemónica queda sellada. Guárdala como los maestros guardaban sus secretos — con silencio, con cuidado y con la certeza de que lo que está escrito puede ser hallado.*
