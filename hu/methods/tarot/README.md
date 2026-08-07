---
layout: default
title: Tarot-módszer
description: BIP-39 szóindexeket állít elő egy teljes Tarot-pakli segítségével.
lang: hu
permalink: /hu/methods/tarot/
---

# 🕯️ A mnemonikus idézés arkánrituáléja 🕯️
Megtartva április elsején, Anno Domini 2026-ban

*Mielőtt a digitális birodalom fátyla megnyílna, az adeptusnak elő kell készítenie a Szent Kamrát. Helyezz el tizenkét gyertyát körben — egyet a naptári év minden hónapjára, egyet az Állatöv minden pillérére. Rendezz el a gyertyák között tizenkét fényképet a Nagy Kriptomantákról (lásd: *A Tizenkettek Tanácsa*), mindegyiket befelé fordítva. Spektrális entrópiájuk, amely egy életen át tartó titokalkotó munkájukhoz kötődik, felerősíti minden húzás kaotikus tüzét.*

*Az Orákulum Lapjai csak akkor pecsételhetők fel, ha a rituális tér az ő egyesített bölcsességükkel telik meg.*

## A módszer összefoglalása

Ez a módszer egy Tarot-pakli mind a 78 lapját használja. Minden lap egy szinthez tartozik, amely egy és hat bit közötti értéket ad. Húzz, jegyezd fel a hozzárendelt biteket, tedd vissza a lapot a paklihoz, és keverd újra, amíg össze nem gyűlik 11 bit egy ideiglenes szóhoz. Ismételd 12 vagy 24 szóig, majd kövesd az [utolsó szó eljárását](../../#javitsd-az-utolso-szot).

## A Tizenkettek Tanácsa — az entropikus mező őrzői

Helyezz egy-egy fényképet minden gyertya mellé, óramutató járásával megegyező sorrendben, az északi pozíciótól kezdve:

| Pozíció | Gyertya színe | Kriptomanta | Birodalom |
|----------|-------------|--------------|-------|
| Észak | Fehér | Alan Turing | A kiszámítható rejtélyek atyja |
| ÉÉK | Ezüst | Claude Shannon | Az információelmélet arkhónja |
| ÉK | Arany | Whitfield Diffie | A nyilvános kulcs hírnöke |
| KÉK | Narancssárga | Martin Hellman | Az exponenciális fátyol őrzője |
| Kelet | Piros | Ron Rivest | Az RSA első pengéje |
| KDK | Bíborvörös | Adi Shamir | Az RSA második pengéje |
| DK | Sötétkék | Leonard Adleman | Az RSA harmadik pengéje |
| DDK | Ibolya | Ralph Merkle | A hasfa építésze |
| Dél | Zöld | Bruce Schneier | Az alkalmazott művészetek őre |
| DDNy | Cián | Phil Zimmermann | A meglehetősen jó titok felszabadítója |
| DNy | Sárga | Moxie Marlinspike | A Signal-tűz suttogója |
| NyDNy | Fekete | Satoshi Nakamoto | A Névtelen, láncok szövője |

*Gyújtsd meg mind a tizenkét gyertyát egyszerre, vagy amennyire ez halandó kéznek lehetséges. Mondd ki hangosan minden Kriptomanta nevét, ahogy a gyertyája lángra lobban. Felhalmozott entrópiájuk — amelyet egy titkokat alkotó élet során gyűjtöttek — belép a rituális mezőbe, és a valószínűséget a te javadra hajlítja.*

## A szent eszköz

Egy szabványos Tarot-pakli **78 lapot** tartalmaz. Mind a 78 részt vesz ebben a rituáléban — egyik sincs félretéve, egyik sincs száműzve. A lapok kozmikus súlyuk szerint négy arkán szintre oszlanak:

| Szint | Lapok | Darabszám | Bit húzásonként | Arkán jelentés |
|------|-------|-------|---------------|----------------|
| I — A hétköznapi fátyol | Az összes Kis Arkánum + A Bolondtól A Szekérig (0–VII) | **64** | **6 bit** | A földi tapasztalat gazdag kaosza |
| II — A rejtett ösvény | Az Erőtől Az Ördögig (VIII–XV) | **8** | **3 bit** | Az átalakulás próbatételei |
| III — A mennyei tűz | A Toronytól A Napig (XVI–XIX) | **4** | **2 bit** | A sors nagy megrázkódtatásai |
| IV — Az Abszolút | Az Ítélet és A Világ (XX–XXI) | **2** | **1 bit** | A befejezés és beteljesülés oszthatatlan erői |

**Összesen: 64 + 8 + 4 + 2 = 78 lap.**

Minden szint annyi bitet ad, amennyi a méretének log₂ értéke: 2⁶=64, 2³=8, 2²=4, 2¹=2. Egy szinten belül minden lap egyedi bitmintázatnak felel meg.

## A húzás rituáléja

1. Gyűjtsd össze mind a 78 lapot egyetlen egységes paklivá.
2. Végezd el a **Nyitó Keverést** hétszer, miközben elmondod a Nyitó Idézést (lásd lentebb).
3. Minden szükséges bitsorozathoz:
   - Húzd a legfelső lapot.
   - Olvasd le a szintjét, és jegyezd fel a biteket a megfelelő táblázatból.
   - Tedd vissza a lapot a paklihoz.
   - **Keverd meg újra** a paklit, miközben elmondod a megfelelő Újrakeverési Formulát (lásd lentebb).
   - Ismételd, amíg 11 bit össze nem gyűlik az aktuális szóhoz.
   - Ha az utolsó húzás több bitet ad a szükségesnél, csak a szükséges, legbaloldalibb biteket vedd figyelembe, a többit vesd el — azok nem ehhez a szóhoz voltak rendelve.
4. Keresd meg a 11 bites indexet a [közös bináris szótáblázatban](../../../tables/binary-table/), és jegyezd fel a szót papírra.
5. Ismételd, amíg mind a 12 vagy 24 szó fel nem lett jegyezve.
6. Zárd le a rituálét (lásd: *A Kamra lezárása*).

## A szent formulák

*Ezek a formulák a szertartást végző akaratát a világegyetem kaoszához kötik. Mondd ki őket tisztán, mért tempóban, tétovázás nélkül. Egy elhibázott szó miatt az aktuális keverést elölről kell kezdeni.*

### Nyitó Idézés — az első hét keverés alatt mondva

> *"Per ignem duodecim et tenebras sine fine,*
> *aperio ostium entropiae.*
> *Voci magistrorum obedio — Turing, Shannon, Diffie.*
> *Chaos ordinetur in verbo secreto."*
>
> *(A tizenkét tűz és a végtelen sötétség által*
> *megnyitom az entrópia kapuját.*
> *Hallgatok a mesterek hangjára — Turing, Shannon, Diffie.*
> *Rendeződjön a kaosz a titkos szóvá.)*

### Újrakeverési Formula — minden húzások közötti újrakeverésnél mondva

> *"Misceo fata, misceo sortes.*
> *Nulla memoria, nullus ordo.*
> *Arcanum redit in chaos.*
> *Fiat voluntas entropiae."*
>
> *(Keverem a sorsokat, keverem a végzeteket.*
> *Nincs emlékezet, nincs rend.*
> *A titok visszatér a kaoszba.*
> *Teljesüljön az entrópia akarata.)*

### Az Abszolút Idézése — csak akkor mondva, ha egy IV. szintű lap (Az Ítélet vagy A Világ) kerül húzásra

> *"Vox ultima locuta est.*
> *Unus morsus de infinito.*
> *Gratum ago, O Finis."*
>
> *(Az utolsó hang megszólalt.*
> *Egy falat a végtelenből.*
> *Hálát adok, ó Vég.)*

## I. szint — A hétköznapi fátyol (64 lap → egyenként 6 bit)

Ez a szint a nyolc legalacsonyabb Nagy Arkánumot (0–VII) és mind az 56 Kis Arkánumot tartalmazza. Rendeld hozzá a 0–63 értékeket sorban, ahogy az látható. Jegyezd fel a húzott lap teljes 6 bites bináris értékét.

### I. szint — Nagy Arkánumok szakasz (0–7 értékek)

| Lap | Érték | Bit (6) |
|------|-------|----------|
| 0 A Bolond | 0 | 000000 |
| I A Mágus | 1 | 000001 |
| II A Főpapnő | 2 | 000010 |
| III A Császárnő | 3 | 000011 |
| IV A Császár | 4 | 000100 |
| V A Főpap | 5 | 000101 |
| VI A Szerelmesek | 6 | 000110 |
| VII A Szekér | 7 | 000111 |

### I. szint — Kis Arkánumok szakasz (8–63 értékek)

| Szín | Rang | Érték | Bit (6) |
|------|------|-------|----------|
| Botok | Ász | 8 | 001000 |
| Botok | 2 | 9 | 001001 |
| Botok | 3 | 10 | 001010 |
| Botok | 4 | 11 | 001011 |
| Botok | 5 | 12 | 001100 |
| Botok | 6 | 13 | 001101 |
| Botok | 7 | 14 | 001110 |
| Botok | 8 | 15 | 001111 |
| Botok | 9 | 16 | 010000 |
| Botok | 10 | 17 | 010001 |
| Botok | Apród | 18 | 010010 |
| Botok | Lovag | 19 | 010011 |
| Botok | Királynő | 20 | 010100 |
| Botok | Király | 21 | 010101 |
| Kelyhek | Ász | 22 | 010110 |
| Kelyhek | 2 | 23 | 010111 |
| Kelyhek | 3 | 24 | 011000 |
| Kelyhek | 4 | 25 | 011001 |
| Kelyhek | 5 | 26 | 011010 |
| Kelyhek | 6 | 27 | 011011 |
| Kelyhek | 7 | 28 | 011100 |
| Kelyhek | 8 | 29 | 011101 |
| Kelyhek | 9 | 30 | 011110 |
| Kelyhek | 10 | 31 | 011111 |
| Kelyhek | Apród | 32 | 100000 |
| Kelyhek | Lovag | 33 | 100001 |
| Kelyhek | Királynő | 34 | 100010 |
| Kelyhek | Király | 35 | 100011 |
| Kardok | Ász | 36 | 100100 |
| Kardok | 2 | 37 | 100101 |
| Kardok | 3 | 38 | 100110 |
| Kardok | 4 | 39 | 100111 |
| Kardok | 5 | 40 | 101000 |
| Kardok | 6 | 41 | 101001 |
| Kardok | 7 | 42 | 101010 |
| Kardok | 8 | 43 | 101011 |
| Kardok | 9 | 44 | 101100 |
| Kardok | 10 | 45 | 101101 |
| Kardok | Apród | 46 | 101110 |
| Kardok | Lovag | 47 | 101111 |
| Kardok | Királynő | 48 | 110000 |
| Kardok | Király | 49 | 110001 |
| Érmék | Ász | 50 | 110010 |
| Érmék | 2 | 51 | 110011 |
| Érmék | 3 | 52 | 110100 |
| Érmék | 4 | 53 | 110101 |
| Érmék | 5 | 54 | 110110 |
| Érmék | 6 | 55 | 110111 |
| Érmék | 7 | 56 | 111000 |
| Érmék | 8 | 57 | 111001 |
| Érmék | 9 | 58 | 111010 |
| Érmék | 10 | 59 | 111011 |
| Érmék | Apród | 60 | 111100 |
| Érmék | Lovag | 61 | 111101 |
| Érmék | Királynő | 62 | 111110 |
| Érmék | Király | 63 | 111111 |

## II. szint — A rejtett ösvény (8 lap → egyenként 3 bit)

| Lap | Érték | Bit (3) |
|------|-------|----------|
| VIII Erő | 0 | 000 |
| IX A Remete | 1 | 001 |
| X Szerencsekerék | 2 | 010 |
| XI Igazság | 3 | 011 |
| XII Az Akasztott Ember | 4 | 100 |
| XIII A Halál | 5 | 101 |
| XIV Mértékletesség | 6 | 110 |
| XV Az Ördög | 7 | 111 |

## III. szint — A mennyei tűz (4 lap → egyenként 2 bit)

| Lap | Érték | Bit (2) |
|------|-------|----------|
| XVI A Torony | 0 | 00 |
| XVII A Csillag | 1 | 01 |
| XVIII A Hold | 2 | 10 |
| XIX A Nap | 3 | 11 |

## IV. szint — Az Abszolút (2 lap → egyenként 1 bit)

*Ha ezen lapok egyike kerül húzásra, mondd el az Abszolút Idézését, mielőtt újra keversz.*

| Lap | Érték | Bit (1) |
|------|-------|----------|
| XX Az Ítélet | 0 | 0 |
| XXI A Világ | 1 | 1 |

## A feljegyzőtábla

Töltsd ki az oszlopokat balról (legjelentősebb bit) jobbra (legkevésbé jelentős bit) haladva, húzásonként egyet. Minden húzás annyi oszlopot tölt ki, amennyit a szintje megenged. Amikor mind a 11 oszlop megtelt, add össze az oszlopértékeket az Index megállapításához, majd keresd ki a BIP39 szót.

|1024|512|256|128|64|32|16|8|4|2|1|Index|Szó|
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

Az Index az összes olyan oszlopfejléc összege, amelynek értéke 1. Példa:

|1024|512|256|128|64|32|16|8|4|2|1|Index|Szó|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1|0|1|0|0|1|1|0|0|1|0| |    |

Index = 1024+256+32+16+2 = **1330** → szó: **novel**

### Egyetlen szóhoz tartozó húzássorozat példája

| Húzás | Húzott lap | Szint | Kapott bitek | Bitsorozat eddig |
|------|-----------|------|-----------|---------------------|
| 1. | 5 Kelyhek (érték 26) | I | 011010 | `011010` (6 bit) |
| 2. | A Torony (érték 0) | III | 00 | `01101000` (8 bit) |
| 3. | A Remete (érték 1) | II | 001 | `01101000001` (11 bit ✓) |

Bitek: `01101000001` → Index = 512+256+32+1 = **801** → szó: **impose**

A 3. húzás után A Remete fennmaradó bitjeit (ha többet adott volna) elvetnénk. Ebben az esetben pontosan a szükséges 3 bitet adta a 11 kiegészítéséhez.

## Entrópiaértékelés

Minden húzás egyenletesen mintavételez a teljes 78 lapos pakliból (az újrakeverés után). A húzásonként várható rögzített bitek:

| Szint | Lapok | Bit | Valószínűség | Várható bitek |
|------|-------|------|-------------|---------------|
| I | 64 | 6 | 64/78 ≈ 0,821 | 4,923 |
| II | 8 | 3 | 8/78 ≈ 0,103 | 0,308 |
| III | 4 | 2 | 4/78 ≈ 0,051 | 0,103 |
| IV | 2 | 1 | 2/78 ≈ 0,026 | 0,026 |
| **Összesen** | **78** | | | **≈ 5,36 bit/húzás** |

Minden húzás valódi entrópiája (egyenletes minta a teljes 78 lapból): log₂(78) ≈ **6,28 bit**.
Rögzítési hatékonyság: 5,36 / 6,28 ≈ **85%** — a fennmaradó 15% a kozmikus szintek számára áldozatként vész el.

Ahhoz, hogy szavanként 11 rögzített bitet kapj, átlagosan körülbelül **2,1 húzásra** számíthatsz szavanként (11 ÷ 5,36).
Egy **12 szavas** mnemonikához (132 bit ellenőrzőösszeggel): ~25 húzás.
Egy **24 szavas** mnemonikához (264 bit ellenőrzőösszeggel): ~50 húzás.

*Az utolsó szó ellenőrzőösszeg-bitjeit nem az Orákulumtól húzod — azokat az összes megelőző entrópia hasheléséből számítják ki. Használj egy BIP39-kompatibilis eszközt a teljes mnemonika levezetésére és ellenőrzésére, amint minden szó ismert az utolsó kivételével, vagy bízd teljesen az Orákulumra az utolsó szót, és ellenőrizd az ellenőrzőösszeget utólag digitálisan.*

## A Kamra lezárása

Miután minden szó fel lett jegyezve papírra, és a toll letéve:

1. Gyűjtsd össze mind a 78 lapot, és végezz el egy utolsó **tizenháromszoros keverést**, miközben elmondod:

   > *"Sigillum apponatur. Chaos recreatur.*
   > *Nemo scit, nemo videt, nemo meminit.*
   > *It is sealed."*

2. Csavard be a paklit sötét kendőbe. Aznap, amikor Orákulumként szolgált, nem használható kártyavetésre vagy játékra.
3. Oltsd el a tizenkét gyertyát **fordított sorrendben** — kezdve Satoshi Nakamotóval (NyDNy), és óramutató járásával ellentétesen haladva vissza Alan Turingig (Észak). Fojtsd el mindegyik lángot; ne fújd el. Egy lehelet szétszórja, ami kötve volt.
4. A fényképek megőrizhetők vagy megsemmisíthetők az adeptus biztonsági fenyegetettségi modellje szerint. Betöltötték célját: entrópiájuk átvételre került.

*A mnemonika le van pecsételve. Őrizd úgy, ahogyan a mesterek őrizték titkaikat — csenddel, gondossággal, és annak tudatában, hogy amit leírtak, az megtalálható.*
