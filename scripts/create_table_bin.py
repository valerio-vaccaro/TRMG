from pathlib import Path


WORDLIST_PATH = Path(__file__).resolve().parent / "english.txt"


def load_words():
    with WORDLIST_PATH.open(encoding="utf-8") as wordlist_file:
        return [word.strip() for word in wordlist_file]


def generate_word(d11, d10, d9, d8, d7, d6, d5, d4, d3, d2, d1):
    return (
        d11 * 1024
        + d10 * 512
        + d9 * 256
        + d8 * 128
        + d7 * 64
        + d6 * 32
        + d5 * 16
        + d4 * 8
        + d3 * 4
        + d2 * 2
        + d1
    )


def generate_table(wordlist):
    print("|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|Index in binary|Group 12|Group 24|")
    print("|----|---|---|---|--|--|--|-|-|-|-|-----|----|---------------|--------|--------|")
    for index in range(2048):
        bits = tuple(int(bit) for bit in f"{index:011b}")
        binary = f"{index:011b}"
        print(
            f"|{'|'.join(map(str, bits))}|{index}|{wordlist[index]}|{binary}|"
            f"{binary[:7]}|{binary[:3]}|"
        )


def main():
    generate_table(load_words())


if __name__ == "__main__":
    main()
