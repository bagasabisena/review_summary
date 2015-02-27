import nltk


class Sentence(object):

    def __init__(self, raw):
        self.raw = raw
        self.generate_tokens()
        self.generate_tags()
        self.generate_features()

    def generate_tokens(self):
        self.tokens = nltk.word_tokenize(self.raw.lower())

    def generate_tags(self):
        self.tags = nltk.pos_tag(self.tokens)

    def generate_features(self):
        grammar = "NP: {<JJ.*>*<NN.*>+}"
        cp = nltk.RegexpParser(grammar)
        chunk_tree = cp.parse(self.tags)
        self.features = []
        for node in chunk_tree:
            if isinstance(node, nltk.tree.Tree):
                if node.label() == "NP":
                    feature = []
                    for value in node:
                        feature.append(value[0])
                    self.features.append(" ".join(feature))


class Review(object):

    def __init__(self, raw):
        self.raw = raw
        self.generate_sentences()
        self.aggregate_features()

    def generate_sentences(self):
        dirty_sentences = nltk.sent_tokenize(self.raw)
        self.sentences = [Sentence(s) for s in dirty_sentences]

    def aggregate_features(self):
        self.features = []
        for s in self.sentences:
            self.features = self.features + s.features
        self.features = tuple(self.features)


class ReviewSet(object):

    def __init__(self, raw):
        self.raw = raw
        self.generate_reviews()

    def generate_reviews(self):
        self.reviews = [Review(s) for s in self.raw]

    def create_transaction_list(self):
        self.features = []
        for review in self.reviews:
            self.features.append(review.features)

