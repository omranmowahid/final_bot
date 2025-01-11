from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
import json
import pickle

with open('provinces_age.json', 'r', encoding='utf-8') as data:
    province_age = json.load(data)
with open('cities_KeyboardButton.pkl', 'rb') as f:
    cities_KeyboardButton = pickle.load(f)

Q0, Q1, Q2, Q3 = 1,2,3,4

async def process_account(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    keyboard = [[KeyboardButton('پسر'), KeyboardButton('دختر')]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.callback_query.edit_message_text('جنسیت خود را لست ذیل انتخاب کنید')
    await update.callback_query.message.reply_text('👇',reply_markup=reply_markup)
    return Q0

async def q0(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'پسر' or update.message.text == 'دختر':
        gender = update.message.text
        context.user_data['gender'] = gender
    else:
        gender = 'پسر'
        context.user_data['gender'] = gender
    keyboard = []
    keyboard_in = []
    count_0 = 0
    for i in range(9, 70):
        keyboard_in.append(KeyboardButton(f'{i}'))
        count_0 += 1
        if count_0 % 5 == 0:
            keyboard.append(keyboard_in)
            keyboard_in = []
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(f'سن خود را وارد کنید', reply_markup=reply_markup)
    await update.message.reply_text('👇')
    return Q1

async def q1(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if update.message.text in province_age[1]['list_age']:
        age = update.message.text
        context.user_data['age'] = age
    else:
        age = '18'
        context.user_data['age'] = age
    keyboard = cities_KeyboardButton['province']

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(f'ولایت خود را انتخاب کنید', reply_markup=reply_markup)
    await update.message.reply_text('👇')
    return Q2
async def q2(update:Update, context:ContextTypes.DEFAULT_TYPE):
    with open('provinces_age.json', 'r', encoding='utf-8') as data:
        province_age = json.load(data)
    if update.message.text in list(province_age[0].keys()):
        province = update.message.text
        context.user_data['province'] = province
    else:
        province = 'کابل'
        context.user_data['province'] = province

    if province == 'کابل':
        keyboard = cities_KeyboardButton['کابل']
    elif province == 'مزار':
        keyboard = keyboard = cities_KeyboardButton['مزار']
    elif province == 'هرات':
        keyboard = keyboard = cities_KeyboardButton['هرات']
    elif province == 'کندز':
        keyboard = keyboard = cities_KeyboardButton['کندز']
    elif province == 'کندهار':
        keyboard = keyboard = cities_KeyboardButton['کندهار']
    elif province == 'بامیان':
        keyboard = keyboard = cities_KeyboardButton['بامیان']
    elif province == 'بدخشان':
        keyboard = keyboard = cities_KeyboardButton['بدخشان']
    elif province == 'بغلان':
        keyboard = keyboard = cities_KeyboardButton['بغلان']
    elif province == 'پروان':
        keyboard = keyboard = cities_KeyboardButton['پروان']
    elif province == 'پنجشیر':
        keyboard = keyboard = cities_KeyboardButton['پنجشیر']
    elif province == 'ننگرهار':
        keyboard = keyboard = cities_KeyboardButton['ننگرهار']
    elif province == 'غزنی':
        keyboard = keyboard = cities_KeyboardButton['غزنی']
    elif province == 'کاپیسا':
        keyboard = keyboard = cities_KeyboardButton['کاپیسا']
    elif province == 'کنر':
        keyboard = keyboard = cities_KeyboardButton['کنر']
    elif province == 'لوگر':
        keyboard = keyboard = cities_KeyboardButton['لوگر']
    elif province == 'وردک':
        keyboard = keyboard = cities_KeyboardButton['وردک']
    elif province == 'دایکندی':
        keyboard = keyboard = cities_KeyboardButton['دایکندی']
    elif province == 'نورستان':
        keyboard = keyboard = cities_KeyboardButton['نورستان']
    elif province == 'نیمروز':
        keyboard = keyboard = cities_KeyboardButton['نیمروز']
    elif province == 'هلمند':
        keyboard = keyboard = cities_KeyboardButton['هلمند']
    elif province == 'تخار':
        keyboard = keyboard = cities_KeyboardButton['تخار']
    elif province == 'لغمان':
        keyboard = keyboard = cities_KeyboardButton['لغمان']
    elif province == 'فراه':
        keyboard = keyboard = cities_KeyboardButton['فراه']
    elif province == 'فاریاب':
        keyboard = keyboard = cities_KeyboardButton['فاریاب']
    elif province == 'غور':
        keyboard = keyboard = cities_KeyboardButton['غور']
    elif province == 'سمنگان':
        keyboard = keyboard = cities_KeyboardButton['سمنگان']
    elif province == 'سرپل':
        keyboard = keyboard = cities_KeyboardButton['سرپل']
    elif province == 'زابل':
        keyboard = keyboard = cities_KeyboardButton['زابل']
    elif province == 'خوست':
        keyboard = keyboard = cities_KeyboardButton['خوست']
    elif province == 'جوزجان':
        keyboard = keyboard = cities_KeyboardButton['جوزجان']
    elif province == 'پکتیکا':
        keyboard = keyboard = cities_KeyboardButton['پکتیکا']
    elif province == 'پکتیا':
        keyboard = keyboard = cities_KeyboardButton['پکتیا']
    elif province == 'بادغیس':
        keyboard = keyboard = cities_KeyboardButton['بادغیس']
    elif province == 'ارزگان':
        keyboard = keyboard = cities_KeyboardButton['ارزگان']
    else:
        keyboard = keyboard = cities_KeyboardButton['کابل']

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(f'شهر تان را انتخاب کنید', reply_markup=reply_markup)
    await update.message.reply_text('👇')
    return Q3

async def q3(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    if any(update.message.text in locations for locations in province_age[0].values()):
        city = update.message.text
        context.user_data['city'] = city
    else:
        city = 'خیرخانه'
        context.user_data['city'] = city

    await update.message.reply_text(text=
                                    f" جنسیت:     {context.user_data['gender']}"
                                    f"\nسن:          {context.user_data['age']}"
                                    f"\nولایت:       {context.user_data['province']}"
                                    f"\nشهر:         {context.user_data['city']}"
                                    f"\n"
                                    f"\n"
                                    f"اکونت شما ساخته شد حالا وارد /chat شوید",
                                    reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

async def cancel(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('you canceled')
    return ConversationHandler.END






























def new():'''same as previous just conversation handler works not have more functionality than previous when you press /start -> account, chat (account -> email, phone)'''
     #async def process_account(update:Update, context:ContextTypes.DEFAULT_TYPE):
        #CHOOSE, EMAIL, PHONE = 0, 1, 2
        #await update.callback_query.answer()
        #keyboard = [[InlineKeyboardButton('email', callback_data='email'),
                    #InlineKeyboardButton(text='phone', callback_data='phone')]]
        #reply_markup = InlineKeyboardMarkup(keyboard)
        #await update.callback_query.message.reply_text('choose', reply_markup=reply_markup)
        #return CHOOSE

    #async def choose(update:Update, context:ContextTypes.DEFAULT_TYPE):
        #await update.callback_query.answer()
        #if update.callback_query.data == 'email':
           # await update.callback_query.edit_message_text(text='enter your email')
            #return EMAIL
     #   elif update.callback_query.data == 'phone':
           # await update.callback_query.edit_message_text("enter phone")
            #return PHONE

   # async def email_process(update:Update, context:ContextTypes.DEFAULT_TYPE):
        #a = update.message.text
        #print(a)
       # return ConversationHandler.END

    #async def phone_process(update:Update, context:ContextTypes.DEFAULT_TYPE):
       # a = update.message.text
        #print(a)
        #return ConversationHandler.END
    #
    #async def cancel(update:Update, context:ContextTypes.DEFAULT_TYPE):
        #await update.message.reply_text('you canceled')
        #return ConversationHandler.END
    #def previous():'''same as new() when you press /start -> account, chat (account -> email, phone) but it has bugs since conversation handler doesnt work'''
         #         from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
        #             ReplyKeyboardRemove
        #         from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler, Application, CommandHandler, \
        #             MessageHandler, filters
        #         import re
        #         from code import BOT_TOKEN
        #
        #         PHONE, EMAIL, CHOOSE = range(3)
        #         USERS_CONTACT_BOOK = {}
        #         USERNAMES_BOOK = {}
        #         USERS_ID_BOOK = set()
        #
        #         # async def process_account(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             user_name = update.effective_user.username
        #             user_id = update.effective_user.id
        #             await update.callback_query.answer()
        #             if user_name:
        #                 USERNAMES_BOOK[user_id] = user_name
        #                 keyboard = [
        #                     [
        #                         InlineKeyboardButton(text='phone', callback_data='phone'),
        #                         InlineKeyboardButton(text='email', callback_data='email')
        #                     ]
        #                 ]
        #                 reply_markup = InlineKeyboardMarkup(keyboard)
        # #                 await update.callback_query.message.reply_text('choose one of options: ', reply_markup=reply_markup)
        #                 return CHOOSE
        #             else:
        #                 keyboard = [[
        #                     InlineKeyboardButton(text='iOS', callback_data='iOS'),
        #                     InlineKeyboardButton(text='android', callback_data='android')
        #                 ]]
        #                 reply_markup = InlineKeyboardMarkup(keyboard)
        #                 # await update.callback_query.message.reply_text(text='username is essential \nlets set username',
        #                 #                                                reply_markup=reply_markup)
        #
        #         async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             await update.callback_query.answer()
        #             if update.callback_query.data == 'email':
        # #                 await update.callback_query.message.reply_text('Enter your email:')
        #                 return EMAIL
        #             elif update.callback_query.data == 'phone':
        #                 keyboard = [[KeyboardButton(text='cancel'),
        #                              KeyboardButton(text='tap', request_contact=True)]]
        #                 reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        # #                 await update.callback_query.message.reply_text("by adding your phone you'll get 50 bonus",
        # #                                                                reply_markup=reply_markup)
        #                 return PHONE
        #
        #         async def handle_phone_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             # user_id = update.effective_user.id
        #             # if update.message.contact:
        #             #     phone = update.message.contact.phone_number
        #             #     if phone in USERS_CONTACT_BOOK.values():
        #             #         keyboard = [[InlineKeyboardButton(text='Try again', callback_data='phone'),
        #             #              InlineKeyboardButton(text='Cancel', callback_data='cancel')]]
        #             #         reply_markup = InlineKeyboardMarkup(keyboard)
        #             #         await update.message.reply_text(text=f'your phone {update.message.contact} already exist', reply_markup=reply_markup)
        #             #         return PHONE
        #             #
        #             #
        #             #     USERS_CONTACT_BOOK[user_id] = phone
        #             #     await update.message.reply_text(text=f'you number {phone} is saved')
        #             #     await update.message.reply_text(text='thanks', reply_markup=ReplyKeyboardRemove())
        #             #     return await start(update, context), ConversationHandler.END
        #             a = update.message.text
        #             print(a)
        #             return ConversationHandler.END
        #             #
        #             # elif update.message.text == 'cancel':
        #             #     return await start(update, context), ConversationHandler.END
        #             # else:
        #             #     await update.message.reply_text('tap')
        #             #     return PHONE
        #
        #         async def handle_email_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             # valid, message = validate_email(update.message.text)
        #             # if valid:
        #             #     await update.message.reply_text(text=f'email is saved to you account {update.message.text}')
        #             #     return await start(update, context), ConversationHandler.END
        #             # else:
        #             #     keyboard = [[InlineKeyboardButton(text='cancel', callback_data='cancel')]]
        #             #     reply_markup = InlineKeyboardMarkup(keyboard)
        #             #     await update.message.reply_text(text=f'invalid {update.message.text} try again or cancel', reply_markup=reply_markup)
        #             #     return EMAIL
        #             a = update.message.text
        #             print(a)
        #             return ConversationHandler.END
        #
        #         # guidance of ios & android
        #         async def process_ios(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             await update.callback_query.answer()
        #             with open(r"C:\Users\emran\Downloads\iOS.jpg", 'rb') as photo:
        #                 keyboard = [[InlineKeyboardButton(text='continue', callback_data='continue')]]
        #                 reply_markup = InlineKeyboardMarkup(keyboard)
        #                 # await update.callback_query.message.reply_photo(photo=photo, caption='set username for your telegram',
        #                 #                                                 reply_markup=reply_markup)
        #
        #         async def process_android(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             await update.callback_query.answer()
        #             with open(r"C:\Users\emran\Downloads\iOS.jpg", 'rb') as photo:
        #                 keyboard = [[InlineKeyboardButton(text='continue', callback_data='continue')]]
        #                 reply_markup = InlineKeyboardMarkup(keyboard)
        #                 # await update.callback_query.message.reply_photo(photo=photo, caption='set username for your telegram',
        #                 #                                                 reply_markup=reply_markup)
        #
        #         # conversation of chatting
        #         async def process_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
        #             await update.callback_query.answer()
        #             await update.callback_query.edit_message_text('chatting with a random guy')
        #
        #         def main():
        #             print('application started')
        #             application = Application.builder().token(BOT_TOKEN).build()
        #             # application.add_handler(CommandHandler('start', start))
        #
        #             application.add_handler(CallbackQueryHandler(process_account, '^account$'))
        #             application.add_handler(CallbackQueryHandler(process_account, 'cancel'))
        #             application.add_handler(CallbackQueryHandler(process_account, '^continue'))
        #             application.add_handler(CallbackQueryHandler(process_chat, '^chat$'))
        #             application.add_handler(CallbackQueryHandler(process_ios, '^iOS$'))
        #             application.add_handler(CallbackQueryHandler(process_android, '^android$'))
        #
        #             conversation_handler = ConversationHandler(
        #                 entry_points=[CallbackQueryHandler(process_account, 'account'), ],
        #                 states={
        #                     CHOOSE: [CallbackQueryHandler(choose, 'email'), CallbackQueryHandler(choose, 'phone')],
        #                     PHONE: [MessageHandler(filters.CONTACT, handle_phone_process),
        #                             MessageHandler(filters.TEXT & ~filters.COMMAND, handle_phone_process)],
        #                     EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_email_process)],
        #                 },
        #                 fallbacks=[]
        #             )
        #
        #             application.add_handler(conversation_handler)
        #
        #             application.run_polling()
        #
        #         main()
        #
