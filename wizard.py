from itertools import permutations, product
import multiprocessing

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

def apply_transformations(word, suffix_range=100):
    length = len(word)
    transformations = {word}

    for i in range(1 << length):
        transformed = ''.join(word[idx].upper() if (i >> idx) & 1 else word[idx].lower() for idx in range(length))
        transformations.add(transformed)

    transformations |= {t + str(num) for t in transformations for num in range(suffix_range)}

    transformed_set = set()
    for t in transformations:
        transformed_set |= replace_with_symbols(t)
    
    return transformed_set

def generate_wordlist(words, min_length=6, max_length=12, suffix_range=100):
    wordlist = set()
    
    for r in range(1, len(words) + 1):
        for combo in permutations(words, r):
            combined = ''.join(combo)
            if min_length <= len(combined) <= max_length:
                wordlist |= apply_transformations(combined, suffix_range)
    
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

    try:
        min_length = int(input("Minimum length of words (default 6): ") or 6)
        max_length = int(input("Maximum length of words (default 12): ") or 12)
        suffix_range = int(input("Number of numerical suffixes (default 100): ") or 100)
    except ValueError:
        print("Invalid input, using default values.")
        min_length, max_length, suffix_range = 6, 12, 100

    if not words:
        print("No words provided. Exiting.")
        return

    print("\nGenerating wordlist...")

    with multiprocessing.Pool() as pool:
        chunk_size = max(1, len(words) // (pool._processes * 2))
        wordlist_chunks = pool.starmap(generate_wordlist, [(words, min_length, max_length, suffix_range)])
    
    wordlist = set().union(*wordlist_chunks)

    output_file = "custom_wordlist.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(wordlist))

    print(f"Wordlist generated and saved to {output_file} ({len(wordlist)} entries).")

if __name__ == "__main__":
    wordlist_generator()
