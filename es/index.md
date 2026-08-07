---
layout: default
title: Generar una frase mnemónica sin conexión
description: Guía para crear palabras BIP-39 con aleatoriedad física.
lang: es
---

<section class="hero">
  <div class="eyebrow">Aleatoriedad física verificable a mano</div>
  <h1>Genera palabras mnemónicas desde el mundo real.</h1>
  <p>TRMG convierte resultados de dados, monedas y cartas en índices BIP-39. Registra 11 bits para cada palabra provisional y corrige sin conexión la palabra de suma de comprobación final.</p>
  <a class="button" href="#methods">Elegir un método</a>
</section>

## Cómo funciona

Cada método produce un número de 11 bits entre `0` y `2047`. Busca ese número en la tabla de palabras, repite hasta tener 12 o 24 palabras provisionales y corrige la última palabra.

> **La calidad de la entropía importa.** Usa solo dados, monedas o cartas que sean lo más justos y libres de sesgo posible. Revísalos para detectar daños o sesgos de fabricación y baraja las cartas a fondo entre extracciones. Una fuente física sesgada reduce la calidad de la entropía de la mnemónica resultante.

> **Úsalo bajo tu propia responsabilidad.** Estos métodos y este sitio web se proporcionan tal cual, sin ninguna garantía sobre la seguridad de tu mnemónica o tus fondos. Eres la única persona responsable de verificar el proceso y de cualquier pérdida de fondos derivada de su uso.

> **Haz una copia de seguridad segura de tu mnemónica.** Una copia de seguridad confiable y sin conexión es esencial para no perder el acceso a tus fondos. Guárdala protegida contra pérdidas, daños, robos y accesos no autorizados; nunca dependas de una sola copia ni de una captura de pantalla digital.

> **Limita la exposición de tu mnemónica.** No copies ni introduzcas tu mnemónica en varios dispositivos u ordenadores. Úsala solo con la cartera de software o hardware para la que fue generada y únicamente cuando sea necesario.

## Métodos {#methods}

|Método|Cómo produce cada palabra provisional|
|------|-------------------------------------|
|[Moneda](methods/coin/)|Once lanzamientos: cara es `0` y cruz es `1`.|
|[D6](methods/d6/)|Convierte cada tirada en uno o dos bits.|
|[D8](methods/d8/)|Cuatro tiradas producen 12 bits; conserva los primeros 11.|
|[D8/D16/D16](methods/d8d16d16/)|Tres dados seleccionan un índice en una sola ronda.|
|[D8/D8/D8/moneda/moneda](methods/888cc/)|Tres tiradas y dos lanzamientos seleccionan un índice.|
|[Póquer](methods/poker/)|Roba una carta, conviértela en bits, devuélvela y baraja.|
|[Cartas piacentinas](methods/piacentine/)|Usa una baraja regional italiana de 40 cartas.|
|[Tarot](methods/tarot/)|Usa las 78 cartas y sus valores de bits por nivel.|

## Corregir la última palabra {#correct-the-final-word}

Para una mnemónica de 12 palabras, genera 12 palabras provisionales y corrige solo la duodécima. Para una de 24, genera 24 y corrige solo la vigesimocuarta. La última palabra combina entropía y la suma de comprobación BIP-39.

|Longitud|Parte conservada de la última palabra provisional|Candidatas del grupo|
|--------|-----------------------------------------------|--------------------|
|12 palabras|Primeros 7 bits|16|
|24 palabras|Primeros 3 bits|128|

Encuentra el grupo en la [tabla binaria de palabras](../tables/binary-table/) y usa una cartera o herramienta BIP-39 confiable y sin conexión para obtener la candidata correcta. Nunca introduzcas tu mnemónica en un sitio web ni en un dispositivo no confiable.
