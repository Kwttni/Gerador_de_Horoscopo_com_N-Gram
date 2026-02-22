import pickle
import random
import streamlit as st
from deep_translator import GoogleTranslator
from data_treatment import treat_data

# ---------- Config da página ----------
st.set_page_config(page_title="Horóscopo N-Gram", page_icon="🌌", layout="centered")

# ---------- Cache: carrega modelo 1x ----------
@st.cache_resource
def load_model():
    with open("ngram_model.pkl", "rb") as f:
        return pickle.load(f)

# ---------- Cache: carrega listas e traduções 1x ----------
@st.cache_resource
def load_data_and_translations():
    _, sign_list, mood_list, color_list, lucky_number_list = treat_data()
    translator = GoogleTranslator(source="en", target="pt")

    sign_list_br = [translator.translate(sign) for sign in sign_list]

    return sign_list, sign_list_br, mood_list, color_list, lucky_number_list

model = load_model()
sign_list_en, sign_list_br, mood_list, color_list, lucky_number_list = load_data_and_translations()

translator = GoogleTranslator(source="en", target="pt")


def generate_horoscope(selected_sign_pt: str):
    # OBS: seu modelo atual não usa o signo para gerar (é só estético na UI).
    # Se quiser que influencie, a gente muda depois.

    automatic_seeds = ["<s>", "<s>", "<s>"]

    daily_words = model.generate_text(automatic_seeds, 120)

    clean_daily_words = daily_words.replace("<s>", "").replace("</s>", "").strip()

    br_daily_words = translator.translate(clean_daily_words)

    todays_mood = random.choice(mood_list)
    todays_color = random.choice(color_list)
    todays_number = random.choice(lucky_number_list)

    todays_mood_br = translator.translate(todays_mood)
    todays_color_br = translator.translate(todays_color)

    return br_daily_words, todays_color_br, todays_mood_br, str(todays_number)


# ---------- UI ----------
st.title("🌌 Horóscopo")
st.write("Selecione seu signo para gerar as previsões do dia baseadas em modelos estatísticos de N-grams.")

selected_sign = st.selectbox("Selecione seu signo:", options=sign_list_br, index=0)

if st.button("Gerar previsão para hoje", type="primary"):
    texto, cor, humor, numero = generate_horoscope(selected_sign)

    st.subheader("Previsão do Dia")
    st.text_area("", value=texto, height=160)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Cor da Sorte**")
        st.write(cor)
    with c2:
        st.markdown("**Humor**")
        st.write(humor)
    with c3:
        st.markdown("**Número da sorte**")
        st.write(numero)