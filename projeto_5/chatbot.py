"""
This script creates a ChatBot instance using the ChatterBotCorpusTrainer from the chatterbot library. The bot is trained on the Portuguese language corpus and is ready to engage in conversations.

The script starts the bot and enters a loop where the user can input questions. The bot will respond with an appropriate answer. The loop can be exited by typing 'sair' (exit in Portuguese).
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'LeonBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'minimum_similarity_threshold': 0.65
        }
    ]
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')

print("Chatbot está pronto para conversar! Digite 'sair' para encerrar.")

while True:
    pergunta = input("Voce: ")
    if pergunta.lower == 'sair':
        print("Chatbot: Tchau!")
        break
    resposta = chatbot.get_response(pergunta)
    print("Chatbot:", resposta)