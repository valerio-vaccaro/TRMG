---
layout: default
title: Methodenleitfaden
description: BIP-39-Wörter mit Münzen, Würfeln und Karten erzeugen.
lang: de
permalink: /de/methods/
---

## Methodenleitfaden

Jede Methode erzeugt einen 11-Bit-Index für ein vorläufiges BIP-39-Wort. Erzeuge 12 oder 24 vorläufige Wörter und korrigiere dann das letzte wie auf der deutschen Startseite beschrieben.

<a id="coin"></a>
### Münze

Wirf die Münze 11-mal pro Wort: Kopf ist `0`, Zahl ist `1`. Lies die Bits von links nach rechts und suche das Wort in der [binären Tabelle](../../tables/binary-table/).

<a id="d6"></a>
### D6

Wandle `1–4` in `00`, `01`, `10`, `11` um; `5` ist `0`, `6` ist `1`. Wirf bis 11 Bits gesammelt sind; ist der letzte Wert zu lang, behalte nur die benötigten linken Bits.

<a id="d8"></a>
### D8

Wandle `1–8` in `000–111` um. Vier Würfe ergeben 12 Bits: Behalte die ersten 11 und suche sie in der binären Tabelle.

<a id="d8d16d16"></a>
### D8/D16/D16

Wirf einen D8 und zwei D16. Der Index ist `(D8 - 1) × 256 + (erster D16 - 1) × 16 + (zweiter D16 - 1)`. Jede Serie wählt einen Index; siehe [vollständige Tabelle](d8d16d16/).

<a id="888cc"></a>
### D8/D8/D8/Münze/Münze

Wirf drei D8 und zwei Münzen. Kopf ist `0`, Zahl ist `1`. Der Index ist `(erster D8 - 1) × 256 + (zweiter D8 - 1) × 32 + (dritter D8 - 1) × 4 + erste Münze × 2 + zweite Münze`; siehe [vollständige Tabelle](888cc/).

<a id="poker"></a>
### Pokerkarten

Nutze 52 Karten ohne Joker. Wandle jede Karte mit der [Pokertabelle](poker/) um, lege sie zurück und mische bis 11 Bits gesammelt sind.

<a id="piacentine"></a>
### Piacentine-Karten

Nutze ein Piacentine-Deck mit 40 Karten. Sammle 11 Bits mit der [Kartentabelle](piacentine/); lege nach jeder Ziehung zurück und mische.

<a id="tarot"></a>
### Tarot

Nutze alle 78 Karten. Ihre Stufe liefert ein bis sechs Bits; ziehe, notiere, lege zurück und mische bis 11 Bits gesammelt sind. Siehe [Tarot-Tabelle](tarot/).
