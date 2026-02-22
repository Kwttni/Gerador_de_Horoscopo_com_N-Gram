<h1>Gerador de Horóscopo com N-Gram</h1>

## Integrantes

- Gabriella Nascimento dos Santos da Silva
- João Vinícius de Almeida Argolo
- José Victor Ribeiro de Jesus
- Mariana Silva Costa
- Tiago Rodrigues dos Santos


<h2>Descrição</h2>

Este projeto tem como objetivo desenvolver uma aplicação capaz de gerar previsões de horóscopo utilizando um modelo estatístico baseado em <strong>N-grams</strong>.

O modelo é treinado a partir de um conjunto de descrições de horóscopo e aprende padrões de sequência de palavras. A partir disso, ele consegue gerar novos textos que simulam previsões diárias.

A aplicação possui uma interface interativa desenvolvida com <strong>Streamlit</strong>,
permitindo que o usuário selecione seu signo e gere uma previsão automaticamente.

<h2>Tecnologias Utilizadas</h2>

<ul>
<li>Python</li>
<li>Pandas</li>
<li>Streamlit</li>
<li>Deep Translator</li>
<li>Modelo estatístico N-Gram</li>
</ul>

<h2>Como o Projeto Funciona</h2>

<ol>
<li>O dataset contendo horóscopos é carregado e tratado.</li>
<li>Um modelo N-Gram é treinado com as descrições.</li>
<li>O modelo aprende probabilidades de sequência entre palavras.</li>
<li>Ao selecionar um signo, o sistema gera um novo texto baseado nessas probabilidades.</li>
<li>O texto é traduzido para português.</li>
<li>Também são sorteados:
<ul>
<li>Humor do dia</li>
<li>Cor da sorte</li>
<li>Número da sorte</li>
</ul>
</li>
</ol>

<h2>Estrutura do Projeto</h2>

<ul>
<li><strong>src/app.py</strong> — Interface da aplicação com Streamlit</li>
<li><strong>src/train_model.py</strong> — Treinamento do modelo N-Gram</li>
<li><strong>src/ngram_model.py</strong> — Implementação do modelo</li>
<li><strong>src/data_treatment.py</strong> — Tratamento e leitura dos dados</li>
<li><strong>data/horoscope.csv</strong> — Base de dados</li>
</ul>

<h2>Instalação</h2>

<h3>1. Clonar o repositório</h3>

Abra o terminal dentro da pasta desejada e execute:

<pre>
git clone https://github.com/Kwttni/Gerador_de_Horoscopo_com_N-Gram.git
</pre>

Entre na pasta do projeto:

<pre>
cd Gerador_de_Horoscopo_com_N-Gram
</pre>

---

# Windows

<h3>2. Criar ambiente virtual</h3>

<pre>
python -m venv venv
</pre>

<h3>3. Ativar ambiente virtual</h3>

<pre>
venv\Scripts\activate
</pre>

---

# Linux / Mac

<h3>2. Criar ambiente virtual</h3>

<pre>
python3 -m venv venv
</pre>

<h3>3. Ativar ambiente virtual</h3>

<pre>
source venv/bin/activate
</pre>

---

<h3>4. Instalar dependências</h3>

<pre>
pip install -r requirements.txt
</pre>

---

<h2>Treinar o modelo</h2>

Antes de executar a aplicação, é necessário treinar o modelo N-Gram.

<pre>
python src/train_model.py
</pre>

Isso criará o arquivo:

<pre>
ngram_model.pkl
</pre>

---

<h2>Executar a aplicação</h2>

<pre>
streamlit run src/app_streamlit.py
</pre>

O Streamlit irá iniciar um servidor local e mostrará algo semelhante a:

<pre>
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
</pre>

Abra o endereço exibido no terminal no seu navegador para acessar a aplicação.

---

<h2>Exemplo de Uso</h2>

<ol>
<li>Selecione seu signo</li>
<li>Clique em <strong>Gerar previsão para hoje</strong></li>
<li>O sistema irá gerar:</li>
<ul>
<li>Previsão do dia</li>
<li>Cor da sorte</li>
<li>Humor</li>
<li>Número da sorte</li>
</ul>
</ol>

<h2>Modelo Utilizado</h2>

O projeto utiliza um modelo <strong>4-gram</strong>, no qual a previsão da próxima palavra é baseada nas três palavras anteriores.

Durante o treinamento, o modelo aprende probabilidades condicionais entre sequências de palavras presentes no dataset. Na geração de texto, a próxima palavra é escolhida com base nessas probabilidades. Isso permite gerar textos com estrutura semelhante aos dados utilizados no treinamento.
