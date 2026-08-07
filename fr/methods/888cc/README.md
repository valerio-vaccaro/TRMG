---
layout: default
title: D8/D8/D8/pièce/pièce
lang: fr
permalink: /fr/methods/888cc/
---

## D8/D8/D8/pièce/pièce

Lancez trois D8 et deux pièces. Pile vaut `0` et face vaut `1`. L'indice est `(premier D8 - 1) × 256 + (second D8 - 1) × 32 + (troisième D8 - 1) × 4 + première pièce × 2 + seconde pièce`; consultez la [table complète](../../../methods/888cc/).

## Procédure complète
1. Appliquez la règle jusqu à 11 bits.
2. Notez les bits dans leur ordre.
3. Cherchez le mot BIP-39 anglais dans la table liée.
4. Répétez pour 12 ou 24 mots provisoires.
5. Corrigez le dernier mot.

[Retour au guide complet](../)
