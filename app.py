import itertools

def mutate(word):
    mutations = set()

    mutations.add(word)
    mutations.add(word.lower())
    mutations.add(word.upper())
    mutations.add(word.capitalize())

    leet_map = str.maketrans({
        "a": "@",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "$"
    })

    mutations.add(word.translate(leet_map))

    # suffix numbers
    for i in range(0, 10):
        mutations.add(f"{word}{i}")

    # symbols
    for s in ["!", "@", "#"]:
        mutations.add(f"{word}{s}")

    return mutations


def combine_words(words):
    combos = set()

    # single words
    for w in words:
        combos.add(w)

    # 2-word combinations
    for r in range(2, len(words) + 1):
        for combo in itertools.permutations(words, r):
            combos.add("".join(combo))
            combos.add("_".join(combo))
            combos.add("-".join(combo))
            combos.add(".".join(combo))

    return combos


def generate_wordlist(words, output="wordlist.txt"):
    wordlist = set()

    # step 1: combinations
    combos = combine_words(words)

    # step 2: mutations on combinations
    for c in combos:
        wordlist.update(mutate(c))

    # save
    with open(output, "w") as f:
        for item in sorted(wordlist):
            f.write(item + "\n")

    print(f"[+] Generated {len(wordlist)} passwords -> {output}")


if __name__ == "__main__":
    words = input("Enter words (space separated): ").split()
    generate_wordlist(words)