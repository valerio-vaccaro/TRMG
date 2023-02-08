import os

def load_words():
    d = os.path.join(os.path.dirname(__file__), f"english.txt")
    if os.path.exists(d) and os.path.isfile(d):
        with open(d, "r", encoding="utf-8") as f:
            wordlist = [w.strip() for w in f.readlines()]
        
    return wordlist
    
def generate_word(first, second, third):
    index = (first-1)*2**8 + (second-1)*2**4 + (third-1)
    return index

def generate_table(wordlist):
    print(f'|First|Second|Third|Index|Word|Index in binary|Group 12|Group 24|')
    print('|-----|------|-----|-----|----|---------------|--------|--------|')
    for first in range(1,9):
        for second in range(1,17):
            for third in range(1,17):
                index = generate_word(first, second, third)
                binary = format(index, "#013b")
                binary = '0'*(13-len(binary))+binary
                print(f'|{first}|{second}|{third}|{index}|{wordlist[index]}|{binary[2:]}|{binary[2:2+7]}|{binary[2:2+3]}|')
                           
def main():
    wordlist = load_words()
    generate_table(wordlist)

if __name__ == "__main__":
    main()
