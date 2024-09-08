from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response
