import pandas as pd

def treat_data():
    df = pd.read_csv("data\horoscope.csv")
    
    horoscope_df = df.dropna(subset=['description', 'mood', 'color', 'lucky_number', 'sign']).copy()

    daily_words = horoscope_df['description'].tolist()

    sign_list = df['sign'].unique().tolist()
    mood_list = df['mood'].unique().tolist()
    color_list = df['color'].unique().tolist()
    lucky_number_list = df['lucky_number'].unique().tolist()

    return daily_words, sorted(sign_list), mood_list, color_list, lucky_number_list

if __name__ == "__main__":
    treat_data()