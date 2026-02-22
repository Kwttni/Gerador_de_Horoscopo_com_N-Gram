"""
train_model.py

Responsável por treinar o modelo de linguagem N-Gram a partir do dataset
de horóscopos e salvar o modelo treinado em um arquivo .pkl para uso
posterior na aplicação.
"""

import pandas as pd
import pickle
import random
from data_treatment import treat_data
from ngram_model import NGramModel

def train_and_save():
    random.seed(42)

    # Carrega as descrições do dataset
    daily_words_list, _, _, _, _ = treat_data()

    # Cria o modelo N-gram (4-gram)
    model = NGramModel(n = 4)

    # Treina o modelo com os textos
    model.train_model(daily_words_list)

    # Salva o modelo treinado
    with open("ngram_model.pkl", "wb") as f:
        pickle.dump(model, f)

# Executa o treinamento ao rodar o arquivo
if __name__ == "__main__":
    train_and_save()