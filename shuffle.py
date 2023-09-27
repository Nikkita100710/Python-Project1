import random

# UKRAINIAN_ALPHABET = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя0123456789,.!?:;-()[]{}<>'
# UKRAINIAN_ALPHABET2 = '\"\''
UKRAINIAN_ALPHABET = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя0123456789,.!?:;-()[]{}<>'

numbers = list(range(1, len(UKRAINIAN_ALPHABET)))  # Создание списка чисел от 1 до 50
random.shuffle(numbers)  # Перемешивание списка

print(numbers)

ukr_alphabet_str = UKRAINIAN_ALPHABET[0]
for i in numbers:
    ukr_alphabet_str = ukr_alphabet_str + UKRAINIAN_ALPHABET[i]

# ukr_alphabet_str = ukr_alphabet_str + UKRAINIAN_ALPHABET2
print(UKRAINIAN_ALPHABET)
print(ukr_alphabet_str)
print(len(UKRAINIAN_ALPHABET))
print(len(ukr_alphabet_str))
