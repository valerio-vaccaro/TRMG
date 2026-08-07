---
layout: default
title: Mnemonikus kifejezés létrehozása offline
description: BIP-39 szavak létrehozása fizikai véletlennel.
lang: hu
---

<section class="hero">
  <div class="eyebrow">Kézzel ellenőrizhető fizikai véletlen</div>
  <h1>Hozz létre mnemonikus szavakat a valós világból.</h1>
  <p>A TRMG a kockák, érmék és kártyák eredményeit BIP-39 indexekké alakítja. Minden ideiglenes szóhoz jegyezz fel 11 bitet, majd offline javítsd az utolsó ellenőrzőösszeg-szót.</p>
  <a class="button" href="#methods">Módszer választása</a>
</section>

## Hogyan működik

Minden módszer egy `0` és `2047` közötti, 11 bites számot hoz létre. Keresd ki ezt a szótáblázatban, ismételd 12 vagy 24 ideiglenes szóig, majd javítsd az utolsó szót.

> **Az entrópia minősége fontos.** Csak a lehető leginkább szabályos és torzításmentes kockát, érmét vagy kártyát használj. Ellenőrizd, hogy nincs-e sérülésük vagy gyártási torzításuk, és a húzások között alaposan keverd meg a kártyákat. A torzított fizikai forrás rontja a létrejövő mnemonika entrópiájának minőségét.

> **Saját felelősségre használd.** Ezeket a módszereket és ezt a webhelyet adott állapotban, a mnemonika vagy a pénzeszközök biztonságára vonatkozó bármiféle garancia nélkül biztosítjuk. Egyedül te felelsz a folyamat ellenőrzéséért és a használatából eredő esetleges pénzveszteségért.

> **Készíts biztonságos biztonsági mentést a mnemonikáról.** A megbízható, offline mentés alapvető fontosságú ahhoz, hogy ne veszítsd el a hozzáférést a pénzeszközeidhez. Úgy tárold, hogy védve legyen elvesztés, sérülés, lopás és jogosulatlan hozzáférés ellen; soha ne hagyatkozz egyetlen példányra vagy digitális képernyőképre.

> **Korlátozd a mnemonika kitettségét.** Ne másold vagy írd be a mnemonikát több eszközön vagy számítógépen. Csak azzal a szoftveres vagy hardveres tárcával használd, amelyhez létrehoztad, és csak szükség esetén.

## Módszerek {#methods}

|Módszer|Hogyan jön létre minden ideiglenes szó|
|-------|--------------------------------------|
|[Érme](methods/coin/)|Tizenegy dobás: fej `0`, írás `1`.|
|[D6](methods/d6/)|Minden dobást egy vagy két bittel alakíts át.|
|[D8](methods/d8/)|Négy dobás 12 bitet ad; tartsd meg az első 11-et.|
|[D8/D16/D16](methods/d8d16d16/)|Három kocka egy dobássorozattal kiválaszt egy indexet.|
|[D8/D8/D8/érme/érme](methods/888cc/)|Három dobás és két érmedobás választ ki egy indexet.|
|[Pókerkártyák](methods/poker/)|Húzz kártyát, alakítsd bitekké, tedd vissza és keverd meg.|
|[Piacentine kártyák](methods/piacentine/)|Használj egy 40 lapos olasz regionális paklit.|
|[Tarot](methods/tarot/)|Használd mind a 78 lapot és szintenkénti bitértékeiket.|

## Az utolsó szó javítása {#correct-the-final-word}

12 szavas mnemonikához hozz létre 12 ideiglenes szót, és csak a tizenkettediket javítsd. 24 szavas mnemonikához hozz létre 24-et, és csak a huszonnegyediket javítsd. Az utolsó szó entrópiát és BIP-39 ellenőrzőösszeget is tartalmaz.

|Hossz|Az ideiglenes utolsó szóból megtartott rész|Jelöltek száma a csoportban|
|-----|--------------------------------------------|---------------------------|
|12 szó|Első 7 bit|16|
|24 szó|Első 3 bit|128|

Keresd meg a csoportot a [bináris szótáblázatban](../tables/binary-table/), majd egy megbízható, offline BIP-39-kompatibilis tárcával vagy eszközzel határozd meg a helyes jelöltet. Soha ne írd be a mnemonikát webhelyre vagy nem megbízható eszközre.
