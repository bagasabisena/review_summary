import nltk
import models


def summarize(raw_text):
    review_set = models.ReviewSet(raw_text.lower())

