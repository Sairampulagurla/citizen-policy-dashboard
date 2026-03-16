import re
from collections import Counter
import tiktoken


def count_tokens(text):

    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    return len(tokens)


def split_blocks(text, block_size=5000):

    words = text.split()
    blocks = []

    for i in range(0, len(words), block_size):
        blocks.append(" ".join(words[i:i+block_size]))

    return blocks


def compress_block(text):

    sentences = re.split(r'(?<=[.!?]) +', text)

    words = re.findall(r'\w+', text.lower())
    word_freq = Counter(words)

    scores = {}

    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            scores[sentence] = scores.get(sentence, 0) + word_freq[word]

    ranked = sorted(scores, key=scores.get, reverse=True)

    return " ".join(ranked[:5])


def compress_text(pages):

    full_text = " ".join(pages)

    blocks = split_blocks(full_text)

    compressed_parts = []

    for block in blocks:
        compressed_parts.append(compress_block(block))

    compressed_text = " ".join(compressed_parts)

    original_tokens = count_tokens(full_text)
    compressed_tokens = count_tokens(compressed_text)

    return compressed_text, original_tokens, compressed_tokens