#!/usr/bin/env python3
"""Word frequency counter for plain-text files.

Usage:
    python wordfreq.py notes.txt [--top 20] [--min-length 3] [--ignore-stopwords]

Reads one or more text files, counts words (case-insensitive, punctuation
stripped), and prints the most frequent words, one per line, as
"count  word". Exit code 2 on a usage error (missing file, bad number).
No dependencies, standard library only.
"""
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if",
    "in", "into", "is", "it", "no", "not", "of", "on", "or", "such",
    "that", "the", "their", "then", "there", "these", "they", "this",
    "to", "was", "will", "with",
}
WORD_RE = re.compile(r"[a-z0-9']+")


def count_words(paths, min_length, ignore_stopwords):
    counts = Counter()
    for path in paths:
        text = Path(path).read_text(encoding="utf-8", errors="replace").lower()
        for word in WORD_RE.findall(text):
            word = word.strip("'")
            if len(word) < min_length:
                continue
            if ignore_stopwords and word in STOPWORDS:
                continue
            counts[word] += 1
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description="Count word frequencies in text files.")
    parser.add_argument("files", nargs="+", help="text file(s) to analyse")
    parser.add_argument("--top", type=int, default=20, help="how many words to show (default: 20)")
    parser.add_argument("--min-length", type=int, default=1, help="ignore words shorter than this")
    parser.add_argument("--ignore-stopwords", action="store_true", help="skip common stopwords")
    args = parser.parse_args(argv)

    if args.top < 1 or args.min_length < 1:
        parser.error("--top and --min-length must be at least 1")

    for path in args.files:
        if not Path(path).is_file():
            print(f"error: file not found: {path}", file=sys.stderr)
            return 2

    counts = count_words(args.files, args.min_length, args.ignore_stopwords)
    for word, count in counts.most_common(args.top):
        print(f"{count}  {word}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
