import spacy
import nltk

from nltk.tokenize import word_tokenize
from transformers import pipeline

# Load models once when the application starts
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")


def analyze_text(text: str) -> dict:
    """
    Analyze user input using several NLP techniques.

    Returns:
        dict containing tokens, POS tags, named entities and sentiment.
    """

    # Tokenization
    tokens = word_tokenize(text)

    # Part-of-speech tagging
    pos_tags = nltk.pos_tag(tokens)

    # Named Entity Recognition
    doc = nlp(text)

    entities = []

    for entity in doc.ents:
        entities.append({
            "text": entity.text,
            "label": entity.label_
        })

    # Sentiment analysis
    sentiment = sentiment_analyzer(text)

    return {
        "tokens": tokens,
        "pos_tags": pos_tags,
        "entities": entities,
        "sentiment": sentiment
    }
