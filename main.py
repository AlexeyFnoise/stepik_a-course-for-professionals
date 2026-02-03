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

# Функция convert()
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

# Схожие слова 🌶️
list_vow = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
pattern = [i for i, c in enumerate(input()) if c in list_vow]
for _ in range(int(input())):
    word = input()
    if [i for i, c in enumerate(word) if c in list_vow] == pattern: print(word)

# Корпоративная почта 🌶️
digits = '0123456789'
names = []
for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)
for _ in range(int(input())):
    name =  input()
    counter = 0
    while name in names:
        counter += 1
        name = name.rstrip(digits) + str(counter)
    names.append(name)
    print(f'{name}@beegeek.bzz')

# Файлы в файле 🌶️🌶️
d = {}
d_units = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
d_units_trans = {1: 'B', 2: 'KB', 3: 'MB', 4: 'GB'}
def converter(x):
    s = 1024
    for i in range(1, 5):
        if x > s: x /= s
        else: break
    return str(round(x)), d_units_trans[i]

with open('files.txt', encoding='utf-8') as file:
    for line in file:
        name_full, size, unit = line.split()
        name, f_ext = name_full.split('.')
        d.setdefault(f_ext, []).append((name, int(size) * d_units[unit]))
    for k in sorted(d):
        total = 0
        for i in sorted(d[k]):
            print(i[0] + '.' + k)
            total += i[1]
        print('----------')
        print('Summary:', *converter(total))
        print()

# Работа с датой
from datetime import date
dates = [date(2010, 9, 28), date(2017, 1, 13),
         date(2009, 12, 25), date(2010, 2, 27),
         date(2021, 10, 11), date(2020, 3, 13),
         date(2000, 7, 7), date(1999, 4, 14),
         date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]
for x in dates:
    print(f'{x.year}-Q{(x.month + 2) // 3}')

# Функция get_date_range()
from datetime import date
def get_date_range(date1, date2):
    if date1 > date2: return []
    else: return [date.fromordinal(i) for i in range(date1.toordinal(), date2.toordinal() + 1)]

# Функция saturdays_between_two_dates()
from datetime import date
def saturdays_between_two_dates(start, end):
    if start < end: return len([date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1) if date.fromordinal(i).weekday() == 5])
    else: return len([date.fromordinal(i) for i in range(end.toordinal(), start.toordinal() + 1) if date.fromordinal(i).weekday() == 5])

# Две даты
year1, moth1, day1 = input().split('-')
year2, moth2, day2 = input().split('-')
dat1 = date(int(year1), int(moth1), int(day1))
dat2 = date(int(year2), int(moth2), int(day2))
if dat1 < dat2: print(dat1.strftime('%d-%m (%Y)'))
else: print(dat2.strftime('%d-%m (%Y)'))

# Отсортированные даты
dates = [date.fromisoformat(input()) for _ in range(int(input()))]
for i in sorted(dates):
    print(i.strftime('%d/%m/%Y'))

# Функция print_good_dates()
def print_good_dates(ls):
    for i in sorted(filter(lambda i: i.year == 1992 and i.month + i.day == 29, ls)):
        print(i.strftime('%B %d, %Y'))
dates = [date(1992, 10, 19), date(1991, 12, 6),
         date(1992, 9, 20)]
print_good_dates(dates)

# Функция get_min_max()
from datetime import date
def get_min_max(ls = list):
    if ls: return (min(ls), max(ls))
    else: return ()
dates = [date(2021, 10, 5), date(1992, 6, 10),
         date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))

# Функция is_correct()
def is_correct(day, month, year):
    try:
        my_date = date(int(year), int(month), int(day))
        print(True)
    except ValueError:
        print(False)

# Корректные даты
def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except ValueError:
        return False
count = 0
x_date = input()
while x_date != 'end':
    day, month, year = x_date.split('.')
    if is_correct(int(day), int(month), int(year)):
        count += 1
        print('Корректная')
    else: print('Некорректная')
    x_date = input()
print(count)


data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
pattern = '%H:%M'
result = 0
for el in data:
    result+= int((datetime.strptime(el[1], pattern) - datetime.strptime(el[0], pattern)).seconds / 60)
print(result)

