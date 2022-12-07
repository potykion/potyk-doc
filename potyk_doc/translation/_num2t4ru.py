"""
Ru translation of numbers
Source:
https://github.com/seriyps/ru_number_to_text
"""

from typing import List, Tuple

units = (
    u"ноль",
    (u"один", u"одна"),
    (u"два", u"две"),
    u"три",
    u"четыре",
    u"пять",
    u"шесть",
    u"семь",
    u"восемь",
    u"девять",
)

teens = (
    u"десять",
    u"одиннадцать",
    u"двенадцать",
    u"тринадцать",
    u"четырнадцать",
    u"пятнадцать",
    u"шестнадцать",
    u"семнадцать",
    u"восемнадцать",
    u"девятнадцать",
)

tens = (
    teens,
    u"двадцать",
    u"тридцать",
    u"сорок",
    u"пятьдесят",
    u"шестьдесят",
    u"семьдесят",
    u"восемьдесят",
    u"девяносто",
)

hundreds = (
    u"сто",
    u"двести",
    u"триста",
    u"четыреста",
    u"пятьсот",
    u"шестьсот",
    u"семьсот",
    u"восемьсот",
    u"девятьсот",
)

orders = (
    ((u"", u"", u""), "m"),
    ((u"тысяча", u"тысячи", u"тысяч"), "f"),
    ((u"миллион", u"миллиона", u"миллионов"), "m"),
    ((u"миллиард", u"миллиарда", u"миллиардов"), "m"),
)

minus = u"минус"


def num2text(num: int) -> str:
    """
    http://ru.wikipedia.org/wiki/Gettext#.D0.9C.D0.BD.D0.BE.D0.B6.D0.B5.D1.81.\
    D1.82.D0.B2.D0.B5.D0.BD.D0.BD.D1.8B.D0.B5_.D1.87.D0.B8.D1.81.D0.BB.D0.B0_2
    """
    if num == 0:
        return " ".join((units[0], orders[0][0][2])).strip()  # ноль

    rest = abs(num)
    ord = 0
    name = []
    while rest > 0:
        plural, nme = thousand(rest % 1000, orders[ord][1])
        if nme or ord == 0:
            name.append(orders[ord][0][plural])
        name += nme
        rest = int(rest / 1000)
        ord += 1
    if num < 0:
        name.append(minus)
    name.reverse()
    return " ".join(name).strip()


def thousand(rest: int, sex: str) -> Tuple[int, List[str]]:  # pylint: disable=too-complex
    """Converts numbers from 19 to 999"""
    prev = 0
    plural = 2
    name = []
    use_teens = 10 <= rest % 100 <= 19

    data: List[Tuple[Tuple, int]]
    if use_teens:
        data = [(teens, 10), (hundreds, 1000)]
    else:
        data = [(units, 10), (tens, 100), (hundreds, 1000)]

    for names, x in data:
        cur = int(((rest - prev) % x) * 10 / x)
        prev = rest % x
        if x == 10 and use_teens:
            plural = 2
            name.append(teens[cur])
        elif cur == 0:
            continue
        elif x == 10:
            name_ = names[cur]
            if isinstance(name_, tuple):
                name_ = name_[0 if sex == "m" else 1]
            name.append(name_)
            if 2 <= cur <= 4:
                plural = 1
            elif cur == 1:
                plural = 0
            else:
                plural = 2
        else:
            name.append(names[cur - 1])
    return plural, name
