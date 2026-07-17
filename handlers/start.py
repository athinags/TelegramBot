from bot_instance import bot

@bot.message_handler(commands=['start'])
def welcome(mensagem):
    texto = f'Bem-Vindo ao bot usuário {mensagem.from_user.first_name}'
    bot.send_message(mensagem.chat.id, texto)