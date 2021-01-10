from django.core.mail import send_mail


def send_email(user_email):
    send_mail(
        subject="Подписка на сайт DjangoMovie",
        message="Вы подписались на рассылку с сайта DjangoMovie",
        from_email="iterex91@gmail.com",
        recipient_list=[user_email],
        fail_silently=False,
    )
