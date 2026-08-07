---
layout: default
title: Módszerútmutató
description: BIP-39 szavak létrehozása érmékkel, kockákkal és kártyákkal.
lang: hu
permalink: /hu/methods/
---

## Módszerútmutató

Minden módszer 11 bites indexet hoz létre egy ideiglenes BIP-39 szóhoz. Hozz létre 12 vagy 24 ideiglenes szót, majd javítsd az utolsót a magyar főoldal útmutatása szerint.

<a id="coin"></a>
### Érme

Szavanként 11-szer dobd fel az érmét: a fej `0`, az írás `1`. Balról jobbra olvasd a biteket, és keresd ki a szót a [bináris táblázatban](../../tables/binary-table/).

<a id="d6"></a>
### D6

Alakítsd át az `1–4` értékeket `00`, `01`, `10`, `11` értékekké; az `5` `0`, a `6` `1`. Dobj, amíg 11 bitet gyűjtesz; ha az utolsó eredmény túl hosszú, csak a szükséges bal oldali biteket tartsd meg.

<a id="d8"></a>
### D8

Alakítsd át az `1–8` értékeket `000–111` értékekké. Négy dobás 12 bitet ad: tartsd meg az első 11-et, és keresd ki a bináris táblázatban.

<a id="d8d16d16"></a>
### D8/D16/D16

Dobj egy D8-cal és két D16-tal. Az index: `(D8 - 1) × 256 + (első D16 - 1) × 16 + (második D16 - 1)`. Minden sorozat indexet választ; lásd a [teljes táblázatot](../../methods/d8ff/).

<a id="888cc"></a>
### D8/D8/D8/érme/érme

Dobj három D8-cal és két érmével. A fej `0`, az írás `1`. Az index: `(első D8 - 1) × 256 + (második D8 - 1) × 32 + (harmadik D8 - 1) × 4 + első érme × 2 + második érme`; lásd a [teljes táblázatot](../../methods/888cc/).

<a id="poker"></a>
### Pókerkártyák

Használj 52 lapot jokerek nélkül. Alakítsd át minden kártyát a [pókertáblázat](../../methods/poker/) szerint, tedd vissza és keverd meg, amíg 11 bitet gyűjtesz.

<a id="piacentine"></a>
### Piacentine kártyák

Használj 40 lapos Piacentine paklit. Gyűjts 11 bitet a [kártyatáblázat](../../methods/piacentine/) alapján; minden húzás után tedd vissza és keverd meg.

<a id="tarot"></a>
### Tarot

Használd mind a 78 lapot. A szintjük egytől hat bitig ad; húzz, jegyezd fel, tedd vissza és keverd meg, amíg 11 bitet gyűjtesz. Lásd a [Tarot-táblázatot](../../methods/tarot/).
