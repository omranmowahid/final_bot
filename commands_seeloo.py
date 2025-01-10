from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from datetime import datetime, timedelta


waiting_users = []
active_chats = {}

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton('اکونت', callback_data='account')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text='بخاطر چت کردن لینک /chat ره کلک کو\nیا بخاطر ساختن اکونت دکمه پایانی ره فشار بتی', reply_markup=reply_markup,)
    with open(file='db_start.txt', mode='a') as db:
        utc = datetime.utcnow()
        user_name = update.effective_user.username or 'NoUsername'
        usr_id = update.effective_user.id
        db.write(f'{usr_id}, {user_name} at {utc + timedelta(hours=4, minutes=30)}\n')

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard_start = [[KeyboardButton('دیدن اکونت مخاطب'), KeyboardButton('/end')]]
    reply_markup_start = ReplyKeyboardMarkup(keyboard_start, resize_keyboard=True)
    user_id = update.message.from_user.id

    if user_id in active_chats:
        await update.message.reply_text('در حال حاضر در چت هستین برای پایان چت /end را انتخاب کنید')
        return

    if waiting_users:
        # Remove the user from the waiting list if they are already in it
        if user_id in waiting_users:
            waiting_users.remove(user_id)

        # Check for a partner who is not the same as the current user
        partner_id = None
        for waiting_user in waiting_users:
            if waiting_user != user_id:
                partner_id = waiting_user
                break

        if partner_id:
            waiting_users.remove(partner_id)
            active_chats[user_id] = partner_id
            active_chats[partner_id] = user_id

            await context.bot.send_message(chat_id=partner_id, text='به مخاطب ات سلام کن', reply_markup=reply_markup_start)
            await update.message.reply_text(text='به مخاطب ات سلام کن', reply_markup=reply_markup_start)
            with open(file='couple.txt', mode='a') as couple:
                utc = datetime.utcnow()
                user_name = update.effective_user.username or 'NoUsername'
                partner_user = await context.bot.get_chat(partner_id)
                partner_username = partner_user.username or 'NoUsername'
                couple.write(f'{user_id}({user_name}) is with {partner_id}({partner_username}) at {utc + timedelta(hours=4, minutes=30)}')
        else:
            # If no suitable partner is found
            waiting_users.append(user_id)
            await update.message.reply_text('در حال انتظار برای پیوستن کسی در چت')
    else:
        # Add the user to the waiting list if it's empty
        waiting_users.append(user_id)
        await update.message.reply_text('در حال انتظار برای پیوستن کسی در چت')

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    # Check if user is in an active chat
    if user_id in active_chats:
        partner_id = active_chats[user_id]

        if update.message.text == 'دیدن اکونت مخاطب':

            # Notify the partner that their profile was viewed
            await context.bot.send_message(chat_id=partner_id, text='مخاطب اکونت شما را دید')

            # Fetch the partner's profile data
            partner_user_data = context.application.user_data.get(partner_id, {})
            print('user', context.user_data, 'partner', partner_user_data)

            # Send profile details to the user who clicked 'Show partner profile'
            if partner_user_data:
                await update.message.reply_text(text=(

                                    f" جنسیت:     {partner_user_data.get('gender', 'نامشخص')}"
                                    f"\nسن:          {partner_user_data.get('age', 'نامشخص')}"
                                    f"\nولایت:       {partner_user_data.get('province', 'نامشخص')}"
                                    f"\nشهر:         {partner_user_data.get('city', 'نامشخص')}"
                ))
            else:
                await update.message.reply_text('مخاطب شما اکونت ندارد.')

            # Do not forward 'show partner profile' text to the partner
            return

        # Forward regular chat messages to the partner (excluding the 'show partner profile' command)
        await context.bot.send_message(chat_id=partner_id, text=update.message.text)

    else:
        await update.message.reply_text('شما در چت نیستید. برای پیوستن بالای /chat کلیک کنید')


async def end_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in active_chats:
        partner_id = active_chats.pop(user_id)
        active_chats.pop(partner_id, None)
        await context.bot.send_message(chat_id=partner_id, text='مخاطب شما چت را ترک کرد. برای چت جدید /chat کلیک کنید', reply_markup=ReplyKeyboardRemove())
        await update.message.reply_text('شما جت را ترک کردید برای چت جدید /chat کلک کنید', reply_markup=ReplyKeyboardRemove())
    else:
        await update.message.reply_text('شما در هیچ چت ای نیستید برای چت جدید /chat کلیک کنید')

async def profile(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if context.user_data:
        try:
            await update.message.reply_text(f" جنسیت:     {context.user_data['gender']}"
                                    f"\nسن:          {context.user_data['age']}"
                                    f"\nولایت:       {context.user_data['province']}"
                                    f"\nشهر:         {context.user_data['city']}")
        except:
            await update.message.reply_text('شما اکونت ندارید')
            return await start(update, context)
    else:
        await update.message.reply_text('شما اکونت ندارید')
        return await start(update, context)
