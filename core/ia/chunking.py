# core/ia/chunking.py

import re
from typing import List

def split_sentences(text: str) -> List[str]:
    """
    Divide o texto em sentenças preservando pontuação.
    """
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 20]


def chunk_text(text, max_chars=800):
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + max_chars])
        start += max_chars

    return chunks

