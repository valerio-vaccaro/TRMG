---
layout: default
title: Méthode avec D8
description: Génère des indices de mots BIP-39 avec un dé à huit faces.
lang: fr
permalink: /fr/methods/d8/
---

## Générer une phrase de récupération avec un D8

Chaque lancer fournit trois bits ; quatre lancers en donnent 12. Gardez les 11 premiers bits de chaque mot provisoire, répétez pour 12 ou 24 mots, puis suivez la [procédure du dernier mot](../../#corriger-le-dernier-mot).

|Résultat|Bits|
|------|----|
|1|000|
|2|001|
|3|010|
|4|011|
|5|100|
|6|101|
|7|110|
|8|111|

Après quatre lancers, écartez le dernier bit et utilisez la [table binaire des mots](../../../tables/binary-table/).
