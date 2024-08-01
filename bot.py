# -*- encoding: utf-8 -*-

from telebot import TeleBot, types

#Masukan token bot
_bot_ = TeleBot("")

# Sambutan
_GARIS_ = "───────────────────"
_PILIH_ = "/start\n .\n├─[ /website ]\n├─[ bold [text] ]\n├─[ inline [text] ]\n├─[ italic [text] ]\n├─[ !pdfPython ]\n├─[ !pdfPhp ]\n├─[ !pdfCss ]\n├─[ !pdfJs ]\n├─[ !pdfC++ ]\n├─[ !pdfPyFlask ]"
_WELCOME_= "{}\nSelamat datang\n{}\n\n{}".format(_GARIS_,_GARIS_,_PILIH_)

@_bot_.message_handler(commands=["start"])
def start_handler(_message_):
    _markup_ = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _markup_.add(types.KeyboardButton(text="siapa saya?"))
    # Sand nomber kontak sendiri
    _markup_.add(types.KeyboardButton(text="kirim nomor", request_contact=True))
    # Sand location
    _markup_.add(types.KeyboardButton(text="Kirim Lokasi", request_location=True))

    _message_ = _bot_.send_message(_message_.from_user.id, text="{}\n".format(_WELCOME_), reply_markup=_markup_)
    print(_message_)


@_bot_.message_handler(content_types=["contact"])
def _contact_handler_(_message_):
    _message_ = _bot_.reply_to(_message_, text='terima kasih untuk nomber teleponnya', reply_markup=types.ReplyKeyboardRemove())
    print(_message_)



@_bot_.message_handler(commands=["website"])
def _media_sosial_(_message_):
    _markup_ = types.InlineKeyboardMarkup()
    _markup_.add(types.InlineKeyboardButton(text="website", url="https://one-tlaw.rf.gd"))
    _markup_.add(types.InlineKeyboardButton(text='hubungi saya', callback_data='contact_me'))
    _markup_.add(types.InlineKeyboardButton(text='switch inline', switch_inline_query="Haloo"))
    _markup_.add(types.InlineKeyboardButton(text='switch inline current chat', switch_inline_query_current_chat='panda'))
    _message_ = _bot_.send_message(_message_.from_user.id, text="hello ada yang bisa saya bantu", reply_markup=_markup_)
    print(_message_)


@_bot_.callback_query_handler(func=lambda call: True)
def handler(call):
    print("we receive callback {}".format(call.data))
    _message_ = _bot_.send_message(call.from_user.id, text="support kami akan menghubungi anda")
    print(_message_)


@_bot_.message_handler(regexp="bold")
def bold_handler(_message_):
    _text_ = _message_.text.replace("bold","")
    _message_ = _bot_.reply_to(_message_,text="*{}*".format(_text_),parse_mode="markdown")
    print(_message_)

@_bot_.message_handler(regexp="italic")
def italic_handler(message):
    text = message.text.replace("italic","")
    msg = _bot_.reply_to(message, text="_{}_".format(text),parse_mode="markdown")
    print(msg)

@_bot_.message_handler(regexp="inline")
def inline_handler(message):
    text = message.text.replace("inline","")
    msg = _bot_.reply_to(message, text="`{}`".format(text),parse_mode="markdown")
    print(msg)


#Mengirim file documemt
@_bot_.message_handler(regexp="!pdfPhp")
def _panda_handler_(_message_):
    _message_ = _bot_.send_document(_message_.from_user.id, open("pdf/PHP.pdf", "rb"))
    print(_message_)

@_bot_.message_handler(regexp="!horse")
def _horse_handler_(_message_):
    _message_ = _bot_.send_photo(_message_.chat.id, open("img/horse.jpg", "rb"))
    print(_message_)


_bot_.polling()
