# PRODIGY_CS_01

A Caesar cipher tool written in Python, built for Task 1 of the Prodigy InfoTech
Cyber Security internship.

You give it a message and a shift number. It moves every letter along the alphabet
by that amount to encrypt, and back the other way to decrypt.

## What it does

- Encrypts and decrypts text with the classic Caesar shift
- Runs from the command line or an interactive menu
- Leaves numbers, spaces and symbols untouched
- Handles any shift value, even negative or bigger than 26 (uses mod 26)

## Setup

No install needed, just Python 3.

## How to run

```bash
# interactive menu
python3 caesar.py

# direct
python3 caesar.py --encrypt --shift 3 --text "Hello World"
python3 caesar.py --decrypt --shift 3 --text "Khoor Zruog"
```

## Example output

```
$ python3 caesar.py --encrypt --shift 3 --text "Hello World"
Khoor Zruog

$ python3 caesar.py --decrypt --shift 3 --text "Khoor Zruog"
Hello World
```

## Files

- `caesar.py` — the tool. `caesar_encrypt` and `caesar_decrypt` do the work.
