from pathlib import Path


WORDLIST_PATH = Path(__file__).resolve().parent / "english.txt"


def load_words():
    with WORDLIST_PATH.open(encoding="utf-8") as wordlist_file:
        return [word.strip() for word in wordlist_file]


def generate_word(d8, first_d16, second_d16):
    return (d8 - 1) * 256 + (first_d16 - 1) * 16 + (second_d16 - 1)


def generate_table(wordlist):
    print("|D8|First D16|Second D16|Index|Word|Index in binary|Group 12|Group 24|")
    print("|--|---------|----------|-----|----|---------------|--------|--------|")
    for d8 in range(1, 9):
        for first_d16 in range(1, 17):
            for second_d16 in range(1, 17):
                index = generate_word(d8, first_d16, second_d16)
                binary = f"{index:011b}"
                print(
                    f"|{d8}|{first_d16}|{second_d16}|{index}|{wordlist[index]}|"
                    f"{binary}|{binary[:7]}|{binary[:3]}|"
                )


def main():
    generate_table(load_words())


if __name__ == "__main__":
    main()
