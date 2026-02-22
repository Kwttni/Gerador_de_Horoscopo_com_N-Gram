import re
import random
from collections import defaultdict, Counter

def preprocess_and_tokenize(corpus):
    """
    Responsável por normalizar e tokenizar o texto.

    1. Converte todo o texto para minúsculas para evitar duplicação
       de palavras como "Today" e "today".
    2. Usa regex para separar o texto em tokens.

    Retorna uma lista de tokens.
    """
    corpus = corpus.lower()
    tokens = re.findall(r"<[^>]+>|\d+/\d+|\d+|\w+", corpus)
    return tokens

def add_padding(tokens, n):
    """
    Adiciona tokens especiais no início e fim da sequência.

    Para um modelo n-gram, precisamos de n-1 tokens iniciais
    para formar o primeiro histórico.

    """

    padding = ["<s>"] * (n - 1)
    return padding + tokens + ["</s>"]

class NGramModel:
    def __init__(self, n): 
        """
        Inicializa o modelo N-gram.

        n = tamanho do n-gram.
        Exemplo:
        n = 4 -> o modelo olha para as 3 palavras anteriores.

        Estruturas usadas:
        counts:
        dicionário onde:
        chave   -> histórico de palavras
        valor   -> contador de próximas palavras

        context_totals:
        número total de ocorrências de cada histórico.
        """
        self.n = n
        self.counts = defaultdict(Counter)
        self.context_totals = Counter()

    def train_model(self, corpus_list):
        """
        Treina o modelo utilizando uma lista de textos.

        Para cada texto:
        1. Tokeniza
        2. Adiciona padding
        3. Percorre janelas de tamanho n
        """
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
        """
        Calcula a probabilidade condicional
        """
        history = tuple(history)

        numerator = self.counts[history][word]
        denominator = self.context_totals[history]

        if denominator == 0:
            return 0 
        
        return numerator / denominator
    
    def generate_text(self, seed_history, length):
        """
        Gera um novo texto baseado no modelo treinado.

        seed_history:
        histórico inicial usado para começar a geração.
        Exemplo:
        ["<s>", "<s>", "<s>"]

        length:
        número máximo de tokens a gerar.
        """
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
