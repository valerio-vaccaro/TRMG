---
layout: default
title: Generare una frase mnemonica offline
description: Guida per creare parole BIP-39 con casualità fisica.
lang: it
---

<section class="hero">
  <div class="eyebrow">Casualità fisica verificabile a mano</div>
  <h1>Genera parole mnemoniche dal mondo reale.</h1>
  <p>TRMG trasforma i risultati di dadi, monete e carte in indici BIP-39. Annota 11 bit per ogni parola provvisoria e correggi offline la parola finale di controllo.</p>
  <a class="button" href="#methods">Scegli un metodo</a>
</section>

## Come funziona

Ogni metodo produce un numero di 11 bit compreso tra `0` e `2047`. Cerca il numero nella tabella delle parole, ripeti fino a ottenere 12 o 24 parole provvisorie e poi correggi l'ultima parola.

> **La qualità dell’entropia è importante.** Usa solo dadi, monete o carte quanto più possibile equilibrati e privi di distorsioni. Verifica che non siano danneggiati o soggetti a difetti di fabbricazione e mescola accuratamente le carte tra un’estrazione e l’altra. Una fonte fisica distorta riduce la qualità dell’entropia della frase mnemonica risultante.

> **Usa a tuo rischio.** Questi metodi e questo sito web sono forniti così come sono, senza alcuna garanzia sulla sicurezza della tua frase mnemonica o dei tuoi fondi. Sei l’unico responsabile della verifica del processo e di qualsiasi perdita di fondi derivante dal suo utilizzo.

> **Conserva una copia di sicurezza della frase mnemonica.** Un backup offline affidabile è essenziale per non perdere l’accesso ai tuoi fondi. Conservalo al riparo da smarrimento, danni, furto e accessi non autorizzati; non fare mai affidamento su una sola copia o su uno screenshot digitale.

> **Limita l’esposizione della frase mnemonica.** Non copiare né inserire la frase mnemonica su più dispositivi o computer. Usala solo con il wallet software o hardware per cui è stata generata e soltanto quando necessario.

## Metodi {#methods}

|Metodo|Come produce ogni parola provvisoria|
|------|-------------------------------------|
|[Moneta](methods/coin/)|Undici lanci: testa vale `0` e croce vale `1`.|
|[D6](methods/d6/)|Converti ogni lancio in uno o due bit.|
|[D8](methods/d8/)|Quattro lanci producono 12 bit; conserva i primi 11.|
|[D8/D16/D16](methods/d8d16d16/)|Tre dadi selezionano un indice in un'unica serie di lanci.|
|[D8/D8/D8/moneta/moneta](methods/888cc/)|Tre lanci e due monete selezionano un indice.|
|[Carte da poker](methods/poker/)|Estrai una carta, convertila in bit, rimettila nel mazzo e mescola.|
|[Carte piacentine](methods/piacentine/)|Usa un mazzo regionale italiano da 40 carte.|
|[Tarocchi](methods/tarot/)|Usa tutte le 78 carte e i loro valori in bit per livello.|

## Correggere l'ultima parola {#correct-the-final-word}

Per una frase di 12 parole, genera 12 parole provvisorie e correggi solo la dodicesima. Per una frase di 24 parole, generane 24 e correggi solo la ventiquattresima. L'ultima parola combina entropia e checksum BIP-39.

|Lunghezza|Parte conservata dell'ultima parola provvisoria|Possibili parole finali (con l'entropia selezionata)|
|---------|-----------------------------------------------|-------------------|
|12 parole|Primi 7 bit|16|
|24 parole|Primi 3 bit|256|

Trova il gruppo nella [tabella binaria delle parole](../tables/binary-table/) e usa un wallet o strumento BIP-39 affidabile e offline per trovare la candidata corretta. Non inserire mai la frase mnemonica in un sito web o in un dispositivo non affidabile.
