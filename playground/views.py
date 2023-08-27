from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from django.core.mail import BadHeaderError


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name="emails/hello.html", context={"name": "Aashir"}
        )
        message.send(["john@gmail.com"])
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Mosh"})
