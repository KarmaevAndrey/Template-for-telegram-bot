from baza_working import *
from utis import *
from setings import *


# Sending a message with a link to a donation
def menu(message, text="В меню"):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_text_id = types.KeyboardButton(text_button_text)
    item_text_= types.KeyboardButton(text_button_text)
    item_text = types.KeyboardButton(text_button_text)

    markup3 = markup.add(item_text).add(item_text).add(item_text)
    bot.send_message(message.chat.id, text, reply_markup=markup3)


@bot.message_handler(commands=['donate'])
def call_up_donate(message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    markup = types.InlineKeyboardMarkup()
    item_shere = types.InlineKeyboardButton(
        text="Перевести на тинькоф",
        url=tinkoff_url)
    markup.add(item_shere)
    bot.send_message(message.chat.id, f"Спасибо за поддержку🤗 я ОЧЕНЬ её ценю. Поэтому я не буду показывать "
                                      f"тебе рекламу, но не забудь указать эти цифры в комментарии к донату."
                                      f"⏩`{message.chat.id}`⏪",
                     reply_markup=markup, parse_mode='Markdown')


@bot.message_handler(commands=['my_tim'])
def my_tim(message, speed=0.7):
    j = 0
    bar = "■■■■■■■■■■"
    msg = bot.send_message(message.chat.id, bar)
    for i in range(len(bar) - 1, -1, -1):
        j += 1
        bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=str(bar[:i]) + "□" * j)
        time.sleep(speed)
    bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)


def register_user(message, chat_id):
    try:
        json_add_user(message)
        bot.send_message(chat_id,
                         f'Привет! {str(message.from_user.first_name)}, вы тут впервые, держите инструкцию:')
        my_tim()
        menu(message, 'Попробуйте сейчас!')
    except Exception:
        bot.send_message(message.chat.id, '😭ОЙ... Что то пошло не так попробуйте ещё раз😕')


def adding_user_sending_instructions(message, chat_id, is_old_user, ref_url=None):
    try:
        if not is_old_user:
            add_info_from_location(ref_url, chat_id)
            menu(message, f'Привет, {str(message.from_user.first_name)}, давно не виделись.')
            sti = open('media/cherry.tgs', 'rb')
            bot.send_sticker(chat_id, sti)
        else:
            if ref_url==None:
                bot_admin.send_message(admin_id, f"НОВЫЙ ПОЛЬЗОВАТЕЛЬ: @{message.chat.username}\n"
                                                 f"имя: {message.chat.username}\n"
                                                 f"фамилия: {message.from_user.last_name}\n")
                register_user(message, chat_id)
            elif chat_id in return_info_from_location(ref_url)[2]:
                register_user(message, chat_id)

            else:
                bot_admin.send_message(admin_id, f"НОВЫЙ ПОЛЬЗОВАТЕЛЬ: @{message.chat.username}\n"
                                                 f"имя: {message.chat.username}\n"
                                                 f"фамилия: {message.from_user.last_name}\n"
                                                 f"перешёл из: {return_info_from_location(ref_url)[0]}")
                add_info_from_location(ref_url, chat_id)
                register_user(message, chat_id)

    except Exception:
        pass



@bot.message_handler(commands=['start'])
def start(message):
    chat_id = int(message.from_user.id)
    is_old_user = not (json_is_old_user(chat_id))
    try:
        if is_old_user:
            adding_user_sending_instructions(message, chat_id, is_old_user=True)
        else:
            menu(message, f'Привет, {str(message.from_user.first_name)}, давно не виделись.')
            sti = open('media/cherry.tgs', 'rb')
            bot.send_sticker(chat_id, sti)
    except Exception:
        bot.send_message(message.chat.id, 'нажми на /start')


@bot.message_handler(content_types=['text'])
def get_txt(message):
    try:
        mes_text = str(message.text)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        mci = message.chat.id
        if mes_text == text_button_text:
            bot.send_message(message.chat.id, "YESS")

    except Exception:
        bot.send_message(message.chat.id, text_error)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    cmi = call.message.chat.id
    text_call = call.data
    if False:
        pass
    else:
        bot.send_message(cmi, f"ERROR: 404 not fund {text_call}")


bot.polling(none_stop=True)
