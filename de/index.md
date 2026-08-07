---
layout: default
title: Mnemonik offline erzeugen
description: Anleitung zum Erzeugen von BIP-39-Wörtern mit physikalischem Zufall.
lang: de
---

<section class="hero">
  <div class="eyebrow">Von Hand überprüfbarer physikalischer Zufall</div>
  <h1>Erzeuge Mnemonik-Wörter aus der realen Welt.</h1>
  <p>TRMG wandelt Ergebnisse von Würfeln, Münzen und Karten in BIP-39-Indizes um. Notiere 11 Bits für jedes vorläufige Wort und korrigiere das abschließende Prüfsummenwort offline.</p>
  <a class="button" href="#methods">Methode wählen</a>
</section>

## So funktioniert es

Jede Methode erzeugt eine 11-Bit-Zahl von `0` bis `2047`. Suche die Zahl in der Worttabelle, wiederhole dies für 12 oder 24 vorläufige Wörter und korrigiere dann das letzte Wort.

## Methoden

|Methode|Wie jedes vorläufige Wort entsteht|
|-------|---------------------------------|
|[Münze](methods/coin/)|Elf Würfe: Kopf ist `0`, Zahl ist `1`.|
|[D6](methods/d6/)|Wandle jeden Wurf in ein oder zwei Bits um.|
|[D8](methods/d8/)|Vier Würfe ergeben 12 Bits; behalte die ersten 11.|
|[D8/D16/D16](methods/d8d16d16/)|Drei Würfel wählen mit einer Wurfserie einen Index.|
|[D8/D8/D8/Münze/Münze](methods/888cc/)|Drei Würfe und zwei Münzwürfe wählen einen Index.|
|[Pokerkarten](methods/poker/)|Ziehe eine Karte, wandle sie in Bits um, lege sie zurück und mische.|
|[Piacentine-Karten](methods/piacentine/)|Nutze ein italienisches Regionaldeck mit 40 Karten.|
|[Tarot](methods/tarot/)|Nutze alle 78 Karten und ihre Bitwerte je Stufe.|

## Letztes Wort korrigieren

Für eine Mnemonik mit 12 Wörtern erzeugst du 12 vorläufige Wörter und korrigierst nur das zwölfte. Für 24 Wörter erzeugst du 24 und korrigierst nur das vierundzwanzigste. Das letzte Wort enthält Entropie und die BIP-39-Prüfsumme.

|Länge|Beibehaltener Teil des vorläufigen letzten Worts|Kandidaten in der Gruppe|
|-----|-----------------------------------------------|------------------------|
|12 Wörter|Erste 7 Bits|16|
|24 Wörter|Erste 3 Bits|128|

Finde die Gruppe in der [binären Worttabelle](../tables/binary-table/) und verwende eine vertrauenswürdige Offline-BIP-39-Wallet oder ein entsprechendes Werkzeug, um den richtigen Kandidaten zu bestimmen. Gib deine Mnemonik niemals auf einer Website oder einem nicht vertrauenswürdigen Gerät ein.
