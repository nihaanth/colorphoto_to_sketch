# urls.py

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sketch/', views.sketch_view, name='sketch'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
