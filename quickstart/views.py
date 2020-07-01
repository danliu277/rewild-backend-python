from django.contrib.auth.models import User
from rest_framework import viewsets
# from rewild_backend_python.quickstart.serializers import UserSerializer
from django.http import HttpResponse

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")