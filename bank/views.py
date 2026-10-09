from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Checks
from .serializer import ChecksSerializer

class ChecksListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer

    def get_queryset(self):
        queryset = Checks.objects.all()
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ChecksDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Checks.objects.all()
    serializer_class = ChecksSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) 

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)