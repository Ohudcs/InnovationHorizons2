from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('assignment', ArticleViewSet, basename='assignment')

urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),
  path('change_password/', change_password, name='change_password'),
]