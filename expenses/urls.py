from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.expense_list),
    path("create/", views.expense_create),
    path("<int:pk>/", views.expense_detail, name="detail"),
]
