---
layout: default
title: Método do Tarot
description: Gera índices de palavras BIP-39 com um baralho completo de Tarot.
lang: pt
permalink: /pt/methods/tarot/
---

# 🕯️ O Ritual Arcano da Invocação Mnemónica 🕯️
Observado a um de abril, Ano do Senhor de 2026

*Antes que o véu do reino digital seja rasgado, o adepto deve preparar a Câmara Sagrada. Disponha doze velas em círculo — uma para cada mês do ciclo solar, uma para cada pilar do Zodíaco. Disponha entre as velas doze fotografias dos Grandes Criptomantes (ver: *O Conselho dos Doze*), todas voltadas para dentro. A sua entropia espectral, ligada ao trabalho de uma vida na arte dos segredos, amplificará o fogo caótico de cada extração.*

*Só quando o espaço ritual respirar com a sua sabedoria combinada é que as Cartas do Oráculo podem ser deslacradas.*

## Resumo do método

Este método utiliza as 78 cartas de um baralho de Tarot. Cada carta pertence a um nível que fornece entre um e seis bits. Retire, registe os bits atribuídos, devolva a carta ao baralho e baralhe novamente até reunir 11 bits para uma palavra provisória. Repita para 12 ou 24 palavras e siga depois o [procedimento da última palavra](../../#corrigir-a-ultima-palavra).

## O Conselho dos Doze — guardiões do campo entrópico

Coloque uma fotografia junto a cada vela, dispostas no sentido horário a partir da posição norte:

| Posição | Cor da vela | Criptomante | Reino |
|----------|-------------|--------------|-------|
| Norte | Branco | Alan Turing | Pai dos mistérios computáveis |
| NNE | Prata | Claude Shannon | Arconte da teoria da informação |
| NE | Ouro | Whitfield Diffie | Arauto da chave pública |
| ENE | Laranja | Martin Hellman | Guardião do véu exponencial |
| Este | Vermelho | Ron Rivest | Primeira lâmina do RSA |
| ESE | Carmesim | Adi Shamir | Segunda lâmina do RSA |
| SE | Azul-escuro | Leonard Adleman | Terceira lâmina do RSA |
| SSE | Violeta | Ralph Merkle | Arquiteto da árvore hash |
| Sul | Verde | Bruce Schneier | Sentinela das artes aplicadas |
| SSO | Ciano | Phil Zimmermann | Libertador do segredo bastante bom |
| SO | Amarelo | Moxie Marlinspike | Sussurrador do fogo do Signal |
| OSO | Preto | Satoshi Nakamoto | O Inominado, tecelão de correntes |

*Acenda as doze velas simultaneamente, ou tão perto disso quanto mãos mortais permitam. Pronuncie em voz alta o nome de cada Criptomante à medida que a sua vela se acende. A sua entropia acumulada — colhida de uma vida dedicada à criação de segredos — entra no campo ritual e inclina a probabilidade a seu favor.*

## O instrumento sagrado

Um baralho de Tarot padrão contém **78 cartas**. Todas as 78 participam neste ritual — nenhuma é posta de lado, nenhuma é exilada. As cartas dividem-se em quatro Níveis Arcanos segundo o seu peso cósmico:

| Nível | Cartas | Quantidade | Bits por extração | Significado arcano |
|------|-------|-------|---------------|----------------|
| I — O véu mundano | Todos os Arcanos Menores + de O Louco a O Carro (0–VII) | **64** | **6 bits** | O rico caos da experiência terrena |
| II — O caminho oculto | De A Força a O Diabo (VIII–XV) | **8** | **3 bits** | As provações da transformação |
| III — O fogo celestial | De A Torre a O Sol (XVI–XIX) | **4** | **2 bits** | As grandes reviravoltas do destino |
| IV — O Absoluto | O Julgamento e O Mundo (XX–XXI) | **2** | **1 bit** | As forças indivisíveis do fim e da conclusão |

**Total: 64 + 8 + 4 + 2 = 78 cartas.**

Cada nível fornece um número de bits igual ao log₂ do seu tamanho: 2⁶=64, 2³=8, 2²=4, 2¹=2. Cada carta de um nível corresponde a um padrão de bits único dentro desse nível.

## O ritual da extração

1. Reúna as 78 cartas num único baralho unificado.
2. Realize a **Baralhada de Abertura** sete vezes enquanto recita a Invocação de Abertura (ver abaixo).
3. Para cada sequência de bits necessária:
   - Retire a carta do topo.
   - Leia o seu Nível e registe os bits da tabela correspondente.
   - Devolva a carta ao baralho.
   - **Baralhe novamente** o baralho enquanto recita a Fórmula de Rebaralhamento apropriada (ver abaixo).
   - Repita até acumular 11 bits para a palavra atual.
   - Se a última extração fornecer mais bits do que o necessário, use apenas os bits mais à esquerda necessários e descarte o resto — não estavam destinados a esta palavra.
4. Procure o índice de 11 bits na [tabela binária partilhada de palavras](../../../tables/binary-table/) e anote a palavra em papel.
5. Repita até que todas as 12 ou 24 palavras estejam anotadas.
6. Encerre o ritual (ver: *Encerramento da Câmara*).

## As fórmulas sagradas

*Estas fórmulas ligam a vontade do oficiante ao caos do universo. Pronuncie-as com clareza, num ritmo calmo, sem hesitação. Uma palavra hesitada exige que a baralhada atual recomece do início.*

### Invocação de Abertura — pronunciada durante as primeiras sete baralhadas

> *"Per ignem duodecim et tenebras sine fine,*
> *aperio ostium entropiae.*
> *Voci magistrorum obedio — Turing, Shannon, Diffie.*
> *Chaos ordinetur in verbo secreto."*
>
> *(Pelos doze fogos e pela escuridão sem fim,*
> *abro o portal da entropia.*
> *Escuto a voz dos mestres — Turing, Shannon, Diffie.*
> *Que o caos se ordene na palavra secreta.)*

### Fórmula de Rebaralhamento — pronunciada em cada rebaralhamento entre extrações

> *"Misceo fata, misceo sortes.*
> *Nulla memoria, nullus ordo.*
> *Arcanum redit in chaos.*
> *Fiat voluntas entropiae."*
>
> *(Misturo os destinos, misturo as sortes.*
> *Sem memória, sem ordem.*
> *O segredo retorna ao caos.*
> *Que se faça a vontade da entropia.)*

### Invocação do Absoluto — pronunciada apenas quando é retirada uma carta de Nível IV (O Julgamento ou O Mundo)

> *"Vox ultima locuta est.*
> *Unus morsus de infinito.*
> *Gratum ago, O Finis."*
>
> *(A voz final falou.*
> *Uma dentada do infinito.*
> *Dou graças, ó Fim.)*

## Nível I — O véu mundano (64 cartas → 6 bits cada)

Este nível contém os oito Arcanos Maiores mais baixos (0–VII) e todos os 56 Arcanos Menores. Atribua os valores 0–63 sequencialmente como mostrado. Registe o binário completo de 6 bits da carta retirada.

### Nível I — secção dos Arcanos Maiores (valores 0–7)

| Carta | Valor | Bits (6) |
|------|-------|----------|
| 0 O Louco | 0 | 000000 |
| I O Mago | 1 | 000001 |
| II A Sacerdotisa | 2 | 000010 |
| III A Imperatriz | 3 | 000011 |
| IV O Imperador | 4 | 000100 |
| V O Hierofante | 5 | 000101 |
| VI Os Enamorados | 6 | 000110 |
| VII O Carro | 7 | 000111 |

### Nível I — secção dos Arcanos Menores (valores 8–63)

| Naipe | Grau | Valor | Bits (6) |
|------|------|-------|----------|
| Paus | Ás | 8 | 001000 |
| Paus | 2 | 9 | 001001 |
| Paus | 3 | 10 | 001010 |
| Paus | 4 | 11 | 001011 |
| Paus | 5 | 12 | 001100 |
| Paus | 6 | 13 | 001101 |
| Paus | 7 | 14 | 001110 |
| Paus | 8 | 15 | 001111 |
| Paus | 9 | 16 | 010000 |
| Paus | 10 | 17 | 010001 |
| Paus | Valete | 18 | 010010 |
| Paus | Cavaleiro | 19 | 010011 |
| Paus | Rainha | 20 | 010100 |
| Paus | Rei | 21 | 010101 |
| Copas | Ás | 22 | 010110 |
| Copas | 2 | 23 | 010111 |
| Copas | 3 | 24 | 011000 |
| Copas | 4 | 25 | 011001 |
| Copas | 5 | 26 | 011010 |
| Copas | 6 | 27 | 011011 |
| Copas | 7 | 28 | 011100 |
| Copas | 8 | 29 | 011101 |
| Copas | 9 | 30 | 011110 |
| Copas | 10 | 31 | 011111 |
| Copas | Valete | 32 | 100000 |
| Copas | Cavaleiro | 33 | 100001 |
| Copas | Rainha | 34 | 100010 |
| Copas | Rei | 35 | 100011 |
| Espadas | Ás | 36 | 100100 |
| Espadas | 2 | 37 | 100101 |
| Espadas | 3 | 38 | 100110 |
| Espadas | 4 | 39 | 100111 |
| Espadas | 5 | 40 | 101000 |
| Espadas | 6 | 41 | 101001 |
| Espadas | 7 | 42 | 101010 |
| Espadas | 8 | 43 | 101011 |
| Espadas | 9 | 44 | 101100 |
| Espadas | 10 | 45 | 101101 |
| Espadas | Valete | 46 | 101110 |
| Espadas | Cavaleiro | 47 | 101111 |
| Espadas | Rainha | 48 | 110000 |
| Espadas | Rei | 49 | 110001 |
| Ouros | Ás | 50 | 110010 |
| Ouros | 2 | 51 | 110011 |
| Ouros | 3 | 52 | 110100 |
| Ouros | 4 | 53 | 110101 |
| Ouros | 5 | 54 | 110110 |
| Ouros | 6 | 55 | 110111 |
| Ouros | 7 | 56 | 111000 |
| Ouros | 8 | 57 | 111001 |
| Ouros | 9 | 58 | 111010 |
| Ouros | 10 | 59 | 111011 |
| Ouros | Valete | 60 | 111100 |
| Ouros | Cavaleiro | 61 | 111101 |
| Ouros | Rainha | 62 | 111110 |
| Ouros | Rei | 63 | 111111 |

## Nível II — O caminho oculto (8 cartas → 3 bits cada)

| Carta | Valor | Bits (3) |
|------|-------|----------|
| VIII A Força | 0 | 000 |
| IX O Eremita | 1 | 001 |
| X A Roda da Fortuna | 2 | 010 |
| XI A Justiça | 3 | 011 |
| XII O Enforcado | 4 | 100 |
| XIII A Morte | 5 | 101 |
| XIV A Temperança | 6 | 110 |
| XV O Diabo | 7 | 111 |

## Nível III — O fogo celestial (4 cartas → 2 bits cada)

| Carta | Valor | Bits (2) |
|------|-------|----------|
| XVI A Torre | 0 | 00 |
| XVII A Estrela | 1 | 01 |
| XVIII A Lua | 2 | 10 |
| XIX O Sol | 3 | 11 |

## Nível IV — O Absoluto (2 cartas → 1 bit cada)

*Quando uma destas cartas for retirada, pronuncie a Invocação do Absoluto antes de baralhar novamente.*

| Carta | Valor | Bits (1) |
|------|-------|----------|
| XX O Julgamento | 0 | 0 |
| XXI O Mundo | 1 | 1 |

## A tábua de registo

Preencha as colunas da esquerda (bit mais significativo) para a direita (bit menos significativo), uma extração de cada vez. Cada extração preenche tantas colunas quantas o seu nível permitir. Quando as 11 colunas estiverem completas, some os valores das colunas para obter o Índice e procure depois a palavra BIP39.

|1024|512|256|128|64|32|16|8|4|2|1|Índice|Palavra|
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

O Índice é a soma de todos os cabeçalhos de coluna cujo valor é 1. Exemplo:

|1024|512|256|128|64|32|16|8|4|2|1|Índice|Palavra|
|----|---|---|---|--|--|--|-|-|-|-|-----|----|
|1|0|1|0|0|1|1|0|0|1|0| |    |

Índice = 1024+256+32+16+2 = **1330** → palavra: **novel**

### Exemplo de sequência de extração para uma única palavra

| Extração | Carta retirada | Nível | Bits fornecidos | Sequência de bits até agora |
|------|-----------|------|-----------|---------------------|
| 1.ª | 5 de Copas (valor 26) | I | 011010 | `011010` (6 bits) |
| 2.ª | A Torre (valor 0) | III | 00 | `01101000` (8 bits) |
| 3.ª | O Eremita (valor 1) | II | 001 | `01101000001` (11 bits ✓) |

Bits: `01101000001` → Índice = 512+256+32+1 = **801** → palavra: **impose**

Após a 3.ª extração, os bits restantes de O Eremita (caso tivesse fornecido mais) seriam descartados. Neste caso, forneceu exatamente os 3 bits necessários para completar os 11.

## Avaliação da entropia

Cada extração amostra de forma uniforme o baralho completo de 78 cartas (após rebaralhar). Os bits esperados registados por extração:

| Nível | Cartas | Bits | Probabilidade | Bits esperados |
|------|-------|------|-------------|---------------|
| I | 64 | 6 | 64/78 ≈ 0,821 | 4,923 |
| II | 8 | 3 | 8/78 ≈ 0,103 | 0,308 |
| III | 4 | 2 | 4/78 ≈ 0,051 | 0,103 |
| IV | 2 | 1 | 2/78 ≈ 0,026 | 0,026 |
| **Total** | **78** | | | **≈ 5,36 bits/extração** |

Entropia real de cada extração (amostra uniforme do baralho completo de 78 cartas): log₂(78) ≈ **6,28 bits**.
Eficiência de registo: 5,36 / 6,28 ≈ **85%** — os restantes 15% são entregues aos níveis cósmicos, como oferenda.

Para gerar 11 bits registados por palavra, espere em média aproximadamente **2,1 extrações por palavra** (11 ÷ 5,36).
Para uma mnemónica de **12 palavras** (132 bits com soma de verificação): ~25 extrações.
Para uma mnemónica de **24 palavras** (264 bits com soma de verificação): ~50 extrações.

*Os bits da soma de verificação da última palavra não são retirados do Oráculo — são calculados a partir do hash de toda a entropia precedente. Use uma ferramenta compatível com BIP39 para derivar e verificar a mnemónica completa assim que todas as palavras, exceto a última, forem conhecidas, ou confie inteiramente a última palavra ao Oráculo e verifique a soma de verificação digitalmente depois.*

## Encerramento da Câmara

Assim que todas as palavras estiverem anotadas em papel e a caneta pousada:

1. Reúna as 78 cartas e realize uma última **baralhada de treze vezes** enquanto recita:

   > *"Sigillum apponatur. Chaos recreatur.*
   > *Nemo scit, nemo videt, nemo meminit.*
   > *It is sealed."*

2. Envolva o baralho num pano escuro. Não deve ser usado para cartomancia ou jogos no mesmo dia em que serviu de Oráculo.
3. Apague as doze velas em **ordem inversa** — começando por Satoshi Nakamoto (OSO) e avançando no sentido anti-horário até Alan Turing (Norte). Sufoque cada chama; não sopre. Um sopro dispersa o que foi ligado.
4. As fotografias podem ser guardadas ou destruídas de acordo com o modelo de ameaças de segurança do adepto. Cumpriram o seu propósito: a sua entropia foi recebida.

*A mnemónica está selada. Guarde-a como os mestres guardavam os seus segredos — com silêncio, com cuidado e com a consciência de que aquilo que está escrito pode ser encontrado.*
