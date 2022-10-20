
import telebot

import random


bot = telebot.TeleBot('5615645123:AAF9qf79ga9BGPdNjjWQT58XRH9ajQ7dIEU')


from telebot import types


first = ["The best day to study the subject. And the last one.",
         "Don't teach. You can't.",
         "Be careful, the subject can affect your mental condition.",
         "The best time to start a new task or finish old ones.",
         "There are still many incomprehensible things in the world. Leave this one alone."]

second = ["But remember that even in this case, you should not forget about",
          "If you go out of town, return back and think about",
          "Those who are aiming to do a lot of things today should remember about",
          "If you have a breakdown, pay attention to",
          "Remember that thoughts are material, which means that you need to constantly think about"]

second_add = ["Python and Python.",
              "quizzes that can interfere with plans so inopportunely.",
              "your mental health, otherwise a complete breakdown is possible by the evening.",
              "deadlines — especially those that you did not finish yesterday.",
              "the rest?"]

third = ["Evil tongues may tell you this, but you don't need to listen to them today.",
         "Know that success favors only the persistent, so dedicate this day to the education of the Python.",
         "Even if you cannot reduce the influence of retrograde Mercury, don't think about deadlines.",
         "There is no need to be afraid of functions — today is the time when they mean a lot.",
         "If you meet professor on the way, take part, and then this meeting will promise you pleasant troubles."]



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "/start":



        bot.send_message(message.from_user.id, "Hi! I can predict your succses in the subject and give you a piece of advice.")



        keyboard = types.InlineKeyboardMarkup()


        key_datam = types.InlineKeyboardButton(text='Data management in database design', callback_data='subject')


        keyboard.add(key_datam)

        key_python = types.InlineKeyboardButton(text='Programming in Python', callback_data='subject')

        keyboard.add(key_python)

        key_stat = types.InlineKeyboardButton(text='Mathematical Statistics', callback_data='subject')

        keyboard.add(key_stat)

        key_account = types.InlineKeyboardButton(text='Financial and Organizational Accounting', callback_data='subject')

        keyboard.add(key_account)

        key_bank = types.InlineKeyboardButton(text='Fundamentals of Banking', callback_data='subject')

        keyboard.add(key_bank)

        key_systems = types.InlineKeyboardButton(text='Introduction to information systems', callback_data='subject')

        keyboard.add(key_systems)

        key_ethics = types.InlineKeyboardButton(text='Business Ethics and Corporate Social Responsibility', callback_data='subject')

        keyboard.add(key_ethics)

        key_infrastruct = types.InlineKeyboardButton(text='Digital infrastructures for business', callback_data='subject')

        keyboard.add(key_infrastruct)

        key_iso = types.InlineKeyboardButton(text='Information Systems and Organisations', callback_data='subject')

        keyboard.add(key_iso)

        key_architec = types.InlineKeyboardButton(text='Enterprise Architecture', callback_data='subject')

        keyboard.add(key_architec)

        key_globe = types.InlineKeyboardButton(text='Business and Management in Global Context', callback_data='subject')

        keyboard.add(key_globe)

        key_learn = types.InlineKeyboardButton(text='Machine Learning with Python', callback_data='subject')

        keyboard.add(key_learn)


        bot.send_message(message.from_user.id, text="Choose the subject:", reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id,
                         "This bot can predict your success in the subject. To get started, write /start")

    else:

        bot.send_message(message.from_user.id, "I don't understand you. Please write /help.")



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "subject":

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)


        bot.send_message(call.message.chat.id, msg)


def main_loop():
    while True:
        bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main_loop()