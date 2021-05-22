from django.urls import path
from airiq_app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.air_settings, name='settings'),
    path('ajax/getData',views.getData,name='getData')
]
