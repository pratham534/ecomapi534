from django.urls import path, include
from . import views

urlpatterns = [
    path('get_token/<str:id>/<str:token>/', views.generate_token, name="get_token"),
    path('process/<str:id>/<str:token>/', views.payment_process, name="process")
]
