from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
def str_to_list(string): #give a string of province's cities and return a list of cities
    pure_string = string.replace('\u200c','')
    a = pure_string.split('،')
    return [item.strip() for item in a]
dic_province = {'کابل': ['خیرخانه', 'ارزان قیمت', 'چهلستون',  'دشت برچی', 'کارته نو','کوته سنگی','دارالمان', 'بت خاک','کلوله پشته','افشار','سیلو','گلدره', 'کلکان', 'قره باغ','بگرامی','پلچرخی','سروبی', 'ده سبز', 'خاک جبار','استالف','شار','دشت برچی', 'کارته نو', 'وزیر اکبر خان','خوشحال خان','دهبوری', 'میر بجه کوت','موسایی','فرزه', 'شکردره','چهار آسیاب','پغمان', 'هودخیل','شیوه کی'],
                'مزار': str_to_list('بلخ، چارپولَک، چارکُنت، چَمتال، خَلَم، دولت‌آباد، دِهدادی، زاری، شورتپه، شولگره، کَشنده، کُلدار، مارمَل، مزار شریف، گذرگاهِ نور' ),
                'هرات': str_to_list('شهر هرات، اَدرَسکن، اِنجیل، اوبه، شافلان، چِشت شریف، زنده‌جان، سبزوار، غوریان، فَرسی، کَرُخ، کُشک، کُشک کهنه، کُهسان، گُذَره، گُلران'),
                'کندز': str_to_list('امام‌صاحب، چهاردره، خان‌آباد، دشت اَرچی، علی‌آباد، قلعهٔ ذال، کُندوز'),
                'کندهار': str_to_list('ارغستان، ارغنداب، پَنجوائی، خاکریز، دامان، ریگستان، ژِرَی، سپین‌بولدَک، شاه‌ولی‌کوت، شورابَک، غورَک، قندهار، میانَشین، مَیوَند، نیِش'),
                'بامیان': str_to_list('بامیان، کَهمَرد، پنجاب، سَیغان، شیبَر، وَرَس، یکاولنگ'),
                'بدخشان': str_to_list('اَرغَنج‌خواه، اَرگو، اِشکاشِم، بهارک، تَگاب (کِشِمِ بالا)، تیشکان، جُرم، خاش، خواهان، دَرایِم، مایمَی، نِسَی، راغستان، زیباک، شِغنان، شِکی، شهدا، شهر بزرگ، فیض‌آباد، کُران و مُنجان، کِشِم، کوف‌آب، کوهستان، واخان، وَردوج، یاوان، یفتلِ پایین، یَمگان (گیروان)، فیض اباد'),
                'بغلان': str_to_list('اندراب، بغلان جدید، بُرکه، پُلِ حصار، پُلِ خُمری، تاله و برفک، جَلگه، خِنجان، خوست و فِرِنگ، دوشی، دهانه غوری، دِه‌صلاح، فِرِنگ و غارو، گذرگاه نور، نَهرین، پل خمری'),
                'پروان': str_to_list('بَگرام، جبل‌سراج، چاریکار، سالَنگ، سرخِ پارسا، سیدخیل، شیخ‌علی، شینواری، غوربند، کوهِ صافی، چاریکار'),
                'پنجشیر': str_to_list('بازارک، اَنابه، بازارک، پریان، خِنج، دَره، روخه، شُتُل'),
                'ننگرهار': str_to_list('اَچین، بَتی‌کوت، بِهسود، پَچیرواَگام، جلال‌آباد، حصارک، چَپَرهار، خوگیانی، دَربابا، درهٔ نور، ده‌بالا، رودات، سرخ‌رود، شیرزاد، شینوار، کوت، کوزکُنر، گوشته، لعل‌پور، مُهمنددره، نازیان'),
                'غزنی': str_to_list('شهر غزنی، آب‌بند، اَجرستان، اَندَر، بهرام شهید، جاغوری، عُمری، ده‌یک، رشیدان، زنه‌خان، غزنی، قره‌باغ، گیرو، گیلان، مالستان، مُقُر، ناوَر، ناوه، واغَز، ولی‌محمد شهید خوگیانی'),
                'کاپیسا': str_to_list('اَلِه‌سائی، تَگاب، حصهٔ اول کوهستان، حصهٔ دوم کوهستان، کوه‌بند، محمود راقی، نَجراب'),
                'کنر': str_to_list('اسدآباد، بَرکُنر، خاص‌کُنر، دانگام، دره‌پیچ، چپه‌دره، چوکی، سرکانی، شیگل و شِلتَن، غازی‌آباد، مَرَوَره، ناری، نَرَنگ، نورگُل، وَتَه‌پور'),
                'لوگر': str_to_list('اَزره، بَرَکی بَرَک، پُلِ عَلَم، چَرخ، خروار، خوشی، محمدآغه'),
                'وردک': str_to_list('میدان شهر ، جلریز، جَغَتو، چکِ وردک، حصهٔ اول بهسود، دایمیرداد، سیدآباد، مرکزِ بهسود، نِرخ'),
                'دایکندی': str_to_list('نیلی، اَشتَرَلی، خِدیر، سنگِ تخت، شهرستان، کِجران، کیتی، میرامور، نیلی'),
                'نورستان': str_to_list('برگِ مَتال، پارون، دوآب، کامدیش، مَندول، نورگَرام، واما، وایگَل'),
                'نیمروز': str_to_list('چَخانسور، چهاربُرجک، خاش‌رود، زَرَنج، کَنگ'),
                'هلمند': str_to_list('بَغران، دیشو، ریگِ خان‌نشین، سَنگین، کَجَکی، گرمسیر، لشکرگاه، موسی‌قلعه، نادعلی، ناوهٔ بارکزائی، نوزاد، نهرِ سراج، واشیر'),
                'تخار': str_to_list('تالقان، اِشکمِش، بَنگی، بهارک، تالقان، چال، چاه‌آب، خواجه بهاءالدین، خواجه غار، دَرقَد، دشتِ قلعه، روستاق، فَرخار، کلفگان، نمک‌آب، وَرسَج، هزارسَموچ، یَنگی‌قلعه'),
                'لغمان': str_to_list('دولت‌شاه، قَرغه‌ای، علیشِنگ، علینگار، مِهترلام'),
                'فراه': str_to_list('اناردره، بالابلوک، بَکواه، پرچمن، پُشت‌رود، خاک سفید، شیب‌کوه، فراه، قلعهٔ کاه، گلستان، لاش و جُوَین'),
                'فاریاب': str_to_list('اَلمار، اَندخوی، بُلچراغ، پشتون‌کوت، خان چارباغ، دولت‌آباد، خواجه سبزپوش ولی، شیرین‌تَگاب، قَرغان، قَرَم‌قُل، قیصار، کوهستان، گَرزیوان، میمنه'),
                'غور': str_to_list('پسابند، مرغاب، تولک، تیوره، دولت‌یار، دولینه، چارسده، فیروزکوه، ساغر، شهرک، لعل و سرجنگل'),
                'سمنگان': str_to_list('آیبک، حضرتِ سلطان، خُرم و سارباغ، درهٔ صوف بالا، درهٔ صوف پایین، روی دوآب، فیروزنَخچیر'),
                'سرپل': str_to_list('شهر سرپل، بلخاب، سرپل، سانچارک، سوزمه‌قلعه، صیاد، کوهستانات، گوسفندی'),
                'زابل': str_to_list('قلات، اَتغَر، اَرغَنداب، تَرنگ و جَلدک، دایچوپان، شاه‌جوی، شمَلزائی، شینکَی، قَلات، کاکَر، میزان'),
                'خوست': str_to_list('شهر خوست، باک، تَنی، تیریزائی، جاجی‌میدان، خوست مَتون، سپیره، شَمَل، صَبری (یعقوبی)، قَلَندر، گُربُز، مَندوزی، موسی‌خیل، نادرشاه‌کوت'),
                'جوزجان': str_to_list('شبرغان، آقچه، خانقاه، خُم‌آب، خواجه دوکوه، دَرزاب، شِبِرغان، فیض‌آباد، قَرقین، قوش‌تپه، مَردیان، مِنگَجِک'),
                'پکتیکا': str_to_list('شرن، اُرگون، اومَنه، بَرمَل، تَروُو، جانی‌خیل، دیله و خوشامند، زرغون‌شهر، زیروک، سرحوضه، سَروبی، شَرَن، گومَل، گیان، مَتاخان، نِکه، وازه‌خواه، وَرمَمی، یحیی‌خیل، یوسف‌خیل'),
                'پکتیا': str_to_list('گردیز،احمدآباد، جاجی، جانی‌خیل، چاوک، چَمکَنی، دَند پَتان، زَدران (پشتو: ځدران)، زُرمت، سیدکَرَم، شَواک، علی‌خیل، گردیز، لجه احمدخیل'),
                'بادغیس': str_to_list('آب‌کَمَری، جَوَند، غورماچ، قادِس، قلعهٔ نو، بالامرغاب، مُقُر'),
                'ارزگان': str_to_list('ترین‌کوت، چوره، خاص‌ارزگان، دهراوود، شهید حساس، گیزاب')
                }

