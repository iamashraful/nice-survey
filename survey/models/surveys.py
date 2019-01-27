from django.db import models
from fast_drf.utils.enums import HTTPVerbsEnum

from survey.models.survey_base import SurveyBase

__author__ = 'Ashraful'


class Survey(SurveyBase):
    title = models.CharField(max_length=256, blank=True)
    group = models.ForeignKey('survey.SurveyGroup', on_delete=models.SET_NULL, related_name='surveys', null=True)
    version = models.PositiveSmallIntegerField(default=1)
    code = models.CharField(max_length=16, null=True)

    class Meta:
        app_label = 'survey'

    @classmethod
    def exposed_api(cls, *args, **kwargs):
        return {
            'api_url': 'api/surveys'
        }


class SurveyGroup(SurveyBase):
    title = models.CharField(max_length=256)

    class Meta:
        app_label = 'survey'

    @classmethod
    def exposed_api(cls, *args, **kwargs):
        return {
            'api_url': 'api/survey-groups',
            'allowed_methods': [HTTPVerbsEnum.GET.value, HTTPVerbsEnum.POST.value, HTTPVerbsEnum.PUT.value]
        }
