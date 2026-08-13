---
layout: default
title: Générer une phrase mnémonique hors ligne
description: Guide de création de mots BIP-39 avec de l'aléa physique.
lang: fr
---

<section class="hero">
  <div class="eyebrow">Un aléa physique vérifiable à la main</div>
  <h1>Générez des mots mnémoniques depuis le monde réel.</h1>
  <p>TRMG convertit les résultats de dés, de pièces et de cartes en indices BIP-39. Notez 11 bits pour chaque mot provisoire, puis corrigez hors ligne le mot de contrôle final.</p>
  <a class="button" href="#methods">Choisir une méthode</a>
</section>

## Fonctionnement

Chaque méthode produit un nombre de 11 bits entre `0` et `2047`. Cherchez ce nombre dans la table des mots, répétez jusqu'à obtenir 12 ou 24 mots provisoires, puis corrigez le dernier mot.

> **La qualité de l’entropie compte.** Utilisez uniquement des dés, pièces ou cartes aussi équilibrés et non biaisés que possible. Vérifiez qu’ils ne sont ni endommagés ni affectés par un biais de fabrication, et mélangez soigneusement les cartes entre les tirages. Une source physique biaisée réduit la qualité de l’entropie de la phrase mnémonique obtenue.

> **Utilisez à vos propres risques.** Ces méthodes et ce site sont fournis tels quels, sans aucune garantie concernant la sécurité de votre phrase mnémonique ou de vos fonds. Vous êtes seul responsable de vérifier le processus et de toute perte de fonds résultant de son utilisation.

> **Sauvegardez votre phrase mnémonique de façon sûre.** Une sauvegarde hors ligne fiable est essentielle pour éviter de perdre l’accès à vos fonds. Conservez-la à l’abri de la perte, des dommages, du vol et des accès non autorisés ; ne vous fiez jamais à une seule copie ni à une capture d’écran numérique.

> **Limitez l’exposition de votre phrase mnémonique.** Ne la copiez ni ne la saisissez sur plusieurs appareils ou ordinateurs. Utilisez-la uniquement avec le portefeuille logiciel ou matériel pour lequel elle a été générée, et seulement lorsque cela est nécessaire.

## Méthodes {#methods}

|Méthode|Comment elle produit chaque mot provisoire|
|-------|-------------------------------------------|
|[Pièce](methods/coin/)|Onze lancers : face vaut `0` et pile vaut `1`.|
|[D6](methods/d6/)|Convertissez chaque lancer en un ou deux bits.|
|[D8](methods/d8/)|Quatre lancers donnent 12 bits ; conservez les 11 premiers.|
|[D8/D16/D16](methods/d8d16d16/)|Trois dés sélectionnent un indice en une seule série de lancers.|
|[D8/D8/D8/pièce/pièce](methods/888cc/)|Trois lancers et deux pièces sélectionnent un indice.|
|[Cartes de poker](methods/poker/)|Tirez une carte, convertissez-la en bits, remettez-la et mélangez.|
|[Cartes piacentines](methods/piacentine/)|Utilisez un jeu régional italien de 40 cartes.|
|[Tarot](methods/tarot/)|Utilisez les 78 cartes et leurs valeurs binaires par niveau.|

## Corriger le dernier mot {#correct-the-final-word}

Pour une phrase de 12 mots, générez 12 mots provisoires et corrigez uniquement le douzième. Pour une phrase de 24 mots, générez-en 24 et corrigez uniquement le vingt-quatrième. Le dernier mot contient l'entropie et la somme de contrôle BIP-39.

|Longueur|Partie conservée du dernier mot provisoire|Derniers mots possibles (avec l’entropie sélectionnée)|
|--------|-------------------------------------------|-------------------|
|12 mots|7 premiers bits|16|
|24 mots|3 premiers bits|256|

Trouvez le groupe dans la [table binaire des mots](../tables/binary-table/) et utilisez un portefeuille ou outil BIP-39 fiable et hors ligne pour obtenir le bon candidat. Ne saisissez jamais votre phrase mnémonique sur un site web ou un appareil non fiable.
