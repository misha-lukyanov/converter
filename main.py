from aiogram import Bot, Dispatcher, types, executor
from currency_converter import CurrencyConverter
from aiogram.types.web_app_info import WebAppInfo




API_TOKEN = "7777928330:AAGXdxVtvx8Gy3TTG0k4BsAERLDiyE3QOsA"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

currency = CurrencyConverter()
amount = 0
values = 0
peremen = {}
user_id = {}
fav = {}
id = {}
user_data = {}



@dp.message_handler(commands=["help"])
async def helping_func(message: types.Message):
    await message.answer("<b>Список команд:</b>\n/settings - настройки\n/feedback [text] - обратная связь с владельцем телеграм-бота\n/well - ознакомиться с курсом валют на сайте ЦБ РФ.\n/news - последние новости валютного рынка.\n/top_currencies - актуальный список самых популярных валют в мире.\n/terms - основная терминология, связанная с валютами и экономикой.\n/calculator - онлайн-калькулятор для вычислений.", parse_mode=types.ParseMode.HTML)
                         


@dp.message_handler(commands=["well"])
async def helped(message: types.Message):
    await message.answer(
        "Перейдя по ссылке, Вы можете дополнительно ознакомиться с актуальным курсом валют, установленным Центральным Банком РФ: "
        "[ЦБ РФ](https://www.cbr.ru/currency_base/daily/)",
        parse_mode=types.ParseMode.MARKDOWN
    )

@dp.message_handler(commands=["feedback"])
async def feedback(message: types.Message):
    await message.reply("Ваше сообщение успешно доставлено <b>владельцу</b> телеграм-бота.", parse_mode=types.ParseMode.HTML)
    try:
        await bot.forward_message(
            chat_id=-1002490165473,  # ID чата владельца
            from_chat_id=message.chat.id,  # ID чата пользователя
            message_id=message.message_id  # ID сообщения для пересылки
        )
    except Exception as e:
        await message.answer(f"Ошибка при пересылке сообщения: {e}")


