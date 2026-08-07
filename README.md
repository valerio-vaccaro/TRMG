# TRMG -True Random Mnemonic Generator

## Introduction
Creating a mnemonic phrase using dice is often preferred over relying on a random number generator (RNG) chip or software script for the following reasons:

- True Randomness: Physical dice provide true randomness because their outcomes are determined by physical processes (e.g., rolling motion and surface interaction) that are inherently unpredictable. When rolled properly, dice are not influenced by external factors such as software bugs or hardware flaws. By contrast, hardware RNGs or software-based generators often rely on pseudo-random number generation (PRNG), whose output may be predictable if the seed or algorithm is compromised. Even true RNG chips can be tampered with or have manufacturing flaws, reducing trust in their randomness.

- Transparency and Verifiability: The process of rolling dice is transparent and verifiable by the user. You can physically see and confirm the outcome of each roll, ensuring no hidden manipulation. This makes it easy to audit the process yourself. RNG chips are black-box systems. You cannot easily verify the integrity of the chip or script. Software may have hidden backdoors, and hardware RNGs may have biases or vulnerabilities that are difficult to detect.

- No Dependency on Technology: Dice are low-tech, requiring no electricity, internet access, or software updates. This reduces the attack surface, as there is no risk of malware, hacking, or software vulnerabilities compromising the process. Specialized chips or scripts rely on electronic devices, which can be hacked, infected with malware, or subject to supply-chain attacks. A compromised device could leak your mnemonic phrase or generate predictable outputs.

- Resistance to Side-Channel Attacks: Rolling dice is immune to digital side-channel attacks like electromagnetic emissions, timing attacks, or power analysis, which can compromise hardware or software RNGs. Sophisticated attackers can exploit side-channel attacks to extract information from hardware RNGs or software running on a device, potentially compromising the generated mnemonic.

- User Control and Reproducibility: You have full control over the process, and it’s reproducible with minimal tools (just dice and a word list). You can repeat the process anywhere, anytime, without relying on specific hardware or software. RNG chips or scripts require access to specific devices or software, which may not always be available or trustworthy.

- Simplicity and Trust: The simplicity of dice makes them trustworthy. They’re physical objects with no hidden mechanisms, and their randomness is based on well-understood physical principles. Chips are complex systems, usually closed source, that require trust in the manufacturer, developer, or supply chain. Any flaw, intentional or not, could compromise security.

## Generate mnemonic
The first step is to generate 12 or 24 words. This can be done with dice, coins, or cards.

### Coin
[Coin guide](https://github.com/valerio-vaccaro/TRMG/blob/main/coin.md)

### D6 die
[D6 guide](https://github.com/valerio-vaccaro/TRMG/blob/main/d6.md)

### D8 die
[D8 guide](https://github.com/valerio-vaccaro/TRMG/blob/main/d8.md)

### A D8 die and two D16 dice
[Guide D8/D16/D16](https://github.com/valerio-vaccaro/TRMG/blob/main/d8ff.md)

### Three D8 dice and two coins
[Guide D8/D8/D8/coin/coin](https://github.com/valerio-vaccaro/TRMG/blob/main/888cc.md)

### Poker cards
[Cards](https://github.com/valerio-vaccaro/TRMG/blob/main/poker.md)

This process is entirely manual, auditable, and free from digital vulnerabilities.

### Piacentine cards
[Piacentine](https://github.com/valerio-vaccaro/TRMG/blob/main/piacentine.md)

Once again: a process entirely manual, totally lacking from digital fragilities.

### Tarot
[Tarot](https://github.com/valerio-vaccaro/TRMG/blob/main/tarot.md)

## Correct the final word

In BIP-39, the final word contains both entropy and a checksum. The checksum is calculated from all the entropy, so a final word selected entirely by dice is not necessarily valid. Keep the entropy portion from the dice result and replace only the checksum portion with the value required by the preceding words.

For a 12-word mnemonic, first generate 12 provisional words, then correct the 12th (final) word. For a 24-word mnemonic, first generate 24 provisional words, then correct the 24th (final) word. The first 11 or 23 words remain unchanged.

|Mnemonic length|Entropy bits in final word|Checksum bits|Possible final words|
|---------------|--------------------------|-------------|--------------------|
|12 words|7|4|16|
|24 words|3|8|128|

The [binary words table](binary-table.md) shows these entropy portions as **Group 12** and **Group 24**. Generate the first 11 or 23 words normally, then use the provisional final word obtained from your dice, cards, or coins to identify the appropriate group.

1. Find the provisional final word in the binary words table.
2. For a 12-word mnemonic, note its Group 12 value; for a 24-word mnemonic, note its Group 24 value.
3. Use an offline BIP-39-compatible wallet or tool to calculate valid final-word candidates from the preceding words.
4. Select the one candidate that belongs to the same group. Do not enter a mnemonic into a website or an untrusted device.

### Example: 12-word mnemonic

Suppose the provisional final word is index `1418`, **rally**. Its binary value is `10110001010`; the first seven bits are `1011000`. In the binary words table, its Group 12 value is therefore `1011000`.

Every index from `1408` through `1423` shares that seven-bit prefix, so the correct final word must be one of those 16 words. After entering the first 11 words into an offline BIP-39-compatible wallet or tool, it calculates the checksum and identifies exactly one valid word in that group. The correct word cannot be determined from `rally` alone: it depends on the preceding 11 words.

### Hardware wallets with final-word support

If your hardware wallet supports calculating valid final words (for example, Jade), compare its suggestions with the relevant group. Only one suggestion will belong to that group.

### If your wallet cannot calculate the final word

Test the candidates in the relevant group offline. There are at most 16 candidates for a 12-word mnemonic or 128 candidates for a 24-word mnemonic. Only one will have the correct checksum and produce a valid BIP-39 mnemonic.
