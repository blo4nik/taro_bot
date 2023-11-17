import telebot
import random
import time
from telebot import types
from telebot import custom_filters
from telebot.custom_filters import StateFilter
from admin import MyStates
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

bot.add_custom_filter(StateFilter(bot))
bot.add_custom_filter(custom_filters.ChatFilter())

initial_card_deck_1 = ['deck_1/1.jpg', 'deck_1/2.jpg', 'deck_1/3.jpg', 'deck_1/4.jpg', 'deck_1/5.jpg', 'deck_1/6.jpg', 'deck_1/7.jpg', 'deck_1/8.jpg', 'deck_1/9.jpg', 'deck_1/10.jpg', 'deck_1/11.jpg', 'deck_1/12.jpg', 'deck_1/13.jpg', 'deck_1/14.jpg', 'deck_1/15.jpg', 'deck_1/16.jpg', 'deck_1/17.jpg', 'deck_1/18.jpg', 'deck_1/19.jpg', 'deck_1/20.jpg', 'deck_1/21.jpg', 'deck_1/22.jpg', 'deck_1/23.jpg', 'deck_1/24.jpg', 'deck_1/25.jpg', 'deck_1/26.jpg', 'deck_1/27.jpg', 'deck_1/28.jpg', 'deck_1/29.jpg', 'deck_1/30.jpg', 'deck_1/31.jpg', 'deck_1/32.jpg', 'deck_1/33.jpg', 'deck_1/34.jpg', 'deck_1/35.jpg', 'deck_1/36.jpg', 'deck_1/37.jpg', 'deck_1/38.jpg', 'deck_1/39.jpg', 'deck_1/40.jpg', 'deck_1/41.jpg', 'deck_1/42.jpg', 'deck_1/43.jpg', 'deck_1/44.jpg', 'deck_1/45.jpg', 'deck_1/46.jpg', 'deck_1/47.jpg', 'deck_1/48.jpg', 'deck_1/49.jpg', 'deck_1/50.jpg', 'deck_1/51.jpg', 'deck_1/52.jpg', 'deck_1/53.jpg', 'deck_1/54.jpg', 'deck_1/55.jpg', 'deck_1/56.jpg', 'deck_1/57.jpg', 'deck_1/58.jpg', 'deck_1/59.jpg', 'deck_1/60.jpg', 'deck_1/61.jpg', 'deck_1/62.jpg', 'deck_1/63.jpg', 'deck_1/64.jpg', 'deck_1/65.jpg', 'deck_1/66.jpg', 'deck_1/67.jpg', 'deck_1/68.jpg', 'deck_1/69.jpg', 'deck_1/70.jpg', 'deck_1/71.jpg', 'deck_1/72.jpg', 'deck_1/73.jpg', 'deck_1/74.jpg', 'deck_1/75.jpg', 'deck_1/76.jpg', 'deck_1/77.jpg', 'deck_1/78.jpg', 'deck_1/79.jpg', 'deck_1/80.jpg', 'deck_1/81.jpg', 'deck_1/82.jpg', 'deck_1/83.jpg', 'deck_1/84.jpg', 'deck_1/85.jpg', 'deck_1/86.jpg', 'deck_1/87.jpg', 'deck_1/88.jpg', 'deck_1/89.jpg', 'deck_1/90.jpg', 'deck_1/91.jpg', 'deck_1/92.jpg', 'deck_1/93.jpg', 'deck_1/94.jpg', 'deck_1/95.jpg', 'deck_1/96.jpg', 'deck_1/97.jpg', 'deck_1/98.jpg', 'deck_1/99.jpg', 'deck_1/100.jpg']

