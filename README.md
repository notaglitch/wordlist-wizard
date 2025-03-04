# Custom Wordlist Generator

## Overview
The **Custom Wordlist Generator** is a Python script that generates highly customized wordlists for password cracking or security testing. It takes user input such as names, birthdates, and custom words, then applies various transformations (case variations, leetspeak substitutions, and numerical suffixes) to create a diverse wordlist.

## Features
- Generates wordlists based on personal information (e.g., first name, last name, nickname, birthdate, etc.).
- Applies **case variations** (uppercase/lowercase transformations).
- Supports **leetspeak substitutions** (e.g., `a -> @, 4`, `e -> 3`, `i -> 1, !`, etc.).
- Appends **numerical suffixes** (0-99) for enhanced wordlist diversity.
- Saves the final wordlist to a `.txt` file.

## Prerequisites
- Python 3.x

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/notaglitch/wordlist-wizard.git
   ```
2. Navigate to the project directory:

## Usage
Run the script using:
```sh
python wizard.py
```
Follow the on-screen prompts to enter details like:
- First name
- Last name
- Nickname
- Birthdate (e.g., `YYYY` or `DDMMYYYY`)
- Custom words (comma-separated)
- Minimum and maximum word lengths

Once all inputs are provided, the script will generate a wordlist and save it as:
```
custom_wordlist.txt
```

## Example
### Input:
```
First name: John
Last name: Doe
Nickname: JD
Birthdate: 1990
Custom words: hacker,password
Minimum length: 6
Maximum length: 12
```
### Output (Sample Entries):
```
johnDoe
JoHnDoE
j0hnD03
john1990
JD1990
H@ck3r
p@ssw0rd99
```
