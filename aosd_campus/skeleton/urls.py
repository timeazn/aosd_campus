from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'skeleton'

urlpatterns = [
    path('',views.FrontView.as_view(), name='front'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('base/', views.BaseView.as_view(), name = 'base'),
    path('connect/', views.ConnectView.as_view(), name = 'connect'),
    path('gallery/', views.GalleryView.as_view(), name = 'gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
