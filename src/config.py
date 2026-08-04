"""Global constants for the Kafka SpaCy vs LLM agreement project."""

RANDOM_SEED = 42

# Approximate sample size per language (proposal default)
N_SENTENCES_PER_LANGUAGE = 300

SPACY_MODEL_DE = "de_core_news_md"
SPACY_MODEL_EN = "en_core_web_md"

# Universal POS tagset (UD); LLM outputs must map into this set
UPOS_TAGS = frozenset(
    {
        "ADJ",
        "ADP",
        "ADV",
        "AUX",
        "CCONJ",
        "DET",
        "INTJ",
        "NOUN",
        "NUM",
        "PART",
        "PRON",
        "PROPN",
        "PUNCT",
        "SCONJ",
        "SYM",
        "VERB",
        "X",
    }
)

RAW_DE = "data/raw/kafka_1925_der-prozess.txt"
RAW_EN = "data/raw/kafka_1925_the-trial.txt"
