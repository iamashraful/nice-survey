from crequest.middleware import CrequestMiddleware
from django.contrib.auth.models import User
from django.db import models
from fast_drf.mixins.expose_api_model_mixin import ExposeApiModelMixin

__author__ = 'Ashraful'


class SurveyBase(ExposeApiModelMixin, models.Model):
    start_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    end_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')

    class Meta:
        app_label = 'survey'
        abstract = True

    def save(self, **kwargs):
        _request = CrequestMiddleware.get_request()
        if not self.pk:
            self.created_by = _request.user if _request and _request.user else None
        self.updated_by = _request.user if _request and _request.user else None
        super(SurveyBase, self).save(**kwargs)
