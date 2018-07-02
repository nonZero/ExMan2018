"""exman2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random
from django.contrib import admin
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.urls import path, re_path


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
        }

    # Django REST Framework (DRF)

def home(request):  # view function
    return JsonResponse({
        'status': "OK",
        'value': random.randint(1, 10),
    })
    # return HttpResponseBadRequest("Hello World!", "text/plain")
    # return HttpResponse("Hello World!", content_type="text/plain",
    # status=400)


def hello(request, name):
    return HttpResponse(f"Hello {name.title()}!")


def birthday(request, name, age):
    return HttpResponse(f"{name.title()} is {age} years old!")


# def plus(request, a, b):
#     return HttpResponse(f"<p>{a} + {b} = <b>{int(a) + int(b)}</b></p>")
#
def plus(request, a, b):
    return HttpResponse(f"<p>{a} + {b} = <b>{a + b}</b></p>")


urlpatterns = [
    re_path(r"^$", home),
    re_path(r"^hello/$", hello, kwargs={'name': "joe"}),
    re_path(r"^hellllllooooo/$", hello, kwargs={'name': "danny"}),
    re_path(r"^hello/([a-zA-Z]+)/$", hello),
    # re_path(r"^plus/([0-9]+)/([0-9]+)/$", plus),
    path(r"plus/<int:a>/<int:b>/", plus),
    # re_path(r"^plus/(\d+)/(\d+)/$", plus),
    re_path(r"^birthday/(\w+)/([0-9]+)/$", birthday),
    re_path(r"^birthday/(?P<age>[0-9]+)/(?P<name>\w+)/$", birthday),
    path('admin/', admin.site.urls),
]
