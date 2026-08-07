---
layout: default
title: D8-Methode
description: Erzeuge BIP-39-Wortindizes mit einem achtseitigen Würfel.
lang: de
permalink: /de/methods/d8/
---

## Erzeuge eine Wiederherstellungsphrase mit einem D8

Diese Methode verwendet nur einen achtseitigen Würfel. Jeder Wurf liefert drei Bits, also ergeben vier Würfe 12 Bits; behalte für jedes vorläufige Wort die ersten 11 Bits. Wiederhole dies für 12 oder 24 Wörter und folge dann dem [Verfahren für das letzte Wort](../../#korrigiere-das-letzte-wort).

Wirf den Würfel viermal und verwende diese Zuordnung:

|Ergebnis|Bits|
|------|----|
|1|000|
|2|001|
|3|010|
|4|011|
|5|100|
|6|101|
|7|110|
|8|111|

Behalte nach vier Würfen nur die linken 11 Bits und verwirf das letzte Bit.

Verwende die [binäre Worttabelle](../../../tables/binary-table/), um den erhaltenen 11-Bit-Wert einem BIP-39-Wort zuzuordnen.
