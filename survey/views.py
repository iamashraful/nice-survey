from django.shortcuts import render
from rest_framework.permissions import AllowAny


def index(request):
    return render(request, 'index.html')
