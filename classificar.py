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
    frase = input(" Comentário: ")

    if frase.lower() in ("sair", "exit"):
        break

    resultado = modelo.predict([frase])[0]
    sentimento = "Positivo 😊" if resultado == 1 else "Negativo 😞"

    print(f"\n Sentimento: {sentimento}")
    print("-------------------------------------------------------")

print("\n=======================================================")
print(" Obrigado por usar o classificador!")
print("=======================================================")
