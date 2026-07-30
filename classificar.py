import pickle
import os

MODEL_PATH = "modelo_sentimentos.pkl"

if not os.path.exists(MODEL_PATH):
    print("Arquivo 'modelo_sentimentos.pkl' não encontrado.")
    print("Baixe o modelo treinado no link do README e coloque nesta mesma pasta.")
    exit()

print("Carregando modelo...")
with open(MODEL_PATH, "rb") as f:
    modelo = pickle.load(f)

print("\n=======================================================")
print(" Classificador de Sentimentos de Comentários em Inglês")
print("=======================================================")
print(" Digite uma frase para classificar o sentimento.")
print(" Digite 'sair' ou 'exit' para encerrar.")
print("=======================================================")

while True:
    print("\n-------------------------------------------------------")
    frase = input("Digite um comentário (em inglês): ")

    if frase.lower() in ("sair", "exit"):
        break

    resultado = modelo.predict([frase])[0]
    sentimento = "Este foi um comentário Positivo" if resultado == 1 else "Este foi um comentário Negativo"

    print(f"\n Classificação do MoodClassifier: {sentimento}")
    print("-------------------------------------------------------")

print("\n=======================================================")
print(" Obrigado por usar o classificador!")
print("=======================================================")
