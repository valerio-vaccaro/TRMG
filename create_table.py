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

def generate_word_bin(d11, d10, d9, d8, d7, d6, d5, d4, d3, d2, d1):
    index = d11*1024 + d10*512 + d9*256 + d8*128 + d7*64 + d6*32 + d5*16 + d4*8 + d3*4 + d2*2 + d1
    return index
    
def generate_table(wordlist):
    print('|First|Second|Third|Index|Word|Index in binary|Group 12|Group 24|')
    print('|-----|------|-----|-----|----|---------------|--------|--------|')
    for first in range(1,9):
        for second in range(1,17):
            for third in range(1,17):
                index = generate_word(first, second, third)
                binary = format(index, "#013b")
                binary = '0'*(13-len(binary))+binary
                print(f'|{first}|{second}|{third}|{index}|{wordlist[index]}|{binary[2:]}|{binary[2:2+7]}|{binary[2:2+3]}|')

def generate_table_bin(wordlist):
    print('|1024|512|256|128|64|32|16|8|4|2|1|Index|Word|Group 12|Group 24|')
    print('|----|---|---|---|--|--|--|-|-|-|-|-----|----|--------|--------|')
    for d11 in range(0,2):
        for d10 in range(0,2):
            for d9 in range(0,2):
                for d8 in range(0,2):
                    for d7 in range(0,2):
                        for d6 in range(0,2):
                            for d5 in range(0,2):
                                for d4 in range(0,2):
                                    for d3 in range(0,2):
                                        for d2 in range(0,2):
                                            for d1 in range(0,2):
                                                index = generate_word_bin(d11, d10, d9, d8, d7, d6, d5, d4, d3, d2, d1)
                                                binary = format(index, "#013b")
                                                binary = '0'*(13-len(binary))+binary
                                                print(f'|{d11}|{d10}|{d9}|{d8}|{d7}|{d6}|{d5}|{d4}|{d3}|{d2}|{d1}|{index}|{wordlist[index]}|{binary[2:]}|{binary[2:2+7]}|{binary[2:2+3]}|')

def main():
    wordlist = load_words()
    generate_table(wordlist)
    print('\n\n')
    generate_table_bin(wordlist)

if __name__ == "__main__":
    main()
