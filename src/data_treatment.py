import pandas as pd

"""
data_treatment.py

Responsável por:
1. Carregar o dataset de horóscopo
2. Remover dados incompletos
3. Preparar listas usadas pelo modelo N-gram e pela interface
"""

def treat_data():
    """
    Carrega o dataset de horóscopo, remove registros incompletos
    e retorna os dados necessários para o treinamento e interface.
    """

    df = pd.read_csv("data/horoscope.csv")
    
    horoscope_df = df.dropna(subset=['description', 'mood', 'color', 'lucky_number', 'sign']).copy()

    # Lista de textos usados para treinar o modelo N-gram
    daily_words = horoscope_df['description'].tolist()

    sign_list = horoscope_df['sign'].unique().tolist()
    mood_list = horoscope_df['mood'].unique().tolist()
    color_list = horoscope_df['color'].unique().tolist()
    lucky_number_list = horoscope_df['lucky_number'].unique().tolist()

    return daily_words, sorted(sign_list), mood_list, color_list, lucky_number_list

if __name__ == "__main__":
    treat_data()