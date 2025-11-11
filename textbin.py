#!/usr/bin/env python3
import sys

def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_text(bstr):
    try:
        chars = bstr.split()
        return ''.join(chr(int(c, 2)) for c in chars)
    except ValueError:
        return "[Error] Input biner tidak valid!"

def detect_and_convert(arg):
    # jika semua karakter 0/1/space → biner
    if all(c in '01 ' for c in arg):
        # konversi biner ke teks
        return binary_to_text(arg)
    else:
        # konversi teks ke biner
        return text_to_binary(arg)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan: python textbin.py \"teks atau biner\"")
        sys.exit(1)

    input_arg = sys.argv[1]
    result = detect_and_convert(input_arg)
    print(result)
