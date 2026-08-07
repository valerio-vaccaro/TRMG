from pathlib import Path


WORDLIST_PATH = Path(__file__).resolve().parent / "english.txt"


def load_words():
    with WORDLIST_PATH.open(encoding="utf-8") as wordlist_file:
        return [word.strip() for word in wordlist_file]


def generate_word(first_d8, second_d8, third_d8, first_coin, second_coin):
    return (
        (first_d8 - 1) * 256
        + (second_d8 - 1) * 32
        + (third_d8 - 1) * 4
        + first_coin * 2
        + second_coin
    )


def generate_table(wordlist):
    print("|First D8|Second D8|Third D8|First coin|Second coin|Index|Word|Index in binary|Group 12|Group 24|")
    print("|--------|---------|--------|----------|-----------|-----|----|---------------|--------|--------|")
    for first_d8 in range(1, 9):
        for second_d8 in range(1, 9):
            for third_d8 in range(1, 9):
                for first_coin in range(2):
                    for second_coin in range(2):
                        index = generate_word(
                            first_d8,
                            second_d8,
                            third_d8,
                            first_coin,
                            second_coin,
                        )
                        binary = f"{index:011b}"
                        first_coin_result = "T" if first_coin else "H"
                        second_coin_result = "T" if second_coin else "H"
                        print(
                            f"|{first_d8}|{second_d8}|{third_d8}|{first_coin_result}|{second_coin_result}|"
                            f"{index}|{wordlist[index]}|{binary}|{binary[:7]}|{binary[:3]}|"
                        )


def main():
    generate_table(load_words())


if __name__ == "__main__":
    main()
