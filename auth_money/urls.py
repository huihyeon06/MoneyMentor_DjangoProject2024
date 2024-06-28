# myapp/urls.py
from django.urls import path
from . import views

app_name = 'auth_money'

urlpatterns = [
    path('', views.main_money_view, name='main_money'),
    path('login/', views.login_view, name='login'),
    path('add_money/', views.add_money_view, name='add_money'),
    path('content_list/', views.ContentsList.as_view(), name="content_list"),
    path('content_create/', views.ContentsCreate.as_view(), name="content_create"),
    path('content_update/<int:pk>/', views.ContentsUpdate.as_view(), name="content_update"),
    path('content_delete/<int:pk>/', views.ContentsDelete.as_view(), name="content_delete"),
    path('content_review/', views.content_review_view, name="content_review")
]