import telebot
from knapsack import knapsack

token = "YOUR_TELEGRAM_TOKEN_HERE"
bot = telebot.TeleBot(token)
W, val, itens, wt = 0, [], [], []


@bot.message_handler(commands=["knapsack"])  # /knapsack
def ask_itens(message):
    global W, val, itens, wt
    W, val, itens, wt = 0, [], [], []
    chat_id = message.chat.id
    bot.send_message(chat_id, "Digite o nome dos itens separados por vírgula")
    bot.register_next_step_handler(message, ask_values)


def ask_values(message):
    global itens
    chat_id = message.chat.id
    itens = message.text.split(",")
    bot.send_message(chat_id, "Digite os valores dos itens separados por vírgula")
    bot.register_next_step_handler(message, ask_weights)


def ask_weights(message):
    global val
    chat_id = message.chat.id
    val = list(map(int, message.text.split(",")))
    bot.send_message(chat_id, "Digite os pesos dos itens separados por vírgula.")
    bot.register_next_step_handler(message, ask_max_weight)


def ask_max_weight(message):
    global wt
    chat_id = message.chat.id
    wt = list(map(int, message.text.split(",")))
    bot.send_message(chat_id, "Digite o peso máximo suportado pela mochila")
    bot.register_next_step_handler(message, show_answer)


def show_answer(message):
    global W, val, itens, wt
    chat_id = message.chat.id
    W = int(message.text)
    answer = knapsack(W, wt, val, itens, len(val))
    backpack = " ".join(answer[0])
    total_value = answer[1]
    bot.send_message(chat_id, f"Leve na mochilas os seguites itens: {backpack}")
    bot.send_message(chat_id, f"Sua mochila terá o valor máximo de {total_value}")


bot.infinity_polling()