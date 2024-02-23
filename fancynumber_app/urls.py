# urls.py
from django.urls import path
from . import views
from .views import AdminLoginView

urlpatterns = [
    path('', AdminLoginView.as_view(), name='admin_login'),
    path('add/', views.add_fancy_phone_number, name='add_fancy_phone_number'),
    path('view/', views.fancy_phone_number_list, name='fancy_phone_number_list'),
    path('<int:number_id>/delete/', views.delete_fancy_phone_number, name='delete_fancy_phone_number'),
]