# Пятница 13-е
days = {
    0: 0,  # понедельник
    1: 0,  # вторник
    2: 0,  # среда
    3: 0,  # четверг
    4: 0,  # пятница
    5: 0,  # суббота
    6: 0   # воскресенье
}
start = datetime(1, 1, 1)
end = datetime(9999, 12, 31)
current = start
for i in range(1, (end - start).days):
    day_of_week = current.weekday()
    if current.day == 13:
        days[day_of_week] +=1
    current += timedelta(days=1)
for el in days: print(days[el])

time_work = {1: [9, 21],
             2: [10, 18]}
pattern_day_time = '%d.%m.%Y %H:%M'
pattern_only_time = '%H:%M'
dt = datetime.strptime(input(), pattern_day_time)
if dt.weekday() in range(0, 4):
    if dt.time() < time(hour=time_work[1][0]) or dt.time() > time(time_work[1][1]):
        print('Магазин не работает')
    else:
        print(int(abs(timedelta(hours=dt.hour, minutes=dt.minute) - timedelta(hours=time_work[0][1])).seconds / 60))
if dt.weekday() in [5, 6]:
    if dt.time() < time(hour=time_work[2][0]) or dt.time() > time(time_work[2][1]):
        prnt('Магазин не работает')
    else:
        print(int(abs(timedelta(hours=dt.hour, minutes=dt.minute) - timedelta(hours=time_work[2][1])).seconds / 60)

staff_dates = {}
res = 0
for i in range(int(input())):
    name, first_name, dt = input().split()
    staff_dates.setdefault(datetime.strptime(dt, '%d.%m.%Y'), (name, first_name))
    res += 1
if len(staff_dates) == res:
    mx = min(staff_dates.keys())
    print(f'{mx.date().strftime('%d.%m.%Y')} {staff_dates[mx][0]} {staff_dates[mx][1]}')
else:
    print(min(staff_dates.keys()).date().strftime('%d.%m.%Y'), res - len(staff_dates) + 1)

def choose_plural(amout, word):
    if amout % 10 == 1 and amout % 100 != 11: return word[0]
    elif 2 <= amout % 10 <= 4 and not 12 <= amout % 100 <= 14: return word[1]
    else: return word[2]
plural_dict = {'day': ("день", "дня", "дней"),
               'hour': ("час", "часа", "часов"),
               'minute': ("минута", "минуты", "минут")}
date_const = datetime(day=8, month=11, year=2022, hour=12)
date_reliese = datetime.strptime(input(), '%d.%m.%Y %H:%M')
result ='До выхода курса осталось: '
print(date_const - date_reliese)
current_dat = date_const - date_reliese
if date_reliese < date_const:
    if current_dat.days != 0 and (current_dat.seconds // 60) % 60 != 0:
        print(f'{result}{current_dat.days} {choose_plural(current_dat.days, plural_dict['day'])} и '
              f'{current_dat.seconds // 3600} {choose_plural(current_dat.seconds // 3600, plural_dict['hour'])} ')
    elif current_dat.days != 0 and (current_dat.seconds // 60) % 60 == 0:
        print(f'{result}{current_dat.days} {choose_plural(current_dat.days, plural_dict['day'])}')
    elif current_dat.days == 0:
        if (current_dat.seconds // 60) % 60 != 0 and current_dat.seconds // 3600 != 0:
            print(f'{result}{current_dat.seconds // 3600} {choose_plural(current_dat.seconds // 3600, plural_dict['hour'])} и '
                  f'{(current_dat.seconds // 60) % 60} {choose_plural((current_dat.seconds // 60) % 60, plural_dict['minute'])}')
        elif current_dat.seconds // 3600 == 0:
            print(f'{result}{(current_dat.seconds // 60) % 60} {choose_plural((current_dat.seconds // 60) % 60, plural_dict['minute'])}')
        elif (current_dat.seconds // 60) % 60 == 0:
            print(f'{result}{current_dat.seconds // 3600} {choose_plural(current_dat.seconds // 3600, plural_dict['hour'])} ')
else: print('Курс уже вышел!')

import calendar, datetime
year = int(input())
for month in range(1, 13):
    cnt = 0
    for week in calendar.monthcalendar(year, month):
        thursday = week[3]
        if thursday:
            cnt += 1
            if cnt == 3:
                print(datetime.date(year=year, month=month, day=thursday).strftime('%d.%m.%Y'))
