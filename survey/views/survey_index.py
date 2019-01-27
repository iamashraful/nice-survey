from django.shortcuts import render

__author__ = 'Ashraful'


def index(request):
    return render(request, 'survey-index.html')
