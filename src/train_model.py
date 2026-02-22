import pandas as pd
import pickle
import random
from data_treatment import treat_data
from ngram_model import NGramModel

def train_and_save():
    random.seed(42)

    daily_words_list, _, _, _, _ = treat_data()

    model = NGramModel(n = 4)
    model.train_model(daily_words_list)

    with open("ngram_model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_and_save()