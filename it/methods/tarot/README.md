---
layout: default
title: Metodo dei Tarocchi
description: Genera indici di parole BIP-39 con un mazzo completo di Tarocchi.
lang: it
permalink: /it/methods/tarot/
---

# 🕯️ Il rituale arcano per evocare una frase mnemonica 🕯️
Osservato il primo aprile, Anno Domini 2026

*Prima che il velo del regno digitale venga squarciato, l’adepto deve preparare la Camera Sacra. Disponi dodici candele in cerchio — una per ogni mese del ciclo solare, una per ogni pilastro dello Zodiaco. Disponi tra le candele dodici fotografie dei Grandi Criptomanti (vedi: *Il Consiglio dei Dodici*), tutte rivolte verso l’interno. La loro entropia spettrale, legata al lavoro di una vita nell’arte dei segreti, amplificherà il fuoco caotico di ogni estrazione.*

*Solo quando lo spazio rituale respira della loro saggezza congiunta le Carte dell’Oracolo possono essere dissigillate.*

## Sintesi del metodo

Questo metodo usa tutte le 78 carte di un mazzo di Tarocchi. Ogni carta appartiene a un livello che fornisce da uno a sei bit. Estrai, registra i bit assegnati, rimetti la carta nel mazzo e rimescola finché non hai 11 bit per una parola provvisoria. Ripeti per 12 o 24 parole, quindi segui la [procedura per l’ultima parola](../../#correggi-lultima-parola).

## Il Consiglio dei Dodici — guardiani del campo entropico

Colloca una fotografia accanto a ogni candela, disposta in senso orario a partire dalla posizione nord:

| Posizione | Colore della candela | Criptomante | Regno |
|----------|-------------|--------------|-------|
| Nord | Bianco | Alan Turing | Padre dei misteri computabili |
| NNE | Argento | Claude Shannon | Arconte della teoria dell’informazione |
| NE | Oro | Whitfield Diffie | Araldo della chiave pubblica |
| ENE | Arancione | Martin Hellman | Custode del velo esponenziale |
| Est | Rosso | Ron Rivest | Prima lama di RSA |
| ESE | Cremisi | Adi Shamir | Seconda lama di RSA |
| SE | Blu scuro | Leonard Adleman | Terza lama di RSA |
| SSE | Viola | Ralph Merkle | Architetto dell’albero hash |
| Sud | Verde | Bruce Schneier | Sentinella delle arti applicate |
| SSO | Cyan | Phil Zimmermann | Liberatore del segreto abbastanza buono |
| SO | Giallo | Moxie Marlinspike | Sussurratore del fuoco di Signal |
| OSO | Nero | Satoshi Nakamoto | L’innominato, tessitore di catene |

*Accendi tutte e dodici le candele simultaneamente, o quanto più possibile alle mani mortali. Pronuncia ad alta voce il nome di ogni Criptomante mentre la sua candela si accende. La loro entropia accumulata — raccolta da una vita dedicata alla creazione di segreti — entra nel campo rituale e piega la probabilità a tuo favore.*

## Lo strumento sacro

Un mazzo standard di Tarocchi contiene **78 carte**. Tutte le 78 partecipano a questo rituale — nessuna è messa da parte, nessuna è esiliata. Le carte sono divise in quattro livelli arcani secondo il loro peso cosmico:

| Livello | Carte | Numero | Bit per estrazione | Significato arcano |
|------|-------|-------|---------------|----------------|
| I — Il velo mondano | Tutti gli Arcani Minori + dal Matto al Carro (0–VII) | **64** | **6 bit** | Il ricco caos dell’esperienza terrena |
| II — Il sentiero nascosto | dalla Forza al Diavolo (VIII–XV) | **8** | **3 bit** | Le prove della trasformazione |
| III — Il fuoco celeste | dalla Torre al Sole (XVI–XIX) | **4** | **2 bit** | I grandi sconvolgimenti del destino |
| IV — L’assoluto | Giudizio e Mondo (XX–XXI) | **2** | **1 bit** | Le forze indivisibili della fine e del compimento |

**Totale: 64 + 8 + 4 + 2 = 78 carte.**

Ogni livello fornisce un numero di bit pari al log₂ della sua dimensione: 2⁶=64, 2³=8, 2²=4, 2¹=2. Ogni carta di un livello corrisponde a un unico schema di bit all’interno di quel livello.

## Il rituale dell’estrazione

1. Riunisci tutte le 78 carte in un unico mazzo.
2. Esegui sette volte il **rimescolamento di apertura** recitando l’invocazione di apertura (vedi sotto).
3. Per ogni sequenza di bit necessaria:
   - Estrai la carta in cima al mazzo.
   - Leggi il suo livello e registra i bit dalla tabella corrispondente.
   - Rimetti la carta nel mazzo.
   - **Rimescola** il mazzo recitando l’appropriata formula di rimescolamento (vedi sotto).
   - Ripeti finché non hai accumulato 11 bit per la parola corrente.
   - Se l’ultima estrazione fornisce più bit del necessario, prendi soltanto i bit più a sinistra richiesti e scarta gli altri — non erano destinati a questa parola.
4. Cerca l’indice di 11 bit nella [tabella binaria condivisa delle parole](../../../tables/binary-table/) e annota la parola su carta.
5. Ripeti finché tutte le 12 o 24 parole non sono annotate.
6. Chiudi il rituale (vedi: *Chiusura della Camera*).

## Le formule sacre

*Queste formule legano la volontà dell’officiante al caos dell’universo. Pronunciale chiaramente, a ritmo misurato, senza esitazioni. Una parola inciampata richiede di ricominciare il rimescolamento corrente.*

### Invocazione di apertura — pronunciata durante i primi sette rimescolamenti

> *"Per ignem duodecim et tenebras sine fine,*
> *aperio ostium entropiae.*
> *Voci magistrorum obedio — Turing, Shannon, Diffie.*
> *Chaos ordinetur in verbo secreto."*
>
> *(Per i dodici fuochi e il buio senza fine,*
> *apro il cancello dell’entropia.*
> *ascolto la voce dei maestri — Turing, Shannon, Diffie.*
> *Il caos sia ordinato nella parola segreta.)*

### Formula di rimescolamento — pronunciata durante ogni rimescolamento tra le estrazioni

> *"Misceo fata, misceo sortes.*
> *Nulla memoria, nullus ordo.*
> *Arcanum redit in chaos.*
> *Fiat voluntas entropiae."*
>
> *(Mescolo i destini, mescolo le sorti.*
> *Nessuna memoria, nessun ordine.*
> *Il segreto ritorna al caos.*
> *Sia fatta la volontà dell’entropia.)*

### Invocazione dell’Assoluto — pronunciata soltanto quando viene estratta una carta di livello IV (Giudizio o Mondo)

> *"Vox ultima locuta est.*
> *Unus morsus de infinito.*
> *Gratum ago, O Finis."*
>
> *(La voce finale ha parlato.*
> *Un morso dell’infinito.*
> *Rendo grazie, o Fine.)*

## Livello I — Il velo mondano (64 carte → 6 bit ciascuna)

Questo livello contiene gli otto Arcani Maggiori più bassi (0–VII) e tutti i 56 Arcani Minori. Assegna in sequenza i valori da 0 a 63 come mostrato. Registra il binario completo di 6 bit della carta estratta.

### Livello I — sezione degli Arcani Maggiori (valori 0–7)

| Carta | Valore | Bit (6) |
|------|-------|----------|
| 0 Il Matto | 0 | 000000 |
| I Il Bagatto | 1 | 000001 |
| II La Papessa | 2 | 000010 |
| III L’Imperatrice | 3 | 000011 |
| IV L’Imperatore | 4 | 000100 |
| V Il Papa | 5 | 000101 |
| VI Gli Amanti | 6 | 000110 |
| VII Il Carro | 7 | 000111 |

### Livello I — sezione degli Arcani Minori (valori 8–63)

| Seme | Valore | Bit (6) |
|------|------|-------|----------|
| Bastoni | Asso | 8 | 001000 |
| Bastoni | 2 | 9 | 001001 |
| Bastoni | 3 | 10 | 001010 |
| Bastoni | 4 | 11 | 001011 |
| Bastoni | 5 | 12 | 001100 |
| Bastoni | 6 | 13 | 001101 |
| Bastoni | 7 | 14 | 001110 |
| Bastoni | 8 | 15 | 001111 |
| Bastoni | 9 | 16 | 010000 |
| Bastoni | 10 | 17 | 010001 |
| Bastoni | Fante | 18 | 010010 |
| Bastoni | Cavaliere | 19 | 010011 |
| Bastoni | Regina | 20 | 010100 |
| Bastoni | Re | 21 | 010101 |
| Coppe | Asso | 22 | 010110 |
| Coppe | 2 | 23 | 010111 |
| Coppe | 3 | 24 | 011000 |
| Coppe | 4 | 25 | 011001 |
| Coppe | 5 | 26 | 011010 |
| Coppe | 6 | 27 | 011011 |
| Coppe | 7 | 28 | 011100 |
| Coppe | 8 | 29 | 011101 |
| Coppe | 9 | 30 | 011110 |
| Coppe | 10 | 31 | 011111 |
| Coppe | Fante | 32 | 100000 |
| Coppe | Cavaliere | 33 | 100001 |
| Coppe | Regina | 34 | 100010 |
| Coppe | Re | 35 | 100011 |
| Spade | Asso | 36 | 100100 |
| Spade | 2 | 37 | 100101 |
| Spade | 3 | 38 | 100110 |
| Spade | 4 | 39 | 100111 |
| Spade | 5 | 40 | 101000 |
| Spade | 6 | 41 | 101001 |
| Spade | 7 | 42 | 101010 |
| Spade | 8 | 43 | 101011 |
| Spade | 9 | 44 | 101100 |
| Spade | 10 | 45 | 101101 |
| Spade | Fante | 46 | 101110 |
| Spade | Cavaliere | 47 | 101111 |
| Spade | Regina | 48 | 110000 |
| Spade | Re | 49 | 110001 |
| Denari | Asso | 50 | 110010 |
| Denari | 2 | 51 | 110011 |
| Denari | 3 | 52 | 110100 |
| Denari | 4 | 53 | 110101 |
| Denari | 5 | 54 | 110110 |
| Denari | 6 | 55 | 110111 |
| Denari | 7 | 56 | 111000 |
| Denari | 8 | 57 | 111001 |
| Denari | 9 | 58 | 111010 |
| Denari | 10 | 59 | 111011 |
| Denari | Fante | 60 | 111100 |
| Denari | Cavaliere | 61 | 111101 |
| Denari | Regina | 62 | 111110 |
| Denari | Re | 63 | 111111 |

## Livello II — Il sentiero nascosto (8 carte → 3 bit ciascuna)

| Carta | Valore | Bit (3) |
|------|-------|----------|
| VIII La Forza | 0 | 000 |
| IX L’Eremita | 1 | 001 |
| X La Ruota della Fortuna | 2 | 010 |
| XI La Giustizia | 3 | 011 |
| XII L’Appeso | 4 | 100 |
| XIII La Morte | 5 | 101 |
| XIV La Temperanza | 6 | 110 |
| XV Il Diavolo | 7 | 111 |

## Livello III — Il fuoco celeste (4 carte → 2 bit ciascuna)

| Carta | Valore | Bit (2) |
|------|-------|----------|
| XVI La Torre | 0 | 00 |
| XVII La Stella | 1 | 01 |
| XVIII La Luna | 2 | 10 |
| XIX Il Sole | 3 | 11 |

## Livello IV — L’assoluto (2 carte → 1 bit ciascuna)

*Quando viene estratta una di queste carte, pronuncia l’Invocazione dell’Assoluto prima di rimescolare.*

| Carta | Valore | Bit (1) |
|------|-------|----------|
| XX Il Giudizio | 0 | 0 |
| XXI Il Mondo | 1 | 1 |

## La tavola di registrazione

Compila le colonne da sinistra (bit più significativo) a destra (bit meno significativo), un’estrazione alla volta. Ogni estrazione riempie tante colonne quante ne permette il livello. Quando 11 colonne sono piene, somma i valori delle colonne per ottenere l’indice, quindi cerca la parola BIP39.

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Parola|
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

L’indice è la somma di tutte le intestazioni di colonna il cui valore è 1. Esempio:

|1024|512|256|128|64|32|16|8|4|2|1|Indice|Parola|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1|0|1|0|0|1|1|0|0|1|0| |    |

Indice = 1024+256+32+16+2 = **1330** → parola: **novel**

### Esempio di sequenza di estrazioni per una parola

| Estrazione | Carta estratta | Livello | Bit forniti | Sequenza di bit finora |
|------|-----------|------|-----------|---------------------|
| 1ª | 5 di Coppe (valore 26) | I | 011010 | `011010` (6 bit) |
| 2ª | La Torre (valore 0) | III | 00 | `01101000` (8 bit) |
| 3ª | L’Eremita (valore 1) | II | 001 | `01101000001` (11 bit ✓) |

Bit: `01101000001` → Indice = 512+256+32+1 = **801** → parola: **impose**

Dopo la terza estrazione, i bit rimanenti dell’Eremita (se ne avesse forniti di più) sarebbero scartati. In questo caso ha fornito esattamente i 3 bit necessari per completare 11.

## Valutazione dell’entropia

Ogni estrazione campiona uniformemente dall’intero mazzo di 78 carte (dopo il rimescolamento). I bit attesi registrati per estrazione sono:

| Livello | Carte | Bit | Probabilità | Bit attesi |
|------|-------|------|-------------|---------------|
| I | 64 | 6 | 64/78 ≈ 0.821 | 4.923 |
| II | 8 | 3 | 8/78 ≈ 0.103 | 0.308 |
| III | 4 | 2 | 4/78 ≈ 0.051 | 0.103 |
| IV | 2 | 1 | 2/78 ≈ 0.026 | 0.026 |
| **Totale** | **78** | | | **≈ 5,36 bit/estrazione** |

Entropia effettiva di ogni estrazione (campione uniforme dell’intero mazzo di 78 carte): log₂(78) ≈ **6,28 bit**.
Efficienza di registrazione: 5,36 / 6,28 ≈ **85%** — il restante 15% è offerto ai livelli cosmici.

Per generare 11 bit registrati per parola, prevedi in media circa **2,1 estrazioni per parola** (11 ÷ 5,36).
Per una frase mnemonica di **12 parole** (132 bit con checksum): circa 25 estrazioni.
Per una frase mnemonica di **24 parole** (264 bit con checksum): circa 50 estrazioni.

*I bit di checksum dell’ultima parola non vengono estratti dall’Oracolo — sono calcolati dall’hash di tutta l’entropia precedente. Usa uno strumento conforme a BIP39 per derivare e verificare la frase mnemonica completa quando tutte le parole tranne l’ultima sono note, oppure affida interamente l’ultima parola all’Oracolo e verifica successivamente il checksum in digitale.*

## Chiusura della Camera

Una volta annotate tutte le parole su carta e riposta la penna:

1. Raccogli tutte le 78 carte ed esegui un ultimo **rimescolamento di tredici volte** recitando:

   > *"Sigillum apponatur. Chaos recreatur.*
   > *Nemo scit, nemo videt, nemo meminit.*
   > *It is sealed."*

2. Avvolgi il mazzo in un panno scuro. Non deve essere usato per cartomanzia o giochi nello stesso giorno in cui è servito da Oracolo.
3. Spegni le dodici candele in **ordine inverso** — iniziando da Satoshi Nakamoto (OSO) e procedendo in senso antiorario fino ad Alan Turing (Nord). Soffoca ogni fiamma; non soffiare. Un respiro disperde ciò che era stato legato.
4. Le fotografie possono essere conservate o distrutte secondo il modello di minaccia dell’adepto. Hanno assolto il loro scopo: la loro entropia è stata ricevuta.

*La frase mnemonica è sigillata. Custodiscila come i maestri custodivano i loro segreti — con silenzio, con cura e con la consapevolezza che ciò che è scritto può essere trovato.*
