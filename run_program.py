from telegram.request import HTTPXRequest
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from code import BOT_TOKEN
from commands_seeloo import start, chat, profile, message_handler, end_chat
from main_seeloo import process_account, cancel,q0, q1, q2, q3,Q0, Q1, Q2, Q3

def main():
    request = HTTPXRequest(read_timeout=10, connect_timeout=10)
    application = Application.builder().token(BOT_TOKEN).request(request).build()
    print(application.bot.get_me())
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('chat', chat))
    application.add_handler(CommandHandler('profile', profile))
    application.add_handler(CommandHandler('end', end_chat))

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(process_account, 'account')],
        states={
            Q0: [MessageHandler(filters.TEXT & ~filters.COMMAND, q0)],
            Q1: [MessageHandler(filters.TEXT & ~filters.COMMAND, q1)],
            Q2: [MessageHandler(filters.TEXT & ~filters.COMMAND, q2)],
            Q3: [MessageHandler(filters.TEXT & ~filters.COMMAND, q3)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])

    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(process_account, 'account'))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    application.run_polling()

main()
