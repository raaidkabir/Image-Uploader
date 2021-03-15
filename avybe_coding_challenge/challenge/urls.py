from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='challenge-home'),
    path('upload_to_home/', views.upload_to_home, name='challenge-upload_to_home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)