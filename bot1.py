from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download
download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
ListTrainer

chatbot = ChatBot("House", tagger_language=ENGSM)

conversa = [
    "Ola",
    "Ola, como vai?",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

while True:
    mensagem = chatbot.get_response(input("Diga alguma coisa: "))
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)

