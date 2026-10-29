# word-frequency

A tiny word-frequency counter in one Python file — no dependencies, no server.

## What it does

Reads one or more plain-text files and prints the most frequent words,
one per line, as `count  word`. Matching is case-insensitive and
punctuation is stripped, so "Hello," and "hello" count as the same word.

## How to run

```bash
python wordfreq.py notes.txt
python wordfreq.py chapter1.txt chapter2.txt --top 10
python wordfreq.py draft.txt --min-length 4 --ignore-stopwords
```

Options:

- `--top N` — show only the top N words (default: 20)
- `--min-length N` — ignore words shorter than N letters (default: 1)
- `--ignore-stopwords` — skip common words like "the", "and", "of"

A missing file or a missing-file error exits with code 2 and an error message.

## Example output

Input file containing "The cat sat. The cat ran. A dog barked.":

```
$ python wordfreq.py sample.txt --top 3
3  the
2  cat
1  sat
```

## Requirements

Python 3.8 or newer. Standard library only.
