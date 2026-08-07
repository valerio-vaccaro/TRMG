---
layout: default
title: Guide des méthodes
description: Créer des mots BIP-39 avec des pièces, dés et cartes.
lang: fr
permalink: /fr/methods/
---

## Guide des méthodes

Chaque méthode produit un indice de 11 bits pour un mot BIP-39 provisoire. Générez 12 ou 24 mots provisoires, puis corrigez le dernier comme indiqué sur la page d'accueil française.

<a id="coin"></a>
### Pièce

Lancez la pièce 11 fois par mot : face vaut `0` et pile vaut `1`. Lisez les bits de gauche à droite et cherchez le mot dans la [table binaire](../../tables/binary-table/).

<a id="d6"></a>
### D6

Convertissez `1–4` en `00`, `01`, `10`, `11` ; `5` vaut `0` et `6` vaut `1`. Lancez jusqu'à 11 bits ; si le dernier résultat est trop long, ne gardez que les bits nécessaires à gauche.

<a id="d8"></a>
### D8

Convertissez `1–8` en `000–111`. Quatre lancers donnent 12 bits : gardez les 11 premiers et cherchez-les dans la table binaire.

<a id="d8d16d16"></a>
### D8/D16/D16

Lancez un D8 et deux D16. L'indice est `(D8 - 1) × 256 + (premier D16 - 1) × 16 + (second D16 - 1)`. Chaque série sélectionne un indice ; consultez la [table complète](d8d16d16/).

<a id="888cc"></a>
### D8/D8/D8/pièce/pièce

Lancez trois D8 et deux pièces. Face vaut `0` et pile vaut `1`. L'indice est `(premier D8 - 1) × 256 + (second D8 - 1) × 32 + (troisième D8 - 1) × 4 + première pièce × 2 + seconde pièce`; consultez la [table complète](888cc/).

<a id="poker"></a>
### Cartes de poker

Utilisez 52 cartes sans Jokers. Convertissez chaque carte avec la [table de poker](poker/), remettez-la et mélangez jusqu'à 11 bits.

<a id="piacentine"></a>
### Cartes piacentines

Utilisez un jeu piacentin de 40 cartes. Collectez 11 bits avec la [table des cartes](piacentine/) ; remettez et mélangez après chaque tirage.

<a id="tarot"></a>
### Tarot

Utilisez les 78 cartes. Leur niveau fournit de un à six bits ; tirez, notez, remettez et mélangez jusqu'à 11 bits. Consultez la [table de Tarot](tarot/).
