from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("my/", views.MyView.as_view(), name="my"),
    path("", views.ExpenseListView.as_view(), name="list"),
    path("create/", views.ExpenseCreateView.as_view(), name="create"),
    # path("<int:pk>/", views.expense_detail, name="detail"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
]
