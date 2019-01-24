from django.urls import path

from survey.views import index

urlpatterns = [
    path('', index, name='index-url'),
]
