from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from survey.views import index

urlpatterns = [
    path('', index, name='index-url'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
