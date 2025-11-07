#!/usr/bin/env python3
"""
textbin.py - konversi teks <-> biner (UTF-8)

Usage:
  python3 textbin.py encode "Halo dunia"
  python3 textbin.py encode "Halo" --nosep
  python3 textbin.py decode "01001000 01100001 01101100 01101111"
  echo "Halo" | python3 textbin.py encode
"""
import sys
import argparse
import textwrap
from typing import List


def text_to_binary(s: str, sep: str = " ") -> str:
    """
    Convert a string to binary (UTF-8), bytes separated by sep.
    Each byte as 8 bits.
    """
    b = s.encode("utf-8")
    bits = [format(byte, "08b") for byte in b]
    return sep.join(bits)


def binary_to_text(bstr: str) -> str:
    """
    Convert a binary string to text (UTF-8).
    Accepts bytes separated by whitespace OR a contiguous bitstring length multiple of 8.
    Raises ValueError on invalid input or decoding error.
    """
    raw = bstr.strip()
    if raw == "":
        return ""

    if any(ch.isspace() for ch in raw):
        parts = raw.split()
    else:
        if len(raw) % 8 != 0:
            raise ValueError("Binary string length must be multiple of 8 when no separators provided.")
        parts = [raw[i:i+8] for i in range(0, len(raw), 8)]

    bytes_list = []
    for p in parts:
        if len(p) != 8:
            raise ValueError(f"Each byte must be exactly 8 bits (got length {len(p)} for '{p}').")
        if any(c not in "01" for c in p):
            raise ValueError(f"Binary input contains invalid characters: '{p}'")
        bytes_list.append(int(p, 2))

    try:
        data = bytes(bytes_list)
        return data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise ValueError(f"Decoded bytes are not valid UTF-8: {e}")


def main():
    parser = argparse.ArgumentParser(
        prog="textbin",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Konversi teks <-> biner (UTF-8).",
        epilog=textwrap.dedent("""
        Contoh:
          python3 textbin.py encode "Halo dunia"
          python3 textbin.py encode "Halo" --nosep
          python3 textbin.py decode "01001000 01100001 01101100 01101111"
          echo "Halo" | python3 textbin.py encode
        """)
    )
    sub = parser.add_subparsers(dest="cmd", required=True, help="Perintah")

    p_enc = sub.add_parser("encode", help="Ubah teks jadi biner (UTF-8).")
    p_enc.add_argument("text", nargs="?", help="Teks yang akan dikonversi. Jika kosong, baca dari stdin.")
    p_enc.add_argument("--nosep", action="store_true", help="Jangan pakai pemisah di antar byte (concat).")

    p_dec = sub.add_parser("decode", help="Ubah biner jadi teks (UTF-8).")
    p_dec.add_argument("binary", nargs="?", help="String biner (pisah spasi atau concat). Jika kosong, baca dari stdin.")

    args = parser.parse_args()

    if args.cmd == "encode":
        if args.text is None:
            text = sys.stdin.read() or ""
        else:
            text = args.text
        sep = "" if args.nosep else " "
        out = text_to_binary(text, sep=sep)
        print(out)

    elif args.cmd == "decode":
        if args.binary is None:
            bin_input = sys.stdin.read() or ""
        else:
            bin_input = args.binary
        try:
            out = binary_to_text(bin_input)
            print(out)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(2)


if __name__ == "__main__":
    main()
