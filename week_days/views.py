from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

days_dict = {
    "monday": "Понедельник",
    "tuesday": "Вторник",
    "wednesday": "Среда",
    "thursday": "Четверг",
    "friday": "Пятница",
    "saturday": "Суббота",
    "sunday": "Воскресенье"
}

def main(request):
    return render(request, 'week_days/greeting.html')


def todo_week_days(request, day: str):
    day_in_rus = days_dict.get(day)
    if day_in_rus:
        return HttpResponse(day_in_rus)
    else:
        return HttpResponseNotFound(f'Неверный день недели - {day}')


def todo_week_days_number(request, day: int):
    numbers = list(days_dict)
    if day > len(numbers):
        return HttpResponseNotFound(f'Неверный день недели - {day}')
    else:
        name_day_in_rus = numbers[day - 1]
        redirect_url = reverse('todo_week_day_str', args=[name_day_in_rus])
        return HttpResponseRedirect(redirect_url)