from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# 
from .views import home
# 
from rest_framework.authtoken import views

urlpatterns = [
    # 
    path('', home, name="home"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    # 
    path('api-token-auth/', views.obtain_auth_token, name="obtain_auth_token")
]