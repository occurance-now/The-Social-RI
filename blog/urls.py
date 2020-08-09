from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('', views.home, name = 'social-home'),
    path('news/', views.news, name = 'social-news'),
    path('shows/', views.shows, name = 'social-shows'),
    path('sustainability/', views.sustainability, name = 'social-sustainability'),
    path('contact/', views.contact, name = 'social-contact'),
    path('about/', views.about, name = 'social-about'),
    path('signup/', views.signup, name = 'social-signup'),

    path('artist1/', views.artist1, name = 'social-artist1'),
    path('artist2/', views.artist2, name = 'social-artist2'),
    path('artist3/', views.artist3, name = 'social-artist3'),
    path('artist4/', views.artist4, name = 'social-artist4'),
    path('artist5/', views.artist5, name = 'social-artist5'),
    path('artist6/', views.artist6, name = 'social-artist6'),
    path('artist7/', views.artist7, name = 'social-artist7'),

    path('show1/', views.show1, name = 'social-show1'),
    path('show2/', views.show2, name = 'social-show2'),
    path('show3/', views.show3, name = 'social-show3'),
    path('show4/', views.show4, name = 'social-show4'),
    path('show5/', views.show5, name = 'social-show5'),
    path('show6/', views.show6, name = 'social-show6'),
    path('show7/', views.show7, name = 'social-show7'),

    path('sustainability1/', views.sustainability1, name = 'social-sustainability1'),
    path('sustainability2/', views.sustainability2, name = 'social-sustainability2'),
    path('sustainability3/', views.sustainability3, name = 'social-sustainability3'),
    path('sustainability4/', views.sustainability4, name = 'social-sustainability4'),
    path('sustainability5/', views.sustainability5, name = 'social-sustainability5'),
    path('sustainability6/', views.sustainability6, name = 'social-sustainability6'),
    path('sustainability7/', views.sustainability7, name = 'social-sustainability7'),


] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