initial_card_deck_2 = ['deck_2/1.png', 'deck_2/2.png', 'deck_2/3.png', 'deck_2/4.png', 'deck_2/5.png', 'deck_2/6.png', 'deck_2/7.png', 'deck_2/8.png', 'deck_2/9.png', 'deck_2/10.png', 'deck_2/11.png', 'deck_2/12.png', 'deck_2/13.png', 'deck_2/14.png', 'deck_2/15.png', 'deck_2/16.png', 'deck_2/17.png', 'deck_2/18.png', 'deck_2/19.png', 'deck_2/20.png', 'deck_2/21.png', 'deck_2/22.png', 'deck_2/23.png', 'deck_2/24.png', 'deck_2/25.png', 'deck_2/26.png', 'deck_2/27.png', 'deck_2/28.png', 'deck_2/29.png', 'deck_2/30.png', 'deck_2/31.png', 'deck_2/32.png', 'deck_2/33.png', 'deck_2/34.png', 'deck_2/35.png', 'deck_2/36.png', 'deck_2/37.png', 'deck_2/38.png', 'deck_2/39.png', 'deck_2/40.png', 'deck_2/41.png', 'deck_2/42.png', 'deck_2/43.png', 'deck_2/44.png', 'deck_2/45.png', 'deck_2/46.png', 'deck_2/47.png', 'deck_2/48.png', 'deck_2/49.png', 'deck_2/50.png', 'deck_2/51.png', 'deck_2/52.png', 'deck_2/53.png', 'deck_2/54.png', 'deck_2/55.png', 'deck_2/56.png', 'deck_2/57.png', 'deck_2/58.png', 'deck_2/59.png', 'deck_2/60.png', 'deck_2/61.png', 'deck_2/62.png', 'deck_2/63.png', 'deck_2/64.png', 'deck_2/65.png', 'deck_2/66.png', 'deck_2/67.png', 'deck_2/68.png', 'deck_2/69.png', 'deck_2/70.png', 'deck_2/71.png', 'deck_2/72.png', 'deck_2/73.png', 'deck_2/74.png', 'deck_2/75.png', 'deck_2/76.png', 'deck_2/77.png', 'deck_2/78.png', 'deck_2/79.png', 'deck_2/80.png', 'deck_2/81.png', 'deck_2/82.png', 'deck_2/83.png', 'deck_2/84.png', 'deck_2/85.png', 'deck_2/86.png', 'deck_2/87.png', 'deck_2/88.png', 'deck_2/89.png', 'deck_2/90.png', 'deck_2/91.png', 'deck_2/92.png', 'deck_2/93.png', 'deck_2/94.png', 'deck_2/95.png', 'deck_2/96.png', 'deck_2/97.png', 'deck_2/98.png']

card_deck_1 = []
card_deck_2 = []

admins = [618628269, 457811689]

def check_subscription_and_update_markup(chat_id, message_id, user_id):
    with open('text/start_subscribed.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    is_id_chat_member = bot.get_chat_member(chat_id=-1001867137079, user_id=user_id)
    is_subscribed = is_id_chat_member.status in status
    
    if is_subscribed:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='НАЧАТЬ ИГРУ', callback_data=f'start_game{message_id}'))
        bot.edit_message_text(chat_id=chat_id, text=text, message_id=message_id, parse_mode='HTML')
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=markup)

    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='ПОДПИСАТЬСЯ НА КАНАЛ', url='https://t.me/nobilissima13'))
        markup.add(types.InlineKeyboardButton(text='ПРОВЕРИТЬ ПОДПИСКУ', callback_data=f'chek{message_id}'))
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=markup)
    
status = ['member', 'administrator', 'creator']

@bot.message_handler(chat_id=[618628269, 457811689], commands=['edit_start_no_subscribe'])
def edit_0_1(message):
    bot.set_state(message.from_user.id, MyStates.start_no_subscribe, message.chat.id)
    bot.send_message(message.chat.id, 'Введите текст')

