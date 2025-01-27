from itertools import permutations, product

def replace_with_symbols(word):
    replacements = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        'l': ['1']
    }
    results = set([word])

    for i, char in enumerate(word):
        if char.lower() in replacements:
            for symbol in replacements[char.lower()]:
                for w in list(results):
                    results.add(w[:i] + symbol + w[i+1:])

    return results

def apply_transformations(word):
    transformations = set([word])

    for i in range(1 << len(word)):
        transformed = "".join(
            char.upper() if (i >> idx) & 1 else char.lower()
            for idx, char in enumerate(word)
        )
        transformations.add(transformed)

    for suffix in range(0, 100):
        for t in list(transformations):
            transformations.add(t + str(suffix))

    for t in list(transformations):
        transformations.update(replace_with_symbols(t))

    return transformations

def wordlist_generator():
    print("Custom Wordlist Generator")
    print("Press Enter to skip any field you don't have.")

    firstname = input("First name: ").strip()
    lastname = input("Last name: ").strip()
    nickname = input("Nickname: ").strip()
    birthdate = input("Birthdate (e.g., YYYY or DDMMYYYY): ").strip()
    custom_words = input("Custom words (comma-separated): ").strip()

    words = []
    if firstname:
        words.append(firstname)
    if lastname:
        words.append(lastname)
    if nickname:
        words.append(nickname)
    if birthdate:
        words.append(birthdate)
    if custom_words:
        words.extend(custom_words.split(","))

    min_length = int(input("Minimum length of words (default 6): ") or 6)
    max_length = int(input("Maximum length of words (default 12): ") or 12)

    print("\nGenerating wordlist...")

    wordlist = set()
    for r in range(1, len(words) + 1):
        for combo in permutations(words, r):
            combined = "".join(combo)
            if min_length <= len(combined) <= max_length:
                wordlist.update(apply_transformations(combined))

    output_file = "custom_wordlist.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(wordlist))

    print(f"Wordlist generated and saved to {output_file}!")

if __name__ == "__main__":
    wordlist_generator()
