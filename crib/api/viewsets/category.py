from rest_framework.viewsets import ModelViewSet
from crib.models import Category
from crib.api.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    class Meta:
        model = Category
