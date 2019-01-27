from django.urls import path
from fast_drf.router import BasicRouter

from survey.views.survey_index import index

urlpatterns = [
    path('', index, name='index-url'),
] + BasicRouter.get_urls()
