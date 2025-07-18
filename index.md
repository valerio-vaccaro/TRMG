# TRMG -True Random Mnemonic Generator

## Introduction
Creating a mnemonic phrase using dice is often preferred over relying on a random number generator (RNG) chip or software script for the following reasons:

- True Randomness: Physical dice provide true randomness because their outcomes are determined by physical processes (e.g., rolling motion, surface interaction) that are inherently unpredictable. When rolled properly, dice are not influenced by external factors like software bugs or hardware flaws. On the other hand Hardware RNGs or software-based generators often rely on pseudo-random number generation (PRNG), which uses algorithms that can be predictable if the seed or algorithm is compromised. Even true RNG chips can be tampered with or have manufacturing flaws, reducing trust in their randomness.

- Transparency and Verifiability: The process of rolling dice is transparent and verifiable by the user. You can physically see and confirm the outcome of each roll, ensuring no hidden manipulation. This makes it easy to audit the process yourself. RNG chips are black-box systems. You cannot easily verify the integrity of the chip or script. Software may have hidden backdoors, and hardware RNGs may have biases or vulnerabilities that are difficult to detect.

- No Dependency on Technology: Dice are low-tech, requiring no electricity, internet, or software updates. This reduces the attack surface, as there’s no risk of malware, hacking, or software vulnerabilities compromising the process. Specialied chips or scripts rely on electronic devices, which can be hacked, infected with malware, or subject to supply chain attacks. A compromised device could leak your mnemonic phrase or generate predictable outputs.

- Resistance to Side-Channel Attacks: Rolling dice is immune to digital side-channel attacks like electromagnetic emissions, timing attacks, or power analysis, which can compromise hardware or software RNGs. Sophisticated attackers can exploit side-channel attacks to extract information from hardware RNGs or software running on a device, potentially compromising the generated mnemonic.

- User Control and Reproducibility: You have full control over the process, and it’s reproducible with minimal tools (just dice and a word list). You can repeat the process anywhere, anytime, without relying on specific hardware or software. RNG chips or scripts require access to specific devices or software, which may not always be available or trustworthy.

- Simplicity and Trust: The simplicity of dice makes them trustworthy. They’re physical objects with no hidden mechanisms, and their randomness is based on well-understood physical principles. Chips are complex systems, usually closed source, that require trust in the manufacturer, developer, or supply chain. Any flaw, intentional or not, could compromise security.

## Generate mnemonic
First step is to generate 12 or 24 words using dices, this can be done using different dices or coins or cards.

### D8 dices, D6 dices or coins
[Guide D8, D6 or coin](https://github.com/valerio-vaccaro/TRMG/blob/main/d6.md)

### D8+D16+D16 dices
[Guide D8/D16/D16](https://github.com/valerio-vaccaro/TRMG/blob/main/d8ff.md)

### Poker cards
[Cards](https://github.com/valerio-vaccaro/TRMG/blob/main/poker.md)

This process is entirely manual, auditable, and free from digital vulnerabilities.

## Fix last word
Last word is partially based on checksum of previouse words so need a fix in order to follow correctly the Bip39 standard, the groups of possible ending words are present in the table as Group 12 for 12 words mnemonics or Group 24 for the mnemonics with 24 words.

Based on your last word obtained with dice you can identify the group of possible ending words.

Groups are based on partial entropy, if you are using D8/D16/D16 dices for a 12 words long mnemonic you can consider only the First and Second dice result, as you can see considering First and Second dice only you will identify 16 possible words (you can also check binary label on the column Group 12). You can try to import this mnemonics changing the last word if the software or hardware used give you an error message. In the case of 24 words long mnemonic you need to check only First dice result and check in a 128 words group (identified by the same label on Group 24 column).

### Hardware wallet with last word functionalities
You can generate all valid ending words if you hardware wallet allow you to do (like Jade), only one word will be present in the intesection between Jade calculate words and words with the same group.

### Bruteforce last word
If your hardware/software wallet don't allow calculation of last possible words you can simple bruteforce testing all the words with the same group, only one will have the right checksum and will create a valid Bip39 mnemonic.