---
layout: default
title: D6-Methode
description: Erzeuge BIP-39-Wortindizes mit einem sechsseitigen Würfel.
lang: de
permalink: /de/methods/d6/
---

## Erzeuge eine Wiederherstellungsphrase mit einem D6

Diese Methode verwendet einen normalen sechsseitigen Würfel. Die Ergebnisse 1 bis 4 liefern jeweils zwei Bits, 5 und 6 jeweils ein Bit; die Anzahl nötiger Würfe pro vorläufigem Wort variiert daher. Fahre fort, bis du 11 Bits hast, wiederhole dies für 12 oder 24 Wörter und folge dann dem [Verfahren für das letzte Wort](../../#korrigiere-das-letzte-wort).

Wirf den Würfel, bis du 11 Bits hast, und verwende diese Zuordnung:

|Ergebnis|Bits|
|------|----|
|1|00|
|2|01|
|3|10|
|4|11|
|5|0|
|6|1|

Liefert der letzte Wurf mehr Bits als nötig, behalte nur die linken Bits, die zum Erreichen von 11 Bits nötig sind.

Lies den gesammelten 11-Bit-Wert von links nach rechts und verwende die [binäre Worttabelle](../../../tables/binary-table/), um das BIP-39-Wort zu finden.
