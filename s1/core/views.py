from django.http import HttpResponse


def home(request):
    html = "<h1>Добро пожаловать на мой сайт</h1>"
    html += "<a href='/about'>Обо мне</a>"
    return HttpResponse(html)


def about(request):
    html = "<h1>Обо мне</h1><p>Я - Надежда, изучаю веб-разработку на Python в GeekBrains.</p>"
    html += "<a href='/'>Вернуться на главную</a>"
    return HttpResponse(html)
