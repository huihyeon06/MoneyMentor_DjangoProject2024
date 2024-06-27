# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_money_view, name='main_money'),
    path('login/', views.login_view, name='login'),
    path('add_money/', views.add_money_view, name='add_money'),
    path('contents_list/', views.ContentsList.as_view(), name="contents_list"),
]