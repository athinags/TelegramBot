from bot_instance import bot
from services.contato_servisse import salvar_contato

@bot.callback_query_handler(func=lambda call: call.data.startswith("contato_"))
def responder_contato(call):
    bot.answer_callback_query(call.id)
    user_name = call.from_user.first_name
    option = call.data.replace("contato_", "")
    salvar_contato(user_name, option)

    if call.data == "contato_suporte":
        bot.send_message(call.message.chat.id,  "Entre em contato com suporte: suporte@email.com")
    elif call.data == "contato_vendas":
        bot.send_message(call.message.chat.id,  "Fale com vendas: vendas@email.com")
    elif call.data == "contato_outros":
        bot.send_message(call.message.chat.id, "Descreva sua dúvida que iremos ajudar.")