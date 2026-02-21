import pickle
import gradio as gr
import random
from deep_translator import GoogleTranslator
from data_treatment import treat_data

with open("ngram_model.pkl", "rb") as f:
    model = pickle.load(f)

_, sign_list, mood_list, color_list, lucky_number_list = treat_data()
translator = GoogleTranslator(source='en', target='pt')
sign_list_br = [translator.translate(sign) for sign in sign_list]

def generate_horoscope(selected_sign):
    automatic_seeds = ["<s>", "<s>", "<s>"]

    daily_words = model.generate_text(automatic_seeds, 500)

    clean_daily_words = daily_words.replace("<s>", "").replace("</s>", "").strip()

    br_daily_words = GoogleTranslator(source='en', target='pt').translate(clean_daily_words)

    todays_mood = random.choice(mood_list)
    todays_color = random.choice(color_list)
    todays_number = random.choice(lucky_number_list) 

    todays_mood_br = GoogleTranslator(source='en', target='pt').translate(todays_mood)
    todays_color_br = GoogleTranslator(source='en', target='pt').translate(todays_color)
    

    return br_daily_words, todays_color_br, todays_mood_br, str(todays_number)

def interface():
    with gr.Blocks(title="Horóscopo N-Gram") as demo:
        gr.Markdown("# 🌌 Horóscopo")
        gr.Markdown("Selecione seu signo para gerar as previsões do dia baseadas em modelos estatísticos de N-grams.")
        
        with gr.Row():
            input_signo = gr.Dropdown(
                choices = sign_list_br, 
                label = "Selecione seu signo:", 
                value = sign_list_br[0]
            )
        
        btn = gr.Button("Gerar previsão para hoje")
        
        with gr.Column():
            output_texto = gr.Textbox(label="Previsão do Dia", lines=5)
            with gr.Row():
                output_cor = gr.Textbox(label="Cor da Sorte")
                output_humor = gr.Textbox(label="Humor")
                output_num = gr.Textbox(label="Número da sorte")

        btn.click(
            fn = generate_horoscope, 
            inputs = input_signo, 
            outputs = [output_texto, output_cor, output_humor, output_num]
        )

    demo.launch()

if __name__ == "__main__":
    interface()