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
    path('events/', views.EventView.as_view(), name = 'events'),
    path('resources/', views.ResourceView.as_view(), name = 'resources'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('picgame/', views.PicGameView.as_view(), name = 'picgame'),
    path('strangers/', views.StrangersView.as_view(), name = 'strangers')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
