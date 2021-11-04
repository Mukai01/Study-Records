from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
    send_mail(
        'タイトル',
        '本文.',
        'xxx@gmail.com',
        ['xxx@gmail.com'],
        fail_silently = False
    )
    return HttpResponse('')