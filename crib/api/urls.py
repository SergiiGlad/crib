from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crib.api.viewsets.category import CategoryViewSet

router = DefaultRouter()
router.register('crib', CategoryViewSet, basename='crib')

urlpatterns = [
    path('', include(router.urls)),
]
