import telebot
from telebot import types
from telebot.handler_backends import State, StatesGroup
from telebot.custom_filters import StateFilter

class MyStates(StatesGroup):
    start_no_subscribe = State()
    start_subscribed = State()
    start_game = State()
    first_card = State()
    next_question = State()
    second_card = State()
    conclusions = State()
    endgame = State()