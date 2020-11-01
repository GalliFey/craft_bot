import telebot
from telebot import types


bot = telebot.TeleBot('1480297713:AAH0tCm4Vt0FqlbSX30kv2Fenn-n8H9D1G8')


@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Напишите то что вы хотите создать ?")
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('Правила крафта')
    keyboard.row('Пища', 'Оружие')
    keyboard.row('Строительные блоки', 'Декоративные блоки')
    keyboard.row('Механизмы', 'Инструменты')
    keyboard.row('Разное')
    bot.send_message(m.chat.id, 'В ином случае выберите '
                     'в меню основные крафты!',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def craft(m):
    if m.text.lower() == 'главное меню':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Правила крафта')
        keyboard.row('Пища', 'Оружие')
        keyboard.row('Строительные блоки', 'Декоративные блоки')
        keyboard.row('Механизмы', 'Инструменты')
        keyboard.row('Разное')
        bot.send_message(m.chat.id, 'выберите в '
                         'меню основные крафты!',
                         reply_markup=keyboard)
    elif m.text.lower() == 'инструменты':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Топор', 'Кирка', 'Лопата')
        keyboard.row('Мотыга', 'Компас', 'Удочка')
        keyboard.row('Часы', 'Ножницы')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'пища':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Хлеб')
        keyboard.row('Тушенные грибы', 'Тыквенный пирог')
        keyboard.row('Торт', 'Суп', 'Печенье')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'оружие':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Лук', 'Стрела', 'Арбалет')
        keyboard.row('Меч', 'Щит', 'Шлем')
        keyboard.row('Нагрудник', 'Поножи', 'Ботинки')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'строительные блоки':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Доски', 'Стекло', 'Плита')
        keyboard.row('Шерсть', 'Каменный кирпич')
        keyboard.row('Книжная полка', 'Светильник Джека')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'механизмы':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Поршень', 'Динамит')
        keyboard.row('Рычаг', 'Люк', 'Факел')
        keyboard.row('Калитка', 'Крюк', 'Дверь')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'декоративные блоки':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('Сундук', 'Верстак', 'Печь')
        keyboard.row('Забор', 'Прутья', 'кровать')
        keyboard.row('Наковальня')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'разное':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('палка', 'Ведро')
        keyboard.row('Бумага', 'миска')
        keyboard.row('Семена', 'Чистая карта')
        keyboard.row('Главное меню')
        bot.send_message(m.chat.id, 'Выберите нужный крафт',
                         reply_markup=keyboard)

    elif m.text.lower() == 'правила крафта':
        bot.send_message(m.chat.id, 'Процесс крафта предметов осуществляется'
                         ' с помощью сетки крафта в инвентаре или на верстаке.'
                         ' Сетка крафта в инвентаре необходимана '
                         'начальном этапе'
                         ' игры для того, чтобы вы могли создать верстак. '
                         'Также вы'
                         'можете использовать ее для быстрого крафта предметов'
                         ', например,'
                         ' палок и досок.')

    elif m.text.lower() == 'верстак':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp''-content/uploads/2011/07/ReceptKraft-4.png')
        bot.send_message(m.chat.id, '4 x Дубовые доски')
    elif m.text.lower() == 'доски':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-197.png')
        bot.send_message(m.chat.id, '1 x Дубовое бревно')
    elif m.text.lower() == 'палка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-5.png')
        bot.send_message(m.chat.id, '2 x Дубовые доски')
    elif m.text.lower() == 'факел':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-6.png')
        bot.send_message(m.chat.id, '1 x Уголь\n1 x Палка')
    elif m.text.lower() == 'сундук':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-8.png')
        bot.send_message(m.chat.id, '8 x Дубовые доски')
    elif m.text.lower() == 'печь':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-7.png')
        bot.send_message(m.chat.id, '8 x Булыжник')
    elif m.text.lower() == 'стол зачарования':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-10.png')
        bot.send_message(m.chat.id, '4 x Обсидиан\n2 x Алмаз\n1 x Книга')
    elif m.text.lower() == 'шерсть':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-18.png')
        bot.send_message(m.chat.id, 'Шерсть собирается с овец при помощи '
                         'ножниц или же ее можно скрафтить и'
                         'з нитей.\n4 x Нить')
    elif m.text.lower() == 'динамит':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-33.png')
        bot.send_message(m.chat.id, '4 x Песок\n5 x Порох')
    elif m.text.lower() == 'плита':
        bot.send_message(m.chat.id, 'Скрафтить плиту в Minecraft '
                         'можно из дерева, камня, кирпича, п'
                         'еска и булыжника.')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-35.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-34.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-37.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-40.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-41.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru'
                       '/wp-content/uploads/2011/07/ReceptKraft-39.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-36.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-38.png')
        bot.send_message(m.chat.id, '3 x N')
    elif m.text.lower() == 'ступеньки':
        bot.send_message(m.chat.id, 'Скрафтить ступеньки в Minecraft'
                         ' можно из дерева, камня, кирпича, песк'
                         'а и булыжника.')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-45.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-48.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-44.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-47.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-46.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-43.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-42.png')
        bot.send_message(m.chat.id, '6 x N')
    elif m.text.lower() == 'книжная полка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-55.png')
        bot.send_message(m.chat.id, '6 x Дубовые доски\n3 x Книга')
    elif m.text.lower() == 'светильник джека':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-63.png')
        bot.send_message(m.chat.id, '1 x Факел\n1 x Вырезанная тыква')
    elif m.text.lower() == 'лопата':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-74.png')
        bot.send_message(m.chat.id, '1 x Доски\n2 x Палка')
    elif m.text.lower() == 'каменная лопата':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-77.png')
        bot.send_message(m.chat.id, '1 x Булыжник\n2 x Палка')
    elif m.text.lower() == 'железная лопата':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-76.png')
        bot.send_message(m.chat.id, '1 x Железный слито\n2 x Палка')
    elif m.text.lower() == 'золотая лопата':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-75.png')
        bot.send_message(m.chat.id, '1 x Золотой слиток\n2 x Палка')
    elif m.text.lower() == 'алмазная лопата':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-73.png')
        bot.send_message(m.chat.id, '1 x Алмаз\n2 x Палка')
    elif m.text.lower() == 'кирка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-68.png')
        bot.send_message(m.chat.id, '3 x Дубовые доски\n2 x Палка')
    elif m.text.lower() == 'железная кирка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-72.png')
        bot.send_message(m.chat.id, '3 x Железная руда\n2 x Палка')
    elif m.text.lower() == 'каменная кирка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-77.png')
        bot.send_message(m.chat.id, '3 x Булыжник\n2 x Палка')
    elif m.text.lower() == 'золотая кирка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-71.png')
        bot.send_message(m.chat.id, '3 x Золотой слиток\n2 x Палка')
    elif m.text.lower() == 'алмазная кирка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-69.png')
        bot.send_message(m.chat.id, '3 x Алмаз\n2 x Палка')
    elif m.text.lower() == 'топор':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-66.png')
        bot.send_message(m.chat.id, '3 x Дубовые доски\n2 x Палка')
    elif m.text.lower() == 'каменный топор':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-57.png')
        bot.send_message(m.chat.id, '3 x Булыжник\n2 x Палка')
    elif m.text.lower() == 'железный топор':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-72.png')
        bot.send_message(m.chat.id, '3 x Железная руда\n2 x Палка')
    elif m.text.lower() == 'золотой топор':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-67.png')
        bot.send_message(m.chat.id, '3 x Золотой слиток\n2 x Палка')
    elif m.text.lower() == 'алмазный топор':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-64.png')
        bot.send_message(m.chat.id, '3 x Алмаз\n2 x Палка')
    elif m.text.lower() == 'мотыга':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-79.png')
        bot.send_message(m.chat.id, '2 x Дубовые доски\n2 x Палка')
    elif m.text.lower() == 'каменная мотыга':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-81.png')
        bot.send_message(m.chat.id, '2 x Булыжник\n2 x Палка')
    elif m.text.lower() == 'железная мотыга':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-78.png')
        bot.send_message(m.chat.id, '2 x Железная руда\n2 x Палка')
    elif m.text.lower() == 'золотая мотыга':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-80.png')
        bot.send_message(m.chat.id, '2 x Золотой слиток\n2 x Палка')
    elif m.text.lower() == 'алмазная мотыга':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-82.png')
        bot.send_message(m.chat.id, '2 x Алмаз\n2 x Палка')
    elif m.text.lower() == 'ведро':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-85.png')
        bot.send_message(m.chat.id, '3 x Железная руда')
    elif m.text.lower() == 'огниво':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-83.png')
        bot.send_message(m.chat.id, '1 x Железный слиток\n1 x Кремень')
    elif m.text.lower() == 'карта':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-87.png')
        bot.send_message(m.chat.id, '8 x Бумага\n1 x Компас')
    elif m.text.lower() == 'компас':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-86.png')
        bot.send_message(m.chat.id, '4 x Железный слиток\n1 x Редстоун')
    elif m.text.lower() == 'часы':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-88.png')
        bot.send_message(m.chat.id, '4 x Золотой слиток\n1 x Редстоун')
    elif m.text.lower() == 'ножницы':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-84.png')
        bot.send_message(m.chat.id, '2 x Железный слиток')
    elif m.text.lower() == 'удочка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-89.png')
        bot.send_message(m.chat.id, '3 x Палка\n2 x Нить')
    elif m.text.lower() == 'наковальня':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-11.png')
        bot.send_message(m.chat.id, '3 x Железный блок\n4 x Железный слиток')
    elif m.text.lower() == 'меч':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-93.png')
        bot.send_message(m.chat.id, '2 x Дубовые доски\n1 x Палка')
    elif m.text.lower() == 'каменный меч':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-91.png')
        bot.send_message(m.chat.id, '2 x Булыжник\n1 x Палка')
    elif m.text.lower() == 'железный меч':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-92.png')
        bot.send_message(m.chat.id, '2 x Железный слиток\n1 x Палка')
    elif m.text.lower() == 'золотой меч':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-95.png')
        bot.send_message(m.chat.id, '2 x Золотой слиток\n1 x Палка')
    elif m.text.lower() == 'алмазный меч':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-94.png')
        bot.send_message(m.chat.id, '2 x Алмаз\n1 x Палка')
    elif m.text.lower() == 'лук':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru'
                       'wp-content/uploads/2011/07/ReceptKraft-96.png')
        bot.send_message(m.chat.id, '3 x Палка\n3 x Нить')
    elif m.text.lower() == 'шлем':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-99.png')
        bot.send_message(m.chat.id, '5 х кожа')
    elif m.text.lower() == 'нагрудник':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-106.png')
        bot.send_message(m.chat.id, '8 х кожа')
    elif m.text.lower() == 'поножи':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-108.png')
        bot.send_message(m.chat.id, '7 х кожа')
    elif m.text.lower() == 'ботинки':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-113.png')
        bot.send_message(m.chat.id, '4 х кожа')
    elif m.text.lower() == 'железная броня':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-115.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-107.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-115.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-115.png')

    elif m.text.lower() == 'золотая броня':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-101.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-105.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-112.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-116.png')

    elif m.text.lower() == 'алмазная броня':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-98.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-104.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-111.png')
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-117.png')

    elif m.text.lower() == 'рельсы':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-122.png')
        bot.send_message(m.chat.id, '6 x Железный слиток\n1 x Палка')
    elif m.text.lower() == 'энергорельсы':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/wp-'
                       'content/uploads/2011/07/ReceptKraft-123.png')
        bot.send_message(m.chat.id, '6 x Золотой слиток\n1 x '
                         'Палка\n1 x Редстоун')
    elif m.text.lower() == 'вагонетка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-118.png')
        bot.send_message(m.chat.id, '5 x Железный слиток')
    elif m.text.lower() == 'лодка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-125.png')
        bot.send_message(m.chat.id, '5 x Доски')
    elif m.text.lower() == 'дверь':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-127.png')
        bot.send_message(m.chat.id, '6 x доски')
    elif m.text.lower() == 'железная дверь':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-128.png')
        bot.send_message(m.chat.id, '6 x Железный слиток')
    elif m.text.lower() == 'люк':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-129.png')
        bot.send_message(m.chat.id, '6 x  доски')
    elif m.text.lower() == 'миска':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-148.png')
        bot.send_message(m.chat.id, '3 x Дубовые доски')
    elif m.text.lower() == 'хлеб':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-150.png')
        bot.send_message(m.chat.id, '3 x Пшеница')
    elif m.text.lower() == 'сахар':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-151.png')
        bot.send_message(m.chat.id, '1 х Сахарный тростник')
    elif m.text.lower() == 'печенье':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-153.png')
        bot.send_message(m.chat.id, '2 x Пшеница\n1 x сахар')
    elif m.text.lower() == 'тыквенный пирог':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-158.png')
        bot.send_message(m.chat.id, '1 x Тыква\n1 x Яйцо\n1 x Сахар')
    elif m.text.lower() == 'торт':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-152.png')
        bot.send_message(m.chat.id, '3 x Пшеница\n3 x Ведро молока\n1 x'
                         ' Яйцо\n2 x Сахар')
    elif m.text.lower() == 'бумага':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-162.png')
        bot.send_message(m.chat.id, '3 x Сахарный тростник')
    elif m.text.lower() == 'книга':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-163.png')
        bot.send_message(m.chat.id, '1 x Кожа\n3 x Бумага')
    elif m.text.lower() == 'картина':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-159.png')
        bot.send_message(m.chat.id, '1 x Белая шерсть\n8 x Палка')
    elif m.text.lower() == 'кровать':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-170.png')
        bot.send_message(m.chat.id, '3 x Дубовые доски\n3 x Белая шерсть')
    elif m.text.lower() == 'табличка':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/'
                       'wp-content/uploads/2011/07/ReceptKraft-160.png')
        bot.send_message(m.chat.id, '6 x Дубовые доски\n1 x Палка')
    elif m.text.lower() == 'рельсы':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/'
                       'posts/2011-09/1317410584_craftingminecarttracksio.png')
        bot.send_message(m.chat.id, '6 x Слиток железо\n1 x Палка')
    elif m.text.lower() == 'суп':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2016-09/1473365629_svekolnyy-sup.png')
        bot.send_message(m.chat.id, '1 x Миска\n6 x Свёкл')
    elif m.text.lower() == 'тушенные грибы':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2011-09/1317411186_craftingmushroomstewio.png')
        bot.send_message(m.chat.id, '1 x Коричневый гриб\n1 x Кр'
                         'асный гриб\n1 x Миска')
    elif m.text.lower() == 'стрела':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2011-09/1317248394_craftingarrowsio.png')
        bot.send_message(m.chat.id, '1 x Палка\n1 x Перо\n1 x Кремень')
    elif m.text.lower() == 'арбалет':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2019-04/1555988664_16.jpg')
        bot.send_message(m.chat.id, '1 x Крюк\n1 x Железный слито'
                         'к\n3 x Палка\n2 x Нить')
    elif m.text.lower() == 'щит':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2016-09/1473364788_schit.png')
        bot.send_message(m.chat.id, '6 x Дубовые доски\n1 x Железный слиток')
    elif m.text.lower() == 'каменный кирпич':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2016-09/1473362396_kamennyy-kirpich.jpg')
        bot.send_message(m.chat.id, '4 x Камень')
    elif m.text.lower() == 'стекло':
        bot.send_photo(m.chat.id, 'http://images.minecraft-book.ru/iblock'
                       '/2d1/2d114c8b6ce3b92a273b07fe0d311513.jpeg')
        bot.send_message(m.chat.id, '1 x Песок')
    elif m.text.lower() == 'калитка':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2011-10/1317542136_1316632611_smkll3awny.jpg')
        bot.send_message(m.chat.id, '2 x Дубовые доски\n4 x Палка')
    elif m.text.lower() == 'забор':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/wp-content/'
                       'uploads/2011/07/ReceptKraft-165.png')
        bot.send_message(m.chat.id, '4 x Дубовые доски\n2 x Палка')
    elif m.text.lower() == 'прутья':
        bot.send_photo(m.chat.id, 'https://minecraft-game.ru/wp-content/'
                       'uploads/2011/07/ReceptKraft-169.png')
        bot.send_message(m.chat.id, '6 x Железный слиток')
    elif m.text.lower() == 'поршень':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts'
                       '/2011-10/1317541034_41.jpg')
        bot.send_message(m.chat.id, '4 x Булыжник\n3 x Дубовые доски\n1 x'
                         ' Железный слиток\n1 x Редстоун')
    elif m.text.lower() == 'рычаг':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2011-09/1317411123_craftingleverio.png')
        bot.send_message(m.chat.id, '1 x Булыжник\n1 x Палка')
    elif m.text.lower() == 'крюк':
        bot.send_photo(m.chat.id, 'https://images.minecraft-book.ru/iblock/'
                       '565/56564a145387a4cdff728dc8e1fb2d37.jpeg')
        bot.send_message(m.chat.id, '1 x Дубовые доски\n1 x Железный слиток'
                         '\n1 x Палка')
    elif m.text.lower() == 'чистая карта':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/posts/'
                       '2016-09/1473361510_pustaya-karta.jpg')
        bot.send_message(m.chat.id, '8 x Бумага\n1 x Компас')
    elif m.text.lower() == 'семена':
        bot.send_photo(m.chat.id, 'https://ru-minecraft.ru/uploads/po'sts/201'
                       '7-05/1496090571_5a81e1b3a5d4577d7f20abff3de68dca.png')
    else:
        bot.send_message(m.chat.id, 'Такой крафт отсутсвует')


bot.polling(none_stop=True)
