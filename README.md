# 💬 Classificador de Sentimentos em Comentários

Projeto acadêmico desenvolvido para a disciplina de **Exploração Digital e Fundamentos Tecnológicos** do período passado da faculdade, com o objetivo de construir um modelo de Machine Learning capaz de classificar automaticamente o sentimento de comentários em inglês como **positivo** ou **negativo**.

---

## 📋 Sobre o projeto

O modelo foi treinado com o dataset **Sentiment140**, contendo 1,6 milhão de tweets em inglês previamente rotulados. O pipeline de classificação consiste em:

1. **Limpeza do texto** — remoção de links, menções e padronização
2. **Vetorização TF-IDF** — conversão do texto em representação numérica, considerando unigramas, bigramas e trigramas (até 100 mil termos)
3. **Regressão Logística** — algoritmo de classificação que aprende o "peso emocional" de cada termo

O modelo atingiu aproximadamente **82% de acurácia** nos dados de teste (320 mil comentários reservados para validação);
Para melhor visualização, segue abaixo a matriz de confusão do MoodClassifier:

![Matriz de Confusão (HeatMap)](asset/matrizDeConfusao.png){fig.align='center'}   

---

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [scikit-learn](https://scikit-learn.org/) — vetorização TF-IDF e Regressão Logística
- [pandas](https://pandas.pydata.org/) — manipulação dos dados
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) — visualização da Matriz de Confusão
- [Google Colab](https://colab.research.google.com/) — ambiente de treinamento

---

## ▶️ Como testar

### Opção 1 — Rodar no Google Colab (recomendado)

Abra o notebook diretamente no Colab, execute todas as células em ordem e use o campo de input ao final para digitar comentários:

> ⚠️ O treinamento leva entre 2 a 4 minutos no Colab.

### Opção 2 — Rodar localmente com o modelo já treinado

Se não quiser esperar o treinamento, baixe o modelo já treinado:

📥 **[Download do modelo (modelo_sentimentos.pkl) — Google Drive](COLE_O_LINK_AQUI)**

Depois, com o Python instalado:


Depois, com o Python instalado:
 
```bash
# Clone o repositório
git clone https://github.com/MiguelReisB/NOME_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
 
# Cria e ativa o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
```
```bash
python3 -m venv venv
venv\Scripts\activate         # Windows (PowerShell)
```
```bash
# Instale as dependências
pip install scikit-learn
 
# Coloque o arquivo modelo_sentimentos.pkl nesta mesma pasta
# e execute:
python classificar.py
```
 
> Toda vez que abrir um terminal novo, ative o ambiente antes com `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows). Para sair, digite `deactivate`.

https://drive.google.com/file/d/1LlCJ54vKPd9qrUKI0CK64KMSnywQ7NJI/view?usp=sharing
