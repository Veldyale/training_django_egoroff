from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'my_list': [],
    }
    return render(request, 'horoscope/horoscope.html', context=data)


def get_info_about_zodiac_sign_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    else:
        name_zodiac = zodiacs[sign_zodiac - 1]
        redirect_url = reverse('horoscope-name', args=[name_zodiac])
        return HttpResponseRedirect(redirect_url)
