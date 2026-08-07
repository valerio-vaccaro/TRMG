---
layout: default
title: Méthode de la pièce
description: Génère des indices de mots BIP-39 avec des lancers de pièce.
lang: fr
permalink: /fr/methods/coin/
---

## Générer une phrase de récupération avec une pièce

C’est la méthode la plus simple : elle ne demande qu’une pièce équilibrée. Chaque lancer fournit un bit ; générez chaque mot BIP-39 provisoire avec 11 lancers. Répétez pour 12 ou 24 mots, puis suivez la [procédure du dernier mot](../../#corriger-le-dernier-mot).

|Résultat|Bit|
|------|---|
|Face|0|
|Pile|1|

Lisez les 11 résultats de gauche à droite et utilisez la [table binaire des mots](../../../tables/binary-table/) pour trouver le mot BIP-39.
