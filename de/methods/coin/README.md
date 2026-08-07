---
layout: default
title: Münzmethode
description: Erzeuge BIP-39-Wortindizes mit Münzwürfen.
lang: de
permalink: /de/methods/coin/
---

## Erzeuge eine Wiederherstellungsphrase mit einer Münze

Dies ist die einfachste Methode: Sie benötigt nur eine faire Münze. Jeder Wurf liefert ein Bit; erstelle daher jedes vorläufige BIP-39-Wort mit 11 Würfen. Wiederhole dies für 12 oder 24 Wörter und folge anschließend dem [Verfahren für das letzte Wort](../../#korrigiere-das-letzte-wort).

Wirf die Münze für jedes Wort 11-mal und verwende diese Zuordnung:

|Ergebnis|Bit|
|------|---|
|Kopf|0|
|Zahl|1|

Lies die 11 Ergebnisse von links nach rechts und verwende die [binäre Worttabelle](../../../tables/binary-table/), um den erhaltenen Wert einem BIP-39-Wort zuzuordnen.
