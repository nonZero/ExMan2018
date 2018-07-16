from django.urls import path

app_name = "expenses"

from . import views
urlpatterns = [
    path("", views.expense_list),
    path("create/", views.expense_create),
    path("<int:pk>/", views.expense_detail, name="detail"),
]
