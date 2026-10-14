# my caesar cipher - prodigy task 1
# encrypts / decrypts text by shifting letters

import argparse

try:
    from brand import boot
except Exception:
    def boot(*a, **k):
        pass


def caesar_encrypt(text, shift):
    shift = shift % 26
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            out.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            out.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            out.append(ch)
    return ''.join(out)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def interactive():
    print("Caesar Cipher - Prodigy Task 1")
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("choice (1/2/3): ").strip()
        if choice == '3':
            print("bye!")
            break
        if choice not in ('1', '2'):
            print("enter 1, 2 or 3")
            continue
        msg = input("message: ")
        try:
            shift = int(input("shift: ").strip())
        except ValueError:
            print("shift must be a number")
            continue
        if choice == '1':
            print("Encrypted:", caesar_encrypt(msg, shift))
        else:
            print("Decrypted:", caesar_decrypt(msg, shift))


def main():
    p = argparse.ArgumentParser(description="caesar cipher encrypt/decrypt")
    g = p.add_mutually_exclusive_group()
    g.add_argument('--encrypt', action='store_true')
    g.add_argument('--decrypt', action='store_true')
    p.add_argument('--shift', type=int)
    p.add_argument('--text', type=str)
    a = p.parse_args()
    boot("Caesar Cipher", "CS-01", "classic shift cipher - encrypt / decrypt text")
    if a.encrypt or a.decrypt:
        if a.shift is None or a.text is None:
            p.error("need --shift and --text")
        if a.encrypt:
            print(caesar_encrypt(a.text, a.shift))
        else:
            print(caesar_decrypt(a.text, a.shift))
    else:
        interactive()


if __name__ == '__main__':
    main()
