# "Поколение Python": курс для профессионалов
#Функция hide_card()
def hide_card(card_number):
    return 12 * '*' + card_number.replace(' ', '')[-4:]

# Функция same_parity()
def same_parity(numbers):
    return [i for i in numbers if i % 2 == numbers[0] % 2]

# Функция is_valid()
def is_valid(string):
    return string.isdigit() and 4 <= len(string) <= 6

# Функция print_given()
def print_given(*args, **kwargs):
    for i in args: print(i, type(i))
    for key, name in sorted(kwargs.items()): print(key, name, type(name))

Функция convert()
def convert(text):
    lcount = 0
    uccount = 0
    for i in text:
        if i.isupper(): uccount += 1
        elif i.islower(): lcount += 1
    return text.upper() if uccount > lcount else text.lower()

# Функция filter_anagrams()
def filter_anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]

# Функция likes()
def likes(names):
    if len(names) == 0: return 'Никто не оценил данную запись'
    elif len(names) == 1: return f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2: return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3: return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else: return f'{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись'

# Функция index_of_nearest()
def index_of_nearest(numbers, number):
    if numbers:
        min_number = min(numbers, key=lambda x: abs(number - x))
        return min_number.index(min_number)
    else:
        return -1

# Функция spell()
def spell(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result

# Функция choose_plural() 🌶️🌶️
def choose_plural(amout, declensions):
    if amout % 10 == 1 and amout % 100 != 11: return f'{amout} {declensions[0]}'
    elif 2 <= amout % 10 <= 4 and not 12 <= amout % 100 <= 14: return f'{amout} {declensions[1]}'
    else: return f'{amout} {declensions[2]}'

# Функция get_biggest():
def get_biggest(numbers):
    if numbers:
        s = ""
        max_len_num = len(str(max(numbers)))
        numbers = sorted([str(i) for i in numbers], reverse=True, key=lambda x: x * max_len_num)
        return int(s.join(numbers))
    return -1

# Тимур, Артур и новый курс
d1, d2, d3 = [int(input()) for _ in range(3)]
print(min(d1 + d2 + d3, d1 + d1 + d2 + d2, d2 + d3 + d3 + d2, d1 + d3 + d3 + d1))

# Схожие буквы
langs = ['ru', 'mix', 'mix', 'en']
eng = 'AaBCcEeHKMOoPpTXxy'
index = sum([input() in eng for i in range(3)])
print(langs[index])

# Переворатор
n, x, y, a, b = [int(i) for i in input().split()]
numbers = list(range(1, n + 1))
numbers[x - 1:y] = numbers[x - 1:y][::-1]
numbers[a - 1:b] = numbers[a - 1:b][::-1]
print(*numbers)

# Более одного
numbers = [int(i) for i in input().split()]
print(*sorted(filter(lambda x: numbers.count(x) > 1, set(numbers))))
from unicodedata import digit

# Максимальная группа
n = int(input())
numbers = range(1, n + 1)
d = dict()
for num in numbers:
    sum_num = sum([int(digit) for digit in str(num)])
    d.setdefault(sum_num, []).append(num)
print(max(map(len, d.values())))

# Трудности перевода
n = int(input())
lang = set(input().split(', '))
for i in range(n - 1): lang &= set(input().split(', '))
if lang: print(*sorted(lang), sep=', ')
else: print('Сериал снять не удастся')