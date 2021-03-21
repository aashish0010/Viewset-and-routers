from rest_framework.views import APIView
from .models import Home
from .serializations import HomeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets


class GenericViewset1(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = HomeSerializers
    queryset = Home.objects.all()


class GenericViewset(viewsets.ModelViewSet):
    serializer_class = HomeSerializers
    queryset = Home.objects.all()


class Generic(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = HomeSerializers
    queryset = Home.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
