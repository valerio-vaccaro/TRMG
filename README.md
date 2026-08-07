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

### D8 + D16 + D16 dice
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

## Fix last word
The last word is partly determined by the checksum of the previous words, so it must be corrected to comply with the BIP-39 standard. The table lists possible final-word groups: Group 12 for 12-word mnemonics and Group 24 for 24-word mnemonics.

Use the last word obtained with the dice to identify its group of possible final words.

Groups are based on partial entropy. For a 12-word mnemonic created with D8/D16/D16 dice, use only the first and second die results. They identify a group of 16 possible words, shown in the Group 12 column. For a 24-word mnemonic, use only the first die result. It identifies a group of 128 possible words, shown in the Group 24 column. If your software or hardware wallet reports an error, replace the final word with another word from the relevant group.

### Hardware wallets with final-word support

If your hardware wallet supports generating valid final words (for example, Jade), only one of its suggested words will also belong to the relevant group.

### Bruteforce last word
If your hardware or software wallet cannot calculate possible final words, test each word in the relevant group. Only one will have the correct checksum and create a valid BIP-39 mnemonic.
