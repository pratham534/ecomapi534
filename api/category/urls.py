from rest_framework import routers
from . import views
from django.urls import path, include

# router = routers.SimpleRouter()
router = routers.DefaultRouter()
# 👇👇 registering the path to the Category View to the router
router.register(r'', views.CategoryViewset)

urlpatterns = [
    path('', include(router.urls))
]