def arrange_keyboard_button(list):
    keyboard = [[KeyboardButton(text=area) for area in list[i:i+5]] for i in range(0, len(list), 5)]
    return keyboard
list_age = [str(a) for a in range(100)]

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
    if update.message.text in list_age:
        age = update.message.text
        context.user_data['age'] = age
    else:
        age = '18'
        context.user_data['age'] = age
    keyboard = arrange_keyboard_button(list(dic_province.keys()))

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(f'ولایت خود را انتخاب کنید', reply_markup=reply_markup)
    await update.message.reply_text('👇')
    return Q2
async def q2(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if update.message.text in list(dic_province.keys()):
        province = update.message.text
        context.user_data['province'] = province
    else:
        province = 'کابل'
        context.user_data['province'] = province

    if province == 'کابل':
        keyboard = arrange_keyboard_button(dic_province['کابل'])
    elif province == 'مزار':
        keyboard = keyboard = arrange_keyboard_button(dic_province['مزار'])
    elif province == 'هرات':
        keyboard = keyboard = arrange_keyboard_button(dic_province['هرات'])
    elif province == 'کندز':
        keyboard = keyboard = arrange_keyboard_button(dic_province['کندز'])
    elif province == 'کندهار':
        keyboard = keyboard = arrange_keyboard_button(dic_province['کندهار'])
    elif province == 'بامیان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['بامیان'])
    elif province == 'بدخشان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['بدخشان'])
    elif province == 'بغلان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['بغلان'])
    elif province == 'پروان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['پروان'])
    elif province == 'پنجشیر':
        keyboard = keyboard = arrange_keyboard_button(dic_province['پنجشیر'])
    elif province == 'ننگرهار':
        keyboard = keyboard = arrange_keyboard_button(dic_province['ننگرهار'])
    elif province == 'غزنی':
        keyboard = keyboard = arrange_keyboard_button(dic_province['غزنی'])
    elif province == 'کاپیسا':
        keyboard = keyboard = arrange_keyboard_button(dic_province['کاپیسا'])
    elif province == 'کنر':
        keyboard = keyboard = arrange_keyboard_button(dic_province['کنر'])
    elif province == 'لوگر':
        keyboard = keyboard = arrange_keyboard_button(dic_province['لوگر'])
    elif province == 'وردک':
        keyboard = keyboard = arrange_keyboard_button(dic_province['وردک'])
    elif province == 'دایکندی':
        keyboard = keyboard = arrange_keyboard_button(dic_province['دایکندی'])
    elif province == 'نورستان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['نورستان'])
    elif province == 'نیمروز':
        keyboard = keyboard = arrange_keyboard_button(dic_province['نیمروز'])
    elif province == 'هلمند':
        keyboard = keyboard = arrange_keyboard_button(dic_province['هلمند'])
    elif province == 'تخار':
        keyboard = keyboard = arrange_keyboard_button(dic_province['تخار'])
    elif province == 'لغمان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['لغمان'])
    elif province == 'فراه':
        keyboard = keyboard = arrange_keyboard_button(dic_province['فراه'])
    elif province == 'فاریاب':
        keyboard = keyboard = arrange_keyboard_button(dic_province['فاریاب'])
    elif province == 'غور':
        keyboard = keyboard = arrange_keyboard_button(dic_province['غور'])
    elif province == 'سمنگان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['سمنگان'])
    elif province == 'سرپل':
        keyboard = keyboard = arrange_keyboard_button(dic_province['سرپل'])
    elif province == 'زابل':
        keyboard = keyboard = arrange_keyboard_button(dic_province['زابل'])
    elif province == 'خوست':
        keyboard = keyboard = arrange_keyboard_button(dic_province['خوست'])
    elif province == 'جوزجان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['جوزجان'])
    elif province == 'پکتیکا':
        keyboard = keyboard = arrange_keyboard_button(dic_province['پکتیکا'])
    elif province == 'پکتیا':
        keyboard = keyboard = arrange_keyboard_button(dic_province['پکتیا'])
    elif province == 'بادغیس':
        keyboard = keyboard = arrange_keyboard_button(dic_province['بادغیس'])
    elif province == 'ارزگان':
        keyboard = keyboard = arrange_keyboard_button(dic_province['ارزگان'])
    else:
        keyboard = keyboard = arrange_keyboard_button(dic_province['کابل'])

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(f'شهر تان را انتخاب کنید', reply_markup=reply_markup)
    await update.message.reply_text('👇')
    return Q3

async def q3(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    if any(update.message.text in locations for locations in dic_province.values()):
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
