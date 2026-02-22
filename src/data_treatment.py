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
    
    horoscope_df = df.dropna(subset=['description', 'mood', 'color', 'lucky_number', 'sign'])

    horoscope_df['sign'] = horoscope_df['sign'].astype(str).str.lower().str.strip()
    horoscope_df['mood'] = horoscope_df['mood'].astype(str)
    horoscope_df['color'] = horoscope_df['color'].astype(str)
    horoscope_df['description'] = horoscope_df['description'].astype(str)

    # Lista de textos usados para treinar o modelo N-gram
    daily_words = horoscope_df['description'].tolist()
    sign_list = horoscope_df['sign'].unique().tolist()
    mood_list = horoscope_df['mood'].unique().tolist()
    color_list = horoscope_df['color'].unique().tolist()
    lucky_number_list = horoscope_df['lucky_number'].unique().tolist()

    return daily_words, sorted(sign_list), mood_list, color_list, lucky_number_list

if __name__ == "__main__":
    treat_data()