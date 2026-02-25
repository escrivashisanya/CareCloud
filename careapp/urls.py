
from django.contrib import admin
from django.urls import path
from careapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home,name='home'),
    
    path('start/', views.starter,name='start'),

    path('appointment/', views.appointment,name='appointment'),

    path('about/', views.about,name='about'),

    path('show/', views.show,name='show'),


    
]
