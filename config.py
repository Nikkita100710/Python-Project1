
TOKEN_BOT = "6657765382:AAFd5oh9TeiXbJ9KOZwwyJxnloeo1Podvj0"
TOKEN = "6657765382:AAFd5oh9TeiXbJ9KOZwwyJxnloeo1Podvj0"

# UKRAINIAN_ALPHABET = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя0123456789, .!?:;-\"\'()[]{}<>'
UKRAINIAN_ALPHABET = 'АФїПЦ0в;оЬзл<6Х{тЇґь!ЧТЛ?73:О8НИЮЕуюЖЗч4аДЯжШІ]нибпшЩ9іц[Кмр2едг}5,Б(УЙ1>ГРщМсЄ-хйҐВкє.яСф)'


presentation_text = """
Презентація програми Цезар Бот 🇺🇦

✅<b>Вступ</b>

Ласкаво просимо на презентацію програми "Цезар Бот"! Ця програма була розроблена з використанням Python, однієї з найпопулярніших мов програмування у світі. Вона використовує бібліотеку aiogram для створення бота в Telegram, який може кодувати та декодувати текст за допомогою алгоритму Цезаря. Ми обрали aiogram, тому що це одна з бібліотек, яку ми вивчаємо, але є і інші бібліотеки, такі як python-telegram-bot, telebot та інші.

✅<b>Алгоритми</b>

<b>Шифр Цезаря (Сифр Цезаря):</b> Цей метод зсуває кожну літеру на фіксовану кількість позицій у алфавіті. Наприклад, зсув на 3 позиції зробить "A" як "D". Цей метод дуже простий і легко розшифровується методом перебору.

<b>ROT13:</b> Цей шифр є частковим випадком шифру Цезаря, де зсув становить 13 позицій. Він часто використовується для приховування тексту, але також не має високого рівня захисту.

<b>Шифр підстановки (Субституційний шифр):</b> У цьому методі кожна літера замінюється іншою літерою або символом. Він може бути більш складним, якщо використовується випадкова перестановка.

<b>Шифр Віженера (Віженера шифр):</b> Цей метод шифрування використовує ключове слово для циклічного зсуву літер у повідомленні. Він складніший, ніж шифр Цезаря.

<b>Подвійний шифр Цезаря (Подвійний Цезаревий шифр):</b> Це покращена версія шифру Цезаря, де кожна літера зсувається на два різних значення, зазвичай з різними ключами.

<b>Шифр Атбаш (Атбаш шифр):</b> Цей метод замінює літери на протилежні в алфавіті. Наприклад, "A" стає "Z". Ефективний лише для алфавітних символів.

<b>Шифр транспозиції (Транспозиційний шифр):</b> У цьому методі символи в повідомленні переставляються у визначеному порядку. Це не змінює символи, але робить текст більш складним для читання.

<b>Шифр Вернама (Вернам шифр або Одноразова Подушка):</b> Вважається одним з найнадійніших методів шифрування. Кожен символ кодується за допомогою випадкового ключа такої ж довжини. Проте ключі повинні бути дійсно випадковими і використовуватися лише один раз.

<b>Шифр RSA:</b> Цей метод використовує пару ключів, публічний і приватний, для шифрування і розшифрування повідомлень. Він базується на складних математичних алгоритмах і є одним із найбільш надійних методів шифрування в сучасному світі.

<b>Шифр Енігма (Енігма шифр):</b> Цей шифр був використаний німецькою армією під час Другої світової війни. Він складався з багатьох обертових дисків і був дуже складним для розшифрування, поки англійські криптографи не змогли його взламати.

✅<b>Як працює програма?</b>

Програма починається з імпорту необхідних бібліотек та встановлення токена бота. Потім вона ініціалізує бота та диспетчера, а також встановлює промежуточне програмне забезпечення для логування.

Програма пропонує користувачеві дві кнопки: "CODE" та "DECODE". При натисканні на кнопку "CODE", програма просить користувача ввести текст для кодування. Потім вона генерує випадковий ключ від 1 до 30 та зсуває кожну букву вхідного тексту на кількість позицій, рівну цьому ключу, в алфавіті. Результатом є закодований текст.

При натисканні на кнопку "DECODE", програма просить користувача ввести ключ та зашифрований текст. Потім вона зсуває кожну букву зашифрованого тексту назад на кількість позицій, рівну ключу, щоб отримати початковий текст.

Однак програма також вміє кодувати та декодувати текст без використання кнопок. Якщо користувач вводить текст, який не починається з числа не більше 30, програма автоматично кодує його. Це робить використання програми ще простішим та зручним!

✅<b>Заключення</b>

Цезар Бот - це цікавий проект, який демонструє застосування алгоритму Цезаря у реальному програмному продуктови. Вона показують, як можна використовувати Python та aiogram для створення корисних та інтерактивних ботів в Telegram. Дякую за вашу увагу! Якщо у вас є питання, я буду радий на них відповісти.
"""

about_ = """  Цей бот створений для шифрування та розшифрування за допомогою шифру Цезаря. Він кодує символи українського алфавіту, цифри та спеціальні символи. Всі інші символи залишаються без змін - не кодуються.

✅ ШИФРУВАННЯ:
 Натисніть кнопку CODE < i введіть текст> для перекладу. Бот вибере випадковий ключ, закодує повідомлення згідно абетки та виведе вам текст та ключ.\n
 Можна вводити код безпосередньо в рядок введення - він зашифрується, якщо перше слово не є числом від 1 до 30

✅ РОЗШИФРУВАННЯ:
 Натисніть кнопку DECODE <ключ і закодований текст>. Бот розшифрує повідомлення та виведе вам результат.
 Можна вводити код для розшифрування безпосередньо в рядок введення - він розшифрується, якщо перше число від 1 до 30

Розроблено:
 Нікіта Бойко та Микита Каданцев

/help - Вивести список команд"""

commands = [
    "/start - Почати бота",
    "/help - Вивести список команд",
    "/about - Інформація про бота",
    "/presentation - Презентація програми\n",
    "Кнопки:",
    "🔐 CODE < текст > - Зашифрувати текст за допомогою щифру Цезаря",
    "🔓 DECODE < ключ > < текст > - Розшифрувати текст за допомогою шифру Цезаря",
    "ℹ️ About - Інформація про бота",
    "🆘 Help - Вивести список команд",
    "🐍 Presentation< - Презентация программы"
]
