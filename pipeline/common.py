"""Shared helpers: one definition of how a game concept becomes the text that gets embedded.

Both real Steam games (02_clean.py) and generated ideas (06_server.py) go through compose_doc,
so a generated idea is never closer to or farther from real games just because it was formatted differently.
"""

# Tags that describe how a game is sold or received rather than what it is.
META_TAGS = {
    "Indie", "Early Access", "Free to Play", "Great Soundtrack", "Masterpiece", "Classic", "Cult Classic",
    "Remake", "Sequel", "Addictive", "Beautiful", "Funny", "Short", "Replay Value", "Singleplayer",
    "Multiplayer", "Controller", "Software", "Utilities", "Game Development", "Design & Illustration",
    "Animation & Modeling", "Benchmark", "Steam Machine", "Kickstarter", "Crowdfunded", "Moddable",
    "Remaster", "Episodic", "Massively Multiplayer", "Feature Film", "Documentary", "Movie", "Free to Own",
    "Well-Written", "Great Story", "Inventory Management", "Epic", "Hand-drawn",
}
MAX_CONCEPT_TAGS = 12
LONG_DESC_WORDS = 120


def first_words(s: str, n: int) -> str:
    w = s.split()
    return " ".join(w[:n]) + (" …" if len(w) > n else "")


def concept_tags_of(tags_by_weight):
    return [t for t in tags_by_weight if t not in META_TAGS][:MAX_CONCEPT_TAGS]


def compose_doc(concept_tags, short: str, full_text: str) -> str:
    """'<tags>. <short description> <first 120 words of long description>'"""
    full_flat = " ".join(full_text.split("\n"))
    if short and full_flat.startswith(short[:60]):
        full_flat = full_flat[len(short):].strip()
    parts = []
    if concept_tags:
        parts.append(", ".join(concept_tags) + ".")
    if short:
        parts.append(short)
    if full_flat:
        parts.append(first_words(full_flat, LONG_DESC_WORDS))
    return " ".join(parts)
