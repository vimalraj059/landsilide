import random


TAMIL_PROVERBS = [
    "அறம் செய விரும்பு",
    "ஆற்றின் கரையில் ஆமை",
    "அறிவிலான் நடுக்கம்",
    "அறிவுள்ளான் வாளால் வெல்லான்",
]

TAMIL_QUOTES = [
    "வாழ்க தமிழ்!",
    "நன்றி, வணக்கம்!",
]


def random_proverb() -> str:
    return random.choice(TAMIL_PROVERBS)


def random_quote() -> str:
    return random.choice(TAMIL_QUOTES)

