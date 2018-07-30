from django.http import HttpResponse
from django.urls import path

from . import views

app_name = "expenses"


def foo(request):
    import time
    time.sleep(4)
    return HttpResponse("Hello!")


urlpatterns = [
    path("hi/", foo),
    path("", views.ExpenseListView.as_view(), name="list"),
    path("create/", views.ExpenseCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
]
