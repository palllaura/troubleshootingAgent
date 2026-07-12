import logging

import nltk
import spacy
from nltk.tokenize import word_tokenize
from transformers import pipeline

logger = logging.getLogger(__name__)

logger.info("Loading NLP models...")

# Load models once when the application starts
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")

logger.info("NLP models loaded successfully.")


def tokenize(text: str) -> list[str]:
    """Split text into tokens."""
    logger.debug("Tokenizing text.")
    return word_tokenize(text)


def get_pos_tags(tokens: list[str]) -> list[tuple]:
    """Assign part-of-speech tags to tokens."""
    logger.debug("Generating POS tags.")
    return nltk.pos_tag(tokens)


def extract_entities(text: str) -> list[dict]:
    """Extract named entities using spaCy."""
    logger.debug("Extracting named entities.")

    doc = nlp(text)

    return [
        {
            "text": entity.text,
            "label": entity.label_
        }
        for entity in doc.ents
    ]


def analyze_sentiment(text: str) -> list[dict]:
    """Analyze text sentiment."""
    logger.debug("Performing sentiment analysis.")
    return sentiment_analyzer(text)


def analyze_text(text: str) -> dict:
    """
    Analyze user input using several NLP techniques.
    """

    logger.info("Starting NLP analysis.")

    try:
        tokens = tokenize(text)
        pos_tags = get_pos_tags(tokens)
        entities = extract_entities(text)
        sentiment = analyze_sentiment(text)

        logger.info("NLP analysis completed successfully.")

        return {
            "tokens": tokens,
            "pos_tags": pos_tags,
            "entities": entities,
            "sentiment": sentiment
        }

    except Exception:
        logger.exception("Unexpected error during NLP analysis.")
        raise
