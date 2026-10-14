# My Prodigy Task 1 - Caesar Cipher

Caesar cipher in python. You give a message and a shift number, it shifts the letters.

Nothing fancy, just ord/chr and mod 26. Numbers, spaces and symbols stay the same.

## how to run

Interactive:
```
python3 caesar.py
```

Direct:
```
python3 caesar.py --encrypt --shift 3 --text "Hello World"
# Khoor Zruog

python3 caesar.py --decrypt --shift 3 --text "Khoor Zruog"
# Hello World
```

Shift can be negative or bigger than 26, it still works (uses % 26).

## files

- `caesar.py` - everything is here. `caesar_encrypt` and `caesar_decrypt` are the two functions.

Needs only python3, no pip install.
