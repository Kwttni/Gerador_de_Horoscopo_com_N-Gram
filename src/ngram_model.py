import re
import random
from collections import defaultdict, Counter

def preprocess_and_tokenize(corpus):
    corpus = corpus.lower()
    tokens = re.findall(r"<[^>]+>|\d+/\d+|\d+|\w+", corpus)
    return tokens

def add_padding(tokens, n):
    padding = ["<s>"] * (n - 1)
    return padding + tokens + ["</s>"]

class NGramModel:
    def __init__(self, n): 
        self.n = n
        self.counts = defaultdict(Counter)
        self.context_totals = Counter()

    def train_model(self, corpus_list):
        for corpus in corpus_list:
            tokens = preprocess_and_tokenize(corpus)
            tokens = add_padding(tokens, self.n)

            for i in range(len(tokens) - self.n + 1):
                window = tokens[i : i + self.n]
                history = tuple(window[:-1])
                word = window[-1]

                self.counts[history][word] += 1
                self.context_totals[history] += 1

    def get_probality(self, word, history): 
        history = tuple(history)

        numerator = self.counts[history][word]
        denominator = self.context_totals[history]

        if denominator == 0:
            return 0 
        
        return numerator / denominator
    
    def generate_text(self, seed_history, length):
        result = list(seed_history)
        current_history = tuple(seed_history)

        for _ in range(length):
            candidates = self.counts[current_history]

            if not candidates:
                break

            words = list(candidates.keys())
            weights = list(candidates.values())

            next_word = random.choices(words, weights=weights)[0]

            result.append(next_word)
            current_history = tuple(result[-(self.n - 1):])

            if next_word == "</s>":
                break

        return " ".join(result)
