from django.contrib import admin
from django.urls import path
import wordcount_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount_app.views.home, name='home'),
    path('about/', wordcount_app.views.about, name='about'),
    path('result/', wordcount_app.views.result, name='result'),
]