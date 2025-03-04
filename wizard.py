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
    
    word_variants = [[char] if char.lower() not in replacements else [char] + replacements[char.lower()] for char in word]
    return {''.join(variant) for variant in product(*word_variants)}

def apply_transformations(word, suffix_range=10):
    length = len(word)
    transformations = {word}

    for i in range(1 << min(length, 5)):
        transformed = ''.join(word[idx].upper() if (i >> idx) & 1 else word[idx].lower() for idx in range(length))
        transformations.add(transformed)

    transformations |= {t + str(num) for t in transformations for num in range(min(suffix_range, 10))}

    transformed_set = set()
    for t in transformations:
        transformed_set |= replace_with_symbols(t)
    
    return transformed_set

def generate_wordlist(words, min_length, max_length, suffix_range, word_limit):
    wordlist = set()
    count = 0

    for r in range(1, len(words) + 1):
        for combo in permutations(words, r):
            combined = ''.join(combo)
            if min_length <= len(combined) <= max_length:
                transformed_words = apply_transformations(combined, suffix_range)
                for word in transformed_words:
                    print(word)
                    wordlist.add(word)
                    count += 1
                    if count >= word_limit:
                        return wordlist
    return wordlist

def wordlist_generator():
    print("Custom Wordlist Generator")
    print("Press Enter to skip any field you don't have.")

    firstname = input("First name: ").strip()
    lastname = input("Last name: ").strip()
    nickname = input("Nickname: ").strip()
    birthdate = input("Birthdate (e.g., YYYY or DDMMYYYY): ").strip()
    custom_words = input("Custom words (comma-separated): ").strip()
    
    words = [w for w in [firstname, lastname, nickname, birthdate] if w]
    if custom_words:
        words.extend(custom_words.split(","))

    if not words:
        print("No words provided. Exiting.")
        return

    filename = input("Enter output filename (default: custom_wordlist.txt): ").strip() or "custom_wordlist.txt"

    try:
        min_length = int(input("Minimum length of words (default 6): ") or 6)
        max_length = int(input("Maximum length of words (default 12): ") or 12)
        suffix_range = int(input("Number of numerical suffixes (default 10): ") or 10)
        word_limit = int(input("How many words to generate (default 1000): ") or 1000)
    except ValueError:
        print("Invalid input, using default values.")
        min_length, max_length, suffix_range, word_limit = 6, 12, 10, 1000

    print("\nGenerating wordlist...\n")

    wordlist = generate_wordlist(words, min_length, max_length, suffix_range, word_limit)

    with open(filename, "w") as f:
        f.write("\n".join(wordlist))

    print(f"\nWordlist saved to {filename} ({len(wordlist)} entries).")

if __name__ == "__main__":
    wordlist_generator()
