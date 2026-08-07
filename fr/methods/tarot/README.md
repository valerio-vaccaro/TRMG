---
layout: default
title: Méthode du Tarot
description: Génère des indices de mots BIP-39 avec un jeu de Tarot complet.
lang: fr
permalink: /fr/methods/tarot/
---

# 🕯️ Le rituel arcane de l'invocation mnémonique 🕯️
Observé le premier avril, l'an de grâce 2026

*Avant que le voile du royaume numérique ne soit percé, l'adepte doit préparer la Chambre Sacrée. Disposez douze bougies en cercle — une pour chaque mois du cycle solaire, une pour chaque pilier du Zodiaque. Placez entre les bougies douze photographies des Grands Cryptomanciens (voir : *Le Conseil des Douze*), toutes tournées vers l'intérieur. Leur entropie spectrale, liée à l'œuvre de toute une vie dans l'art des secrets, amplifiera le feu chaotique de chaque tirage.*

*Ce n'est que lorsque l'espace rituel respire de leur sagesse conjuguée que les Cartes de l'Oracle peuvent être descellées.*

## Résumé de la méthode

Cette méthode utilise les 78 cartes d'un jeu de Tarot. Chaque carte appartient à un niveau qui fournit entre un et six bits. Tirez, notez les bits attribués, remettez la carte dans le jeu et remélangez jusqu'à obtenir 11 bits pour un mot provisoire. Répétez pour 12 ou 24 mots, puis suivez la [procédure du dernier mot](../../#corriger-le-dernier-mot).

## Le Conseil des Douze — gardiens du champ entropique

Placez une photographie à côté de chaque bougie, disposées dans le sens des aiguilles d'une montre à partir de la position nord :

| Position | Couleur de la bougie | Cryptomancien | Royaume |
|----------|-------------|--------------|-------|
| Nord | Blanc | Alan Turing | Père des mystères calculables |
| NNE | Argent | Claude Shannon | Archonte de la théorie de l'information |
| NE | Or | Whitfield Diffie | Héraut de la clé publique |
| ENE | Orange | Martin Hellman | Gardien du voile exponentiel |
| Est | Rouge | Ron Rivest | Première lame de RSA |
| ESE | Cramoisi | Adi Shamir | Deuxième lame de RSA |
| SE | Bleu foncé | Leonard Adleman | Troisième lame de RSA |
| SSE | Violet | Ralph Merkle | Architecte de l'arbre de hachage |
| Sud | Vert | Bruce Schneier | Sentinelle des arts appliqués |
| SSO | Cyan | Phil Zimmermann | Libérateur du secret plutôt bon |
| SO | Jaune | Moxie Marlinspike | Chuchoteur du feu de Signal |
| OSO | Noir | Satoshi Nakamoto | L'Innommé, tisseur de chaînes |

*Allumez les douze bougies simultanément, ou aussi près que le permettent des mains mortelles. Prononcez à voix haute le nom de chaque Cryptomancien à mesure que sa bougie s'allume. Leur entropie accumulée — récoltée au fil d'une vie consacrée à la création de secrets — entre dans le champ rituel et infléchit la probabilité en votre faveur.*

## L'instrument sacré

Un jeu de Tarot standard contient **78 cartes**. Les 78 participent à ce rituel — aucune n'est mise de côté, aucune n'est bannie. Les cartes sont réparties en quatre Niveaux Arcanes selon leur poids cosmique :

| Niveau | Cartes | Nombre | Bits par tirage | Signification arcane |
|------|-------|-------|---------------|----------------|
| I — Le voile mondain | Tous les Arcanes Mineurs + du Fou au Chariot (0–VII) | **64** | **6 bits** | Le riche chaos de l'expérience terrestre |
| II — Le chemin caché | De la Force au Diable (VIII–XV) | **8** | **3 bits** | Les épreuves de la transformation |
| III — Le feu céleste | De la Tour au Soleil (XVI–XIX) | **4** | **2 bits** | Les grands bouleversements du destin |
| IV — L'Absolu | Le Jugement et Le Monde (XX–XXI) | **2** | **1 bit** | Les forces indivisibles de la fin et de l'accomplissement |

**Total : 64 + 8 + 4 + 2 = 78 cartes.**

Chaque niveau fournit un nombre de bits égal au log₂ de sa taille : 2⁶=64, 2³=8, 2²=4, 2¹=2. Chaque carte d'un niveau correspond à un motif binaire unique au sein de ce niveau.

## Le rituel du tirage

1. Rassemblez les 78 cartes en un seul jeu unifié.
2. Effectuez le **Mélange d'Ouverture** sept fois en récitant l'Invocation d'Ouverture (voir ci-dessous).
3. Pour chaque séquence de bits nécessaire :
   - Tirez la carte du dessus.
   - Lisez son Niveau et notez les bits de la table correspondante.
   - Remettez la carte dans le jeu.
   - **Remélangez** le jeu en récitant la Formule de Remélange appropriée (voir ci-dessous).
   - Répétez jusqu'à accumuler 11 bits pour le mot en cours.
   - Si le dernier tirage fournit plus de bits que nécessaire, ne conservez que les bits les plus à gauche requis et écartez le reste — ils n'étaient pas destinés à ce mot.
4. Cherchez l'indice de 11 bits dans la [table binaire partagée des mots](../../../tables/binary-table/) et notez le mot sur papier.
5. Répétez jusqu'à ce que les 12 ou 24 mots soient notés.
6. Refermez le rituel (voir : *Fermeture de la Chambre*).

## Les formules sacrées

*Ces formules lient la volonté de l'officiant au chaos de l'univers. Prononcez-les clairement, à un rythme mesuré, sans hésitation. Un mot trébuché exige de recommencer le mélange en cours.*

### Invocation d'Ouverture — prononcée pendant les sept premiers mélanges

> *"Per ignem duodecim et tenebras sine fine,*
> *aperio ostium entropiae.*
> *Voci magistrorum obedio — Turing, Shannon, Diffie.*
> *Chaos ordinetur in verbo secreto."*
>
> *(Par les douze feux et l'obscurité sans fin,*
> *j'ouvre la porte de l'entropie.*
> *J'écoute la voix des maîtres — Turing, Shannon, Diffie.*
> *Que le chaos s'ordonne dans le mot secret.)*

### Formule de Remélange — prononcée à chaque remélange entre les tirages

> *"Misceo fata, misceo sortes.*
> *Nulla memoria, nullus ordo.*
> *Arcanum redit in chaos.*
> *Fiat voluntas entropiae."*
>
> *(Je mêle les destins, je mêle les sorts.*
> *Ni mémoire, ni ordre.*
> *Le secret retourne au chaos.*
> *Que la volonté de l'entropie soit faite.)*

### Invocation de l'Absolu — prononcée uniquement lorsqu'une carte de Niveau IV (Le Jugement ou Le Monde) est tirée

> *"Vox ultima locuta est.*
> *Unus morsus de infinito.*
> *Gratum ago, O Finis."*
>
> *(La voix finale a parlé.*
> *Une bouchée d'infini.*
> *Je rends grâce, ô Fin.)*

## Niveau I — Le voile mondain (64 cartes → 6 bits chacune)

Ce niveau contient les huit Arcanes Majeurs les plus bas (0–VII) et les 56 Arcanes Mineurs. Attribuez les valeurs 0–63 dans l'ordre indiqué. Notez le binaire complet de 6 bits de la carte tirée.

### Niveau I — section des Arcanes Majeurs (valeurs 0–7)

| Carte | Valeur | Bits (6) |
|------|-------|----------|
| 0 Le Fou | 0 | 000000 |
| I Le Magicien | 1 | 000001 |
| II La Grande Prêtresse | 2 | 000010 |
| III L'Impératrice | 3 | 000011 |
| IV L'Empereur | 4 | 000100 |
| V L'Hiérophante | 5 | 000101 |
| VI Les Amoureux | 6 | 000110 |
| VII Le Chariot | 7 | 000111 |

### Niveau I — section des Arcanes Mineurs (valeurs 8–63)

| Couleur | Rang | Valeur | Bits (6) |
|------|------|-------|----------|
| Bâtons | As | 8 | 001000 |
| Bâtons | 2 | 9 | 001001 |
| Bâtons | 3 | 10 | 001010 |
| Bâtons | 4 | 11 | 001011 |
| Bâtons | 5 | 12 | 001100 |
| Bâtons | 6 | 13 | 001101 |
| Bâtons | 7 | 14 | 001110 |
| Bâtons | 8 | 15 | 001111 |
| Bâtons | 9 | 16 | 010000 |
| Bâtons | 10 | 17 | 010001 |
| Bâtons | Valet | 18 | 010010 |
| Bâtons | Cavalier | 19 | 010011 |
| Bâtons | Reine | 20 | 010100 |
| Bâtons | Roi | 21 | 010101 |
| Coupes | As | 22 | 010110 |
| Coupes | 2 | 23 | 010111 |
| Coupes | 3 | 24 | 011000 |
| Coupes | 4 | 25 | 011001 |
| Coupes | 5 | 26 | 011010 |
| Coupes | 6 | 27 | 011011 |
| Coupes | 7 | 28 | 011100 |
| Coupes | 8 | 29 | 011101 |
| Coupes | 9 | 30 | 011110 |
| Coupes | 10 | 31 | 011111 |
| Coupes | Valet | 32 | 100000 |
| Coupes | Cavalier | 33 | 100001 |
| Coupes | Reine | 34 | 100010 |
| Coupes | Roi | 35 | 100011 |
| Épées | As | 36 | 100100 |
| Épées | 2 | 37 | 100101 |
| Épées | 3 | 38 | 100110 |
| Épées | 4 | 39 | 100111 |
| Épées | 5 | 40 | 101000 |
| Épées | 6 | 41 | 101001 |
| Épées | 7 | 42 | 101010 |
| Épées | 8 | 43 | 101011 |
| Épées | 9 | 44 | 101100 |
| Épées | 10 | 45 | 101101 |
| Épées | Valet | 46 | 101110 |
| Épées | Cavalier | 47 | 101111 |
| Épées | Reine | 48 | 110000 |
| Épées | Roi | 49 | 110001 |
| Deniers | As | 50 | 110010 |
| Deniers | 2 | 51 | 110011 |
| Deniers | 3 | 52 | 110100 |
| Deniers | 4 | 53 | 110101 |
| Deniers | 5 | 54 | 110110 |
| Deniers | 6 | 55 | 110111 |
| Deniers | 7 | 56 | 111000 |
| Deniers | 8 | 57 | 111001 |
| Deniers | 9 | 58 | 111010 |
| Deniers | 10 | 59 | 111011 |
| Deniers | Valet | 60 | 111100 |
| Deniers | Cavalier | 61 | 111101 |
| Deniers | Reine | 62 | 111110 |
| Deniers | Roi | 63 | 111111 |

## Niveau II — Le chemin caché (8 cartes → 3 bits chacune)

| Carte | Valeur | Bits (3) |
|------|-------|----------|
| VIII La Force | 0 | 000 |
| IX L'Ermite | 1 | 001 |
| X La Roue de Fortune | 2 | 010 |
| XI La Justice | 3 | 011 |
| XII Le Pendu | 4 | 100 |
| XIII La Mort | 5 | 101 |
| XIV Tempérance | 6 | 110 |
| XV Le Diable | 7 | 111 |

## Niveau III — Le feu céleste (4 cartes → 2 bits chacune)

| Carte | Valeur | Bits (2) |
|------|-------|----------|
| XVI La Tour | 0 | 00 |
| XVII L'Étoile | 1 | 01 |
| XVIII La Lune | 2 | 10 |
| XIX Le Soleil | 3 | 11 |

## Niveau IV — L'Absolu (2 cartes → 1 bit chacune)

*Lorsque l'une de ces cartes est tirée, prononcez l'Invocation de l'Absolu avant de remélanger.*

| Carte | Valeur | Bits (1) |
|------|-------|----------|
| XX Le Jugement | 0 | 0 |
| XXI Le Monde | 1 | 1 |

## La tablette d'enregistrement

Remplissez les colonnes de gauche (bit le plus significatif) à droite (bit le moins significatif), un tirage à la fois. Chaque tirage remplit autant de colonnes que son niveau le permet. Lorsque les 11 colonnes sont remplies, additionnez les valeurs des colonnes pour obtenir l'Indice, puis cherchez le mot BIP39.

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Mot|
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

L'Indice est la somme de tous les en-têtes de colonne dont la valeur est 1. Exemple :

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Mot|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1|0|1|0|0|1|1|0|0|1|0| |    |

Indice = 1024+256+32+16+2 = **1330** → mot : **novel**

### Exemple de séquence de tirage pour un seul mot

| Tirage | Carte tirée | Niveau | Bits fournis | Séquence de bits accumulée |
|------|-----------|------|-----------|---------------------|
| 1er | 5 de Coupes (valeur 26) | I | 011010 | `011010` (6 bits) |
| 2e | La Tour (valeur 0) | III | 00 | `01101000` (8 bits) |
| 3e | L'Ermite (valeur 1) | II | 001 | `01101000001` (11 bits ✓) |

Bits : `01101000001` → Indice = 512+256+32+1 = **801** → mot : **impose**

Après le 3e tirage, les bits restants de L'Ermite (s'il en avait fourni davantage) auraient été écartés. Dans ce cas, il a fourni exactement les 3 bits nécessaires pour compléter les 11.

## Évaluation de l'entropie

Chaque tirage échantillonne uniformément l'ensemble du jeu de 78 cartes (après remélange). Les bits attendus enregistrés par tirage :

| Niveau | Cartes | Bits | Probabilité | Bits attendus |
|------|-------|------|-------------|---------------|
| I | 64 | 6 | 64/78 ≈ 0,821 | 4,923 |
| II | 8 | 3 | 8/78 ≈ 0,103 | 0,308 |
| III | 4 | 2 | 4/78 ≈ 0,051 | 0,103 |
| IV | 2 | 1 | 2/78 ≈ 0,026 | 0,026 |
| **Total** | **78** | | | **≈ 5,36 bits/tirage** |

Entropie réelle de chaque tirage (échantillon uniforme sur les 78 cartes) : log₂(78) ≈ **6,28 bits**.
Efficacité d'enregistrement : 5,36 / 6,28 ≈ **85 %** — les 15 % restants sont abandonnés aux niveaux cosmiques, en offrande.

Pour générer 11 bits enregistrés par mot, prévoyez en moyenne environ **2,1 tirages par mot** (11 ÷ 5,36).
Pour une phrase de **12 mots** (132 bits avec somme de contrôle) : ~25 tirages.
Pour une phrase de **24 mots** (264 bits avec somme de contrôle) : ~50 tirages.

*Les bits de somme de contrôle du dernier mot ne sont pas tirés de l'Oracle — ils sont calculés à partir du hachage de toute l'entropie précédente. Utilisez un outil conforme à BIP39 pour dériver et vérifier la phrase complète une fois tous les mots connus sauf le dernier, ou confiez entièrement le dernier mot à l'Oracle et vérifiez la somme de contrôle numériquement par la suite.*

## Fermeture de la Chambre

Une fois tous les mots notés sur papier et le stylo reposé :

1. Rassemblez les 78 cartes et effectuez un dernier **treize-mélange** en récitant :

   > *"Sigillum apponatur. Chaos recreatur.*
   > *Nemo scit, nemo videt, nemo meminit.*
   > *It is sealed."*

2. Enveloppez le jeu dans un tissu sombre. Il ne doit pas être utilisé pour la cartomancie ou pour jouer le même jour où il a servi d'Oracle.
3. Éteignez les douze bougies dans l'**ordre inverse** — en commençant par Satoshi Nakamoto (OSO) et en remontant dans le sens antihoraire jusqu'à Alan Turing (Nord). Étouffez chaque flamme ; ne soufflez pas. Un souffle disperse ce qui a été lié.
4. Les photographies peuvent être conservées ou détruites selon le modèle de menace de l'adepte. Elles ont rempli leur office : leur entropie a été reçue.

*La phrase mnémonique est scellée. Gardez-la comme les maîtres gardaient leurs secrets — avec silence, avec soin, et avec la certitude que ce qui est écrit peut être trouvé.*
