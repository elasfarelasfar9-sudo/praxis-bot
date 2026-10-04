import telebot
from telebot import types

TOKEN = '8674096123:AAFsGj-W9OhmHJzdaNTaIZuEDSEnzsvSwaI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_en = types.InlineKeyboardButton("???? English", callback_data='lang_en')
    btn_ar = types.InlineKeyboardButton("???? «·⁄—»Ì…", callback_data='lang_ar')
    markup.add(btn_en, btn_ar)
    bot.send_message(message.chat.id, "Please choose your language / «Œ — ·€ ﬂ «·„›÷·…:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def set_language(call):
    bot.answer_callback_query(call.id, " „ Õ›Ÿ «·≈⁄œ«œ«  ?")
    welcome_text = (
        "?? „—Õ»« »ﬂ ›Ì „ Ã— Sams Topup! ??\n"
        "«·„‰’… «·√”—⁄ Ê«·√ﬂÀ— √„«‰« ··Œœ„«  «·—ﬁ„Ì….\n\n"
        "?? «Œ — „‰ «·ﬁ«∆„… »«·√”›·:"
    )
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_products = types.InlineKeyboardButton("«·„‰ Ã«  ??", callback_data='menu_products')
    btn_wallet = types.InlineKeyboardButton("„Õ›Ÿ Ì ??", callback_data='menu_wallet')
    btn_orders = types.InlineKeyboardButton("”Ã· ÿ·»« Ì ??", callback_data='menu_orders')
    btn_ref = types.InlineKeyboardButton("œ⁄Ê… «·√’œﬁ«¡ (√—»«Õ USDT) ??", callback_data='menu_ref')
    btn_google = types.InlineKeyboardButton(" ›⁄Ì· ﬁÊﬁ· »—Ê 12 ‘Â— ???", callback_data='menu_google')
    btn_coupon = types.InlineKeyboardButton("«” Œœ«„ ﬂÊ»Ê‰ ???", callback_data='menu_coupon')
    btn_api = types.InlineKeyboardButton("„› «Õ «·„ÿÊ—Ì‰ (API) ??", callback_data='menu_api')
    btn_support = types.InlineKeyboardButton("«·œ⁄„ «·›‰Ì ??", url='https://t.me/YOUR_USERNAME') 
    btn_lang = types.InlineKeyboardButton(" €ÌÌ— «··€… / Language ??", callback_data='lang_reset')
    
    markup.add(btn_products, btn_wallet, btn_orders, btn_ref, btn_google, btn_coupon, btn_api, btn_support, btn_lang)
    
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=welcome_text,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('menu_'))
def handle_menu(call):
    chat_id = call.message.chat.id
    if call.data == 'menu_products':
        prod_markup = types.InlineKeyboardMarkup(row_width=1)
        prod_markup.add(
            types.InlineKeyboardButton("Canva Pro ??", callback_data='buy_canva'),
            types.InlineKeyboardButton("ChatGPT Plus ??", callback_data='buy_chatgpt'),
            types.InlineKeyboardButton("Gemini Advanced ??", callback_data='buy_gemini'),
            types.InlineKeyboardButton("CapCut Pro ??", callback_data='buy_capcut'),
            types.InlineKeyboardButton("?? —ÃÊ⁄ ··ﬁ«∆„… «·—∆Ì”Ì…", callback_data='back_home')
        )
        bot.edit_message_text("?? **ﬁ”„ «·„‰ Ã«  «·—ﬁ„Ì…:**\n«Œ — «·„‰ Ã «·–Ì  —€» ›Ì ‘—«∆Â:", chat_id, call.message.message_id, reply_markup=prod_markup)
    elif call.data == 'menu_wallet':
        wallet_markup = types.InlineKeyboardMarkup()
        wallet_markup.add(types.InlineKeyboardButton("??? —ÃÊ⁄ ··ﬁ«∆„… «·—∆Ì”Ì…", callback_data='back_home'))
        bot.edit_message_text("?? **„Õ›Ÿ ﬂ:**\n—’Ìœﬂ «·Õ«·Ì: `0.00` EGP", chat_id, call.message.message_id, reply_markup=wallet_markup, parse_mode="Markdown")
    elif call.data == 'menu_orders':
        orders_markup = types.InlineKeyboardMarkup()
        orders_markup.add(types.InlineKeyboardButton("?? —ÃÊ⁄ ··ﬁ«∆„… «·—∆Ì”Ì…", callback_data='back_home'))
        bot.edit_message_text("?? **”Ã· ÿ·»« ﬂ:**\n·Ì” ·œÌﬂ √Ì ÿ·»«  ”«»ﬁ… Õ Ï «·¬‰.", chat_id, call.message.message_id, reply_markup=orders_markup)

@bot.callback_query_handler(func=lambda call: call.data == 'back_home')
def back_to_home(call):
    call.data = 'lang_ar'
    set_language(call)

bot.infinity_polling()