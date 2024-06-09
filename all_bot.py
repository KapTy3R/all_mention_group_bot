from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот, который поможет вам отметить всех участников группы и отправить сообщение. Мой разработчик: @MarselleSausage')

# Обработчик команды /all
def all_members(update, context):
    # Отправляем статус "набирает сообщение"
    context.bot.send_chat_action(update.effective_chat.id, action=ChatAction.TYPING)
    
    # Получаем список всех участников группы
    members = update.effective_chat.get_members_count()
    
    # Отправляем сообщение, упоминая каждого участника
    message = ' '.join([f'@{member.user.username}' for member in members])
    context.bot.send_message(update.effective_chat.id, message)

    # Отправляем сообщение, которое было введено после команды /all
    text = ' '.join(context.args)
    context.bot.send_message(update.effective_chat.id, text)

# Обработчик текстовых сообщений
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Создаем экземпляр класса Updater и передаем ему токен бота
    updater = Updater("7285475201:AAEdEXaT5kaNIyrSWvswUt9UVgo0FlTVN7A", use_context=True)

    # Получаем объект диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("all", all_members))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Ждем завершения работы бота
    updater.idle()

if __name__ == '__main__':
    main()
