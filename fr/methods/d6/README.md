---
layout: default
title: Méthode avec D6
description: Génère des indices de mots BIP-39 avec un dé à six faces.
lang: fr
permalink: /fr/methods/d6/
---

## Générer une phrase de récupération avec un D6

Les résultats de 1 à 4 fournissent deux bits, et 5 et 6 un bit. Lancez jusqu’à obtenir 11 bits, répétez pour 12 ou 24 mots, puis suivez la [procédure du dernier mot](../../#corriger-le-dernier-mot).

|Résultat|Bits|
|------|----|
|1|00|
|2|01|
|3|10|
|4|11|
|5|0|
|6|1|

Si le dernier lancer donne trop de bits, ne gardez que les bits de gauche nécessaires. Utilisez la [table binaire des mots](../../../tables/binary-table/).