@bot.message_handler(state=MyStates.start_no_subscribe)
def edit_1(message):
    new_text = message.html_text
    with open('text/start_no_subscribe.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)

    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(chat_id=[618628269, 457811689], commands=['edit_start_subscribed'])
def edit_0_2(message):
    bot.set_state(message.from_user.id, MyStates.start_subscribed, message.chat.id)
    bot.send_message(message.chat.id, 'Введите текст')

@bot.message_handler(state=MyStates.start_subscribed)
def edit_1(message):
    new_text = message.html_text
    with open('text/start_subscribed.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)

    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.start_game)
def edit_3(message):
    new_text = message.html_text
    with open('text/start_game.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.first_card)
def edit_4(message):
    new_text = message.html_text
    with open('text/first_card.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.next_question)
def edit_5(message):
    new_text = message.html_text
    with open('text/next_question.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.second_card)
def edit_6(message):
    new_text = message.html_text
    with open('text/second_card.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.conclusions)
def edit_7(message):
    new_text = message.html_text
    with open('text/conclusions.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(state=MyStates.endgame)
def edit_8(message):
    new_text = message.html_text
    with open('text/endgame.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
    bot.send_message(message.chat.id, 'Текст успешно изменён!')
    bot.delete_state(message.from_user.id, message.chat.id)

@bot.message_handler(commands=['start'])
def main(message):
    global card_deck_1
    card_deck_1 = initial_card_deck_1.copy()

    global card_deck_2
    card_deck_2 = initial_card_deck_2.copy()

    with open('text/start_no_subscribe.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    sended_message_chek = bot.send_message(message.chat.id, text, parse_mode='HTML')
    sended_message_chek_id = sended_message_chek.message_id
    check_subscription_and_update_markup(message.chat.id, sended_message_chek_id, message.from_user.id)
    
@bot.message_handler()
def sent(message):
    if (message.from_user.id not in admins):
        bot.delete_message(message.chat.id, message.message_id)
        sended_message = bot.send_message(message.chat.id, 'Я не понимаю! Пользуйтесь кнопками, пожалуйста')
        time.sleep(2)
        bot.delete_message(message.chat.id, sended_message.message_id)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data[:4] == 'chek':
            sended_message_chek_id = callback.data[4:]
            is_id_chat_member = bot.get_chat_member(chat_id=-1001867137079, user_id=callback.from_user.id)
            is_subscribed = is_id_chat_member.status in status
            
            if is_subscribed:
                with open('text/start_subscribed.txt', 'r', encoding='utf-8') as file:
                    text = file.read()
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text='НАЧАТЬ ИГРУ', callback_data=f'start_game{sended_message_chek_id}'))
                bot.edit_message_text(chat_id=callback.message.chat.id, text=text, message_id=sended_message_chek_id, reply_markup=markup, parse_mode='HTML')
                bot.answer_callback_query(callback.id, 'Спасибо за подписку!', show_alert=True)
            else:
                bot.answer_callback_query(callback.id, 'Вы не подписаны!', show_alert=True)

    if callback.data[:10] == 'start_game':
        with open('text/start_game.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        markup = types.InlineKeyboardMarkup()
        no_markup = types.InlineKeyboardMarkup()

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.data[10:], reply_markup=no_markup)
        sended_msg = bot.send_message(callback.message.chat.id, text, parse_mode='HTML')
        sended_msg_id = sended_msg.message_id
        
        markup.add(types.InlineKeyboardButton('ПОЛУЧИТЬ КАРТУ', callback_data=f'first_card{sended_msg_id}'))
        if callback.from_user.id in admins:
            markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit_text_start_game'))

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=sended_msg_id, reply_markup=markup)
        
    if callback.data[:10] == 'first_card':
        first_card = random.choice(card_deck_1)
        card_deck_1.remove(first_card)

        with open('text/first_card.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        markup = types.InlineKeyboardMarkup()
        no_markup = types.InlineKeyboardMarkup()

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.data[10:], reply_markup=no_markup)

        if (callback.from_user.id in admins):
            markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit_text_first_card'))

        sended_ph_1 = bot.send_photo(callback.message.chat.id, photo=open(first_card, 'rb'))
        sended_ph_id_1 = sended_ph_1.message_id

        sended_msg_1 = bot.send_message(callback.message.chat.id, text, parse_mode='HTML')
        sended_msg_id_1 = sended_msg_1.message_id

        markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'reload_card_deck_1_1.{sended_ph_id_1}.{sended_msg_id_1}'))
        markup.add(types.InlineKeyboardButton('ПЕРЕЙТИ К СЛЕДУЮЩЕМУ ВОПРОСУ', callback_data=f'next_question.{sended_ph_id_1}.{sended_msg_id_1}'))

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=sended_msg_id_1, reply_markup=markup)
        
    if callback.data[:13] == 'next_question':
        markup = types.InlineKeyboardMarkup()
        no_markup = types.InlineKeyboardMarkup()
        

        print(callback.data)
        with open('text/next_question.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        no_markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'after_reload_card_deck_1_1.{ph_id}.{msg_id}'))
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=msg_id, reply_markup=no_markup)

        sended_msg_2 = bot.send_message(callback.message.chat.id, text, parse_mode='HTML')
        sended_msg_id_2 = sended_msg_2.message_id

        
        markup.add(types.InlineKeyboardButton('ПОЛУЧИТЬ КАРТУ', callback_data=f'second_card.{sended_msg_id_2}'))

        if (callback.from_user.id in admins):
            markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit_text_next_question'))

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=sended_msg_id_2, reply_markup=markup)

    if callback.data[:11] == 'second_card':
        next_card = random.choice(card_deck_2)
        card_deck_2.remove(next_card)

        id = callback.data.split(sep='.')
        previous_msg = id[1]
        no_markup = types.InlineKeyboardMarkup()
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=previous_msg, reply_markup=no_markup)

        with open('text/second_card.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        markup = types.InlineKeyboardMarkup()
        

        sended_ph_2 = bot.send_photo(callback.message.chat.id, photo=open(next_card, 'rb'))
        sended_ph_id_2 = sended_ph_2.message_id

        sended_msg_3 = bot.send_message(callback.message.chat.id, text, parse_mode='HTML')
        sended_msg_id_3 = sended_msg_3.message_id

        markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'reload_card_deck_2_1.{sended_ph_id_2}.{sended_msg_id_3}'))
        markup.add(types.InlineKeyboardButton('ПЕРЕЙТИ К ВЫВОДАМ', callback_data=f'conclusions.{sended_ph_id_2}.{sended_msg_id_3}'))

        if (callback.from_user.id in admins):
            markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit_text_second_card'))

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=sended_msg_id_3, reply_markup=markup)        

    if callback.data[:11] == 'conclusions':
        markup = types.InlineKeyboardMarkup()
        no_markup = types.InlineKeyboardMarkup()

        with open('text/conclusions.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        no_markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'after_reload_card_deck_2_1.{ph_id}.{msg_id}'))
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=msg_id, reply_markup=no_markup)

        sended_msg_4 = bot.send_message(callback.message.chat.id, text, parse_mode='HTML')
        sended_msg_id_4 = sended_msg_4.message_id
        markup.add(types.InlineKeyboardButton('ЗАВЕРШИТЬ ИГРУ', callback_data=f'endgame{sended_msg_id_4}'))

        if (callback.from_user.id in admins):
            markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit_text_conclusions'))

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=sended_msg_id_4, reply_markup=markup)
        
    if callback.data[:7] == 'endgame':
        markup = types.InlineKeyboardMarkup()
        no_markup = types.InlineKeyboardMarkup()

        with open('text/endgame.txt', 'r', encoding='utf-8') as file:
            text = file.read()

        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.data[7:], reply_markup=no_markup)
        sended_msg_5 = bot.send_message(callback.message.chat.id, text, parse_mode='HTML')
        sended_msg_id_5 = sended_msg_5.message_id

        if (callback.from_user.id in admins):
            markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit_text_endgame'))

        
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=sended_msg_id_5, reply_markup=markup)

    if callback.data[:26] == 'after_reload_card_deck_1_1':
        print('after_reload_card_deck_1_1')
        next_card = random.choice(card_deck_1)
        card_deck_1.remove(next_card)
        
        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'after_reload_card_deck_1_2.{ph_id}.{msg_id}'))

        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data[:26] == 'after_reload_card_deck_1_2':
        print(f'after_reload_card_deck_1_2')
        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        next_card = random.choice(card_deck_1)
        markup = types.InlineKeyboardMarkup()
        
        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data[:26] == 'after_reload_card_deck_2_1':
        print('after_reload_card_deck_2_1')
        next_card = random.choice(card_deck_2)
        card_deck_2.remove(next_card)
        
        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'after_reload_card_deck_2_2.{ph_id}.{msg_id}'))

        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data[:26] == 'after_reload_card_deck_2_2':
        print(f'after_reload_card_deck_2_2')
        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        next_card = random.choice(card_deck_2)
        card_deck_2.remove(next_card)
        markup = types.InlineKeyboardMarkup()
        
        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data[:20] == 'reload_card_deck_1_1':
        next_card = random.choice(card_deck_1)
        card_deck_1.remove(next_card)
        
        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'reload_card_deck_1_2.{ph_id}.{msg_id}'))
        markup.add(types.InlineKeyboardButton('ПЕРЕЙТИ К СЛЕДУЮЩЕМУ ВОПРОСУ', callback_data=f'next_question.{ph_id}.{msg_id}'))

        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data[:20] == 'reload_card_deck_1_2':
        next_card = random.choice(card_deck_1)

        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]
        
        markup = types.InlineKeyboardMarkup()
        
        markup.add(types.InlineKeyboardButton('ПЕРЕЙТИ К СЛЕДУЮЩЕМУ ВОПРОСУ', callback_data=f'next_question.{ph_id}.{msg_id}'))
        media = types.InputMediaPhoto(open(next_card, 'rb'))
        
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data[:20] == 'reload_card_deck_2_1':
        next_card = random.choice(card_deck_2)
        card_deck_2.remove(next_card)

        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ЗАМЕНИТЬ КАРТУ', callback_data=f'reload_card_deck_2_2.{ph_id}.{msg_id}'))
        markup.add(types.InlineKeyboardButton('ПЕРЕЙТИ К ВЫВОДАМ', callback_data=f'conclusions.{ph_id}.{msg_id}'))

        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data[:20] == 'reload_card_deck_2_2':
        next_card = random.choice(card_deck_2)

        id = callback.data.split(sep='.')
        ph_id = id[1]
        msg_id = id[2]

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('ПЕРЕЙТИ К ВЫВОДАМ', callback_data=f'conclusions.{ph_id}.{msg_id}'))
        
        media = types.InputMediaPhoto(open(next_card, 'rb'))
        bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id = ph_id)

        bot.edit_message_reply_markup(callback.message.chat.id, msg_id, reply_markup=markup)

    if callback.data == 'edit_text_start_game':
        bot.set_state(callback.from_user.id, MyStates.start_game, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Введите текст')

    if callback.data == 'edit_text_first_card':
        bot.set_state(callback.from_user.id, MyStates.first_card, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Введите текст')

    if callback.data == 'edit_text_next_question':
        bot.set_state(callback.from_user.id, MyStates.next_question, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Введите текст')

    if callback.data == 'edit_text_second_card':
        bot.set_state(callback.from_user.id, MyStates.second_card, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Введите текст')

    if callback.data == 'edit_text_conclusions':
        bot.set_state(callback.from_user.id, MyStates.conclusions, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Введите текст')

    if callback.data == 'edit_text_endgame':
        bot.set_state(callback.from_user.id, MyStates.endgame, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, 'Введите текст')


bot.infinity_polling(none_stop=True)