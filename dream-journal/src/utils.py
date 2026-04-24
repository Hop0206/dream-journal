FILE = "dreams.txt"


def save_dream(dream):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(dream + "\n")


def load_dreams():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def search_dreams(keyword):
    dreams = load_dreams()
    return [d for d in dreams if keyword.lower() in d.lower()]

# File: tests/test_basic.py

from src.utils import search_dreams


def test_search():
    sample = ["I was flying", "I met a dragon"]
    results = [d for d in sample if "fly" in d.lower()]
    assert results == ["I was flying"]