@dp.message_handler(commands=["news"])
async def last_news(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Ознакомиться с последними новостями в сфере инвестиций и рынков валют", web_app=WebAppInfo(url="https://www.rbc.ru/quote/tag/currency")))
    await message.answer("Для перехода в приложение нажмите на кнопку ниже.", reply_markup=markup)


@dp.message_handler(commands=["calculator"])
async def calculations(message: types.Message):
    markup13 = types.ReplyKeyboardMarkup()
    markup13.add(types.KeyboardButton("Онлайн-калькулятор", web_app=WebAppInfo(url="https://calculator888.ru/")))
    await message.answer("Для перехода в приложение нажмите кнопку ниже.", reply_markup=markup13)


@dp.message_handler(commands=["top_currencies"])
async def currencies(message: types.Message):
    await message.answer("<b>Список самых популярных валют:</b>\n1. Американский доллар (USD) - Доля в мировых резервах около 60%.\n2. Евро (EUR) - Доля в мировых резервах около 20%.\n3. Японская иена (JPY) - Доля в мировых резервах около 5%.\n4. Британский фунт стерлингов (GBP) - Доля в мировых резервах около 4%.\n5. Швейцарский франк (CHF) - Доля в мировых резервах около 1%.", parse_mode=types.ParseMode.HTML)



@dp.message_handler(commands=["terms"])
async def termins(message: types.Message):
    await message.answer("<b>Основная финансовая терминология, связанная с валютами и экономикой:</b>\n1. Валюта — средство обмена, которое принимается в качестве платежа за товары и услуги. Примеры: доллар (USD), евро (EUR), рубль (RUB).\n2. Курс валюты — цена одной валюты в единицах другой валюты. Например, курс USD к EUR показывает, сколько евро можно получить за один доллар.\n3. Конвертация валюты — процесс обмена одной валюты на другую по установленному курсу.\n4. Финансовый рынок — место, где происходят сделки с финансовыми активами, такими как валюты, акции, облигации и деривативы.\n5. Биржа — организованный рынок, на котором осуществляется торговля ценными бумагами и другими финансовыми инструментами.\n6. Спот-курс — курс, по которому валюта может быть куплена или продана немедленно.\n7. Форвардный курс — курс, по которому валюта будет куплена или продана в будущем, установленный в момент заключения сделки.\n8. Девальвация — снижение стоимости национальной валюты по отношению к другим валютам.\n9. Ревальвация — увеличение стоимости национальной валюты по отношению к другим валютам.\n10. Инфляция — общее повышение цен на товары и услуги в экономике, что приводит к снижению покупательной способности денег.", parse_mode=types.ParseMode.HTML)



@dp.message_handler(commands=["start"])
async def starting(message: types.Message):
    makrup1 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Продолжить", callback_data="continue")
    makrup1.add(btn1)
    await message.answer("Привет, Вы попали в бот <b><i>\"КОНВЕРТАТОР-ВАЛЮТ\"</i></b>.\nДля взаимодействия нажмите <i>\"Продолжить\"</i>.", reply_markup=makrup1, parse_mode=types.ParseMode.HTML)


"""обработка нажатия пользователем кнопки продолжить"""

@dp.callback_query_handler(lambda call: call.data == "continue")
async def mycur(call: types.CallbackQuery):
    photo_path = "E:\\valyuta.jpg"
    with open(photo_path, 'rb') as photo:
        await call.message.answer_photo(photo=photo, caption="Введите число, которое желаете преобразовать между валютами!")


@dp.message_handler(commands=["settings"])
async def settings(message: types.Message):
    markup20 = types.InlineKeyboardMarkup()
    btn20 = types.InlineKeyboardButton("Настроить избранную пару валют", callback_data="favourite")
    markup20.add(btn20)
    await message.answer("Основные настройки телеграмм-бота⚙️.", reply_markup=markup20 )


@dp.callback_query_handler(lambda call: call.data == "favourite")
async def favour(call: types.CallbackQuery):
    markup12 = types.InlineKeyboardMarkup(row_width=3)
    btn56 = types.InlineKeyboardButton("USD/EUR", callback_data="usd/eur")
    btn57 = types.InlineKeyboardButton("EUR/USD", callback_data="eur/usd")
    btn58 = types.InlineKeyboardButton("USD/GBP", callback_data="usd/gbp")
    btn59 = types.InlineKeyboardButton("GBP/USD", callback_data="gbp/usd")
    btn60 = types.InlineKeyboardButton("CNY/USD", callback_data="cny/usd")
    btn61 = types.InlineKeyboardButton("USD/CNY", callback_data="usd/cny")
    btn62 = types.InlineKeyboardButton("SEK/USD", callback_data="sek/usd")
    btn63 = types.InlineKeyboardButton("USD/SEK", callback_data="usd/sek")
    btn64 = types.InlineKeyboardButton("CAD/EUR", callback_data="cad/eur")
    btn65 = types.InlineKeyboardButton("EUR/CAD", callback_data="eur/cad")
    btn66 = types.InlineKeyboardButton("JPY/CAD", callback_data="jpy/cad")
    btn67 = types.InlineKeyboardButton("USD/JPY", callback_data="usd/jpy")
    btn68 = types.InlineKeyboardButton('RUB/USD', callback_data="rub/usd")
    btn69 = types.InlineKeyboardButton('RUB/EUR', callback_data="rub/eur")
    markup12.add(btn56, btn57, btn58, btn59, btn60, btn61, btn62, btn63, btn64, btn65, btn66, btn67, btn68, btn69)
    await bot.send_message(call.message.chat.id, "Выберите пару валют, которую вы хотите назначить избранной <i>(она будет использоваться по умолчанию при конвертации).</i>", reply_markup=markup12, parse_mode=types.ParseMode.HTML)

@dp.callback_query_handler(lambda call: call.data in ["usd/eur", "eur/usd", "usd/gbp", "gbp/usd", "cny/usd", "usd/cny", "sek/usd", "usd/sek", "cad/eur", "eur/cad", "jpy/cad", "usd/jpy", "rub/usd", "rub/eur"])
async def save(call: types.CallbackQuery):
    global id, fav
    id = call.message.from_user.id
    fav = {"user_id":id,"favourite":call.data}  # Сохраняем выбранную валютную пару
    await bot.send_message(call.message.chat.id, f"Параметры сохранены. Вы выбрали: {fav['favourite'].upper()}. Чтобы удалить избранную пару валют введите /delete")

@dp.message_handler(commands=["delete"])
async def delete(message: types.Message):
    fav.pop("favourite")
    await message.answer("Удаление прошло успешно.")


"""общий хендлер - ловит любое сообщение"""


@dp.message_handler()
async def summa(message: types.Message):
    try:
        global user_id, amount, peremen, fav, values
        user_id = message.from_user.id
        amount = int(message.text.strip())
        peremen = {"id": user_id, "sum": amount}
        if amount <= 0:
            raise TypeError("The argument cannot be equal to zero.")
        if fav.get("favourite") != None:
            values = fav.get("favourite").upper().split("/")
            res = currency.convert(peremen["sum"], values[0], values[1])
            await message.answer(f"<b>Получается: <u>{round(res, 2)}</u>. Можете заново вписать новое значение.</b>",
                                 parse_mode=types.ParseMode.HTML)
        else:
            markup5 = types.InlineKeyboardMarkup(row_width=3)
            btn1 = types.InlineKeyboardButton("USD/EUR", callback_data="USD/EUR")
            btn2 = types.InlineKeyboardButton("EUR/USD", callback_data="EUR/USD")
            btn3 = types.InlineKeyboardButton("USD/GBP", callback_data="USD/GBP")
            btn4 = types.InlineKeyboardButton("GBP/USD", callback_data="GBP/USD")
            btn5 = types.InlineKeyboardButton("CNY/USD", callback_data="CNY/USD")
            btn6 = types.InlineKeyboardButton("USD/CNY", callback_data="USD/CNY")
            btn7 = types.InlineKeyboardButton("SEK/USD", callback_data="SEK/USD")
            btn8 = types.InlineKeyboardButton("USD/SEK", callback_data="USD/SEK")
            btn9 = types.InlineKeyboardButton("CAD/EUR", callback_data="CAD/EUR")
            btn10 = types.InlineKeyboardButton("EUR/CAD", callback_data="EUR/CAD")
            btn11 = types.InlineKeyboardButton("JPY/CAD", callback_data="JPY/CAD")
            btn12 = types.InlineKeyboardButton("USD/JPY", callback_data="USD/JPY")
            btn13 = types.InlineKeyboardButton('RUB/USD', callback_data="RUB/USD")
            btn14 = types.InlineKeyboardButton('RUB/EUR', callback_data="RUB/EUR")
            markup5.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14)
            await message.answer("Выберите пару интересующих Вас валют.", reply_markup=markup5)

    except ValueError:
        await message.answer("Введите данные в корректном формате.")
    except TypeError as e:
        await message.answer("Введите число больше нуля.")




@dp.callback_query_handler(lambda call: True)
async def callback(call: types.CallbackQuery):
    global fav, peremen
    if call.data != "else":
        values = call.data.upper().split("/")
        res = currency.convert(peremen["sum"], values[0], values[1])
        await bot.send_message(call.message.chat.id, f"<b>Получается: <u>{round(res, 2)}</u>. Можете заново вписать новое значение.</b>", parse_mode=types.ParseMode.HTML)

executor.start_polling(dp, skip_updates=True)
